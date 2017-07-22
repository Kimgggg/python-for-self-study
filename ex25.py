# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7

def break_words(stuff):
    """this is function will break up words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """sorts the words"""
    return sorted(words)

def print_first_word(words):
    """print the first word after popping it off"""
    word = words.pop(0)
    print word

def print_last_word(words):
    """print the last word after popping it off"""
    word = words.pop(-1)
    return word

def sort_sentence(sentence):
    """take in a full sentence and returns the sorted word"""
    words = break_words(sentence)
    return sort_words()

def print_first_and_last(sentence):
    """print the first and last words of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word()

def print_first_and_last_sorted(sentence):
    """sorts the words then print the first and last one"""
    words = sort_sentence(sentence)
    print_first_word()
    print_last_word()
