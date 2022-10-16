import telebot
bot = telebot.TeleBot("TOKEN")

# Обрабатывает все текстовые сообщения, которые содержат команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
	pass

# Обрабатывает все отправленные документы и аудиофайлы
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
	pass

# Обрабатывает все текстовые сообщения, которые соответствуют регулярному выражению
@bot.message_handler(regexp="SOME_REGEXP")
def handle_message(message):
	pass

# Обрабатывает все сообщения, для которых Lambda возвращает True
@bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
def handle_text_doc(message):
	pass

# Который также может быть определен как:
def test_message(message):
	return message.document.mime_type == 'text/plain'

@bot.message_handler(func=test_message, content_types=['document'])
def handle_text_doc(message):
	pass

# Handlers can be stacked to create a function which will be called if either message_handler is eligible
# Этот обработчик будет вызван, если сообщение начнется с '/hello' или есть смайлики
@bot.message_handler(commands=['hello'])
@bot.message_handler(func=lambda msg: msg.text.encode("utf-8") == SOME_FANCY_EMOJI)
def send_something(message):
	pass