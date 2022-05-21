import telebot
import sqlite3
from telebot import types
import gitignore.tokens

bot = telebot.TeleBot(gitignore.tokens.bot_token)


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
        bot.send_message(message.chat.id,'Выбери тип развлечения',parse_mode='HTML',reply_markup=entertainment_categories)


def show_games(message):
    games_categories = types.ReplyKeyboardMarkup(resize_keyboard=True)
    games_categories.add('🔙Назад в главное меню', 'Топ 10 лучших игр всех времен', 'Топ 10 РПГ игр', 'Топ 10 шутеров',row_width=1)
    msg = bot.send_message(message.chat.id,'<i>Выбери жанр игр</i>',reply_markup=games_categories,parse_mode='HTMl')
    bot.register_next_step_handler(msg,show_games_from_categories)

def show_games_from_categories(message):
    if message.text=='Топ 10 лучших игр всех времен':



bot.infinity_polling()
