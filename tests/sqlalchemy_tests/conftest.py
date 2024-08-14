from functools import cache

import httpx
import pytest
from minio import Minio
from sqlalchemy import Engine, URL
from sqlalchemy.dialects import registry
from sqlalchemy.testing.provision import post_configure_engine

registry.register("dremio.flight", "sqlalchemy_dremio.flight", "DremioDialect_flight")

pytest.register_assert_rewrite("sqlalchemy.testing.assertions")

from sqlalchemy.testing.plugin.pytestplugin import * # noqa



DREMIO_URL = "http://localhost:9047"
DATALAKE_NAME = "datalake"
MINIO_ACCESS_KEY = "minio"
MINIO_SECRET_KEY = "minio1234"
MINIO_ENDPOINT = "minio:9000"

@cache
def _get_client() -> httpx.Client:
    client = httpx.Client(base_url=DREMIO_URL)
    assert client.get("/").is_success, "Dremio needs to be running"

    token = client.post(
        "http://localhost:9047/apiv2/login",
        json={"userName": "dremio", "password": "dremio123"}).json()["token"]
    client.headers.update({"Authorization": f"_dremio{token}"})
    return client


def _create_db():
    client = _get_client()
    existing_db = client.get("/api/v3/catalog/by-path/test")

    if existing_db.is_success:
        # Object Store already exists
        return

    resp = client.post("/api/v3/catalog", json={
        "entityType": "source",
        "type": "S3",
        "name": "test",
        "config": {
            "accessKey": MINIO_ACCESS_KEY,
            "accessSecret": MINIO_SECRET_KEY,
            "secure": False,
            "rootPath": f"/{DATALAKE_NAME}",
            "compatibilityMode": True,
            "propertyList": [
                {"name": "fs.s3a.endpoint", "value": MINIO_ENDPOINT},
                {"name": "fs.s3a.path.style.access", "value": "true"},
            ],
        },
    },
                       )
    resp.raise_for_status()

def _create_bucket() -> None:
    client = Minio(endpoint="localhost:9000",
                   access_key=MINIO_ACCESS_KEY,
                   secure=False,
                   secret_key=MINIO_SECRET_KEY)
    if client.bucket_exists(DATALAKE_NAME):
        return

    client.make_bucket(DATALAKE_NAME)


@post_configure_engine.for_db("dremio")
def _dremio_post_configure_engine(url: URL, engine: Engine, follower_ident: str):
    _create_bucket()
    _create_db()



