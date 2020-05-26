<<<<<<< HEAD
import telebot
from constants import Constants
from controller.DishesListController import DishesListController
from controller.menu_controller import MenuController
=======
from constants import Constants
from controller.DishesListController import DishesListController
from controller.BasketContoller import BasketController
# from controller.MainController import MainContoller
>>>>>>> 699b6180a008cdf1b5cc81a5a82b3e94b324687c
from telegram.ext import Updater


if __name__ == "__main__":
    '''
    This class, which employs the telegram.ext.Dispatcher,
    provides a frontend to telegram.Bot to the programmer,
    so they can focus on coding the bot. Its purpose is to
    receive the updates from Telegram and to deliver them to said dispatcher
    '''
<<<<<<< HEAD
=======
    updater = Updater(token=Constants.BOT_TOKEN.value, use_context=True)
    # dish_controller = MainContoller(updater.dispatcher)
>>>>>>> 699b6180a008cdf1b5cc81a5a82b3e94b324687c

    updater = Updater(token=Constants.BOT_TOKEN, use_context=True)
    # dish_controller = DishesListController(updater.dispatcher)
    menu_controller = MenuController(updater.dispatcher)
    # Starts polling updates from Telegram.
    updater.start_polling(poll_interval=1)
    # Blocks until one of the signals are received and stops the updater.
    updater.idle()
    pass
