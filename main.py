import os

from flask import Flask, request

import telebot
from telebot import types

import parceInst as inst

TOKEN = '1949484698:AAFkkfN586lV2NjFDu6XBcegj_nN6g7T7q8'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)
inst.init_inst_bot()
userinst = ""


def myKeyboard(count=0, btn1_text="", cb_data1="", btn2_text="", cb_data2=""):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(btn1_text, callback_data=cb_data1)
    markup.add(btn1)
    if(count == 2):
        btn2 = types.InlineKeyboardButton(btn2_text, callback_data=cb_data2)
        markup.add(btn2)
    return markup


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    text = "Привет это ДзенБот!!! Хочешь получить бесплатный урок?"
    keyboard = myKeyboard(2,'Да', 'Yes1', 'Нет', 'No1')
    bot.send_message(message.chat.id, text, parse_mode='HTML', reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    global userinst
    if(message.text != ""):
        userinst = message.text
    text = "Хочешь подарок?"
    keyboard = myKeyboard(1,'Да','Yes0')
    # bot.send_message(message.chat.id, text, parse_mode='HTML', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    global userinst
    if call.message:
        if call.data == 'Yes1':
            text1 = "Ты подписан на Ваню???"
            keyboard = myKeyboard(2,'Да', 'Yes3', 'Нет', 'No2')
            bot.delete_message(call.message.chat.id, call.message.id)
            bot.send_message(call.message.chat.id, text1, parse_mode='HTML', reply_markup=keyboard)
        elif call.data == 'No1':
            text1 = "Ты упустил свой шанс заработать миллион рублей, лох"
            keyboard = myKeyboard(1,'Подарок', 'Yes1')
            bot.delete_message(call.message.chat.id, call.message.id)
            bot.send_message(call.message.chat.id, text=text1, parse_mode='HTML', reply_markup=keyboard)
        elif call.data == 'Yes3':
            text1 = "Отправь мне свой ник в инстаграм"
            keyboard = myKeyboard(1,'Готово', 'Yes2')
            bot.delete_message(call.message.chat.id, call.message.id)
            bot.send_message(call.message.chat.id, text=text1, parse_mode='HTML', reply_markup=keyboard)
        elif call.data == 'Yes2':
            if(userinst != "" and inst.check_follow(userinst)):
                text1 = 'Вот твоя ссылка: [http://ссылка.хрю/322qwerty](https://www.youtube.com/watch?v=dQw4w9WgXcQ)'
                bot.delete_message(call.message.chat.id, call.message.id)
                bot.send_message(call.message.chat.id, text=text1, parse_mode='Markdown')
            else:
                text1 = "Ты не подписался((( Скорее подпишись на Ваню!!! И пришли свой никнейм"
                keyboard = types.InlineKeyboardMarkup(row_width=1)
                btn1 = types.InlineKeyboardButton('Инста Вани', url='https://www.instagram.com/funtik_iv/')
                keyboard.add(btn1)
                btn2 = types.InlineKeyboardButton('Подписался!!!', callback_data='Yes2')
                keyboard.add(btn2)
                bot.delete_message(call.message.chat.id, call.message.id)
                bot.send_message(call.message.chat.id, text=text1, parse_mode='HTML', reply_markup=keyboard)
        elif call.data == 'No2':
            text1 = "Скорее подпишись на Ваню!!! И пришли свой никнейм"
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton('Инста Вани', url='https://www.instagram.com/funtik_iv/')
            keyboard.add(btn1)
            btn2 = types.InlineKeyboardButton('Подписался!!!', callback_data='Yes2')
            keyboard.add(btn2)
            bot.delete_message(call.message.chat.id, call.message.id)
            bot.send_message(call.message.chat.id, text=text1, parse_mode='HTML', reply_markup=keyboard)
        elif call.data == 'Yes0':
            text1 = "Ты подписан на Ваню???"
            keyboard = myKeyboard(2,'Да', 'Yes2', 'Нет', 'No2')
            bot.delete_message(call.message.chat.id, call.message.id)
            bot.send_message(call.message.chat.id, text1, parse_mode='HTML', reply_markup=keyboard)



# def myKeyboard(count=0, btn1_text="", cb_data1="", btn2_text="", cb_data2=""):
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     btn1 = types.InlineKeyboardButton(btn1_text, callback_data=cb_data1)
#     markup.add(btn1)
#     if(count == 2):
#         btn2 = types.InlineKeyboardButton(btn2_text, callback_data=cb_data2)
#         markup.add(btn2)
#     return markup


# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     text = "Привет это ДзенБот!!! Хочешь получить бесплатный урок?"
#     keyboard = myKeyboard(2,'Да', 'Yes1', 'Нет', 'No1')
#     bot.send_message(message.chat.id, text, parse_mode='HTML', reply_markup=keyboard)


# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     text = "Хочешь подарок?"
#     keyboard = myKeyboard(1,'Да','Yes0')
#     bot.send_message(message.chat.id, text, parse_mode='HTML', reply_markup=keyboard)


# @bot.callback_query_handler(func=lambda call:True)
# def callback(call):
#     if call.message:
#         if call.data == 'Yes1':
#             text1 = "Ты подписан на Ваню???"
#             keyboard = myKeyboard(2,'Да', 'Yes2', 'Нет', 'No2')
#             bot.delete_message(call.message.chat.id, call.message.id)
#             bot.send_message(call.message.chat.id, text1, parse_mode='HTML', reply_markup=keyboard)
#         elif call.data == 'No1':
#             text1 = "Ты упустил свой шанс заработать миллион рублей, лох"
#             bot.delete_message(call.message.chat.id, call.message.id)
#             bot.send_message(call.message.chat.id, text=text1, parse_mode='HTML')
#         elif call.data == 'Yes2':
#             text1 = 'Вот твоя ссылка: [http://ссылка.хрю/322qwerty](https://www.youtube.com/watch?v=dQw4w9WgXcQ)'
#             bot.delete_message(call.message.chat.id, call.message.id)
#             bot.send_message(call.message.chat.id, text=text1, parse_mode='Markdown')
#         elif call.data == 'No2':
#             text1 = "Скорее подпишись на Ваню!!!"
#             keyboard = types.InlineKeyboardMarkup(row_width=1)
#             btn1 = types.InlineKeyboardButton('Инста Вани', url='https://www.instagram.com/funtik_iv/')
#             keyboard.add(btn1)
#             btn2 = types.InlineKeyboardButton('Подписался!!!', callback_data='Yes2')
#             keyboard.add(btn2)
#             bot.delete_message(call.message.chat.id, call.message.id)
#             bot.send_message(call.message.chat.id, text=text1, parse_mode='HTML', reply_markup=keyboard)
#         elif call.data == 'Yes0':
#             text1 = "Ты подписан на Ваню???"
#             keyboard = myKeyboard(2,'Да', 'Yes2', 'Нет', 'No2')
#             bot.delete_message(call.message.chat.id, call.message.id)
#             bot.send_message(call.message.chat.id, text1, parse_mode='HTML', reply_markup=keyboard)


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://dzenivanbot.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))












# import telebot
# from telebot import types

# import parceInst as inst

# API_TOKEN = '1920270310:AAEkwYN9_0G_4AnFFbZAODYI-HuOtzOJHPA'

# bot = telebot.TeleBot(API_TOKEN)
# inst.init_inst_bot()
# userinst = ""

# def myKeyboard(count=0, btn1_text="", cb_data1="", btn2_text="", cb_data2=""):
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     btn1 = types.InlineKeyboardButton(btn1_text, callback_data=cb_data1)
#     markup.add(btn1)
#     if(count == 2):
#         btn2 = types.InlineKeyboardButton(btn2_text, callback_data=cb_data2)
#         markup.add(btn2)
#     return markup


# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(message):
#     text = "Привет это ДзенБот!!! Хочешь получить бесплатный урок?"
#     keyboard = myKeyboard(2,'Да', 'Yes1', 'Нет', 'No1')
#     bot.send_message(message.chat.id, text, parse_mode='HTML', reply_markup=keyboard)


# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     global userinst
#     if(message.text != ""):
#         userinst = message.text
#     text = "Хочешь подарок?"
#     keyboard = myKeyboard(1,'Да','Yes0')
#     print(userinst)
#     # bot.send_message(message.chat.id, text, parse_mode='HTML', reply_markup=keyboard)


# @bot.callback_query_handler(func=lambda call:True)
# def callback(call):
#     global userinst
#     print(userinst)
#     if call.message:
#         if call.data == 'Yes1':
#             text1 = "Ты подписан на Ваню???"
#             keyboard = myKeyboard(2,'Да', 'Yes3', 'Нет', 'No2')
#             bot.delete_message(call.message.chat.id, call.message.id)
#             bot.send_message(call.message.chat.id, text1, parse_mode='HTML', reply_markup=keyboard)
#         elif call.data == 'No1':
#             text1 = "Ты упустил свой шанс заработать миллион рублей, лох"
#             keyboard = myKeyboard(1,'Подарок', 'Yes1')
#             bot.delete_message(call.message.chat.id, call.message.id)
#             bot.send_message(call.message.chat.id, text=text1, parse_mode='HTML', reply_markup=keyboard)
#         elif call.data == 'Yes3':
#             text1 = "Отправь мне свой ник в инстаграм"
#             keyboard = myKeyboard(1,'Готово', 'Yes2')
#             bot.delete_message(call.message.chat.id, call.message.id)
#             bot.send_message(call.message.chat.id, text=text1, parse_mode='HTML', reply_markup=keyboard)
#         elif call.data == 'Yes2':
#             if(userinst != "" and inst.check_follow(userinst)):
#                 text1 = 'Вот твоя ссылка: [http://ссылка.хрю/322qwerty](https://www.youtube.com/watch?v=dQw4w9WgXcQ)'
#                 bot.delete_message(call.message.chat.id, call.message.id)
#                 bot.send_message(call.message.chat.id, text=text1, parse_mode='Markdown')
#             else:
#                 text1 = "Ты не подписался((( Скорее подпишись на Ваню!!! И пришли свой никнейм" + userinst
#                 keyboard = types.InlineKeyboardMarkup(row_width=1)
#                 btn1 = types.InlineKeyboardButton('Инста Вани', url='https://www.instagram.com/funtik_iv/')
#                 keyboard.add(btn1)
#                 btn2 = types.InlineKeyboardButton('Подписался!!!', callback_data='Yes2')
#                 keyboard.add(btn2)
#                 bot.delete_message(call.message.chat.id, call.message.id)
#                 bot.send_message(call.message.chat.id, text=text1, parse_mode='HTML', reply_markup=keyboard)
#             print(userinst)
#         elif call.data == 'No2':
#             text1 = "Скорее подпишись на Ваню!!! И пришли свой никнейм"
#             keyboard = types.InlineKeyboardMarkup(row_width=1)
#             btn1 = types.InlineKeyboardButton('Инста Вани', url='https://www.instagram.com/funtik_iv/')
#             keyboard.add(btn1)
#             btn2 = types.InlineKeyboardButton('Подписался!!!', callback_data='Yes2')
#             keyboard.add(btn2)
#             bot.delete_message(call.message.chat.id, call.message.id)
#             bot.send_message(call.message.chat.id, text=text1, parse_mode='HTML', reply_markup=keyboard)
#         elif call.data == 'Yes0':
#             text1 = "Ты подписан на Ваню???"
#             keyboard = myKeyboard(2,'Да', 'Yes2', 'Нет', 'No2')
#             bot.delete_message(call.message.chat.id, call.message.id)
#             bot.send_message(call.message.chat.id, text1, parse_mode='HTML', reply_markup=keyboard)


# bot.polling()
