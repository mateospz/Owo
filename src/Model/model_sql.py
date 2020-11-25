import pymysql

from src.Model.model_singleton import singleton


@singleton
class ServerSql(object):

    def __init__(self):
        self.name = None
        self.state = False
        self.connection = None

    def __del__(self):
        pass


def connect_to_sql(self):
    if self.check_connect() == 1:
        data = self.get_data_connect()
        try:
            connection = pymysql.connect(host=data[0],
                                         user=data[1],
                                         passwd=data[2],
                                         database=data[3])

            self.connection = data[3]
            self.state = True

            cursor = connection.cursor()
            return cursor

        except NameError:
            print("Not Working")

