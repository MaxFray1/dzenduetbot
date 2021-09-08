import os
import telebot
from flask import Flask, request
from telebot import types

TOKEN = '1955026785:AAGZbOk7sLGR6QqWHDo-SIuOWS_AG8FR8qk'
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
    text = 'Привет, друг!\n\nПошаговая инструкция по заработку 50-100.000 рублей в месяц на Яндекс Дзене у тебя почти в кармане' \
           '\n\n❗Но хочу тебя кое о чем попросить' \
           '\n\nПодпишись на мой Инстаграм 👉' \
           '\nhttps://www.instagram.com/funtik_iv/'
    keyboard = myKeyboard(1,'Готово', 'Yes1')
    bot.send_message(message.chat.id, text, parse_mode='HTML', reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    text = 'Привет. Хочешь получить Чек-лист "Яндекс Дзеню И как я на нем заработал 5🍋"?'
    keyboard = myKeyboard(1,'Да','Yes1')
    # bot.send_message(message.chat.id, text, parse_mode='HTML', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'Yes1':
            text1 = "Отлично[. ](https://i.imgur.com/YIsLVdg.png)\n\n" \
                    "Еще одна просьба - заполни, пожалуйста, анкету 📝\n" \
                    "https://forms.gle/SDvy9UXVt1xrQfAa6\n\n" \
                    "И, друзья, заполняйте по-чесноку всё. Инфа реально годная, а не очередная бесплатная херня. Всё о Дзене в одном файле.\n\n" \
                    "✅ После заполнении анкеты, Гугл выдаст тебе ссылку на чек-лист\n\n" \
                    "Дерзай ⚡"
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="📝 Заполнить Анкету", url="https://example.com")
            keyboard.add(url_button)
            # keyboard = myKeyboard(1,'📝 Заполнить Анкету', 'Yes666')
            bot.delete_message(call.message.chat.id, call.message.id)
            bot.send_message(call.message.chat.id, text1, parse_mode='Markdown', reply_markup=keyboard)
        elif call.data == 'No2':
            text1 = "Мне будет намного приятнее выдавать чек-лист, если ты на меня подпишешься https://www.instagram.com/funtik_iv/"
            keyboard = myKeyboard(1,'Готово', 'Yes2')
            bot.delete_message(call.message.chat.id, call.message.id)
            bot.send_message(call.message.chat.id, text=text1, parse_mode='HTML', reply_markup=keyboard)
        elif call.data == 'Yes2':
            text1 = 'Отлично, заполни небольшую гугл-форму. После чего получишь ссылку на чек-лист. https://forms.gle/vrBpiY6CKzd3QE177'
            bot.delete_message(call.message.chat.id, call.message.id)
            bot.send_message(call.message.chat.id, text=text1, parse_mode='Markdown')


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
