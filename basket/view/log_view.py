from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton


class LogMenuView: 
    """
    TestView class:
        the main responsibility of this class is 'sending messages of each state in bot'
        and also 'formatting of messages', etc.
    """
    
    def __init__(self):
        
        self.button_list = [
            InlineKeyboardButton("Начало", callback_data="switch_to_registration"),
            InlineKeyboardButton("Назад", callback_data="back_to_main_menu")
        ]

    def show_keyboard_menu(self, update, context):
        chat_id = update.message.chat.id
        print(chat_id)
        custom_keyboard = [[KeyboardButton('Регистрация'), KeyboardButton('Войти')], 
                   [            KeyboardButton('Инфо')]]
        reply_markup = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=chat_id, 
                        text="Добро пожаловать в систему курьеров!", 
                        reply_markup=reply_markup)

    def send_menu(self, update, context):
        chat_id = update.message.chat.id
        reply_markup = InlineKeyboardMarkup(self.build_log_menu(self.button_list, n_cols=1))
        context.bot.send_message(chat_id = chat_id, text = "Чтобы начать проходить опрос, нажмите Начать Опрос, если вы передумали нажмите Выйти", reply_markup=reply_markup)

    def send_message(self, update, context, message = "Hi"):
        chat_id = update.message.chat.id
        context.bot.send_message(chat_id=chat_id, text=message)

    def build_log_menu(self, buttons, n_cols, header_buttons=None, footer_buttons=None):
        menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
        if header_buttons:
            menu.insert(0, [header_buttons])
        if footer_buttons:
            menu.append([footer_buttons])
        return menu

    def call_registration(self): 
        print("Registration was called")