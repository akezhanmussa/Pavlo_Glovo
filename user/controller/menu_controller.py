from telegram.ext import ConversationHandler, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, RegexHandler
<<<<<<< HEAD
from view.main_menu_view import View
from constants import Constants


class MenuController :

    def __init__(self, dispatcher):

        self.states_dict = {
            "Меню": 1
        }

        self.dispatcher = dispatcher
        self.view = View()
        self.data = Constants()
        self.dishes = Constants.DISHES_TYPES
        mm = MessageHandler(Filters.text | Filters.command, self.process_handler)
        handler = ConversationHandler([CommandHandler("start", self.process_handler)], states = {
            self.states_dict["Меню"]: [CallbackQueryHandler(self.xxx)]
        }, fallbacks = [])
        self.dispatcher.add_handler(handler)
        self.dispatcher.add_handler(mm)


    def xxx(self, bot, update):
        query = bot.callback_query
        message = query.data
        chat_id = query.message.chat.id
        update.bot.send_message(chat_id, message)

    def process_handler(self, bot, update):
        message = bot.message.text
        if message == "/start":
            self.process_start_message(bot, update)
        if message == "Меню":
            self.process_menu_message(bot, update)
        return self.states_dict["Меню"]

    def process_start_message(self, bot, update):
=======
from user.view.main_menu_view import View
from user.constants import Constants
from user.controller.checkout_controller import CheckoutController

class MenuController :

    def __init__(self, checkoutCont):
        self.states_dict = {
            "menu": 1,
            "checkout": 2
        }
        self.view = View()
        self.data = Constants()
        self.dishes = Constants.DISHES_TYPES
        self.checkoutCont = checkoutCont

    def process_message_handler(self, bot, update):
        message = bot.message.text
        rt = ""
        if message == "Меню":
            rt = self.process_menu_message(bot, update)
        if message == "Начало":
            rt = self.process_start(bot, update)
        if message == "Корзина":
            rt = self.checkoutCont.process_checkout(bot, update)
        return rt

    def callback_handler(self, bot, update):
        query = bot.callback_query
        chat_id = query.message.chat.id
        if query.data in self.dishes and self.dishes[query.data] != None:
            kb = self.view.inline_keyboard(self.dishes[query.data])
            update.bot.send_message(chat_id, 'Выберите раздел, чтобы вывести список блюд:', reply_markup = kb)
        else :
            update.bot.send_message(chat_id, 'Ake pidor')
        return self.states_dict["menu"]

    def process_start(self, bot, update):
>>>>>>> kuka
        chat_id = bot.message.chat.id
        menu = self.data.MAIN_MENU
        kb = self.view.reply_keyboard(menu)
        update.bot.send_message(chat_id, "Добро Пожаловать!", reply_markup = kb)
<<<<<<< HEAD

    def process_callback(self, call):
        if call.data in self.dishes and self.dishes[call.data] != None:
            kb = self.view.inline_keyboard(self.dishes[call.data])
            self.bot.send_message(call.message.chat.id, 'Выберите раздел, чтобы вывести список блюд:', reply_markup = kb)
        else :
            self.bot.send_message(call.message.chat.id, 'Ake pidor')

=======
        return self.states_dict["menu"]
>>>>>>> kuka

    def process_menu_message(self, bot, update):
        #/// reply_buttons for user after menu pressed
        chat_id = bot.message.chat.id
        kb = self.view.reply_keyboard(self.data.REPLY_BUTTONS)
        update.bot.send_message(chat_id, bot.message.text, reply_markup = kb)
<<<<<<< HEAD

=======
>>>>>>> kuka
        #///
        names = []
        for dish in self.dishes:
            names.append(dish)
        kb = self.view.inline_keyboard(names)
        update.bot.send_message(chat_id, 'Выберите раздел, чтобы вывести список блюд:', reply_markup = kb)
