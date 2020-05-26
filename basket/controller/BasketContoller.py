from telegram.ext import ConversationHandler, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, RegexHandler
from basket.view.BasketView import BasketView

class BasketController:
 
    def __init__(self, dispatcher):
        self.states_dict = {
            "basket_label_state": 1,
            "options_state": 2
        }
        self.dispatcher = dispatcher
        self.__process_handlers()
        self.basket_view = BasketView(index = 1) 
        self.users = {}

    def basket_button_handler(self, update, context):
        # new_user = update.message.from_user["username"]
        chat_id = update.message.chat.id
        if (not chat_id in self.users):
            self.users[chat_id] = 0
        self.basket_view.show_basket_label(update, context, is_first_time=True)
        return self.states_dict["options_state"]

    def operations_handler(self, update, context):
        query = update.callback_query
        chat_id = query.message.chat.id

        if (query.data == "switch_to_inital_state"):
            self.basket_view.show_basket_label(query, context, is_first_time=False)
            return self.states_dict["options_state"]
        
        if (query.data == "one_more"):
            self.users[chat_id] += 1
        elif (query.data == "one_less"):
            self.users[chat_id] -= 1
        elif (query.data == "inital_options"):
            self.users[chat_id] = 1

        self.basket_view.generate_options_view(self.users[chat_id])
        self.basket_view.show_basket_options(query, context)
        
        return self.states_dict["options_state"]


    def __process_handlers(self):
        conversation_handler = ConversationHandler(entry_points=[CommandHandler("basket_2",self.basket_button_handler)],
                                                   states={
                                                       self.states_dict["options_state"]: [
                                                           CallbackQueryHandler(self.operations_handler)],
                                                       self.states_dict["basket_label_state"]: [
                                                           CallbackQueryHandler(self.basket_button_handler)]
                                                   }, fallbacks=[], allow_reentry=True)
        
        #  Dispatcher that handles the updates and dispatches them to the handlers.
        self.dispatcher.add_handler(conversation_handler)

