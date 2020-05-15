import telebot
from constants import Constants
from controller.menu_controller import MenuController

if __name__  == "__main__" :

    bot = telebot.TeleBot(Constants.BOT_TOKEN)
    controller = MenuController(bot)

    bot.polling()
