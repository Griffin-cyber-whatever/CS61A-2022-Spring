import re

def cs_classes(post):
    """
    Returns strings that look like a Berkeley CS or EE class,
    starting with "CS" or "EE", followed by a number, optionally ending with A, B, or C
    and potentially with a space between "CS" or "EE" and the number.
    Case insensitive.

    >>> cs_classes("Is it unreasonable to take CS61A, CS61B, CS70, and EE16A in the summer?")
    True
    >>> cs_classes("how do I become a TA for cs61a? that job sounds so fun")
    True
    >>> cs_classes("Can I take ECON101 as a CS major?")
    False
    >>> cs_classes("Should I do the lab lites or regular labs in EE16A?")
    True
    >>> cs_classes("thoughts on ee127?")
    True
    >>> cs_classes("Is 70 considered an EECS class?")
    False
    >>> cs_classes("What are some good CS upper division courses? I was thinking about CS 161 or CS 169a")
    True
    """
    return bool(re.search(r"((?:cs|CS|EE|ee)\s?\d+\s?[a-zA-Z]?)", post))


def match_time(text):
    """
    >>> match_time("At 07:23AM, I woke up and had some coffee.")
    True
    >>> match_time("I looked at my phone at 12:22 to check the weather.")
    True
    >>> match_time("At 05:24PM, I had sesame bagels with cream cheese.")
    True
    >>> match_time("At 23:59 I was sound asleep.")
    True
    >>> match_time("After, the clocked turned to 00:00.")
    True
    >>> match_time("Mix water in a 1:2 ratio with chicken stock.")
    False
    >>> match_time("At work, I pinged 127.0.0.1:80.")
    False
    >>> match_time("The tennis score was 40:30.")
    False
    """
    minute = r"(?:[0-5][0-9])"
    hour24 = r"(?:(?:[01][0-9])|(?:2[0-3]))"
    houram = r"(?:(?:0[0-9])|(?:1[0-2]))"
    return bool(re.search(fr"\b{hour24}:{minute}|{houram}:{minute}(?:AM|PM)\b", text))

r"""
    tree_node: "Tree(" (label|braches)* "," branches ")"

    ?label: NUMBER | tree_node

    branches: "[" (tree_node ",")* tree_node"]"| nil

    %ignore /\s+/
    %import common.NUMBER
"""

r"""
    rstring: "r\"" regex* "\""

    ?regex: character | word |  group | pipe | class 
    
    group: "(" regex* ")"
    
    pipe:  regex "|" regex
    
    range: LETTER "-" LETTER "|" NUMBER "-" NUMBER 
       
    class: "[" (range|character)+ "]"
    
    character: LETTER | NUMBER
    word: WORD

    %ignore /\s+/
    %import common.LETTER
    %import common.NUMBER
    %import common.WORD
"""