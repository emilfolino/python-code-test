#!/usr/bin/env python3

'''
This is the Marvin2-assignment new functions module 
'''

import random

def randomize_string(original_string):
    '''
    Randomly re-orders the letters in a string
    '''
    random_indices = random.sample(range(0, len(original_string)), len(original_string))
    
    new_string = ''
    for i in random_indices:
        new_string += original_string[i]

    return f'{original_string} --> {new_string}'

def get_acronym(full_string):
    '''
    Creates an acronym from all upper case letters in a string
    '''
    acronym = ''
    for letter in full_string:
        if letter.isupper():
            acronym += letter
    return acronym

def mask_string(plain_string):
    '''
    Masks all but the last four characters of a string
    '''
    hashtags = multiply_str('#', len(plain_string) - 4)
    return hashtags + plain_string[-4:]
    
def multiply_str(my_string, times):
    '''
    Repeats a string
    '''
    return my_string * times

def find_all_indexes(super_string, sub_string):
    '''
    Finds all indices of the substring
    '''
    indices = ''
    start = 0
    while True:
        try:
            indx = super_string.index(sub_string, start)
        except ValueError:
            break
        indices += f'{indx},'
        start = indx + len(sub_string)

    return indices[:-1]

def points_to_grade(max_points, points):
    '''
    Gives a grade based on percentage of max points
    '''
    grade_percent = int(points) / int(max_points) * 100
    grade_str = ''
    if grade_percent >= 90:
        grade_str = 'A'
    elif grade_percent >= 80:
        grade_str = 'B'
    elif grade_percent >= 70:
        grade_str = 'C'
    elif grade_percent >= 60:
        grade_str = 'D'
    else:
        grade_str = 'F'

    return f'score: {grade_str}'

def has_strings(first_str, second_str, third_str, fourth_str):
    '''
    Compares the first string to the other
    '''
    is_match = 'No match'

    if (first_str.startswith(second_str)
        and third_str in first_str
        and first_str.endswith(fourth_str)):
        is_match = 'Match'

    return is_match
