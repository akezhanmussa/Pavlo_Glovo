import telebot

bot = telebot.TeleBot('1078825446:AAET3qLCbC8mj7SCoIlNGQnX1LiAMc0GADU')

menuNames = ["Закуски", "Салаты", "Супы", "Горячие", "Пивво ежже"]


def start_menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width = 2)
    keyboard.add("Меню", "Корзина")
    return keyboard


def dishes_keyboard(names):
    keyboard = telebot.types.InlineKeyboardMarkup(row_width = 2)
    length = len(names)
    ok = 0
    if length % 2 != 0 :
        ok = 1
        length -= 1

    for i in range(0, length, 2):
        button1 = telebot.types.InlineKeyboardButton(names[i], callback_data = names[i])
        button2 = telebot.types.InlineKeyboardButton(names[i + 1], callback_data = names[i + 1])
        keyboard.add(button1, button2)

    if ok == 1:
        button = telebot.types.InlineKeyboardButton(names[-1], callback_data = names[-1])
        keyboard.add(button)

    return keyboard


@bot.message_handler(commands = ["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Добро Пожаловать!", reply_markup = start_menu())

@bot.message_handler(content_types = ["text"])
def start_message(message):
    if (message.text == "Меню"):
        # bot.send_message(message.chat.id, "Меню", reply_markup = start_menu())
        keyboard = dishes_keyboard(menuNames)
        bot.send_message(message.chat.id, 'Выберите раздел, чтобы вывести список блюд:', reply_markup = keyboard)


@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == "first":
        bot.send_message(call.message.chat.id, text = "menu1")

bot.polling()
