import os
import shutil
import pathlib
from instabot import Bot

def init_inst_bot():
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config')
    if pathlib.Path(path).exists():
        shutil.rmtree(path)
    
    global bot
    bot = Bot()
    bot.login(username="_cheiffa_", password="123456789Q!")

def check_follow(username):
    global bot
    user_id = bot.get_user_id_from_username (username)
    my_followers = bot.get_user_followers('funtik_iv')
    if user_id in my_followers:
        print("FOLLOW")
        return True
    else:
        print("UNFOLLOW")
        return False

