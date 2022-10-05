# PIC 16A HW1
# Name: Garret Grant
# Collaborators:
# Date:

import random # This is only needed in Problem 5

# Problem 2 

def make_count_dictionary(L):
    ''' Counts how many times each element in a list appears.
    Args:
        L: A list. Elements may be of different types.
    Returns:
        A dict of counts. A key is a unique element of L,
        and its corresponding value is how many times
        that element is in L.
    Example:
        L = ["a", "a", "b", "c"]
        returns {"a" : 2, "b" : 1, "c" : 1}
    '''
#     counter is a dictionary with keys of the passed in list and values initialized at 0
    counter = dict.fromkeys(L,0)
#     Incrementing each key in the list and returning the dictionary
    for element in L:
        counter[element] += 1
    return counter


# Problem 4

def get_triangular_numbers(k):
    ''' Finds the first k triangular numbers. 
    Args:
        k: A positive integer.  
    Returns:
        A list of the first k triangular numbers,
        in order. Each element is an integer.
    Example:
        k = 6
        returns [1, 3, 6, 10, 15, 21]
    '''
    tri_nums = [1]
    for i in range(2,k+1):
        tri_nums.append(i + tri_nums[-1])
    return tri_nums


def get_consonants(s):
    ''' Finds only the consonant letters in a string.
    Args:
        s: A string that contains only lowercase alphabet letters,
        vowels, spaces, commas, and periods.
    Returns:
        A list of strings. Each element
            - is one character long,
            - is not a vowel, space, comma, nor period,
            - is in s, and
            - may appear multiple times.
        The elements appear in the same order as the letters in s.
    Example:
        s = "make it so, number one."
        returns ["m", "k", "t", "s", "n", "m", "b", "r", "n"]    
    '''
    invalids = ["a", "e", "i", "o", "u", ' ', ',', '.' ]
    consts = []
    for letter in s:
        if letter not in invalids:
            consts.append(letter)
    return consts


def get_list_of_powers(X, k):
    ''' Raise elements of a list to its powers.
    Args:
        X: A list of non-negative integers.
        k: A non-negative integer.
    Returns:
        A list of lists. The ith element is a list
        of the powers of X[i] from 0 to (and including) k, 
        in increasing order.
    Example:
        X = [5,6,7], k = 2
        returns [[1, 5, 25], [1, 6, 36], [1, 7, 49]]
    '''
    powers = []
    for element in X:
        power = []
        for i in range(k+1):
            power.append(element**i)
        powers.append(power)
    return powers
            


def get_list_of_even_powers(L, k):
    ''' Raise elements of a list to its even powers.
    Args:
        X: A list of non-negative integers.
        k: A non-negative integer. May or may not be even.
    Returns:
        A list of lists. The ith element is a list
        of the EVEN powers of X[i] from 0 to (and including) k, 
        in increasing order.
    Example:
        X = [5,6,7], k = 2
        returns [[1, 25], [1, 36], [1, 49]]
    '''
    powers = []
    for element in L:
        power = []
        for i in range(k+1):
            if i % 2 == 0:
                power.append(element**i)
        powers.append(power)
    return powers



# Problem 5

def random_walk(ub, lb):
    ''' Simulates a simple, unbiased random walk.
    Terminates when the walk's position reaches
    the upper bound or lower bound. Initial position is 0.

    Args:
        ub: An integer. Upper bound of the walk.
        lb: An integer. Lower bound of the walk.
        You can assume ub >= lb.
    Returns:
        pos: An integer. The walk's final position.
        positions: A list of integers. A log of the walk's positions, 
        including initial but excluding final position.
        steps: A list of -1s and 1s. A log of the coin flips.
    '''
    pos = 0
    positions = [pos]
    steps = []
    while pos < ub and pos > lb:
        step = random.choice([-1,1])
        pos += step
        positions.append(pos)
        steps.append(step)
    positions.pop()
    return pos, positions, steps
