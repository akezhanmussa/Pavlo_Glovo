from telegram.ext import ConversationHandler, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, RegexHandler
from view.main_menu_view import View
from constants import Constants
from controller.DishesListController import DishesListController

class MenuController :

    def __init__(self, dispatcher):

        self.states_dict = {
            "Меню": 1
        }

        self.dispatcher = dispatcher
        self.view = View()
        self.data = Constants()
        self.dishes = Constants.DISHES_TYPES
        akeController = DishesListController()
        mm = MessageHandler(Filters.text | Filters.command, self.process_handler)
        handler = ConversationHandler([CommandHandler("start", self.process_handler)], states = {
            self.states_dict["Меню"]: [CallbackQueryHandler(self.xxx)]
        }, fallbacks = [])
        handlers = akeController.process_handlers()
        self.dispatcher.add_handler(handlers)

        self.dispatcher.add_handler(handler)
        self.dispatcher.add_handler(mm)

    def xxx(self, bot, update):
        # DishesListController(self.dispatcher)
        query = bot.callback_query
        message = query.data
        print(message)
        # chat_id = query.message.chat.id
        # update.bot.send_message(chat_id, message)

    def process_handler(self, bot, update):
        message = bot.message.text
        if message == "/start":
            self.process_start_message(bot, update)
        if message == "Меню":
            self.process_menu_message(bot, update)
        return self.states_dict["Меню"]

    def process_start_message(self, bot, update):
        chat_id = bot.message.chat.id
        menu = self.data.MAIN_MENU
        kb = self.view.reply_keyboard(menu)
        update.bot.send_message(chat_id, "Добро Пожаловать!", reply_markup = kb)

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
