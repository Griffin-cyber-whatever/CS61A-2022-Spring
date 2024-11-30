HW_SOURCE_FILE = __file__

def line_stepper(start, k):
    """
    Complete the function line_stepper, which returns the number of ways there are to go from
    start to 0 on the number line by taking exactly k steps along the number line.

    >>> line_stepper(1, 1)
    1
    >>> line_stepper(0, 2)
    2
    >>> line_stepper(-3, 3)
    1
    >>> line_stepper(3, 5)
    5
    """
    "*** YOUR CODE HERE ***"
    def f(start, k , n):
        if n == k:
            if start == 0:
                return 1
            return 0 
        forward = f(start - 1, k, n+1)
        backward = f(start + 1, k, n+1)
        return backward + forward
    return f(start, k, 0)
    

def summation(n, term):
    """Return the sum of numbers 1 through n (including n) wíth term applied to each number.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    "*** YOUR CODE HERE ***"
    def f(k, sum):
        if k == n+1:
            return sum
        return f(k+1, sum + term(k))
    return f(1, 0)


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    def f(a, b):
        if a == m and b == n:
            return 1
        elif a > m or b > n : 
            return 0
        moving_up = f(a, b+1)
        moving_right = f(a+1, b)
        return moving_right + moving_up
    return f(1,1)


def pascal(row, column):
    """Returns the value of the item in Pascal's Triangle
    whose position is specified by row and column.
    >>> pascal(0, 0)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 3 (1 3 3 1), Column 2
    3
    >>> pascal(4, 2)     # Row 4 (1 4 6 4 1), Column 2
    6
    """
    "*** YOUR CODE HERE ***"
    #pascal(n,m) = pascal(n-1, m) + pascal(n-1, m-1)
    #if m = n ,return 1
    def g(r, c):
        if r == c or r == 1 or c == 0:
            return 1
        if r <= 0 or c >= r or c <= 0:
            return 0
        return g(r - 1, c) + g(r - 1 , c - 1)
    return g(row, column)
