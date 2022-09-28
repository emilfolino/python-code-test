#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Functions for marvin 1 """

import marvin2

def greet():
    """ greeting """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Gah! The dark lord %s has come!" % name)
    print("Tell me what I need to do to please you?!")

def celcius_to_farenheit():
    """ converts units """
    celsius = input("Please tell me the temperature in Celsius. ")
    fahrenheit = round((float(celsius) * 9 / 5 + 32),2)
    print(celsius, "degrees Celsius is", fahrenheit, "degrees Fahrenheit.")

def word_manipulation():
    """ multiplies words """
    word = input("Please type a word: ")
    number = input("Please type a number: ")

    result = marvin2.multiply_str(word, number)
    
    print(result)

def sum_and_average():
    """ prints sum and mean """
    total = 0
    i = 0
    while True:
        number = input("Please type a number or end with 'done': ")
        if number == 'done':
            break
        i += 1
        total = round(total + float(number), 2)
        mean = round(total / i, 2)

    print('The sum of all numbers is %s and the mean is %s' % (total, mean))

def hyphen_string():
    """ manipulates a word into characters and hyphens """
    string = input("Please enter a string: ")
    new_string = ''
    i = 1
    first = True
    for char in string:
        if first:
            new_string += char * i
            first = False
        else:
            new_string += "-" + char * i
        i += 1

    print(new_string)

def is_isogram():
    """ checks if a word is an isogram """
    word = input("Please enter a word to check if it's an isogram: ")
    iso = "No match!"
    for char1 in word:
        x = 0
        for char2 in word:
            if char1 == char2:
                x += 1
        if x > 1:
            iso = "No match!"
            break
        iso = "Match!"

    print(iso)

def compare_numbers():
    """ compares two numbers """
    num1 = input("Please input a number: ")
    while True:
        num2 = input("Please input another number, or 'done' to stop: ")
        if num2 == 'done':
            break
        try:
            num1 = float(num1)
            num2 = float(num2)
            if num2 < num1:
                print("smaller!")
            elif num2 > num1:
                print("larger!")
            elif num2 == num1:
                print("same!")
            num1 = num2
        except ValueError:
            print("not a number!")

def robber_language():
    """ translates to robber language """
    consonants = "bcdfghjklmnpqrstvwxz"
    word = input("Please input a word to translate: ").lower()
    translated = ''
    for char in word:
        translated += char
        if char in consonants:
            translated += 'o' + char            

    print(translated)

def string_comparison():
    """ checks if all characters in one string is in another """
    string1 = input("Please enter a string: ")
    string2 = input("Please enter another string: ")
    result = "Match!"
    for char in string2:    
        if char not in string1:
            result = "No match!"
            break
        numchars1 = 0
        numchars2 = 0
        for char2 in string1:
            if char2 == char:
                numchars1 += 1
        for char2 in string2:
            if char2 == char:
                numchars2 += 1
        if numchars2 > numchars1:
            result = "No match!"
            break
                    
    print(result)

def all_digit_doubler():
    """ doubles a number until it contains all digits """
    number = int(input("Please enter a number: "))
    stop = int(input("Please enter maximum number of tries: "))

    i=0
    done = False
    while not done:
        if i >= stop:
            i = -1
            break
        for digit in range(10):
            if str(digit) not in str(number):
                number *= 2
                i += 1
                break
            elif digit == 9:
                done = True
                            
    print('Answer:', i, 'times')

def tab_to_space_converter():
    """ converts tab to space """
    old_string = input("Please enter a string with tabs: ")
    new_string = ''
    for char in old_string:
        if char == '\t':
            new_string += '   '
        else:
            new_string += char
    
    print(new_string)

def name_combiner():
    """ combines two names into one"""
    name1 = input("Please enter the first name:")        
    name2 = input("Please enter the second name:") 

    vowels = 'aeiouy'

    new_name1 = ''
    for char in name1:
        if char in vowels:
            break
        else:
            new_name1 += char

    new_name2 = ''
    i = 0
    while i < len(name2):
        if name2[i] in vowels:
            new_name2 = name2[i:]
            break
        else:
            i += 1

    print(new_name1 + new_name2)

def string_game():
    """ a game using a string """
    player_input = input("Please enter a long string, alternating between letters and numbers, "
                            "where the letters can be lower- or uppercase.")          

    result = ''

    first = True
    for char in player_input:
        if char.isalpha():
            if char.lower() in result:
                continue
            i = 1
            score = 0
            for char2 in player_input:
                if char2.lower() == char.lower():
                    if char2.islower():
                        score += int(player_input[i])
                    elif char2.isupper():
                        score -= int(player_input[i])
                i += 1
            if first:
                result += char.lower() + ' ' + str(score)
                first = False
            else:
                result += ', ' + char.lower() + ' ' + str(score) 

    print (result)
