import telebot
from telebot import types

bot = telebot.TeleBot('ВАШ_API_КЛЮЧ')


@bot.message_handler(commands=['website'])
def open_website(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://itproger.com"))
	bot.send_message(message.chat.id,
			"Отличный выбор, нажмите на кнопку ниже и начинайте изучения курсов прямо сейчас",
			parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['insta'])
def instagram(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Перейти в Инстаграм", url="https://www.instagram.com/itproger_official/"))
	bot.send_message(message.chat.id, "Нажмите на кнопку ниже и погрузитесь в мир IT прямо сейчас", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['vk'])
def vk(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Посетить группу Вк", url="https://vk.com/prog_life"))
	bot.send_message(message.chat.id, "Нажмите на кнопку ниже и погрузитесь в мир IT прямо сейчас", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
	btn1 = types.KeyboardButton('Создание игр')
	btn2 = types.KeyboardButton('Мобильные приложения')
	btn3 = types.KeyboardButton('Веб разработка')
	btn4 = types.KeyboardButton('Софт для компьютеров')
	btn5 = types.KeyboardButton('Обработка данных')
	btn6 = types.KeyboardButton('Создание ИИ')
	markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
	send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!\nКакое направление тебя интересует?"
	bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
	get_message_bot = message.text.strip().lower()

	if get_message_bot == "начать тест заново":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Создание игр')
		btn2 = types.KeyboardButton('Мобильные приложения')
		btn3 = types.KeyboardButton('Веб разработка')
		btn4 = types.KeyboardButton('Софт для компьютеров')
		btn5 = types.KeyboardButton('Обработка данных')
		btn6 = types.KeyboardButton('Создание ИИ')
		markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

		final_message = "Решил попробовать что-то ещё? \nВыбери какое направление тебя интересует:"
	elif get_message_bot == "создание игр":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Под мобильные телефоны')
		btn2 = types.KeyboardButton('Компьютеры и консоли')
		btn3 = types.KeyboardButton('Виртуальная реальность')
		btn4 = types.KeyboardButton('Web игра')
		btn5 = types.KeyboardButton("Начать тест заново")
		markup.add(btn1, btn2, btn3, btn4, btn5)
		final_message = "Отлично, геймдев крутая тема, но под что хочется разрабатывать?"
	elif get_message_bot == "под мобильные телефоны":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Посмотреть курсы по Unity", url="https://itproger.com/tag/unity"))
		final_message = "Для разработки игр под мобильные устройства зачастую используется игровой движок <a href='https://itproger.com/tag/unity'>Unity</a>\nДвижок прост в изучении и вы можете просмотреть курсы по нему по кнопке ниже"
	# Здесь различные дополнительные проверки и условия
	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Создание игр')
		btn2 = types.KeyboardButton('Мобильные приложения')
		btn3 = types.KeyboardButton('Веб разработка')
		btn4 = types.KeyboardButton('Софт для компьютеров')
		btn5 = types.KeyboardButton('Обработка данных')
		btn6 = types.KeyboardButton('Создание ИИ')
		markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
		final_message = "Так, так, так\nПостой, лучше нажми на одну из интерактивных кнопок ниже"
	bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)