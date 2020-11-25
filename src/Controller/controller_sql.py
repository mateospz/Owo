import pymysql


def check_connect(self):
    if self.state is False:
        return 1
    else:
        return 0


def get_data_connect(self):
    data = [0, "localhost",
            1, "root",
            2, "",
            3, "Holded"]

    return data
