import os
import telebot
from flask import Flask, request
from telebot import types

TOKEN = '1949484698:AAFTwrDIWL0SFWBPPOHd1jJQ2_KFIJ7OBcA'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


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
    text = 'Привет, друг!\n\n'\
            'Это бот для выдачи Чек-Листа по заработку 50-100.000 рублей в месяц на Яндекс Дзене\n\n'\
            '❗Но хочу задать тебе один вопрос\n\n'\
            '✅ Как ты впервые узнал обо мне?'
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Youtube", callback_data="yt")
    btn2 = types.InlineKeyboardButton("Инстаграм", callback_data="inst")
    btn3 = types.InlineKeyboardButton("Знакомый в НН", callback_data="nn")
    btn4 = types.InlineKeyboardButton("ВК Дзен Дуэт", callback_data="vk")
    btn5 = types.InlineKeyboardButton("Telegram", callback_data="tg")
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    markup.add(btn5)
    bot.send_message(message.chat.id, text, parse_mode='HTML', reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    text = 'Привет, друг!\n\n'\
            'Это бот для выдачи Чек-Листа по заработку 50-100.000 рублей в месяц на Яндекс Дзене\n\n'\
            '❗Но хочу задать тебе один вопрос\n\n'\
            '✅ Как ты впервые узнал обо мне?'
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Youtube", callback_data="yt")
    btn2 = types.InlineKeyboardButton("Инстаграм", callback_data="inst")
    btn3 = types.InlineKeyboardButton("Знакомый в НН", callback_data="nn")
    btn4 = types.InlineKeyboardButton("ВК Дзен Дуэт", callback_data="vk")
    btn5 = types.InlineKeyboardButton("Telegram", callback_data="tg")
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    markup.add(btn5)
    bot.send_message(message.chat.id, text, parse_mode='HTML', reply_markup=markup)


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data in ['yt', 'inst', 'nn', 'vk', 'tg']:
            text1 = 'Все, спасибо 👌🏻\n\n'\
                    'Больше ничего не нужно - просто нажимай на кнопку ниже и бот выдаст тебе ссылку на PDF файл'
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton("Получить Чек-Лист", callback_data="check_list")
            markup.add(btn1)
            bot.send_photo(call.message.chat.id, open('ivan1.jpg', 'rb'))
            bot.send_message(call.message.chat.id, text1, parse_mode='Markdown', reply_markup=markup)
        if call.data == 'check_list':
            text1 = 'Отлично'\
                    '⚡Держи ссылку'\
                    'https://drive.google.com/file/d/1Ks3LgChLqju72YwIdBRTKP4r7Q3zJu_Y ⚡'\
                    'Инфа реально годная, надеюсь, ты оценишь её по достоинству '
            text2 = 'Друг\n\n'\
                    'Меня всегда учили: чтобы что-то получить - сначала нужно отдать взамен. Вот я и поделился Чек-Листом 📝\n\n'\
                    'Ни о чем просить не буду, просто оставлю ссылку на инстаграм, а ты уже решай, мы дружим или прощаемся 👉\n'\
                    'https://www.instagram.com/funtik_iv/\n\n'\
                    'В любом случае спасибо за уделенное время 💫'
            bot.send_message(call.message.chat.id, text1, parse_mode='Markdown')
            # bot.send_photo(call.message.chat.id, open('ivan1.jpg', 'rb'))
            bot.send_message(call.message.chat.id, text2, parse_mode='Markdown')
            bot.send_photo(call.message.chat.id, open('ivan2.jpg', 'rb'))
            

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
