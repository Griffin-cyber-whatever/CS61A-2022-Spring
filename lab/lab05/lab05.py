HW_SOURCE_FILE = __file__

def replace_elements(source_list, dest_list):
    """
    Complete the function replace_elements, a function which takes in source_list
    and dest_list and mutates the elements of dest_list to be the elements at the
    corresponding index in source_list.

    dest_list always has a length greater than or equal to the length of
    source_list.

    >>> s1 = [1, 2, 3]
    >>> s2 = [5, 4]
    >>> replace_elements(s2, s1)
    >>> s1
    [5, 4, 3]
    >>> s3 = [0, 0, 0, 0, 0]
    >>> replace_elements(s1, s3)
    >>> s3
    [5, 4, 3, 0, 0]
    """
    # len(dest_list) >= len(source_list)
    for i in range(len(source_list)):
        dest_list[i] = source_list[i]
    return dest_list
    
def flatten(s):
    """Returns a flattened version of list s.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]     # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x # Ensure x is not mutated
    [1, [2, 3], 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> x
    [[1, [1, 1]], 1, [1, 1]]
    """
    "*** YOUR CODE HERE ***"
    l = []
    def f(x):
        if not isinstance(x, list):
            l.append(x)
        else:
            for i in x:
                f(i) 
    f(s)       
    return l

def couple(s, t):
    """Return a list of two-element lists in which the i-th element is [s[i], t[i]].

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> couple(a, b)
    [[1, 4], [2, 5], [3, 6]]
    >>> c = ['c', 6]
    >>> d = ['s', '1']
    >>> couple(c, d)
    [['c', 's'], [6, '1']]
    """
    assert len(s) == len(t)
    "*** YOUR CODE HERE ***"
    couple = []
    for i in range(len(s)):
        l = [s[i] , t[i]]
        couple.append(l)
    return couple


def insert_items(lst, entry, elem):
    """Inserts elem into lst after each occurence of entry and then returns lst.

    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> double_lst = [1, 2, 1, 2, 3, 3]
    >>> double_lst = insert_items(double_lst, 3, 4)
    >>> double_lst
    [1, 2, 1, 2, 3, 4, 3, 4]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    >>> # Ban creating new lists
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'insert_items',
    ...       ['List', 'ListComp', 'Slice'])
    True
    """
    "*** YOUR CODE HERE ***"
    i = 0
    while i < len(lst):
        if lst[i] == entry:
            lst.insert(i + 1, elem)
            i += 1
        i += 1
    return lst


def change_abstraction(change):
    
    """
    For testing purposes.
    >>> change_abstraction(True)
    >>> change_abstraction.changed
    True
    """
    change_abstraction.changed = change


change_abstraction.changed = False
