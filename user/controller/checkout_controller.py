from telegram.ext import ConversationHandler, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, RegexHandler
from telegram import InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton
from user.view.main_menu_view import View
from user.constants import Constants

class CheckoutController :

    def __init__(self):
        self.states_dict = {
            "checkout": 6
        }
        self.userData = {
            "name": None,
            "delivery_method": "Самовывоз",
            "delivery_address": None,
            "time_option": "Как можно скорее",
            "time": "Как можно скорее",
            "phone": None
        }
        self.ask = {
            "name": False,
            "delivery_method": False,
            "delivery_address": False,
            "time_option": False,
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
        # self.chat_id = chat_id
        # self.uid = bot.message.from_user.id
        # print(self.uid)
        # update.bot.deleteMessage(uid, chat_id)
        # print("here")

    def ask_delivery_method(self, bot, update):
        self.ask["delivery_method"] = True
        self.userData["name"] = bot.message.text

        chat_id = bot.message.chat.id
        kb = self.view.inline_keyboard(["Курьер", "Самовывоз"])
        update.bot.send_message(chat_id, "Выберите Способ Доставки:", reply_markup = kb)


    def ask_delivery_address(self, bot, update):
        self.ask["delivery_address"] = True
        self.userData["delivery_method"] = "Курьер"
        query = bot.callback_query
        chat_id = query.message.chat.id
        kb = self.view.contact_keyboard()
        update.bot.send_message(chat_id, "Укажите адрес доставки, господин барин: ")

    def ask_time_option(self, bot, update):
        self.ask["time_option"] = True
        text = ""
        if self.userData["delivery_method"] == "Курьер":
            chat_id = bot.message.chat.id
            self.userData["delivery_address"] = bot.message.text
            text = "Выберите Время Доставки:"
        else:
            chat_id = bot.callback_query.message.chat.id
            self.userData["delivery_address"] = "Самовывоз"
            text = "Укажите Когда Вам Удобно Забрать:"

        kb = self.view.inline_keyboard(["Как можно скорее", "Укажите время"])
        update.bot.send_message(chat_id, text, reply_markup = kb)

    def ask_exact_time(self, bot, update):
        self.ask["time"] = True
        query = bot.callback_query
        chat_id = query.message.chat.id
        self.userData["time_option"] = query.message.text

        update.bot.send_message(chat_id, "Укажите удобное время (в формате ЧЧ:ММ, например 18:30):")

    def ask_phone_number(self, bot, update):
        self.ask["phone"] = True
        if self.userData["time_option"] == "Как можно скорее":
            chat_id = bot.callback_query.message.chat.id
            self.userData["time"] = "Как можно скорее"
        else:
            chat_id = bot.message.chat.id
            self.userData["time"] = bot.message.text

        kb = self.view.contact_keyboard()
        update.bot.send_message(chat_id, "Укажите свой контактный номер:", reply_markup = kb)

    def finish_asking(self, bot, update):
        print("here")
        phone = bot.message.contact.phone_number
        chat_id = bot.message.chat.id
        self.userData["phone"] = phone
        for x in self.userData:
            print(x + ": " + self.userData[x])
        update.bot.send_message(chat_id, "Спасибо, ожидайте заказа.")

    def process_callback_handler(self, bot, update):
        data = bot.callback_query.data
        if data == "Самовывоз":
            self.ask["delivery_address"] = True
        elif data == "Как можно скорее":
            self.ask["time"] = True
        self.process_checkout(bot, update)

    def process_checkout(self, bot, update):
        if self.ask["name"] == False:
            self.ask_name(bot, update)
        elif self.ask["delivery_method"] == False:
            self.ask_delivery_method(bot, update)
        elif self.ask["delivery_address"] == False:
            self.ask_delivery_address(bot, update)
        elif self.ask["time_option"] == False:
            self.ask_time_option(bot, update)
        elif self.ask["time"] == False:
            self.ask_exact_time(bot, update)
        elif self.ask["phone"] == False:
            self.ask_phone_number(bot, update)
        else:
            self.finish_asking(bot, update)
        return self.states_dict["checkout"]
