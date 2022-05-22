import telebot
import sqlite3
from telebot import types
import gitignore.tokens

bot = telebot.TeleBot(gitignore.tokens.bot_token)
sql_connection = sqlite3.connect('test.db', check_same_thread=False)
cursor = sql_connection.cursor()
sql_connection.commit()


@bot.message_handler(commands=['start'])
def start(message):
    entertainment_categories = types.ReplyKeyboardMarkup(resize_keyboard=True)
    entertainment_categories.add('Игры🎮', 'Фильмы🎬', 'Книги📚')
    bot.send_message(message.chat.id,
                     '<i>Привет!</i>\nС помощью этого бота ты сможешь найти себе <b>книгу/фильм/игру</b> на вечер',
                     parse_mode='HTML', reply_markup=entertainment_categories)


@bot.message_handler(content_types=['text'])
def main(message):
    entertainment_categories = types.ReplyKeyboardMarkup(resize_keyboard=True)
    entertainment_categories.add('Игры🎮', 'Фильмы🎬', 'Книги📚')
    if message.text == 'Игры🎮':
        show_games(message)
    if message.text == '🔙Назад в главное меню':
        bot.send_message(message.chat.id, '<i>Выбери тип развлечения</i>', parse_mode='HTML',
                         reply_markup=entertainment_categories)
    if message.text == 'Топ 10 лучших игр всех времен':
        show_top10_games_all_time(message)
    if message.text == 'Топ 10 РПГ игр':
        show_top10_rpg(message)
    if message.text == 'Топ 10 шутеров':
        show_top10_shooters(message)
    if message.text == 'Фильмы🎬':
        show_movies(message)
    if message.text == 'Топ 10 Ужасов':
        show_top10_horror_movies(message)
    if message.text == 'Топ 10 Комедий':
        show_top10_comedy_movies(message)
    if message.text == 'Топ 10 Фантастики':
        show_top10_fantastic_movies(message)
    if message.text == 'Книги📚':
        show_books(message)
    if message.text == 'Топ 10 кинг в жанре антиутопия':
        show_top10_antiutopia_books(message)
    if message.text == 'Топ 10 кинг в жанре психоделика':
        show_top10_psycho_books(message)
    if message.text=='Топ 10 книг в жанре гуманитарная фантастика':
        show_top10_gumanfant_books(message)


def show_games(message):
    games_categories = types.ReplyKeyboardMarkup(resize_keyboard=True)
    games_categories.add('🔙Назад в главное меню', 'Топ 10 лучших игр всех времен', 'Топ 10 РПГ игр', 'Топ 10 шутеров',
                         row_width=1)
    msg = bot.send_message(message.chat.id, '<i>Выбери жанр игр</i>', reply_markup=games_categories, parse_mode='HTMl')


def show_top10_games_all_time(message):
    cursor.execute('select * from top10_games_all_time')
    games_from_top10_best = cursor.fetchall()
    temp = []
    for row in games_from_top10_best:
        bot.send_message(message.chat.id,
                         f'<i><b>Название</b></i>: {row[0]}\n<i><b>Платформы:</b></i> {row[1]}\n<i><b>Дата выхода:</b></i> {row[2]}\n<i><b>Краткое описание:</b></i> {row[3]}\n<i><b>Оценка на метакритике:</b></i> {row[4]}',
                         parse_mode='HTML')


def show_top10_rpg(message):
    cursor.execute('select * from top10_rpg')
    games_top_10_rpg = cursor.fetchall()
    temp = []
    for row in games_top_10_rpg:
        bot.send_message(message.chat.id,
                         f'<i><b>Название</b></i>: {row[0]}\n<i><b>Платформы:</b></i> {row[1]}\n<i><b>Дата выхода:</b></i> {row[2]}\n<i><b>Краткое описание:</b></i> {row[3]}\n<i><b>Оценка на метакритике:</b></i> {row[4]}',
                         parse_mode='HTML')


def show_top10_shooters(message):
    cursor.execute('select * from top10_shooters')
    games_top_10_shooters = cursor.fetchall()
    temp = []
    for row in games_top_10_shooters:
        bot.send_message(message.chat.id,
                         f'<i><b>Название</b></i>: {row[0]}\n<i><b>Платформы:</b></i> {row[1]}\n<i><b>Дата выхода:</b></i> {row[2]}\n<i><b>Краткое описание:</b></i> {row[3]}\n<i><b>Оценка на метакритике:</b></i> {row[4]}',
                         parse_mode='HTML')


def show_movies(message):
    movies_categories = types.ReplyKeyboardMarkup(resize_keyboard=True)
    movies_categories.add('🔙Назад в главное меню', 'Топ 10 Ужасов', 'Топ 10 Комедий', 'Топ 10 Фантастики',
                          row_width=1)
    msg = bot.send_message(message.chat.id, '<i>Выбери жанр фильмов</i>', reply_markup=movies_categories,
                           parse_mode='HTMl')


def show_top10_horror_movies(message):
    cursor.execute('select * from top10_horror_movies order by score desc')
    movies_from_top10_horror = cursor.fetchall()
    temp = []
    for row in movies_from_top10_horror:
        bot.send_message(message.chat.id,
                         f'<i><b>Название</b></i>: {row[0]}\n<i><b>Длительность:</b></i> {row[1]}\n<i><b>Синопсис:</b></i> {row[2]}\n<i><b>Страна производства:</b></i> {row[3]}\n<i><b>Режиссёр:</b></i> {row[4]}\n<i><b>В ролях</b></i>: {row[5]}\n<i><b>Оценка на кинопоиске</b></i>: {row[6]}',
                         parse_mode='HTML')


def show_top10_comedy_movies(message):
    cursor.execute('select * from top10_comedy_movies order by score desc')
    movies_from_top10_comedy = cursor.fetchall()
    temp = []
    for row in movies_from_top10_comedy:
        bot.send_message(message.chat.id,
                         f'<i><b>Название</b></i>: {row[0]}\n<i><b>Длительность:</b></i> {row[1]}\n<i><b>Синопсис:</b></i> {row[2]}\n<i><b>Страна производства:</b></i> {row[3]}\n<i><b>Режиссёр:</b></i> {row[4]}\n<i><b>В ролях</b></i>: {row[5]}\n<i><b>Оценка на кинопоиске</b></i>: {row[6]}',
                         parse_mode='HTML')


def show_top10_fantastic_movies(message):
    cursor.execute('select * from top10_fantastic_movies order by score desc')
    movies_from_top10_fantastic = cursor.fetchall()
    temp = []
    for row in movies_from_top10_fantastic:
        bot.send_message(message.chat.id,
                         f'<i><b>Название</b></i>: {row[0]}\n<i><b>Длительность:</b></i> {row[1]}\n<i><b>Синопсис:</b></i> {row[2]}\n<i><b>Страна производства:</b></i> {row[3]}\n<i><b>Режиссёр:</b></i> {row[4]}\n<i><b>В ролях</b></i>: {row[5]}\n<i><b>Оценка на кинопоиске</b></i>: {row[6]}',
                         parse_mode='HTML')


def show_books(message):
    books_categories = types.ReplyKeyboardMarkup(resize_keyboard=True)
    books_categories.add('🔙Назад в главное меню', 'Топ 10 кинг в жанре антиутопия', 'Топ 10 кинг в жанре психоделика',
                         'Топ 10 книг в жанре гуманитарная фантастика',
                         row_width=1)
    msg = bot.send_message(message.chat.id, '<i>Выбери жанр книг</i>', reply_markup=books_categories, parse_mode='HTMl')


def show_top10_antiutopia_books(message):
    cursor.execute('select * from top10_antiutopia_books order by score desc')
    top10_antiutopia_books = cursor.fetchall()
    temp = []
    for row in top10_antiutopia_books:
        bot.send_message(message.chat.id,
                         f'<i><b>Название</b></i>: {row[0]}\n<i><b>Автор:</b></i> {row[1]}\n<i><b>Синопсис:</b></i> {row[2]}\n<i><b>Оценка:</b></i> {row[3]}',
                         parse_mode='HTML')


def show_top10_psycho_books(message):
    cursor.execute('select * from top10_psycho_books order by score desc')
    top10_psycho_books = cursor.fetchall()
    temp = []
    for row in top10_psycho_books:
        bot.send_message(message.chat.id,
                         f'<i><b>Название</b></i>: {row[0]}\n<i><b>Автор:</b></i> {row[1]}\n<i><b>Синопсис:</b></i> {row[2]}\n<i><b>Оценка:</b></i> {row[3]}',
                         parse_mode='HTML')


def show_top10_gumanfant_books(message):
    cursor.execute('select * from top10_gumanfant_books order by score desc')
    top10_gumanfant_books = cursor.fetchall()
    temp = []
    for row in top10_gumanfant_books:
        bot.send_message(message.chat.id,
                         f'<i><b>Название</b></i>: {row[0]}\n<i><b>Автор:</b></i> {row[1]}\n<i><b>Синопсис:</b></i> {row[2]}\n<i><b>Оценка:</b></i> {row[3]}',
                         parse_mode='HTML')


bot.infinity_polling()
