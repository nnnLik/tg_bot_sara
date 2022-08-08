import imaplib
import email
import GPUtil
import telebot
from telebot import types

token='5232153760:AAECg3HUYCDp87SCBfbyfhOX_Lm77mnT0cE'
bot=telebot.TeleBot(token)
file = 'E:\Deving\Sara\\notes.txt'


@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, f'Приветик, <b>{message.from_user.first_name}</b> 👀\n<b>Удачи!!!</b>', parse_mode='html')

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
	stat = types.KeyboardButton('Температура GPU')
	notice = types.KeyboardButton('Заметки')
	gmail_parser = types.KeyboardButton('Проверить почту')
	markup.add(stat,  notice, gmail_parser)

@bot.message_handler(content_types=['text'])
def get_user_text(message):

	if message.text.lower() == 'привет':
		bot.send_message(message.chat.id, 'О, приветик', parse_mode='html')

	elif message.text == 'Заметки':

		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

		with open('E:\Deving\Sara\\note.txt', 'r') as f:

			bot.send_message(message.chat.id, text=f.readline(), reply_markup=markup)

		back = types.KeyboardButton('Назад')
		markup.add(back)
		bot.send_message(message.chat.id, text='Я надеюсь ты сделаешь что-то из этого...', reply_markup=markup)

	elif message.text == 'Температура GPU':

		for gpu in GPUtil.getGPUs():
			gpu_stats = gpu.temperature

		if gpu_stats <= 40:
			bot.send_message(message.chat.id, f'Температура GPU:\n\nGeForce GTX 1660 Ti: {gpu_stats}\n\n<b>Прохладненько🥳</b>', parse_mode='html')
		elif gpu_stats >= 60:
			bot.send_message(message.chat.id,  'Температура GPU:\n\nGeForce GTX 1660 Ti: {gpu_stats}\n\n<b>Вырубай...🙀</b>', parse_mode='html')
		else:
			bot.send_message(message.chat.id, f'Температура GPU:\n\nGeForce GTX 1660 Ti: {gpu_stats}\n\n<b>👍</b>', parse_mode='html')

	elif message.text == 'Проверить почту':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

		xion_gmail = types.KeyboardButton('nnnXion')
		back = types.KeyboardButton('Назад')

		markup.add(xion_gmail, back)
		bot.send_message(message.chat.id, text='Какую?', reply_markup=markup)

	elif message.text == 'nnnXion':

		mail = imaplib.IMAP4_SSL('imap.gmail.com')
		mail.login('nnnxion@gmail.com', 'S155hola551')

		mail.list()
		mail.select("inbox")

		result, data = mail.search(None, "ALL")

		ids = data[0]
		id_list = ids.split()
		latest_email_id = id_list[-1]

		result, data = mail.fetch(latest_email_id, "(RFC822)")
		raw_email = data[0][1]
		raw_email_string = raw_email.decode('utf-8')

		email_message = email.message_from_string(raw_email_string)

		to_data = email_message['To']
		from_data = email.utils.parseaddr(email_message['From'])
		date_data = email_message['Date']
		subject_data = email_message['Subject']

		print(to_data)
		print(from_data)
		print(date_data)
		print(subject_data)

		bot.send_message(message.chat.id, f'Кому: {to_data}')
		bot.send_message(message.chat.id, f'От кого: {from_data}')
		bot.send_message(message.chat.id, f'Дата отправки: {date_data}')
		bot.send_message(message.chat.id, f'Заголовок: {subject_data[5::]}')

	elif message.text == 'twilightlik':
		pass

	elif message.text == 'makhmudov_ra':
		pass
	elif message.text == 'Назад':

		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		stat = types.KeyboardButton('Температура GPU')
		notice = types.KeyboardButton('Заметки')
		gmail_parser = types.KeyboardButton('Проверить почту')
		markup.add(stat, notice, gmail_parser)
		bot.send_message(message.chat.id, 'И снова главное меню', reply_markup=markup)

	elif message.text == 'inf':
		bot.send_message(message.chat.id, message, parse_mode='html')

	else:
		bot.send_message(message.chat.id, 'Я тебя не понимаю, дурачок', parse_mode='html')
		sti = open('stic/sticker.webp', 'rb')
		bot.send_sticker(message.chat.id, sti)



bot.polling(none_stop=True)

#Сделать возможным проверять несколько писем

