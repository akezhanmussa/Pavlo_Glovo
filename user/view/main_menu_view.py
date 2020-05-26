from telegram import InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton

class View:

    def build_menu(self, buttons, n_cols, header_buttons=None, footer_buttons=None):
        menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
        if header_buttons:
            menu.insert(0, [header_buttons])
        if footer_buttons:
            menu.append([footer_buttons])
        return menu

    def get_buttons(self, names) :
        buttons = []
        for name in names:
            button = InlineKeyboardButton(name, callback_data = name)
            buttons.append(button)

        return buttons

    def contact_keyboard(self):
        keyboard = ReplyKeyboardMarkup([[KeyboardButton('Отправить контактный номер', request_contact=True)]])
        return keyboard

    def reply_keyboard(self, names):
        button_list = self.get_buttons(names)
        bt = self.build_menu(button_list, n_cols = 2)
        keyboard = ReplyKeyboardMarkup(bt)

        return keyboard

    def inline_keyboard(self, names):
        button_list = self.get_buttons(names)
        bt = self.build_menu(button_list, n_cols = 2)
        keyboard = InlineKeyboardMarkup(bt)

        return keyboard
