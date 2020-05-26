from telegram.ext import ConversationHandler, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, RegexHandler
<<<<<<< HEAD
from basket.controller.DishListController import DishListController

DISH_NUM = 4

class MainController():
 
    def __init__(self, dispatcher):
        self.states_dict        = {
            "basket_label_state": 1,
            "options_state": 2
            }
        self.dispatcher         = dispatcher
        self.test_controller    = DishListController()
        self.__process_handlers()

    def basket_command_handler(self, update, context):
        return self.test_controller.basket_button_handler(update, context)
    
    def __process_handlers(self):
        conversation_handler = ConversationHandler(entry_points=[CommandHandler("basket",self.basket_command_handler)],
                                                   states={
                                                       self.states_dict["options_state"]: [
                                                           CallbackQueryHandler(self.test_controller.operations_handler),
                                                           MessageHandler(Filters.text, self.test_controller.bask_evaluate_handler)],
                                                       self.states_dict["basket_label_state"]: [
                                                           CallbackQueryHandler(self.test_controller.basket_button_handler)]
                                                   }, fallbacks=[], allow_reentry=True)
        
        #  Dispatcher that handles the updates and dispatches them to the handlers.
        self.dispatcher.add_handler(conversation_handler)

=======
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
            MessageHandler(Filters.text | Filters.contact, self.checkoutCont.process_checkout)
            ]
        }, fallbacks = [])
        self.dispatcher.add_handler(handler)
>>>>>>> kuka
