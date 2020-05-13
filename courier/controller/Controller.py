from telegram.ext import ConversationHandler, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, RegexHandler
from view.view import LogMenuView

class Controller:
 
    states_dict = {
        "step_1": 1,
        "step_2": 2,
        "step_3": 3
    }

    def __init__(self, dispatcher):
        self.dispatcher = dispatcher
        self.__process_handlers()
        self.log_view = LogMenuView()

    def main_menu(self, update, context):
        self.log_view.show_keyboard_menu(update, context)
        return self.states_dict["step_2"]

    def login_handler(self, update, context):
        query = update.callback_query
        print(query.data)
        return self.states_dict["step_2"]
        
    def registration_handle(self, update, context):
        self.log_view.send_message(update, context, "Для прохождения регистрации, нужно ответить на неслколько вопросов")
        self.log_view.send_menu(update, context)
        return self.states_dict["step_2"]


    def __process_handlers(self):
        conversation_handler = ConversationHandler(entry_points=[CommandHandler("start", self.main_menu)],
                                                   states={
                                                       self.states_dict["step_3"]: [
                                                           CallbackQueryHandler(self.login_handler)],
                                                       self.states_dict["step_2"]: [
                                                           MessageHandler(Filters.text, self.registration_handle)]
                                                   }, fallbacks=[], allow_reentry=True)
        
        #   Dispatcher that handles the updates and dispatches them to the handlers.
        self.dispatcher.add_handler(conversation_handler)

