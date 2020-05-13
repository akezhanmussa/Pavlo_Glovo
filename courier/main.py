import telebot 
from constants import Constants
from controller.Controller import Controller
from telegram.ext import Updater


if __name__ == "__main__":
    '''
    This class, which employs the telegram.ext.Dispatcher, 
    provides a frontend to telegram.Bot to the programmer, 
    so they can focus on coding the bot. Its purpose is to 
    receive the updates from Telegram and to deliver them to said dispatcher
    '''
    updater = Updater(token=Constants.BOT_TOKEN.value, use_context=True)
    controller = Controller(updater.dispatcher)
    
    # Starts polling updates from Telegram.
    updater.start_polling(poll_interval=1)
    # Blocks until one of the signals are received and stops the updater.
    updater.idle()
    pass

    