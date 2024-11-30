def remove_odd_indices(lst, odd):
    """ 
    Remove elements of lst that have odd indices.
    >>> s = [1, 2, 3, 4]
    >>> t = remove_odd_indices(s, True)
    >>> s
    [1, 2, 3, 4]
    >>> t
    [1, 3]
    >>> l = [5, 6, 7, 8]
    >>> m = remove_odd_indices(l, False)
    >>> m
    [6, 8]
    """
    "*** YOUR CODE HERE ***"
    if odd:
        return [lst[i] for i in range(len(lst)) if  i % 2 != 0]
    return [lst[i] for i in range(len(lst)) if  i % 2 == 0]
    

class SmartFridge:
    """"
    >>> fridgey = SmartFridge()
    >>> fridgey.add_item('Mayo', 1)
    'I now have 1 Mayo'
    >>> fridgey.add_item('Mayo', 2)
    'I now have 3 Mayo'
    >>> fridgey.use_item('Mayo', 2.5)
    'I have 0.5 Mayo left'
    >>> fridgey.use_item('Mayo', 0.5)
    'Uh oh, buy more Mayo!'
    """
    def __init__(self):
        self.items = {}
    def add_item(self, item, quantity):
        "*** YOUR CODE HERE ***"
        self.items[item] = quantity
        print(f'I now have {quantity} {item}')
    def use_item(self, item, quantity):
        if item in self.items:
            if quantity < self.items[item]:
                return print(f"Uh oh, buy more {item}!")
            self.items[item] -= quantity
            return print(f'I have {self.items[item]} {item} left')
        return print("invalid item")
            

def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"
    # return sorted(lst1+lst2)
    # or use merge sort
    merged_list = []
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged_list.append(lst1[i]) 
            i += 1            
        else:
            merged_list.append(lst2[j])
            j += 1
    while i < len(lst1):
        merged_list.append(lst1[i])
        i += 1
    while j < len(lst2):
        merged_list.append(lst2[j])
        j += 1
    return merged_list

class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.present_year.

    >>> mint = Mint()
    >>> mint.year
    2021
    >>> dime = mint.create(Dime)
    >>> dime.year
    2021
    >>> Mint.present_year = 2101  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2021
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2101
    >>> Mint.present_year = 2176     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    """
    present_year = 2021

    def __init__(self):
        self.update()

    def create(self, coin):
        "*** YOUR CODE HERE ***"
        return coin(self.year)

    def update(self):
        "*** YOUR CODE HERE ***"
        self.year = self.present_year


class Coin:
    cents = None  # will be provided by subclasses, but not by Coin itself

    def __init__(self, year):
        self.year = year

    def worth(self):
        "*** YOUR CODE HERE ***"
        # value = origin + (present_year - yaer)
        age = Mint.present_year - self.year
        if self.cents:
            return self.cents + (age - 50 if age > 50 else 0)
        return "invalid cents"

class Nickel(Coin):
    cents = 5


class Dime(Coin):
    cents = 10


class VendingMachine:
    """A vending machine that vends some product for some price.

    # set price for item __init__
    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    # add fund
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    # set quantity for item
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    # one object for one item each
    stocks = 0
    balance = 0

    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price
    
    def vend(self):
        if (self.stocks == 0):
            print(f"'Nothing left to vend. Please restock.'" )
        elif (self.balance < self.product_price):
            print(f"'You must add ${self.product_price - self.balance} more funds.'" )
        elif (self.balance == self.product_price):
            print(f"'Here is your {self.product_name}.'")
            self.balance = 0
            self.stocks -= 1
        else:
            print(f"'Here is your {self.product_name} and ${self.balance - self.product_price} change.'" )
            self.balance = 0
            self.stocks -= 1

    def add_funds(self, funds):       
        if (self.stocks == 0):
            print(f"'Nothing left to vend. Please restock. Here is your ${self.balance}.'" )
        else:
            self.balance += funds
            print(f"'Current balance: ${self.balance}'")

    def restock(self, stock):
        self.stocks += stock
        print(f"'Current {self.product_name} stock: {self.stocks}'")    