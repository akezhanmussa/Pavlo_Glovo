import telebot
from constants import Constants
from controller.menu_controller import MenuController
from telegram.ext import Updater

if __name__  == "__main__" :

    updater = Updater(token=Constants.BOT_TOKEN, use_context=True)
    menu_controller = MenuController(updater.dispatcher)

    # Starts polling updates from Telegram.
    updater.start_polling(poll_interval=1)
    # Blocks until one of the signals are received and stops the updater.
    updater.idle()
    pass
