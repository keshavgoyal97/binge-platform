from contextlib import contextmanager

from app.exceptions.postgres_exceptions import (
    ConnectionException,
    ConnectionPoolException,
)
from app.utils.config import get_config
from app.utils.logger import logger
from psycopg2 import pool

MIN_POOL_CONN = 2
MAX_POOL_CONN = 5

log = logger()


class PostgresDB:
    def __init__(
        self, url: str, min_connections=MIN_POOL_CONN, max_connections=MAX_POOL_CONN
    ):
        self.__extract_creds_from_url(url)
        self.__connection_pool = self.__init_connection_pool(
            min_connections, max_connections
        )

    def __init_connection_pool(
        self, min_connections, max_connections
    ) -> pool.AbstractConnectionPool:
        _pool = pool.SimpleConnectionPool(
            min_connections,
            max_connections,
            database=self.db_name,
            user=self.user,
            password=self.password,
            host=self.host,
        )
        if not _pool:
            raise ConnectionPoolException(
                "Couldn't create connection pool",
                min_connections=min_connections,
                max_connections=max_connections,
            )
        return _pool

    def __extract_creds_from_url(self, url: str):
        db_creds, db_host = url.split("@")
        host_port_info, self.db_name = db_host.split("/")
        self.host = host_port_info.split(":")[0]
        db_creds = db_creds.replace("/", "")
        _, self.user, self.password = db_creds.split(":")

    def execute(self, sql_query: str, params: dict):
        conn = self.__connection_pool._getconn()
        try:
            if conn:
                with conn:
                    with conn.cursor() as cur:
                        output = cur.execute(sql_query, params)
                        conn.commit()
            else:
                raise ConnectionException("Couldn't get a connection from pool.")
        finally:
            self.__connection_pool._putconn(conn)
        return output

    def fetch_one(self, sql_query: str, params: dict):
        conn = self.__connection_pool._getconn()
        try:
            if conn:
                with conn:
                    with conn.cursor() as cur:
                        cur.execute(sql_query, params)
                        output = cur.fetchone()
                        conn.commit()
            else:
                raise ConnectionException("Couldn't get a connection from pool.")
        finally:
            self.__connection_pool._putconn(conn)
        return output

    def fetch_all(self, sql_query: str, params: dict):
        conn = self.__connection_pool._getconn()
        try:
            if conn:
                with conn:
                    with conn.cursor() as cur:
                        cur.execute(sql_query, params)
                        output = cur.fetchall()
                        conn.commit()
            else:
                raise ConnectionException("Couldn't get a connection from pool.")
        finally:
            self.__connection_pool._putconn(conn)
        return output

    def get_connection(self):
        return self.__connection_pool._getconn()

    def health(self) -> bool:
        return not self.__connection_pool.closed

    def close(self) -> None:
        self.__connection_pool._closeall()

prod_others_db_writer = None
def __init_db_pool():
    global prod_others_db_writer
    prod_others_db_writer = PostgresDB(url=get_config("PROD_OTHERS_DB_WRITER_URL"))