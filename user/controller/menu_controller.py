from telegram.ext import ConversationHandler, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, RegexHandler
from user.view.main_menu_view import View
from user.constants import Constants
from user.controller.checkout_controller import CheckoutController
from basket.controller.DishListController import DishListController

class MenuController :

    def __init__(self, checkoutCont, dish_list_controller):
        self.states_dict = {
            "menu": 5,
            "checkout": 6
        }
        self.view = View()
        self.data = Constants()
        self.dishes = Constants.DISHES_TYPES
        self.checkoutCont = checkoutCont
        self.dish_list_controller = dish_list_controller

    def process_message_handler(self, bot, update):
        message = bot.message.text
        rt = ""
        if message == "Меню":
            rt = self.process_menu_message(bot, update)
        if message == "Начало":
            rt = self.process_start(bot, update)
        if message == "Оформить Заказ":
            rt = self.checkoutCont.process_checkout(bot, update)
        return rt

    def callback_handler(self, bot, update):
        query = bot.callback_query
        chat_id = query.message.chat.id
        if query.data in self.dishes and self.dishes[query.data] != None:
            kb = self.view.inline_keyboard(self.dishes[query.data])
            update.bot.send_message(chat_id, 'Выберите раздел, чтобы вывести список блюд:', reply_markup = kb)
            return self.states_dict["menu"]
        else :
            self.dish_list_controller.basket_button_handler(update = query, context = update)
            return self.dish_list_controller.states_dict['options_state']


    def process_start(self, bot, update):
        chat_id = bot.message.chat.id
        menu = self.data.MAIN_MENU
        kb = self.view.reply_keyboard(menu)
        update.bot.send_message(chat_id, "Добро Пожаловать!", reply_markup = kb)
        return self.states_dict["menu"]

    def process_menu_message(self, bot, update):
        #/// reply_buttons for user after menu pressed
        chat_id = bot.message.chat.id
        kb = self.view.reply_keyboard(self.data.REPLY_BUTTONS)
        update.bot.send_message(chat_id, bot.message.text, reply_markup = kb)
        #///
        names = []
        for dish in self.dishes:
            names.append(dish)
        kb = self.view.inline_keyboard(names)
        update.bot.send_message(chat_id, 'Выберите раздел, чтобы вывести список блюд:', reply_markup = kb)
