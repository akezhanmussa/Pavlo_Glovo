from telegram.ext import ConversationHandler, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, RegexHandler
from user.constants import Constants
from user.controller.menu_controller import MenuController
from user.controller.checkout_controller import CheckoutController
from basket.controller.DishListController import DishListController

class MainController():

    def __init__(self, dispatcher):
        self.states_dict = {
            "menu": 5,
            "checkout": 6,
            "basket_label_state": 1,
            "options_state": 2
        }
        self.dispatcher             = dispatcher
        self.checkoutCont           = CheckoutController()
        self.dish_list_controller   = DishListController()
        self.menu_controller        = MenuController(self.checkoutCont, dish_list_controller = self.dish_list_controller)


        self.__process_handlers()

    def __process_handlers(self):
        handler = ConversationHandler([CommandHandler("start", self.menu_controller.process_start)],
            states = {
                self.states_dict["menu"]: [
                    CallbackQueryHandler(self.menu_controller.callback_handler),
                    MessageHandler(Filters.text, self.menu_controller.process_message_handler)
                    ],
                self.states_dict["checkout"]: [
                    CallbackQueryHandler(self.checkoutCont.process_callback_handler),
                    MessageHandler(Filters.text | Filters.contact, self.checkoutCont.process_checkout)
                    ],
                self.states_dict["options_state"]: [
                    CallbackQueryHandler(self.dish_list_controller.operations_handler),
                    MessageHandler(Filters.text, self.dish_list_controller.bask_evaluate_handler)
                    ]
        }, fallbacks = [])

        self.dispatcher.add_handler(handler)
