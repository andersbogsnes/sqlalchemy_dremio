import os
import pathlib
import typing

import httpx
import minio
import pytest
import sqlalchemy as sa
from minio import Minio
from sqlalchemy.dialects import registry

registry.register("dremio.flight", "sqlalchemy_dremio.flight", "DremioDialect_flight")


class MinioConfig(typing.TypedDict):
    endpoint: str
    access_key: str
    secret_key: str


@pytest.fixture()
def minio_credentials() -> MinioConfig:
    return MinioConfig(
        endpoint="http://minio:9000",
        access_key="minio",
        secret_key="minio1234",
    )


@pytest.fixture(scope="session")
def minio_client(minio_credentials: MinioConfig) -> Minio:
    client = minio.Minio(
        minio_credentials["endpoint"],
        minio_credentials["access_key"],
        minio_credentials["secret_key"],
    )
    return client


@pytest.fixture(scope="session")
def datalake_bucket(minio_client: Minio) -> str:
    bucket_name = "datalake"
    minio_client.make_bucket(bucket_name)
    return bucket_name


@pytest.fixture(scope="session")
def dremio_db(minio_credentials: MinioConfig, datalake_bucket: str) -> str:
    return httpx.post(
        "http://localhost:9047/api/v3/catalog",
        json={
            "entityType": "source",
            "type": "S3",
            "config": {
                "accessKey": minio_credentials["access_key"],
                "accessSecret": minio_credentials["secret_key"],
                "secure": False,
                "compatibilityMode": True,
                "propertyList": [
                    {"name": "fs.s3a.endpoint", "value": minio_credentials["endpoint"]},
                    {"name": "fs.s3a.path.style.access", "value": "true"},
                ],
            },
        },
    ).json()["id"]


@pytest.fixture(scope="session")
def db_url() -> str:
    default_url = "dremio+flight://dremio:dremio123@localhost:32010?UseEncryption=false&database=$scratch"
    return os.environ.get("DREMIO_CONNECTION_URL", default_url)


@pytest.fixture(scope="session")
def engine(db_url: str) -> sa.Engine:
    return sa.create_engine(db_url)


@pytest.fixture()
def conn(engine: sa.Engine) -> sa.Connection:
    """
    Creates a connection using the parameters defined in ODBC connect string
    """
    with engine.connect() as conn:
        yield conn
    engine.dispose()


@pytest.fixture()
def db(request: pytest.FixtureRequest, conn: sa.Connection) -> sa.Connection:
    test_sql = pathlib.Path(__file__).parent / "scripts/sample.sql"
    sql = test_sql.read_text()
    conn.execute(sa.text(sql))

    def fin():
        conn.execute(sa.text("DROP TABLE $scratch.sqlalchemy_tests"))

    request.addfinalizer(fin)
    return conn
