class Cat:
    def __init__(self, name, owner, lives=9):
        self.is_alive = True
        self.name = name
        self.owner = owner
        self.lives = lives

    def talk(self):
        return self.name + ' says meow!'

    @classmethod
    def adopt_a_cat(cls, owner):
        """
        Returns a new instance of a Cat.

        This instance's owner is the given owner.
        Its name and its number of lives is chosen programatically
        based on the spec's noted behavior.

        >>> cat1 = Cat.adopt_a_cat("Ifeoma")
        >>> isinstance(cat1, Cat)
        True
        >>> cat1.owner
        'Ifeoma'
        >>> cat1.name
        'Felix'
        >>> cat1.lives
        11
        >>> cat2 = Cat.adopt_a_cat("Ay")
        >>> cat2.owner
        'Ay'
        >>> cat2.name
        'Grumpy'
        >>> cat2.lives
        8
        """
        cat_names = ["Felix", "Bugs", "Grumpy"]
        "*** YOUR CODE HERE ***"
        index =  len(owner) % len(cat_names)
        lives = len(owner) + len(cat_names[index])
        return cls(cat_names[index], owner, lives)


class NoisyCat(Cat):
    """
    >>> my_cat = NoisyCat("Furball", "James")
    >>> my_cat.name
    'Furball'
    >>> my_cat.is_alive
    True
    >>> my_cat.lives
    8
    >>> my_cat.talk()
    'Furball says meow! Furball says meow!'
    >>> friend_cat = NoisyCat("Tabby", "James", 2)
    >>> friend_cat.talk()
    'Tabby says meow! Tabby says meow!'
    >>> friend_cat.lives
    1
    """
    def __init__(self, name, owner, lives=9):
        "*** YOUR CODE HERE ***"
        return super.__init__(name, owner, lives-1)

    def talk(self):
        "*** YOUR CODE HERE ***"
        return super().talk() + " " + super().talk()
        
class Account:
    """An account has a balance and a holder.
    >>> a = Account('John')
    >>> a.deposit(10)
    10
    >>> a.balance
    10
    >>> a.interest
    0.02
    >>> a.time_to_retire(10.25) # 10 -> 10.2 -> 10.404
    2
    >>> a.balance               # balance should not change
    10
    >>> a.time_to_retire(11)    # 10 -> 10.2 -> ... -> 11.040808032
    5
    >>> a.time_to_retire(100)
    117
    """
    max_withdrawal = 10
    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        if amount > self.max_withdrawal:
            return "Can't withdraw that amount"
        self.balance = self.balance - amount
        return self.balance

    def time_to_retire(self, amount):
        """Return the number of years until balance would grow to amount."""
        assert self.balance > 0 and amount > 0 and self.interest > 0
        "*** YOUR CODE HERE ***"
        balance = self.balance
        counter = 0
        while balance < amount:
            balance *= 1 + self.interest
            counter += 1
        return counter  


class FreeChecking(Account):
    """A bank account that charges for withdrawals, but the first two are free!
    >>> ch = FreeChecking('Jack')
    >>> ch.balance = 20
    >>> ch.withdraw(100)  # First one's free
    'Insufficient funds'
    >>> ch.withdraw(3)    # And the second
    17
    >>> ch.balance
    17
    >>> ch.withdraw(3)    # Ok, two free withdrawals is enough
    13
    >>> ch.withdraw(3)
    9
    >>> ch2 = FreeChecking('John')
    >>> ch2.balance = 10
    >>> ch2.withdraw(3) # No fee
    7
    >>> ch.withdraw(3)  # ch still charges a fee
    5
    >>> ch.withdraw(5)  # Not enough to cover fee + withdraw
    'Insufficient funds'
    """
    withdraw_fee = 1
    free_withdrawals = 2

    "*** YOUR CODE HERE ***"
    def __init__(self, account_holder):
        self.withdrawTimes = 0
        super().__init__(account_holder)

    def withdraw(self, amount):
        if self.withdrawTimes < self.free_withdrawals:
            self.withdrawTimes += 1
            return super().withdraw(amount)
        self.withdrawTimes += 1
        return super().withdraw(amount + self.withdraw_fee)