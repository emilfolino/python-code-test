#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Claudio (Marvin) with a simple menu to start up with.
Claudio (Marvin) doesnt do anything, just presents a menu with some choices.
You should add functinoality to Claudio (Marvin).
"""

claudio_image = r"""
      c~~p ,---------. 
 ,---'oo  )           \
( O O                  )/
 `=^='                 /
       \    ,     .   /
       \\  |-----'|  /
       ||__|    |_|__|
"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""
while True:
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(claudio_image)
    print("Hey there, I'm Claudio - the omnipotent hippo. Pleased to eat you! ")
    print("1) Present yourself to Claudio.")
    print("2) Convert celsius to fahrenheit.")
    print("3) Repeat a word (it really is a lot of fun).")
    print("4) Calculate sum and mean.")
    print("5) Spell out a word.")
    print("6) Detect isogram (it's definitely useful).")
    print("7) Smaller, larger or just the same (trust me - you will want to know).")
    print("8) Translate a word to The Robber Language.")
    print("a1) Check if all characters of a word are in another.")
    print("a2) Double a number until it contains al the digits 0-9.")
    print("a3) Replace tabs with spaces.")
    print("a4) Create a catchy word or name combination (portmanteau).")
    print("a5) Score a game.")
    print("q) Quit.")

    choice = input("--> ")

    if choice == "q":
        print("Arrivederci and Goodbye! - Welcome back anytime!")
        break

    elif choice == "1":
        name = input("What is your name? ")
        
        print("\nClaudio says:\n")
        print(f"Cool dude, I once knew a dodo named {name}!")
        print("What can I do for you?!")

    elif choice == "2":
        celsius = float(input("How many degrees °C are we talking? "))
        
        fahrenheit = round(celsius * 9 / 5 + 32, 2)
        
        print("\nClaudio says:\n")
        print(f"That's {fahrenheit} °F!")
        print("What more can I do for you?!")

    elif choice == "3":
        word_to_repeat = input("Let's hear it! What's your special word? ")
        num_times = int(input("And how many times do you whish for me to reapeat it? "))
        
        print("\nClaudio says:\n")
        print(word_to_repeat*num_times)
        print("What more can I do for you?!")
    
    elif choice == "4":
        total = 0
        count = 0

        print("Feed me your numbers (one at a time)! Enter 'done' when you're ... well, done!")
        while True:
            answer = input("")
            
            if answer == "done":
                break
            
            try:
                num = float(answer)

            except ValueError:
                ("Oyy only numbers! I'm a picky eater, okey?")
                continue

            total += num
            count +=1

        average = total/count

        print("\nClaudio says:\n")
        print(f"The sum of all the numbers is {total:.2f} and the average is {average:.2f}.")
        print("What more can I do for you?!")

    elif choice == "5":
        word_to_spell = input("What word do you wan't me to spell out for you? ")
        
        letters = []
        
        # for simplicity, use enumerate to get both the current iteration and item
        for count, letter in enumerate(word_to_spell):
            letters.append(letter * (count + 1)) 
        
        new_string = '-'.join(letters)
        
        print("\nClaudio says:\n")
        print(new_string)
        print("What more can I do for you?!")
            
    elif choice == "6":
        maybe_isogram = input("So what is this could-be-isogram? ")
        memory = ""
        is_isogram = "Match!"

        for letter in maybe_isogram:
            if letter in memory:
                is_isogram = "No match!"
                break
            memory += letter
        
        print("\nClaudio says:\n")
        print(is_isogram)
        print("What more can I do for you?!")

    elif choice == "7":
        last = None

        print("Enter a number to start with ('done' to exit): ")
        while True:
            answer = input("")

            if answer == "done":
                break

            try:
                current_num = int(answer)
            except ValueError:
                print("not a number!")
                continue

            if last is None:
                print("Enter another one to compare it to: ")
                last = current_num
                continue

            if current_num < last:
                print("smaller!")
            elif current_num == last:
                print("same!")
            else:
                print("larger!")

            print("Enter another one to compare to the last: ")
            last = current_num
        
        print("\nWhat more can I do for you?!")
    
    elif choice == "8":
        consonants_sv = "bcdfghjklmnpqrstvwxz"
        word_robber = ""

        word = input("Enter a word: ").lower()

        for letter in word:
            if letter in consonants_sv:
                word_robber += letter + "o" + letter
            else:
                word_robber += letter

        print("\nClaudio says:\n")
        print(word_robber)
        print("What more can I do for you?!")

    elif choice == "a1":
        is_match = "Match!"

        string1 = input("Enter a word: ")
        string2 = input("Enter another: ")

        chars_str1 = list(string1)

        for letter in string2:
            if letter not in chars_str1:
                is_match = "No match!"
                break
            chars_str1.remove(letter)
        
        print("\nClaudio says:\n")
        print(is_match)
        print("What more can I do for you?!")

    elif choice == "a2":
        unique_digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        tries = -1

        my_num = int(input("What number to start with? "))
        max_tries = int(input("How many tries? "))

        for i in range(0, max_tries + 1):
            my_digits = set(str(my_num))

            if unique_digits.issubset(my_digits):
                tries = i
                break

            my_num *= 2

        print("\nClaudio says:\n")
        print(f"Answer: {tries} times")
        print("What more can I do for you?!")
            

    elif choice == "a3":
        word_tabs = input("Enter a word (must contain at least one tab): ")
        
        word_spaces = word_tabs.replace("\t", "   ")

        print("\nClaudio says:\n")
        print(word_spaces)
        print("What more can I do for you?!")

    elif choice == "a4":
        vowels = "aeiouy"

        name1 = input("Enter a name (or word): ")
        name2 = input("Enter another name (or word): ")

        part1 = ""
        part2 = ""

        for i, letter in enumerate(name1):
            if letter in vowels:
                part1 = name1[:i]
                break

        for i, letter in enumerate(name2):
            if letter in vowels:
                part2 = name2[i:]
                break

        combined = part1 + part2

        print("\nClaudio says:\n")
        print(combined)
        print("What more can I do for you?!")

    elif choice == "a5":
        score_dict = {}

        score_str = input("Enter a string of players and their scores: ")

        # look at one player-score pair at a time
        for i in range(0, len(score_str), 2):
            player = score_str[i]
            score = int(score_str[i+1])

            # check if points should be subtracted or added
            if player.isupper():
                score_dict[player.lower()] = score_dict.get(player.lower(), 0) - score
            else:
                score_dict[player] = score_dict.get(player, 0) + score

        # to iterate over all but the last items, convert to list first
        score_list = list(score_dict.items())

        # put together a pretty string with all players and their final scores
        combo_score_str = ""

        for i in range(len(score_list) - 1):
            combo_score_str += score_list[i][0] + " " + str(score_list[i][1]) + ", "

        combo_score_str += score_list[-1][0] + " " + str(score_list[-1][1])
        
        print("\nClaudio says:\n")
        print(f"Final score: {combo_score_str}")
        print("What more can I do for you?!")
        
    else:
        print("That is not a valid choice. You can only choose from the menu.")

    input("\nPress enter to continue...")
