import sqlite3
import telebot
from telebot import *
from telebot.types import *



#VARs
bot = TeleBot('6825416721:AAHEj60rxo7jU28vgchcHKG5HrK4C1V0ggY')

name = ''
vk = ''
contact = ''
type0 = ''
bio = ''
tg = ''



#DEFs




#Name enter
@bot.message_handler(commands=['start', 'new'])
def start(message):
	if message.text == '/start':
		bot.send_message(message.from_user.id, 'Здравствуйте, введите ваше имя и фамилию:', reply_markup=ReplyKeyboardRemove())
	else:
		bot.send_message(message.from_user.id, "Введите имя и фамилию, которое будет отображаться на визитке:", reply_markup=ReplyKeyboardRemove())
	bot.register_next_step_handler(message, tg_enter)

#Tg enter and name saving
def tg_enter(message):
	global name
	#Save name
	name = message.text

	#Tg enter
	markup = ReplyKeyboardMarkup(resize_keyboard=True)
	markup.add(KeyboardButton('Использовать мой ник'), KeyboardButton('Без телеграм'))
	bot.send_message(message.from_user.id, 'Укажите ссылку на ваш телеграм', reply_markup=markup)
	bot.register_next_step_handler(message, vk_enter)

#Vk enter and tg saving
def vk_enter(message):
	global tg
	#Save tg
	if message.text == 'Использовать мой ник':
		tg = 'https://t.me/' + message.from_user.username
	elif message.text == 'Без телеграм':
		tg = ''
	else:
		tg = message.text

	#Vk enter
	markup = ReplyKeyboardMarkup(resize_keyboard=True)
	markup.add(KeyboardButton('Без ВК'))
	bot.send_message(message.from_user.id, 'Укажите ссылку на ваш вк', reply_markup=markup)
	bot.register_next_step_handler(message, contact_enter)

#Email or phone enter
def contact_enter(message):
	global vk
	#Save vk
	if message.text == 'Без ВК':
		vk = ''
	else:
		vk = message.text

	#Email or phone enter
	bot.send_message(message.from_user.id, 'Введите способ связи с вами (телефон или почта):', reply_markup=ReplyKeyboardRemove())
	bot.register_next_step_handler(message, type_select)

#Select type and contacts saving
def type_select(message):
	global contact
	#Save contacts
	contact = message.text

	#Select type
	type1_photo = open('media/type1.jpg', 'rb')
	markup = ReplyKeyboardMarkup(resize_keyboard=True)
	markup.add(KeyboardButton('1'))
	bot.send_photo(message.from_user.id, photo, caption='Выберите макет визитки:', reply_markup=markup)



#Main polling
bot.infinity_polling()