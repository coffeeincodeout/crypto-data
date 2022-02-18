from enum import Enum


class PostgresqlConn(Enum):
    hostname = 'localhost'
    port = 5432


class MysqlConn(Enum):
    hostname = '127.0.0.1'
    port = 3306
