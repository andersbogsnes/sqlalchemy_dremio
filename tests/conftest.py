import typing
from pathlib import Path

import httpx
import minio
import sqlalchemy as sa
from minio import Minio
from sqlalchemy.dialects import registry
from sqlalchemy.testing.plugin.pytestplugin import *
from sqlalchemy.testing.provision import create_db

registry.register("dremio.flight", "sqlalchemy_dremio.flight", "DremioDialect_flight")

@create_db.for_db("dremio")
def _dremio_create_db(cfg, eng, ident):
    _create_bucket()
    _create_db()


def _create_bucket() -> None:
    client = Minio(endpoint="http://localhost:9000",
                   access_key="minio",
                   secret_key="minio1234")
    client.make_bucket("datalake")

def _get_token() -> str:
    resp = httpx.post(
        "http://localhost:9047/apiv2/login",
        json={"userName": "dremio", "password": "dremio123"},
    )
    resp.raise_for_status()
    return resp.json()["token"]

def _create_db():
    resp = httpx.post(
        "http://localhost:9047/api/v3/catalog",
        headers={"Authorization": f"_dremio{_get_token()}"},
        json={
            "entityType": "source",
            "type": "S3",
            "config": {
                "name": "test",
                "accessKey": "minio",
                "accessSecret": "minio1234",
                "secure": False,
                "rootPath": "/datalake",
                "compatibilityMode": True,
                "propertyList": [
                    {"name": "fs.s3a.endpoint", "value": minio["endpoint"]},
                    {"name": "fs.s3a.path.style.access", "value": "true"},
                ],
            },
        },
    )
    resp.raise_for_status()


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
    httpx.post(
        "http://localhost:9047/api/v3/catalog",
        json={
            "entityType": "source",
            "type": "S3",
            "config": {
                "accessKey": minio["access_key"],
                "accessSecret": minio["secret_key"],
                "secure": False,
                "compatibilityMode": True,
                "propertyList": [
                    {"name": "fs.s3a.endpoint", "value": minio["endpoint"]},
                    {"name": "fs.s3a.path.style.access", "value": "true"},
                ],
            },
        },
    )


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
    test_sql = Path("scripts/sample.sql")
    sql = test_sql.read_text()
    conn.execute(sa.text(sql))

    def fin():
        conn.execute(sa.text("DROP TABLE $scratch.sqlalchemy_tests"))

    request.addfinalizer(fin)
    return conn
