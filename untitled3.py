import telebot

TOKEN ="5721389141:AAE3hEZfKPk5NsfbG-oDnIQF4XDYLH41IM8"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['hi'])
def welcome(message):
    response = f'Привет {message.from_user.first_name}'
    bot.send_message(message.chat.id, response)
    
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#  	bot.reply_to(message, message.text)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
 	bot.send_message(message.chat.id, message.text)

bot.infinity_polling()