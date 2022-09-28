#!/usr/bin/env python3

'''
Claudio presents the user with a menu 
and checks the choices to call the corresponding functions
'''

import marvin1
import marvin2
import inventory

claudio_image = r'''
      c~~p ,---------. 
 ,---'oo  )           \
( O O                  )/
 `=^='                 /
       \    ,     .   /
       \\  |-----'|  /
       ||__|    |_|__|
'''

def main():
    '''
    Continuously checks the users choices
    and calls the corresponding functions until q is pressed
    Also lets user keep an inventory of items
    '''

    bag = []

    while True:
        print(chr(27) + '[2J' + chr(27) + '[;H')
        print(claudio_image)
        print('Hey there, I am Claudio - the omnipotent hippo. Pleased to eat you! ')
        print('1) Present yourself to Claudio.')
        print('2) Convert celsius to fahrenheit.')
        print('3) Repeat a word (it really is a lot of fun).')
        print('4) Calculate sum and mean.')
        print('5) Spell out a word.')
        print('6) Detect isogram (it is definitely useful).')
        print('7) Smaller, larger or just the same (trust me - you will want to know).')
        print('8) Translate a word to The Robber Language.')
        print('9) Randomly re-order the letters of a string.')
        print('10) Create an acronym.')
        print('11) Mask the characters of a string.')
        print('12) Get all indexes of a substring.')
        print('a1) Check if all characters of a word are in another.')
        print('a2) Double a number until it contains al the digits 0-9.')
        print('a3) Replace tabs with spaces.')
        print('a4) Create a catchy word or name combination (portmanteau).')
        print('a5) Score a game.')
        print('b1) Grade test points.')
        print('b2) Compare strings.')
        print('q) Quit.')
        print('\n')
        print('Try out my "inv" commands!')
        print('------------')

        choice = input('--> ')

        if choice == 'q':
            print('Arrivederci and Goodbye! - Welcome back anytime!')
            break

        elif choice == '1':
            marvin1.greet()

        elif choice == '2':
            marvin1.celcius_to_farenheit()

        elif choice == '3':
            marvin1.word_manipulation()

        elif choice == '4':
            marvin1.sum_and_average()

        elif choice == '5':
            marvin1.hyphen_string()

        elif choice == '6':
            marvin1.is_isogram()

        elif choice == '7':
            marvin1.compare_numbers()

        elif choice == '8':
            marvin1.robber_lanquage()
        
        elif choice == 'a1':
            marvin1.compare_strings()

        elif choice == 'a2':
            marvin1.double_number()

        elif choice == 'a3':
            marvin1.tabs_to_spaces()
        
        elif choice == 'a4':
            marvin1.portmanteau()

        elif choice == 'a5':
            marvin1.score_game()

        elif choice == '9':
            my_original_string = input('Enter a string: ')
            print(marvin2.randomize_string(my_original_string))

        elif choice == '10':
            my_full_string = input('Enter a string: ')
            print(marvin2.get_acronym(my_full_string))

        elif choice == '11':
            my_plain_string = input('Enter a string: ')
            print(marvin2.mask_string(my_plain_string))

        elif choice == '12':
            my_super_string = input('Enter a string: ')
            my_sub_string = input('And a substring to look for: ')
            print(marvin2.find_all_indexes(my_super_string, my_sub_string))

        elif choice == 'b1':
            my_max_points = input('Max points: ')
            my_points = input('Your points: ')
            print(marvin2.points_to_grade(my_max_points, my_points))

        elif choice == 'b2':
            my_first_str = input("Enter a first string to compare against: ")
            my_second_str = input("Enter a second string: ")
            my_third_str = input("Enter a third string: ")
            my_fourth_str = input("Enter a fourth string: ")
            print(marvin2.has_strings(my_first_str, my_second_str, my_third_str, my_fourth_str))

        elif choice.startswith('inv'):
            # in cases other than the ones described in the assignment, assume inputs are good
            commands = choice.split(' ')

            if len(commands) == 1:
                inventory.inventory(bag)

            elif commands[1] == 'pick':
                if len(commands) == 4:
                    inventory.pick(bag, commands[2], commands[3])         
                elif len(commands) == 3:
                    inventory.pick(bag, commands[2])

            elif commands[1] == 'drop':
                inventory.drop(bag, commands[2])

            elif commands[1] == 'swap':
                inventory.swap(bag, commands[2], commands[3])            

            elif commands[1].isdigit() and commands[2].isdigit():
                inventory.inventory(bag, commands[1], commands[2])

            else:
                print('Invalid inventory command.')

        else:
            print('That is not a valid choice. You can only choose from the menu.')

        input('\nPress enter to continue...')

if __name__ == '__main__':
    main()
