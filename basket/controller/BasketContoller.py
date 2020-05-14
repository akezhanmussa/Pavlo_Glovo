from telegram.ext import ConversationHandler, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, RegexHandler
from view.basket_view import BasketView

class BasketController:
 
    def __init__(self, dispatcher):
        self.states_dict = {
            "basket_label_state": 1,
            "options_state": 2
        }
        self.counter = 0
        self.dispatcher = dispatcher
        self.__process_handlers()
        self.basket_view = BasketView()
 
    

    def basket_button_handler(self, update, context):
        self.basket_view.show_basket_label(update, context, is_first_time=True)
        return self.states_dict["options_state"]

    def operations_handler(self, update, context):
        query = update.callback_query

        if (query.data == "switch_to_inital_state"):
            self.basket_view.show_basket_label(query, context, is_first_time=False)
            return self.states_dict["options_state"]
        
        if (query.data == "one_more"):
            self.counter += 1
        elif (query.data == "one_less"):
            self.counter -= 1
        elif (query.data == "inital_options"):
            self.counter = 1

        self.basket_view.generate_options_view(self.counter)
        self.basket_view.show_basket_options(query, context)
        return self.states_dict["options_state"]


    def __process_handlers(self):
        conversation_handler = ConversationHandler(entry_points=[CommandHandler("basket",self.basket_button_handler)],
                                                   states={
                                                       self.states_dict["options_state"]: [
                                                           CallbackQueryHandler(self.operations_handler)],
                                                       self.states_dict["basket_label_state"]: [
                                                           CallbackQueryHandler(self.basket_button_handler)]
                                                   }, fallbacks=[], allow_reentry=True)
        
        #  Dispatcher that handles the updates and dispatches them to the handlers.
        self.dispatcher.add_handler(conversation_handler)

