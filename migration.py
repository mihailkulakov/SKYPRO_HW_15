import sqlite3
from os.path import join, isfile

DATABASE_PATH = 'animal.db'
SQL_DIR_PATH = 'sql'
INIT_MIGRATION_FILE_PATH = 'init.sql'
DATA_MIGRATION_FILE_PATH = 'migration.sql'


def get_sql_from_file(file_name):
    """
    Получить sql из файла, переданного в качестве параметра
    :param file_name: имя файла
    :return: sql запрос
    """

    content = ''
    if isfile(file_name):
        with open(file_name) as f:
            content = f.read()
    return content


def main():
    """
    Установить соединение с БД, создать новые таблицы, осуществить миграцию данных
    :return: ничего не возвращает
    """
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    init_sql = get_sql_from_file(join(SQL_DIR_PATH, INIT_MIGRATION_FILE_PATH))

    cursor.executescript(init_sql)

    data_sql = get_sql_from_file(join(SQL_DIR_PATH, DATA_MIGRATION_FILE_PATH))
    cursor.executescript(data_sql)

    cursor.close()
    connection.close()


if __name__ == '__main:':
    main()
