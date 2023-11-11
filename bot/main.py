# -*- coding: utf-8 -*-
import sqlite3
import telebot
from telebot import *
from telebot.types import *



#VARs
bot = TeleBot('6825416721:AAHEj60rxo7jU28vgchcHKG5HrK4C1V0ggY')
print('КОСТЫЛЬ')

name = ''
vk = ''
contact = ''
type0 = ''
bio = ''
tg = ''
user_id = ''



#DEFs
def gen_id():
	con = sqlite3.connect("data.db")
	cursor = con.cursor()
	cursor.execute('SELECT id FROM data')
	ids = cursor.fetchall()
	id1 = 0
	for id0 in ids:
		if id1 < int(id0[0]):
			id1 = int(id0[0])

	return (id1+1)

	cursor.close()
	con.close()



#Name enter
@bot.message_handler(commands=['start', 'new'])
def start(message):
	#Set user_id
	global user_id
	user_id = gen_id()

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
	bot.send_photo(message.from_user.id, type1_photo, caption='Выберите макет визитки:', reply_markup=markup)
	bot.register_next_step_handler(message, upload_photo)

#Upload photo and save type
def upload_photo(message):
	global type0
	#Save type
	type0 = message.text

	#Upload photo
	bot.send_message(message.from_user.id, 'Загрузите фото, которое будет отображено на визитке:', reply_markup=ReplyKeyboardRemove())
	bot.register_next_step_handler(message, enter_bio)

#Download photo and enter bio
def enter_bio(message):
	#Download photo
	index = len(message.photo)-1
	file_path = bot.get_file(message.photo[index].file_id).file_path
	file = bot.download_file(file_path)
	filename = 'photo/' + str(user_id) + '.png'
	with open(filename, "wb") as code:
		code.write(file)

	#Enter bio
	bot.send_message(message.from_user.id, 'Напишите кратко о себе (например о том, чем вы занимаетесь, какую должность в какой компании вы занимаете): ')
	bot.register_next_step_handler(message, end)

#Write data to database and save bio
def end(message):
	global name, vk, contact, type0, bio, tg, user_id
	#Save bio
	bio = message.text

	#Write data to database
	conn = sqlite3.connect('data.db')
	cur = conn.cursor()
	cur.execute("INSERT INTO data (id) VALUES (?)", (user_id,))
	cur.execute(f"UPDATE data SET fullname = '{name}' WHERE id = '{user_id}'")
	cur.execute(f"UPDATE data SET telegram = '{tg}' WHERE id = '{user_id}'")
	cur.execute(f"UPDATE data SET vk = '{vk}' WHERE id = '{user_id}'")
	cur.execute(f"UPDATE data SET contact = '{contact}' WHERE id = '{user_id}'")
	cur.execute(f"UPDATE data SET type = '{type0}' WHERE id = '{user_id}'")
	cur.execute(f"UPDATE data SET bio = '{bio}' WHERE id = '{user_id}'")
	conn.commit()
	cur.close()
	conn.close()

	#Returning result
	url = f'https://dd-forms.vercel.app/card/{user_id}'

	bot.send_message(message.from_user.id, f'Успешно! Ссылка на вашу визитку: {url}')




#Main polling
bot.infinity_polling()