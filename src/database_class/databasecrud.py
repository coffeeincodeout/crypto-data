from abc import ABCMeta, abstractmethod


class DatabaseCrud(metaclass=ABCMeta):

    @abstractmethod
    def conn_db(self):
        pass

    @abstractmethod
    def create_db(self, dbname):
        pass

    @abstractmethod
    def delete_db(self, dbname):
        pass

    @abstractmethod
    def create(self, table, columns, data, **kwargs):
        pass

    @abstractmethod
    def read(self, query):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass
