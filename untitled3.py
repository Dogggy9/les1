import telebot

TOKEN = "5721389141:AAE3hEZfKPk5NsfbG-oDnIQF4XDYLH41IM8"

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, как дела?")


@bot.message_handler(commands=['hi'])
def welcome(message):
    response = f'Привет {message.from_user.last_name} ' \
               f'{message.from_user.first_name}'
    bot.send_message(message.chat.id, response)

@bot.message_handler(content_types=['text'])
def hi_user(message):
    if message.text == "hi":
        bot.send_message(message.chat.id, 'Ты сказал привет')
        response = f'Привет {message.from_user.last_name} ' \
                   f'{message.from_user.first_name} ' \
                   f'{message.from_user.id} ' \
                   f'{message.from_user.full_name}'
        bot.send_message(message.chat.id, response)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_message(message.chat.id, message.text)


bot.infinity_polling()
