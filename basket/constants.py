from enum import Enum

class Constants():
    # BOT_TOKEN = "1154427910:AAHfvVd5Rgb-m8wgAUoOd2k2Twk1MZ1JEVE"
    BURGER_URL = "https://rtvi.com/upload/iblock/58e/58e23f14e52fe081141c45cb39a56fd4.jpg"
    BURGER_NAME = "Сочный мощный"
    INGREDIENTS = "хлеб, котлета, кетчуп, помидор"
    PRICE = 1490
    CURRENCY = "тг."

    BOT_TOKEN = "1078825446:AAET3qLCbC8mj7SCoIlNGQnX1LiAMc0GADU"
    SNACKS_TYPES = ["Холодные Закуски", "Горячие Закуски", "К Пиву"]
    SALADE_TYPES = ["1 Salad", "2 Salad", "Potato Salad"]
    DISHES_TYPES = {"Закуски": SNACKS_TYPES, "Салаты": SALADE_TYPES, "Супы": None, "Горячие": None}
    MAIN_MENU = ["Меню", "Корзина", "Отзывы", "О нас"]
    REPLY_BUTTONS = ["Начало Нолана", "Корзина", "Меню"]
    ALL_DISHES = ["Холодные Закуски", "Горячие Закуски", "К Пиву", "1 Salad", "2 Salad", "Potato Salad", "Супы", "Горячие"]
