"""""""""
    Item Reference dictionary
"""""""""

all_item_prices = {
                    'leeks': 3.50,
                    'rhubarb': 3.50,
                    'cauliflower': 3.50,
                    'broccoli': 3.50,
                    'sal_onions': 3.50,     # walla - walla salad onions
                    'asparagus': 3.50,
                    'kale': 3.50,
                    'spinach': 3.50,
                    'lettuce': 1.50,
                    'carrots': 3.50,
                    'beets': 3.50,
                    'potatoes': 3.50,       # red/russet/yukon gold potatoes
                    'swe_onions': 1,        # sweet onions
                    'red_onions': 1,        # red onions
                    'gre_onions': 1,        # sweet onions
                    'strw_pint': 3.5,       # pint of strawberries
                    'strw_four': 12.95,     # four pack of strawberries
                    'strw_six': 18.95,      # six pack of strawberries
                    'strw_crate': 33.95,     # 12 pack of strawberries
                    }

"""""""""

    Produce Classes

"""""""""

# -- Super Class --
class Produce():
    price = None
    discount_price = None
    discount_legal = False

    def check_discount(self):
        if self.discount_legal is False:
            return False
        
        else:
            return True


class Leek(Produce):
    def __init__(self):
        self.price = all_item_prices['leeks']
        self.discount_price = 3
        self.discount_legal = True

    def get_price(self):
        return self.price
    
    def get_discount(self):
        return self.discount_price

    def display_transaction(self, *discount_applied):
        text_price = None
        if discount_applied is True:
            text_price = self.price

        elif discount_applied is False and self.discount_legal is True:
            text_price = self.discount_price

        else:
            text_price = self.price

        return 'Leek\t\t-----------------------' + str(text_price) + '\n'


class Rhubarb(Produce):
    def __init__(self):
        self.price = all_item_prices.get('rhubarb')
        self.discount_price = 3
        self.discount_legal = True
        self.text_price = None

    def get_price(self):
        return self.price

    def get_discount(self):
        return self.discount_price

    def display_transaction(self, discount_applied):
        if discount_applied:
            self.text_price = self.get_price()

        elif discount_applied is False and self.discount_legal is True:
            self.text_price = self.get_discount()

        else:
            self.text_price = self.get_price()

        return "Rhubarb\t\t-----------------------\n" + self.text_price


class Cauliflower(Produce):
    def __init__(self):
        self.price = all_item_prices.get('cauliflower')
        self.discount_price = 3
        self.discount_legal = True
        self.text_price = None

    def get_price(self):
        return self.price

    def get_discount(self):
        return self.discount_price

    def display_transaction(self, discount_applied):
        if discount_applied:
            self.text_price = self.get_price()

        elif discount_applied is False and self.discount_legal is True:
            self.text_price = self.get_discount()

        else:
            self.text_price = self.get_price()

        return "Cauliflower\t-----------------------\n" + self.text_price


class Broccoli(Produce):
    def __init__(self):
        self.price = all_item_prices.get('broccoli')
        self.discount_price = 3
        self.discount_legal = True
        self.text_price = None

    def get_price(self):
        return self.price

    def get_discount(self):
        return self.discount_price

    def display_transaction(self, discount_applied):
        if discount_applied:
            self.text_price = self.get_price()

        elif discount_applied is False and self.discount_legal is True:
            self.text_price = self.get_discount()

        else:
            self.text_price = self.get_price()

        return "Broccoli\t-----------------------\n" + self.text_price


class Walla_Walla(Produce):
    def __init__(self):
        self.price = all_item_prices.get('sal_onions')
        self.discount_price = 3
        self.discount_legal = True
        self.text_price = None

    def get_price(self):
        return self.price

    def get_discount(self):
        return self.discount_price

    def display_transaction(self, discount_applied):
        if discount_applied:
            self.text_price = self.get_price()

        elif discount_applied is False and self.discount_legal is True:
            self.text_price = self.get_discount()

        else:
            self.text_price = self.get_price()

        return "Walla - Walla\t-----------------------\n" + self.text_price


class Asparagus(Produce):
    def __init__(self):
        self.price = all_item_prices.get('asparagus')
        self.discount_price = 3
        self.discount_legal = True
        self.text_price = None

    def get_price(self):
        return self.price

    def get_discount(self):
        return self.discount_price

    def display_transaction(self, discount_applied):
        if discount_applied:
            self.text_price = self.get_price()

        elif discount_applied is False and self.discount_legal is True:
            self.text_price = self.get_discount()

        else:
            self.text_price = self.get_price()

        return "Asparagus\t-----------------------\n" + self.text_price


class Spinach(Produce):
    def __init__(self):
        self.price = all_item_prices.get('spinach')
        self.discount_price = 3
        self.discount_legal = True
        self.text_price = None

    def get_price(self):
        return self.price

    def get_discount(self):
        return self.discount_price

    def display_transaction(self, discount_applied):
        if discount_applied:
            self.text_price = self.get_price()

        elif discount_applied is False and self.discount_legal is True:
            self.text_price = self.get_discount()

        else:
            self.text_price = self.get_price()

        return "Spinach\t-----------------------\n" + self.text_price


class Lettuce(Produce):
    def __init__(self):
        self.price = all_item_prices.get('lettuce')
        self.discount_price = 3
        self.discount_legal = True
        self.text_price = None

    def get_price(self):
        return self.price

    def get_discount(self):
        return self.discount_price

    def display_transaction(self, discount_applied):
        if discount_applied:
            self.text_price = self.get_price()

        elif discount_applied is False and self.discount_legal is True:
            self.text_price = self.get_discount()

        else:
            self.text_price = self.get_price()

        return "Lettuce\t-----------------------\n" + self.text_price


class Kale(Produce):

    def __init__(self):
        self.price = all_item_prices.get('kale')
        self.discount_price = 3
        self.discount_legal = True
        self.text_price = None

    def get_price(self):
        return self.price

    def get_discount(self):
        return self.discount_price

    def display_transaction(self, discount_applied):
        if discount_applied:
            self.text_price = self.get_price()

        elif discount_applied is False and self.discount_legal is True:
            self.text_price = self.get_discount()

        else:
            self.text_price = self.get_price()

        return "Kale\t\t-----------------------\n" + self.text_price


class Carrot(Produce):
    def __init__(self):
        self.price = all_item_prices.get('carrots')
        self.discount_price = 3
        self.discount_legal = True
        self.text_price = None

    def get_price(self):
        return self.price

    def get_discount(self):
        return self.discount_price

    def display_transaction(self, discount_applied):
        if discount_applied:
            self.text_price = self.get_price()

        elif discount_applied is False and self.discount_legal is True:
            self.text_price = self.get_discount()

        else:
            self.text_price = self.get_price()

        return "Carrot\t\t-----------------------\n" + self.text_price


class Beet(Produce):
    def __init__(self):
        self.price = all_item_prices.get('beet')
        self.discount_price = 3
        self.discount_legal = True
        self.text_price = None

    def get_price(self):
        return self.price

    def get_discount(self):
        return self.discount_price

    def display_transaction(self, discount_applied):
        if discount_applied:
            self.text_price = self.get_price()

        elif discount_applied is False and self.discount_legal is True:
            self.text_price = self.get_discount()

        else:
            self.text_price = self.get_price()

        return "Beets\t\t-----------------------\n" + self.text_price


class Tater(Produce):
    def __init__(self):
        self.price = all_item_prices.get('potatoes')
        self.discount_price = 3
        self.discount_legal = True
        self.text_price = None

    def get_price(self):
        return self.price

    def get_discount(self):
        return self.discount_price

    def display_transaction(self, discount_applied):
        if discount_applied:
            self.text_price = self.get_price()

        elif discount_applied is False and self.discount_legal is True:
            self.text_price = self.get_discount()

        else:
            self.text_price = self.get_price()

        return "Potatoe\t-----------------------\n" + self.text_price

        
class Sweet_Onion(Produce):
    def __init__(self):
        self.price = all_item_prices.get('swe_onion')
        self.discount_legal = False

    def get_price(self):
        return self.price

    def get_discount(self):
        return self.discount_price

    def display_transaction(self):
        return "Sweet Onion\t-----------------------\n " + self.price


class Red_Onion(Produce):
    def __init__(self):
        self.price = all_item_prices.get('red_onion')
        self.discount_legal = False
        self.text_price = None

    def get_price(self):
        return self.price

    def display_transaction(self):
        return "Red Onion\t-----------------------\n" + self.price

        
class Green_Onion(Produce):
    def __init__(self):
        self.price = all_item_prices.get('gre_onion')
        self.discount_legal = False

    def get_price(self):
        return self.price

    def display_transaction(self, discount_applied):
        return "Green Onion\t---------------------\n" + self.price


"""""""""

    Strawberry Classes

"""""""""

class Strawberry_Pint(Produce):
    def __init__(self):
        self.price = all_item_prices.get('strw_pint')
        self.text_price = None
        self.discount_legal = False
        
    def get_price(self):
        return self.price

    def display_transaction(self, discount_applied):
        return "Strawberry Pint\t-----------------------\n" + self.text_price


class Strawberry_Fourpack(Produce):
    def __init__(self):
        self.price = all_item_prices.get('strw_four')
        self.discount_legal = False
        
    def get_price(self):
        return self.price

    def display_transaction(self, discount_applied):
        return "Strawberry Fourpack\t-----------------------\n" + self.price


class Strawberry_Sixpack(Produce):
    def __init__(self):
        self.price = all_item_prices.get('strw_six')
        self.discount_legal = False

    def get_price(self):
        return self.price

    def display_transaction(self, discount_applied):
        return "Strawberry Sixpack\t-----------------------\n" + self.price


class Strawberry_Crate(Produce):
    def __init__(self):
        self.price = all_item_prices.get('strw_crate')
        self.discount_legal = False

    def get_price(self):
        return self.price

    def display_transaction(self, discount_applied):
        return "Strawberry Crate\t-----------------------\n" + self.price