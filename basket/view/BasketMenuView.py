from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton,ParseMode


class BasketMenuView(): 
    
    def __init__(self, title):
        self.title = title
        self.custom_keyboard = [[KeyboardButton('Начало'), KeyboardButton('Корзина')], 
                   [            KeyboardButton('Меню')]]
    
    def send_price_details(self, update, context, price_details = "100 тг"):
        chat_id = update.message.chat.id
        context.bot.send_message(chat_id=chat_id, text=f"<b>{price_details}</b>", parse_mode= ParseMode.HTML)

    def send_warning_message(self, update, context, warning_message = "Вы не выбрали никаких блюд"):
        chat_id = update.message.chat.id
        context.bot.send_message(chat_id=chat_id, text=f"<b>{warning_message}</b>", parse_mode= ParseMode.HTML)

    def show_keyboard_menu(self, update, context, text = ""):
        chat_id = update.message.chat.id
        reply_markup = ReplyKeyboardMarkup(self.custom_keyboard, resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=chat_id, 
                        text=text, 
                        reply_markup=reply_markup)
