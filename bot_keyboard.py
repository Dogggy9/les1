import telebot
from telebot import types

bot = telebot.TeleBot('5721389141:AAE3hEZfKPk5NsfbG-oDnIQF4XDYLH41IM8')

@bot.message_handler(commands=["start"])
def startKBoard(message):
    startKBoard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    Catalog = types.KeyboardButton(text="Каталог")
    Info = types.KeyboardButton(text="Инофрмация")
    startKBoard.add(Catalog, Info)
    bot.send_message(message.chat.id, "Добро пожаловать в магазин цифровых товаров", reply_markup=startKBoard)

@bot.message_handler(content_types=['text'])
def catalogchk(message):
    if message.text == "Каталог":
        catalogKBoard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        Steam = types.KeyboardButton(text="Steam")
        Origin = types.KeyboardButton(text="Origin")
        UPlay = types.KeyboardButton(text="UPlay")
        EpicGames = types.KeyboardButton(text="Epic Games")
        VPN = types.KeyboardButton(text="VPN")
        catalogKBoard.add(Steam, Origin, UPlay, EpicGames, VPN)
        bot.send_message(message.chat.id, "Выберите Раздел", reply_markup=catalogKBoard)

if __name__ == '__main__':
    bot.infinity_polling()