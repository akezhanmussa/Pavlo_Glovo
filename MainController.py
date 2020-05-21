from telegram.ext import ConversationHandler, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, RegexHandler
from basket.view.basket_view import BasketView
from basket.view.basket_menu_view import BasketMenuView
from basket.controller.TestController import TestController

DISH_NUM = 4

class MainController():
 
    def __init__(self, dispatcher):
        self.states_dict = {
            "basket_label_state": 1,
            "options_state": 2
            }
        self.dispatcher     = dispatcher
        self.test_controller = TestController()
        self.__process_handlers()

    def basket_command_handler(self, update, context):
        print(update.message.chat.id)
        print("Before calling handler")
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

