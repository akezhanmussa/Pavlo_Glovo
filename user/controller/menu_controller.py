import telebot
from view.main_menu_view import View
from constants import Constants

class MenuController :

    def __init__(self, bot):
        self.bot = bot
        self.view = View()
        self.data = Constants()
        self.dishes = Constants.DISHES_TYPES
        @self.bot.message_handler(commands = ["start"])
        def _process_start_message(message):
            self.process_start_message(message)

        @self.bot.message_handler(content_types = ["text"])
        def _process_user_message(message):
            self.process_user_message(message)

        @self.bot.callback_query_handler(func = lambda call: True)
        def _process_callback(call):
            self.process_callback(call)


    def process_start_message(self, message):
        menu = self.data.MAIN_MENU
        kb = self.view.reply_keyboard(menu)
        self.bot.send_message(message.chat.id, "Добро Пожаловать!", reply_markup = kb)

    def process_user_message(self, message):
        if message.text == "Меню":
            self.menu_button(message)

        if message.text == "Начало Нолана":
            self.process_start_message(message)

    def process_callback(self, call):
        if call.data in self.dishes and self.dishes[call.data] != None:
            kb = self.view.inline_keyboard(self.dishes[call.data])
            self.bot.send_message(call.message.chat.id, 'Выберите раздел, чтобы вывести список блюд:', reply_markup = kb)
        else :
            self.bot.send_message(call.message.chat.id, 'Ake pidor')


    def menu_button(self, message):
        kb = self.view.reply_keyboard(self.data.REPLY_BUTTONS)
        self.bot.send_message(message.chat.id, message.text, reply_markup = kb)
        names = []
        for dish in self.dishes:
            names.append(dish)
        kb = self.view.inline_keyboard(names)
        self.bot.send_message(message.chat.id, 'Выберите раздел, чтобы вывести список блюд:', reply_markup = kb)
