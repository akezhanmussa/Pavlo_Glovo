from telegram.ext import ConversationHandler, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, RegexHandler
from view.basket_view import BasketView
from view.basket_menu_view import BasketMenuView
from constants import Constants
DISH_NUM = 4

class DishesListController:

    def __init__(self):
        self.states_dict = {
            "basket_label_state": 1,
            "options_state": 2
        }
        # self.dispatcher     = dispatcher
        # self.__process_handlers()
        self.basket_views   = [BasketView(index = index) for index in range(DISH_NUM)]
        self.log_menu_view  = BasketMenuView(title = "Список блюд")
        self.users          = {}
        self.shitData = Constants.ALL_DISHES

    def basket_button_handler(self, update, context):
        print(update.message.text)
        # new_user = update.message.from_user["username"]
        # if update.message.text in shitData:
        #     print("here")
        #     chat_id = update.message.chat.id
        #     self.log_menu_view.show_keyboard_menu(update, context, text = "Корзина")
        #
        #     if (not chat_id in self.users):
        #         self.users[chat_id] = {}
        #
        #     for basket_index in range(DISH_NUM):
        #         self.users[chat_id][basket_index] = 0
        #
        #     for index in range(DISH_NUM):
        #         self.basket_views[index].show_basket_label(update, context, is_first_time=True)
        #
        #     return self.states_dict["options_state"]

        print("here")
        chat_id = update.message.chat.id
        self.log_menu_view.show_keyboard_menu(update, context, text = "Корзина")

        if (not chat_id in self.users):
            self.users[chat_id] = {}

        for basket_index in range(DISH_NUM):
            self.users[chat_id][basket_index] = 0

        for index in range(DISH_NUM):
            self.basket_views[index].show_basket_label(update, context, is_first_time=True)

        return self.states_dict["options_state"]


    def operations_handler(self, update, context):

        query = update.callback_query
        chat_id = query.message.chat.id

        data = query.data
        splitted_data = data.split('_')
        basket_index = int(splitted_data[-1])

        if (data == f"switch_to_inital_state_{basket_index}"):
            self.basket_views[basket_index].show_basket_label(query, context, is_first_time=False)
            return self.states_dict["options_state"]

        if (data == f"one_more_{basket_index}"):
            self.users[chat_id][basket_index] += 1
        elif (data == f"one_less_{basket_index}"):
            self.users[chat_id][basket_index] -= 1
        elif (data == f"inital_options_{basket_index}"):
            self.users[chat_id][basket_index] = 1

        self.basket_views[basket_index].generate_options_view(self.users[chat_id][basket_index])
        self.basket_views[basket_index].show_basket_options(query, context)
        return self.states_dict["options_state"]

    def bask_evaluate_handler(self, update, context):
        chat_id = update.message.chat.id
        print(chat_id)
        if update.message["text"] == "Корзина":
            self.log_menu_view.send_price_details(update = update, context = context, price_details= self.calculate_total_sum(chat_id=chat_id))
        self.log_menu_view.show_keyboard_menu(update, context, text = "Корзина")

    def calculate_total_sum(self, chat_id):
        total_price = 0
        currency = ""
        for basket_index, view in enumerate(self.basket_views):
            if currency == "":
                currency = view.currency
            total_price += view.price * self.users[chat_id][basket_index]
        return f"{total_price} {currency}"

    def process_handlers(self):

        conversation_handler = ConversationHandler(entry_points=[CommandHandler(["basket"], self.basket_button_handler)],
                                                   states={
                                                       self.states_dict["options_state"]: [
                                                           CallbackQueryHandler(self.operations_handler),
                                                           MessageHandler(Filters.text, self.bask_evaluate_handler)],
                                                       self.states_dict["basket_label_state"]: [
                                                           CallbackQueryHandler(self.basket_button_handler)]
                                                   }, fallbacks=[], allow_reentry=True)
        #  Dispatcher that handles the updates and dispatches them to the handlers.
        return conversation_handler
        # self.dispatcher.add_handler(conversation_handler)
        # self.dispatcher.add_handler(handler)
