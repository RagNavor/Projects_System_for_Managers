class FoodDeliverySystem:
    order_id = 0
    def __init__(self):
        self.menu = {
            "Burger": 150,
            "Pizza": 250,
            "Pasta": 200,
            "Salad": 120,
            "Beverages": 130,
            "Noodles": 150,
            "Sushi": 270,
            "Bakery":350
            # Add more items to the menu
        }
        self.bill_amount = 0
        
    def display_menu(self):
        """
        Return the menu details in the following format:
        Burger  |  150
        Pizza   |  250
        Pasta   |  200
        Salad   |  120
        Beverages  |  130
        Noodles  |  150
        Sushi   |  270
        Bakery  |  350
        """
        format_menu=''
        for item, price in self.menu:
            format_menu += f'{item}  |  {price}'

        return format_menu
    
test = FoodDeliverySystem

print(test.display_menu())