from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton,ParseMode
import emoji
from constants import Constants

class BasketView:

    def __init__(self):

        self.first_view = [InlineKeyboardButton("Корзина", callback_data="inital_options")]
        
        self.options_view = [
            InlineKeyboardButton("X", callback_data="switch_to_inital_state",  resize_keyboard=True),
            InlineKeyboardButton("1 шт.", callback_data="no_reaction",  resize_keyboard=True),
            InlineKeyboardButton("^", callback_data="one_more",  resize_keyboard=True)
        ]


    def show_basket_label(self, update, context, is_first_time = True):
        chat_id = update.message.chat.id
        message_id = update.message.message_id
        reply_markup = InlineKeyboardMarkup(self.build_basket_options(self.first_view, n_cols=1) )
        if is_first_time:
            context.bot.send_photo(chat_id = chat_id, photo = Constants.BURGER_URL.value)
            context.bot.send_message(chat_id = chat_id, text = "Корзина", reply_markup=reply_markup, parse_mode= ParseMode.HTML)
        else:
            context.bot.edit_message_text(chat_id = chat_id, text = "Корзина", message_id = message_id, reply_markup=reply_markup)

    def show_basket_options(self, update, context): 
        chat_id = update.message.chat.id
        message_id = update.message.message_id
        n_cols = 3 if len(self.options_view) == 3 else 4
        reply_markup = InlineKeyboardMarkup(self.build_basket_options(self.options_view, n_cols=n_cols))
        context.bot.edit_message_text(chat_id = chat_id, text = "Корзина", message_id = message_id, reply_markup=reply_markup)

    def generate_options_view(self, num = 1):
        
        self.options_view = [
            InlineKeyboardButton("X", callback_data="switch_to_inital_state",  resize_keyboard=True),
            InlineKeyboardButton("-", callback_data="one_less",  resize_keyboard=True),
            InlineKeyboardButton(f"{num} шт.", callback_data="no_reaction",  resize_keyboard=True),
            InlineKeyboardButton("+", callback_data="one_more",  resize_keyboard=True)
        ]

        if (num == 1):
            del self.options_view[1]
        

    def build_basket_options(self, buttons, n_cols = 1, header_buttons=None, footer_buttons=None):
        menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
        if header_buttons:
            menu.insert(0, [header_buttons])
        if footer_buttons:
            menu.append([footer_buttons])
        return menu