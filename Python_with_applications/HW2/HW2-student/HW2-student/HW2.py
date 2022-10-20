# HW2
# Name: Garret Grant
# Collaborators:
# Date:

import random
from collections import Counter

def count_characters(s):
    """Count the number of occurrences of each character in a string. 
    Args:
        s: str, the string in which to count. 
    Returns:
        a dict keyed by characters whose values are the number of occurrences in s
    """
    count = {}
    for i in range(len(s)):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    
    return count
        


def count_ngrams(s, n = 1):
    """Count the number of occurrences of n-grams in a string. 
    Args:
        s: str.
        n: positive int. should have default value 1.
    Returns:
        a dict keyed by n-grams whose values are the number of occurrences in s
    """
    count = {}
    for i in range(len(s)):
        ngram = s[i:i+n]
        if len(ngram) == n:
            if ngram in count:
                count[ngram] += 1
            else:
                count[ngram] = 1
            
    return count
        
          


def markov_text(s, n, length = 100, seed = 'Emma Woodhouse'):
    """Generate fake text according to an n-th order Markov model, with data from a user-supplied corpus. 
    Args:
        s: str. the text from which to learn grams.
        n: positive int. the order of the Markov model. 
        length: positive int. the number of synthetic characters to generate. should have a default value. 
        seed: str. should have a default value.
    Returns:
        The output string fake_text. fake_text starts with the seed. 
        length of fake_text = length of seed + argument 'length'
    """
    
    if len(seed) > length:
        return seed[:length]
    my_dict = count_ngrams(s, n+1)
    keys = list(my_dict.keys())
    ngram = random.choices(keys)[0]
    new_str = seed
    while len(new_str) < length:
        strings = []
        chars = new_str[-n:]
        weighted_text = {}
        for text, count in my_dict.items():
            if text[:n] == chars:
                if text in weighted_text:
                    weighted_text[text] += 1
                else:
                    weighted_text[text] = 1
                    
        for text, count in weighted_text.items():
            strings.append([text]*count)
            
        new_character = random.choices(strings)[0][0][-1]
            
        new_str += new_character
            
                    
    return new_str
