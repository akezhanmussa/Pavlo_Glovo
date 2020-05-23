from telegram.ext import ConversationHandler, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, RegexHandler
from user.view.main_menu_view import View
from user.constants import Constants

class CheckoutController :

    def __init__(self):
        self.states_dict = {
            "checkout": 2
        }
        self.userData = {
            "name": None,
            "delivery_method": "Самовывоз",
            "delivery_address": None,
            "time": None,
            "phone": None
        }
        self.ask = {
            "name": False,
            "delivery_method": False,
            "delivery_address": False,
            "time": False,
            "phone": False
        }
        self.view = View()
        self.chat_id = ""
        self.uid = ""

    def ask_name(self, bot, update):
        self.ask["name"] = True
        chat_id = bot.message.chat.id
        update.bot.send_message(chat_id, "Введите Ваше имя:")
        self.chat_id = chat_id
        self.uid = bot.message.from.id
        update.bot.delete_message(chat_id, uid)

    def ask_delivery_method(self, bot, update):
        self.ask["delivery_method"] = True
        self.userData["name"] = bot.message.text

        chat_id = bot.message.chat.id
        kb = self.view.inline_keyboard(["Курьер", "Самовывоз"])
        update.bot.send_message(chat_id, "Выберите Способ Доставки:", reply_markup = kb)


    def ask_delivery_address(self, bot, update):
        print("address")
        self.ask["delivery_address"] = True
        self.userData["delivery_method"] = "Курьер"
        query = bot.callback_query
        chat_id = query.message.chat.id

        update.bot.send_message(chat_id, "Укажите адрес доставки, господин барин: ")


    def ask_time(self, bot, update):
        self.ask["time"] = True
        query = bot.callback_query
        chat_id = query.message.chat.id
        self.userData["delivery_address"] = query.data

        kb = self.view.inline_keyboard(["Как можно скорее", "Укажите время"])
        update.bot.send_message(chat_id, "Выберите Время Доставки:", reply_markup = kb)

    def ask_phone_number(self, bot, update):
        self.ask["phone"] = True
        info = bot.message.text

        if self.userData["delivery_method"] == "Курьер":
            self.userData["delivery_address"] = info
        else:
            self.userData["time"] = info

        chat_id = bot.message.chat.id
        update.bot.send_message(chat_id, "Укажите номер телефона")

    def process_callback_handler(self, bot, update):
        data = bot.callback_query.data
        if data == "Самовывоз":
            self.ask["delivery_address"] = True
        self.process_checkout(bot, update)

    def process_checkout(self, bot, update):

        if self.ask["name"] == False:
            self.ask_name(bot, update)
        elif self.ask["delivery_method"] == False:
            self.ask_delivery_method(bot, update)
        elif self.ask["delivery_address"] == False:
            self.ask_delivery_address(bot, update)
        elif self.ask["time"] == False:
            self.ask_time(bot, update)
        elif self.ask["phone"] == False:
            self.ask_phone_number(bot, update)
        return self.states_dict["checkout"]
