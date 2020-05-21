from telegram.ext import ConversationHandler, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, RegexHandler
from user.constants import Constants
from user.controller.menu_controller import MenuController

class MainController():

    def __init__(self, dispatcher):
        self.states_dict = {
            "menu": 1
        }
        self.dispatcher = dispatcher
        self.menuController = MenuController()
        self.__process_handlers()


    def process_handler(self, bot, update):
        return self.menuController.process_start(bot, update)


    def __process_handlers(self):
        handler = ConversationHandler([CommandHandler("start", self.process_handler)], states = {
            self.states_dict["menu"]: [
            CallbackQueryHandler(self.menuController.callback_handlers),
            MessageHandler(Filters.text, self.menuController.process_message_handler)
            ]
        }, fallbacks = [])
        self.dispatcher.add_handler(handler)
