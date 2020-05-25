from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton,ParseMode
from basket.view.BasketView import BasketView


class DishChoosenView:

    def __init__(self, dishes):
        self.dishes             = dishes
        self.dishes_view        = []
        self.index_map          = {}
        self.overall_selected_dishes = self.count_number_of_selected_dishes(self.dishes)
        self.optional_buttons   = [
            InlineKeyboardButton(f"1 из {self.overall_selected_dishes}", callback_data="no_reaction",  resize_keyboard=True)            
            ]
        self.setup_dishes_view()
    
    def set_dishes(self, dishes):
        self.dishes = dishes

    def count_number_of_selected_dishes(self, dishes):
        overall_num = 0
        for (_, count) in self.dishes.items(): 
            if (count > 0):
                overall_num += 1
        return overall_num

    def delete_dish(self, index):
        if index in self.index_map:
            for_dish_view_index = self.index_map[index]
            print(f"{for_dish_view_index} - for_dish_view_index")
            del self.dishes_view[for_dish_view_index]
            self.overall_selected_dishes -= 1
            self.optional_buttons   = [
                InlineKeyboardButton(f"1 из {self.overall_selected_dishes}", callback_data="no_reaction",  resize_keyboard=True)            
                ]
            return len(self.dishes_view) != 0
        return False


    def setup_dishes_view(self):
        for (dish_index, count) in self.dishes.items():
            if count > 0:
                basket_view = BasketView(
                    index = dish_index, 
                    count = count, 
                    optional_detail="chosen/",
                    optional_buttons=self.optional_buttons
                    )
                self.index_map[dish_index] = len(self.dishes_view)
                self.dishes_view.append(basket_view)
    
    def generate_dish_choosen_view(self, applied_index = -1, new_value = -1):
        if applied_index < 0: 
            for _, dish_view in enumerate(self.dishes_view):
                dish_view.generate_options_view(dish_view.count)
        else:
            for_dish_view_index = self.index_map[applied_index]
            self.dishes_view[for_dish_view_index].generate_options_view(num = new_value)

    def show_dish_choosen_view(self, update, context, index = 0, is_first_time = True):
        dish_view           = self.dishes_view[index]
        
        dish_view.show_basket_options(
            update, 
            context, 
            optional_num_buttons = len(self.optional_buttons), 
            is_first_time = is_first_time
            )