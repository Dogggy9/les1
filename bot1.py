import telebot
from moduls.seting import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    k = message
    print(k)
    bot.send_message(message.chat.id, """Я здороваюсь и рассказываю о возможностях
    /about_author, /get_keyboard, /get_keyboard_inline""")


@bot.message_handler()
def get_message(message):
    bot.send_message(message.chat.id, message)


bot.polling(non_stop=True)
