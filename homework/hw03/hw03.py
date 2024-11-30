HW_SOURCE_FILE = __file__

def neighbor_digits(num, prev_digit=-1):
    """
    Returns the number of digits in num that have the same digit to its right
    or left.
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    "*** YOUR CODE HERE ***"
    num = str(num)
    if prev_digit == len(str(num)) or prev_digit < 0:
        return 0
    else:
        for i in range(len(num)):
            if i != prev_digit and i == num[prev_digit]:
                return 1 + neighbor_digits(num, prev_digit+1)                        
        return neighbor_digits(num, prev_digit+1)


def has_subseq(n, seq):
    """
    Complete has_subseq, a function which takes in a number n and a "sequence"
    of digits seq and returns whether n contains seq as a subsequence, which
    does not have to be consecutive.

    >>> has_subseq(123, 12)
    True
    >>> has_subseq(141, 11)
    True
    >>> has_subseq(144, 12)
    False
    >>> has_subseq(144, 1441)
    False
    >>> has_subseq(1343412, 134)
    True
    """
    "*** YOUR CODE HERE ***"
    #the key is how to make  it in recursion
    #dont have to match sequence consecutivly
    if n == 0:
        return False
    if seq == 0:
        return True
    if n//10 == seq // 10:
        return has_subseq(n//10, seq//10)
    return has_subseq(n//10, seq)
    
    
def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
    if pos == 0:
        return 0
    else:
        if pos % 10 == 8:
            return 1 + num_eights(pos // 10)
        else:
            return num_eights(pos // 10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    """
    value = 0
    postive = True
    for i in range(1, n+1):
        if "8" in str(i) or i % 8 == 0:
            if postive:
                value += 1
                postive = False
            else:
                value -= 1
                postive = True
        elif postive:
            value += 1
        else:
            value -= 1
    """
    #tbh, i guess i will nevre try to learn how to assign a value without using statements
    #another alternative way to assign values is by passing the value we wanna keep track on as an argument inside recursion  loop
    
    def index(k, postive):
        if k == n+1:
            return 0 
        if "8" in str(k) or k % 8 == 0:
            if postive:
                return index(k + 1, False) + 1
            return index(k + 1, True) - 1
        if postive:
            return index(k + 1, True) + 1
        return index(k + 1, False) - 1 
    return index(1,True)
    

def get_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> get_larger_coin(1)
    5
    >>> get_larger_coin(5)
    10
    >>> get_larger_coin(10)
    25
    >>> get_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def get_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> get_smaller_coin(25)
    10
    >>> get_smaller_coin(10)
    5
    >>> get_smaller_coin(5)
    1
    >>> get_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def partition(n,m):
        if n == 0:
            return 1
        if n < 0:
            return 0
        if m >= 5:
            with_m = partition(n-m, m)
            without_m = partition(n, get_smaller_coin(m))
            return without_m + with_m
        with_m = partition(n-m, 1)
        return with_m
    return partition(change,25)

