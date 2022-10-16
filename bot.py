import telebot

TOKEN = '5721389141:AAE3hEZfKPk5NsfbG-oDnIQF4XDYLH41IM8'
tb = telebot.TeleBot(TOKEN)	 # Создаем новый объект 'телеграмбот'

# Называя эту функцию, Telebot начинает опросить серверы Telegram для новых сообщений.
# - interval: int (default 0) - интервал между запросами на опрос
# - timeout: integer (default 20) - Тайм -аут за считанные секунды для длительного опроса.
# - allowed_updates: List of Strings (default None) - Список типов обновлений для запроса
tb.infinity_polling(interval=0, timeout=20)

# getMe
user = tb.get_me()

# setWebhook
tb.set_webhook(url="http://example.com", certificate=open('mycert.pem'))
# unset webhook
tb.remove_webhook()

# # getUpdates
# updates = tb.get_updates()
# # or
# updates = tb.get_updates(1234, 100, 20)  # get_Updates(offset, limit, timeout):

# sendMessage
tb.send_message(chat_id, text)

# editMessageText
tb.edit_message_text(new_text, chat_id, message_id)

# forwardMessage
tb.forward_message(to_chat_id, from_chat_id, message_id)

# Все функции send_xyz, которые могут взять файл в качестве аргумента, также могут взять файл_ид вместо файла.
# sendPhoto
photo = open('/tmp/photo.png', 'rb')
tb.send_photo(chat_id, photo)
tb.send_photo(chat_id, "FILEID")


