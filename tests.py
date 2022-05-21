import sqlite3

try:
    sql_connection = sqlite3.connect('test.db')
    cursor = sql_connection.cursor()
    print('БД подключена')
    sql_connection.commit()
except sqlite3.Error as error:
    print('Ошибка')


cursor.execute('select * from top10_games_all_time')
games = cursor.fetchall()
for row in games:
    print(f'название {row[0]}')
