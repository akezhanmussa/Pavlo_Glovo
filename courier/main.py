import telebot 
from constants import Constants



bot = telebot.TeleBot(Constants.BOT_TOKEN.value)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


bot.polling()

# if __name__ == "__main__":
    


#     pass

    