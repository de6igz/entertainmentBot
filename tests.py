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
massiv = []
"""for row in games:
    massiv.append(row)"""
massiv.append(games)
    #print(f'Название: {row[0]}\n Платформы: {row[1]}')
print(' '.join(str(massiv)))
"""for row in massiv:
    print(f'Название : {row[0]}\nПлатформы : {row[1]}\nГод выхода : {row[2]}')"""