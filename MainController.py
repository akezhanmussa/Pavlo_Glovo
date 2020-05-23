from telegram.ext import ConversationHandler, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, RegexHandler
from user.constants import Constants
from user.controller.menu_controller import MenuController
from user.controller.checkout_controller import CheckoutController
class MainController():

    def __init__(self, dispatcher):
        self.states_dict = {
            "menu": 1,
            "checkout": 2
        }
        self.dispatcher = dispatcher
        self.checkoutCont = CheckoutController()
        self.menuCont = MenuController(self.checkoutCont)
        self.__process_handlers()


    def __process_handlers(self):
        handler = ConversationHandler([CommandHandler("start", self.menuCont.process_start)], states = {
            self.states_dict["menu"]: [
            CallbackQueryHandler(self.menuCont.callback_handler),
            MessageHandler(Filters.text, self.menuCont.process_message_handler)
            ],
            self.states_dict["checkout"]: [
            CallbackQueryHandler(self.checkoutCont.process_callback_handler),
            MessageHandler(Filters.text, self.checkoutCont.process_checkout)
            ]
        }, fallbacks = [])
        self.dispatcher.add_handler(handler)
