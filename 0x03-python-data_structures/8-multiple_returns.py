#!/usr/bin/python3
"""multiple_returns() - function that returns a tuple
                    with the length of a string and its
                    first character.
    sentence: word to be handled
"""


def multiple_returns(sentence):
    if sentence == '':
        sentence = None
    return (len(sentence), sentence[0])
