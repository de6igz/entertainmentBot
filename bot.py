import telebot
import sqlite3
from telebot import types
import gitignore.tokens

bot = telebot.TeleBot(gitignore.tokens.bot_token)


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     '<i>Привет!</i>\nС помощью этого бота ты сможешь найти себе <b>книгу/фильм/игру</b> на вечер',
                     parse_mode='HTML')


bot.infinity_polling()
