import telebot
from telebot import types

TOKEN = "5721389141:AAE3hEZfKPk5NsfbG-oDnIQF4XDYLH41IM8"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, как дела?")


@bot.message_handler(commands=['hi'])
def welcome(message):
    response = f'Привет {message.from_user.last_name} {message.from_user.first_name}'
    bot.send_message(message.chat.id, response)


@bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_message(message.chat.id, message.text)


bot.infinity_polling()
