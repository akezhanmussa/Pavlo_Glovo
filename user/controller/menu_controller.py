import telebot
from view.main_menu_view import View
from constants import Constants

class MenuController :

    def __init__(self, bot):
        self.bot = bot
        self.view = View()
        self.data = Constants()

        @self.bot.message_handler(commands=["start"])
        def _process_start_message(message):
            self.process_start_message(message)

        @self.bot.message_handler(content_types = ["text"])
        def _process_user_message(message):
            self.process_user_message(message)

    def process_start_message(self, message):
        kb = self.view.user_keyboard()
        self.bot.send_message(message.chat.id, "Добро Пожаловать!", reply_markup = kb)

    def process_user_message(self, message):
        if message.text == "Меню":
            kb = self.view.dishes_keyboard(self.data.TYPES_DISHES)
            self.bot.send_message(message.chat.id, 'Выберите раздел, чтобы вывести список блюд:', reply_markup = kb)
