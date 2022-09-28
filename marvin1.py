#!/usr/bin/env python3

'''
This is the Marvin2-assignment old functions module 
'''

import marvin2

def claudio_says(answer):
    '''
    Prints Claudio saying the answers
    '''
    print('\nClaudio says:\n')
    print(answer)
    print('What more can I do for you?!')

def greet():
    '''
    Greets the name given by the user
    '''
    name = input('What is your name? ') 
    claudio_says(f'Cool dude, I once knew a dodo named {name}!')

def celcius_to_farenheit():
    '''
    Converts celsius to farenheit
    '''
    celsius = float(input('How many degrees °C are we talking? '))
    fahrenheit = round(celsius * 9 / 5 + 32, 2)
    claudio_says(f'That is {fahrenheit} °F!')

def word_manipulation():
    '''
    Calls multiply_str to repeat a string
    '''
    word_to_repeat = input('Let\'s hear it! What\'s your special word? ')
    num_times = int(input('And how many times do you whish for me to reapeat it? ')) 
    claudio_says(marvin2.multiply_str(word_to_repeat, num_times))

def sum_and_average():
    '''
    Calculates the sum and average of all numbers given by the user
    '''
    total = 0
    count = 0

    print('Feed me your numbers (one at a time)! Enter "done" when you are ... well, done!')
    while True:
        answer = input('')
        
        if answer == 'done':
            break

        try:
            num = float(answer)

        except ValueError:
            ('Oyy only numbers! I am a picky eater, okey?')
            continue

        total += num
        count +=1

    average = total/count

    claudio_says(f'The sum of all the numbers is {total:.2f} and the average is {average:.2f}.')

def hyphen_string():
    '''
    Join the letters of a string with hyphens
    '''
    word_to_spell = input('What word do you want me to spell out for you? ')  
    letters = []
    
    # for simplicity, use enumerate to get both the current iteration and item
    for count, letter in enumerate(word_to_spell):
        letters.append(letter * (count + 1)) 
    
    new_string = '-'.join(letters)

    claudio_says(new_string)

def is_isogram():
    '''
    Checks whether a string is an isogram or not
    '''
    maybe_isogram = input('So what is this could-be-isogram? ')
    memory = ''
    isogram_or_not = 'Match!'

    for letter in maybe_isogram:
        if letter in memory:
            isogram_or_not = 'No match!'
            break
        memory += letter

    claudio_says(isogram_or_not)

def compare_numbers():
    '''
    Continuously compares two consecutive numbers
    '''
    last = None

    print('Enter a number to start with ("done" to exit): ')
    while True:
        answer = input('')

        if answer == 'done':
            break

        try:
            current_num = int(answer)
        except ValueError:
            print('not a number!')
            continue

        if last is None:
            print('Enter another one to compare it to: ')
            last = current_num
            continue

        if current_num < last:
            print('smaller!')
        elif current_num == last:
            print('same!')
        else:
            print('larger!')

        print('Enter another one to compare to the last: ')
        last = current_num
    
    print('\nWhat more can I do for you?!')

def robber_language():
    '''
    Translates a string to the robber language
    '''
    consonants_sv = 'bcdfghjklmnpqrstvwxz'
    word_robber = ''

    word = input('Enter a word: ').lower()

    for letter in word:
        if letter in consonants_sv:
            word_robber += letter + 'o' + letter
        else:
            word_robber += letter

    claudio_says(word_robber)

def compare_strings():
    '''
    Checks whether all chacacters of the second string are in the first one
    '''
    is_match = 'Match!'

    string1 = input('Enter a word: ')
    string2 = input('Enter another: ')

    chars_str1 = list(string1)

    for letter in string2:
        if letter not in chars_str1:
            is_match = 'No match!'
            break
        chars_str1.remove(letter)

    claudio_says(is_match)

def double_number():
    '''
    Iteratively doubles a number until it contains all digits 0-9
    '''
    unique_digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    tries = -1

    my_num = int(input('What number to start with? '))
    max_tries = int(input('How many tries? '))

    for i in range(0, max_tries + 1):
        my_digits = set(str(my_num))

        if unique_digits.issubset(my_digits):
            tries = i
            break

        my_num *= 2

    claudio_says(f'Answer: {tries} times')

def tabs_to_spaces():
    '''
    Replaces all tabs in a string with three blank spaces
    '''
    word_tabs = input('Enter a word (must contain at least one tab): ')
    word_spaces = word_tabs.replace('\t', '   ')
    claudio_says(word_spaces)

def portmanteau():
    '''
    Combines two words 
    '''
    vowels = 'aeiouy'

    name1 = input('Enter a name (or word): ')
    name2 = input('Enter another name (or word): ')

    part1 = ''
    part2 = ''

    for i, letter in enumerate(name1):
        if letter in vowels:
            part1 = name1[:i]
            break

    for i, letter in enumerate(name2):
        if letter in vowels:
            part2 = name2[i:]
            break

    claudio_says(part1 + part2)

def score_game():
    '''
    Calculates and outputs players final scores
    '''
    score_dict = {}

    score_str = input('Enter a string of players and their scores: ')

    # look at one player-score pair at a time
    for i in range(0, len(score_str), 2):
        player = score_str[i]
        score = int(score_str[i+1])

        # check if points should be subtracted or added
        if player.isupper():
            score_dict[player.lower()] = score_dict.get(player.lower(), 0) - score
        else:
            score_dict[player] = score_dict.get(player, 0) + score
    
    # make a nice string with results
    result_str = ''
    for key, value in score_dict.items():
        result_str += key + ' ' + str(value) + ', '

    claudio_says(f'Final score: {result_str[:-2]}')
