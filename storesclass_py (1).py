"""
Aleksandra Mbuyi
Pramudya Wicaksono
Rei Onishi

Groceries Budgeting and Price Comparison Project - Class File
10/21/2023
"""

class Item:
    def __init__(self, _name, _Target_price, _Aldi_price, _Walmart_price): # Constructor with item name and store prices.
        self.name = _name
        self.Target_price = _Target_price
        self.Aldi_price = _Aldi_price
        self.Walmart_price = _Walmart_price

    def get_Target_price(self): # Getters.
        return self.Target_price

    def get_Aldi_price(self):
        return self.Aldi_price

    def get_Walmart_price(self):
        return self.Walmart_price

    def set__name(self, new_name): # Setters.
        self._name = new_name
        
    def set__Target_price(self, new_price):
        self._Target_price = new_price
        
    def set__Aldi_price(self, new_price):
        self._Aldi_price = new_price
        
    def set__Walmart_price(self, new_price):
        self._Walmart_price = new_price


    def __str__(self): # String representation.
        msg = f"Successfully added {self._name} to the cart"
        return msg
        
    def calculate_average_price(item_info): # Method to calculate average price of an item.
        total_price = 0
        store_count = 0

        # Iterate over the item's information dictionary
        for store, price in item_info.items():
            # Check if the entry is a store price and accumulate the total price
            if store != "Item":
                total_price += price
                store_count += 1

        # Calculate the average price if stores are found
        if store_count > 0:
            average_price = total_price / store_count
            return average_price
        else:
            return None
