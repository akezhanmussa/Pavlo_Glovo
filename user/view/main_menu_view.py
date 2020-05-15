import telebot
from telebot.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton


class View:

    def user_keyboard(self):
        keyboard = ReplyKeyboardMarkup(row_width = 2)
        keyboard.add("Меню", "Корзина")
        return keyboard

    def inline_keyboard(self, names):
        keyboard = InlineKeyboardMarkup(row_width = 2)
        length = len(names)
        ok = 0
        if length % 2 != 0 :
            ok = 1
            length -= 1

        for i in range(0, length, 2):
            button1 = InlineKeyboardButton(names[i], callback_data = names[i])
            button2 = InlineKeyboardButton(names[i + 1], callback_data = names[i + 1])
            keyboard.add(button1, button2)

        if ok == 1:
            button = InlineKeyboardButton(names[-1], callback_data = names[-1])
            keyboard.add(button)

        return keyboard
