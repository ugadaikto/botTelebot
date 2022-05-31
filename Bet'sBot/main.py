import time

import telebot
from config import *
from messages import MESSAGES as ms
from database import Database
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = telebot.TeleBot(BOT_TOKEN, parse_mode='MarkdownV2')
db = Database('database.db')

keyboards = {
  'owner': {
    'main_menu': {
      'Профиль': {'Обратно'},
      'Админка': {'Обратно'},
      'Реферал': {}
    }
  },
  'worker': {
    'main_menu': {
      'Профиль': {'Обратно'},
      'Админка': {'Обратно'},
      'Реферал': {}
    }
  },
  'user': {
    'main_menu': {
      'Профиль': {'Обратно'}
    }
  }
}

def c_k(keyboard):  # CREATE_KEYBOARD
  new_keyboard = InlineKeyboardMarkup()
  for btn in keyboard:
    new_keyboard.add(InlineKeyboardButton(text=btn, callback_data=btn))
  return new_keyboard

user_steps = {'main_menu': {
  'profile',
  'admin_panel'
  }
}

@bot.message_handler(commands=['start', 'help'])
def command_answers(message):
  user_id = message.from_user.id
  user_command = message.text[1:]  # Команда юзера без '/'
  user_info = db.user_info(user_id)
  user_referral = str(user_info[3])
  user_role = user_info[1]
  if db.user_exist(user_id):  # Если пользователь существует
    pass
  else:
    db.add_user(user_id)  # Создаем нового пользователя
  if user_command[:5] == 'start':
    if user_referral == 'none':
      if " " in message.text:
        ref_candidate = message.text.split()[1]
        try:
          ref_candidate = int(ref_candidate)
          if user_id != ref_candidate:
            all_users = db.all_userids()
            for i in all_users:
              if ref_candidate == i[0]:
                db.edit_user_info(user_id, referral=ref_candidate)
                bot.send_message(ref_candidate, 'Новый пользователь зарегистрировался через ваш реферал!')
                break
        except ValueError:
          pass
    db.edit_user_info(user_id, step='main_menu')
    bot.send_message(user_id, ms['start'], reply_markup=c_k(list(keyboards[user_role]['main_menu'])))


@bot.message_handler(content_types=['text'])
def text_answers(message):
  user_id = message.from_user.id
  user_message = message.text.lower()
  if db.user_exist(user_id):
    pass
  else:
    db.add_user(user_id)
  if user_message == 'говно':
    bot.send_message(user_id, 'Сам ты говно')

@bot.callback_query_handler(func=lambda call:True)
def callback_accept(call):
  user_id = call.from_user.id
  user_name = call.from_user.first_name
  user_info = db.user_info(user_id)
  user_all_clients = user_info[5]
  user_balance = user_info[4]
  user_referral = user_info[3]
  user_step = user_info[2]
  user_role = user_info[1]
  message_id = call.message.message_id
  if user_step == 'main_menu':
    if call.data == 'Профиль':
      db.edit_user_info(user_id, step='profile')
      bot.edit_message_text(chat_id=user_id, message_id=message_id, text=ms['profile'].format(name=user_name, balance=user_balance), reply_markup=c_k(list(keyboards[user_role]['main_menu']['Профиль'])))
    if call.data == 'Админка':
      db.edit_user_info(user_id, step='admin_panel')
      bot.edit_message_text(chat_id=user_id, message_id=message_id, text=ms['admin_panel'].format(all_clients=user_all_clients), reply_markup=c_k(list(keyboards[user_role]['main_menu']['Админка'])))
    if call.data == 'Реферал':
      bot.edit_message_text(chat_id=user_id, message_id=message_id, text=f'*Твоя реферальная ссылка*\nhttps://t\.me/superiorBetBot?start\={user_id}')
      time.sleep(5)
      bot.edit_message_text(chat_id=user_id, message_id=message_id, text=ms['start'], reply_markup=c_k(list(keyboards[user_role]['main_menu'])))
  elif user_step == 'profile':
    if call.data == 'Обратно':
      db.edit_user_info(user_id, step='main_menu')
      bot.edit_message_text(chat_id=user_id, message_id=message_id, text=ms['start'], reply_markup=c_k(list(keyboards[user_role]['main_menu'])))


bot.infinity_polling()
