#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Functions for marvin 2 """

import random

def randomize_string(string):
    """ shuffles a string """
    l = list(string)
    random.shuffle(l)
    shuffled = ''.join(l)
    return string + " --> " + shuffled 

def get_acronym(string):
    """ creates an acronym using the uppercase letters """
    result = ""
    for char in string:
        if char.isupper():
            result += char
    return result

def multiply_str(string, integer):
    """ multiplies a string """
    return string * integer

def mask_string(string):
    """ masks all but the last 4 indices of a string """
    masked_string = '#'
    hash_int = len(string) - 4
    masked_string = multiply_str(masked_string, hash_int)

    for i in range(-4, 0):
        masked_string += string[i]

    return masked_string

def find_all_indexes(string, substring):
    """ returns the indexes where a substring can be found in a string"""
    result = ""
    done = False
    first = True
    start = 0
    while not done:
        try:
            index = string.index(substring, start)
            if first:
                result += str(index)
                first = False
            else:
                result += ',' + str(index)
            start = index + 1
        except ValueError:
            done = True
    return result
    
def points_to_grade(max_points, points):
    """ gets the grade from a given point score"""
    percent = int(points) / int(max_points) * 100
    if percent >= 90:
        score = 'A'
    elif percent >= 80:
        score = 'B'
    elif percent >= 70:
        score = 'C'
    elif percent >= 60:
        score = 'D'
    else:
        score = 'F'
    return 'score: ' + score

def has_strings(string1, string2, string3, string4):
    """ checks if str1 begins with str2, contains str3 and ends with str4"""
    result = "No match"
    if string1.startswith(string2) and string3 in string1 and string1.endswith(string4):
        result = "Match"
    return result
    