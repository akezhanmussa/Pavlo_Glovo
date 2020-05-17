import telebot
from telebot.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton


class View:

    def buttons(self, keyboard, names) :
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

    def reply_keyboard(self, names):
        keyboard = ReplyKeyboardMarkup(row_width = 2)
        self.buttons(keyboard, names)

        return keyboard

    def inline_keyboard(self, names):
        keyboard = InlineKeyboardMarkup(row_width = 2)
        self.buttons(keyboard, names)

        return keyboard
