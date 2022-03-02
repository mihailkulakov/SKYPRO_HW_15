from flask import Flask, jsonify
import sqlite3
import queries

app = Flask(__name__)

DATABASE_PATH = 'animal.db'


def serialize_row(row):
    return {key: row[key] for key in row.keys()}

@app.route('/<animal_id>')
def get_animal_by_id(animal_id):
    """
    Получить данные из БД по id животного
    :param animal_id: id животного
    :return: жсон с данными по одному животному. Часть данных передана айдишниками значений
    """
    conn: sqlite3.Connection = app.config['db']
    cursor = conn.cursor()

    cursor.execute(queries.GET_ANIMAL_BY_ID_QUERY, (animal_id, ))
    row = cursor.fetchone()

    cursor.close()

    return jsonify(serialize_row(row))




@app.route('/<animal_id>/full')
def get_animal_by_id_full(animal_id):
    """
    Получить данные из БД по id животного
    :param animal_id: id животного
    :return: жсон с данными по одному животному. Все данные передаются значениями
    """
    conn: sqlite3.Connection = app.config['db']
    cursor = conn.cursor()

    cursor.execute(queries.GET_ANIMAL_BY_ID_QUERY_FULL, (animal_id,))
    row = cursor.fetchone()

    cursor.close()

    return jsonify(serialize_row(row))


if __name__ == '__main__':
    connection = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    app.config['db'] = connection
    try:
        app.run()
    except KeyboardInterrupt:
        connection.close()