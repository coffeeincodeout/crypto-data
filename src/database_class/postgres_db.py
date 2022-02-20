from src.database_class.databasecrud import DatabaseCrud
import psycopg2


class PostgresDataBase(DatabaseCrud):
    """
    Ability to connect to local PostgreSQL database
    with full crud ability.
    """

    def __init__(self, username: str, password: str, hostname: str, port: int, dbname=None):
        self.dbname = dbname
        self.userName = username
        self.password = password
        self.hostname = hostname
        self.port = port
        self.conn = None
        self.cur = None

    def conn_db(self):
        """
        this method will connect to an existing database
        or postgresql so users can create a new database.
        """
        if self.dbname is not None:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.userName,
                password=self.password,
                host=self.hostname,
                port=self.port

            )
        else:
            self.conn = psycopg2.connect(
                user=self.userName,
                password=self.password,
                host=self.hostname,
                port=self.port
            )

    def cursor(self):
        self.cur = self.conn.cursor()

    def close_db_conn(self):
        if self.conn:
            self.conn.close()

    def create_db(self, dbname: str) -> str:
        """
        This method can be used to create a database
        in postgressql by passing the name of the database
        as a string.
        @param dbname:
        @return: str
        """
        create_db_query = "CREATE DATABASE {0}".format(dbname)
        try:
            with self.conn.cursor() as cursor:
                self.conn.autocommit = True
                cursor.execute(create_db_query)
        except Exception as e:
            return e
        finally:
            if self.conn:
                self.conn.close()

        return 'database {0} created'.format(dbname)

    def delete_db(self, dbname: str) -> str:
        """
        Drop database from postgres as long as user
        has the ability to perform the task.
        @param dbname: str
        @return:
        """
        drop_db_query = "DROP DATABASE IF EXISTS {0}".format(dbname)
        try:
            with self.conn.cursor() as cursor:
                self.conn.autocommit = True
                cursor.execute(drop_db_query)
        except Exception as e:
            return e
        finally:
            if self.conn:
                self.conn.close()
            return "database {0} dropped".format(dbname)

    def create(self, table: str, columns, data, **kwargs):
        """
        insert data into a table passing the table name and column/data
        as a list or a dict with the data to insert.
        @param table: str
        @param columns: list
        @param data: list
        @param kwargs: dict
        @return:
        """
        if kwargs:
            columns = ', '.join('"' + key + '"' for key in kwargs.keys())
            values = ', '.join(values for values in kwargs.values())
        else:
            columns = ', '.join('"' + key + '"' for key in columns)
            values = ', '.join("'" + values + "'" if isinstance(values, str) else str(values) for values in data)

        sql = "INSERT INTO %s (%s) VALUES (%s);" % (table, columns, values)
        try:
            with self.conn.cursor() as cursor:
                self.conn.autocommit = True
                cursor.execute(sql)
        except Exception as e:
            print(sql)
            return e
        finally:
            if self.conn:
                self.conn.close()

    def read(self, query: str):
        select_query = query
        try:
            with self.conn.cursor() as cursor:
                self.conn.autocommit = True
                cursor.execute(select_query)
                return cursor.fetchall()
        except Exception as e:
            return e
        finally:
            if self.conn:
                self.conn.close()

    def update(self):
        pass

    def delete(self):
        pass

    def upload_csv(self):
        pass

