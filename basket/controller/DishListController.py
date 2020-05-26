from telegram.ext import ConversationHandler, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, RegexHandler
from basket.view.BasketView import BasketView
from basket.view.BasketMenuView import BasketMenuView
from basket.view.DishChoosenView import DishChoosenView

DISH_NUM = 4

class DishListController():
 
    def __init__(self):
        self.states_dict = {
            "basket_label_state": 1,
            "options_state": 2
        }

        self.basket_views       = [BasketView(index = index) for index in range(DISH_NUM)]
        self.log_menu_view      = BasketMenuView(title = "Список блюд")
        self.users              = {}
        self.choosen_dish_view  = None

    def basket_button_handler(self, update, context):

        chat_id = update.message.chat.id
        self.log_menu_view.show_keyboard_menu(update, context, text = "Корзина")
        
        if (not chat_id in self.users):
            self.users[chat_id] = {}

        for basket_index in range(DISH_NUM):
            self.users[chat_id][basket_index] = 0
        
        # initializing the dish choosen view in accordnace to the chat id of the user

        for index in range(DISH_NUM):
            self.basket_views[index].show_basket_label(update, context, is_first_time=True)

        return self.states_dict["options_state"]

    def operations_handler(self, update, context):
        
        query   = update.callback_query
        chat_id = query.message.chat.id

        data                    = query.data
        splitted_data           = data.split('_')
        attribute_for_chosen    = data.split("/")
        basket_index            = int(splitted_data[-1])
        was_clicked_by_choosen  = False
        detail                  = ""
        
        if (attribute_for_chosen[0] == 'chosen'):
            was_clicked_by_choosen = True
            detail = 'chosen/'

        if (data == f"{detail}switch_to_inital_state_{basket_index}"):
            
            self.users[chat_id][basket_index] = 0

            # was clicked by not the busket button in keyboard menu
            if not was_clicked_by_choosen:
                self.basket_views[basket_index].show_basket_label(query, context, is_first_time=False)
            else: 
                # deleting the choosen dish 
                if self.choosen_dish_view.delete_dish(index = basket_index):
                    self.choosen_dish_view.setup_dishes_view()
                    self.choosen_dish_view.generate_dish_choosen_view()
                    self.choosen_dish_view.show_dish_choosen_view(query, context, is_first_time=False)
                else:
                    self.log_menu_view.send_warning_message(update = query, context = context)

            return self.states_dict["options_state"]
        
        if (data == f"{detail}one_more_{basket_index}"):
            self.users[chat_id][basket_index] += 1
        elif (data == f"{detail}one_less_{basket_index}"):
            self.users[chat_id][basket_index] -= 1
        elif (data == f"{detail}inital_options_{basket_index}"):
            self.users[chat_id][basket_index] = 1
        
        if self.choosen_dish_view is not None:
            self.choosen_dish_view.count_number_of_selected_dishes(dishes = self.users[chat_id])
        
        if not was_clicked_by_choosen:
            self.basket_views[basket_index].generate_options_view(self.users[chat_id][basket_index])
            self.basket_views[basket_index].show_basket_options(query, context, is_first_time=False)
        else:
            self.choosen_dish_view.generate_dish_choosen_view(applied_index=basket_index, new_value = self.users[chat_id][basket_index])
            self.choosen_dish_view.show_dish_choosen_view(query, context, is_first_time=False)

        return self.states_dict["options_state"]

    def are_dishes_existing_in_chat_id(self, chat_id):

        if not chat_id in self.users:
            return False

        if not (self.users[chat_id]):
            return False

        choosen_dishes = self.users[chat_id]

        for (_, count) in choosen_dishes.items():
            if count > 0: 
                return True

        return False

    def bask_evaluate_handler(self, update, context):
        chat_id = update.message.chat.id
        if update.message["text"] == "Корзина":

            if not self.are_dishes_existing_in_chat_id(chat_id): 
                self.log_menu_view.send_warning_message(update = update, context = context)
            else:
                self.choosen_dish_view  = DishChoosenView(dishes = self.users[chat_id])
                self.choosen_dish_view.generate_dish_choosen_view()
                self.choosen_dish_view.show_dish_choosen_view(update, context)
            return self.states_dict["options_state"]
        self.log_menu_view.show_keyboard_menu(update, context, text = "Корзина")
        return self.states_dict["options_state"]

    def calculate_total_sum(self, chat_id): 
        total_price = 0
        currency = ""
        for basket_index, view in enumerate(self.basket_views):
            if currency == "":
                currency = view.currency
            total_price += view.price * self.users[chat_id][basket_index]
        return f"{total_price} {currency}"


