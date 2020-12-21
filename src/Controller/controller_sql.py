from src.Model.model_sql import read_sql, write_sql, modify_sql


def check_connect(self):
    if self.state is False:
        return 1
    else:
        return 0


def get_data_connect():
    data = [0, "localhost",
            1, "root",
            2, "",
            3, "Holded"]

    return data


def sentence_sql(cursor, action, data):
    if action == 0:
        cursor.execute(read_sql(data))
    elif action == 1:
        cursor.execute(write_sql(data))
    elif action == 2:
        cursor.execute(modify_sql(data))

