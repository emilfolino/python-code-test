#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Marvin chatbot"""

import marvin1
import marvin2
import inventory

marvin_image = r"""
          _____
         /_____\
    ____[\`---'/]____
   /\ #\ \_____/ /# /\
  /  \# \_.---._/ #/  \
 /   /|\  |   |  /|\   \
/___/ | | |   | | | \___\
|  |  | | |---| | |  |  |
|__|  \_| |_#_| |_/  |__|
//\\  <\ _//^\\_ />  //\\
\||/  |\//// \\\\/|  \||/
      |   |   |   |
      |---|   |---|
      |---|   |---|
      |   |   |   |
      |___|   |___|
      /   \   /   \
     |_____| |_____|
     |HHHHH| |HHHHH|
"""

def main():
    """ main program loop"""

    bag = []
    
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Marvin. I know it all. What can I do you for?")
        print("1) Present yourself to Marvin.")
        print("2) Convert Celsius to Fahrenheit.")
        print("3) Word muliplication.")
        print("4) Sum and mean.")
        print("5) String manipulation.")
        print("6) Isogram checker.")
        print("7) Number comparison.")
        print("8) Roeverspraak-translator.")
        print("9) Randomize string.")
        print("10) Generate acronym.")
        print("11) Mask string.")
        print("12) Find all indexes.")
        print("Extra DLC:")
        print("a1) String comparison")
        print("a2) All-digit Doubler")
        print("a3) Tab-to-space converter.")
        print("a4) Name combiner.")
        print("a5) Play a game.")
        print("q) Quit.")
        print('\n\nTry out my "inv" commands!')

        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        elif choice == "1":
            marvin1.greet()

        elif choice == "2":
            marvin1.celcius_to_farenheit()

        elif choice == "3":
            marvin1.word_manipulation()

        elif choice == "4":
            marvin1.sum_and_average()

        elif choice == "5":
            marvin1.hyphen_string()

        elif choice == "6":
            marvin1.is_isogram()

        elif choice == "7":
            marvin1.compare_numbers()

        elif choice == "8":
            marvin1.robber_language()

        elif choice == "9":
            string = input("Skriv ett ord eller en mening att blanda: ")
            print(marvin2.randomize_string(string))

        elif choice == "10":
            string = input("Skriv en sträng att akronymisera: ")
            print(marvin2.get_acronym(string))

        elif choice == "11":
            string = input("Skriv en sträng att maskera: ")
            print(marvin2.mask_string(string))
        
        elif choice == "12":
            string = input("Skriv en lång sträng: ")
            substring = input("Skriv en kort sträng: ")
            print(marvin2.find_all_indexes(string, substring))

        elif choice == "a1":
            marvin1.string_comparison()

        elif choice == "a2":
            marvin1.all_digit_doubler()

        elif choice == "a3":
            marvin1.tab_to_space_converter()

        elif choice == "a4":
            marvin1.name_combiner()

        elif choice == "a5":
            marvin1.string_game()

        elif choice == "b1":
            max_points = input("Ange maxpoängen: ")
            points = input("Ange dina poäng: ")
            print(marvin2.points_to_grade(max_points, points))

        elif choice == "b2":
            string1 = input("Ange sträng 1/4: ")
            string2 = input("Ange sträng 2/4: ")
            string3 = input("Ange sträng 3/4: ")
            string4 = input("Ange sträng 4/4: ")
            print(marvin2.has_strings(string1, string2, string3, string4))

        else:
            choice_list = choice.split()
            if choice_list[0] == "inv":
                #check if simple inv
                if len(choice_list) == 1:
                    inventory.inventory(bag)
                
                #inv pick
                elif choice_list[1] == "pick":
                    item = choice_list[2] #mus,tjur
                    if len(choice_list) > 3:
                        index = choice_list[3]
                        bag = inventory.pick(bag, item, index)
                    else:
                        bag = inventory.pick(bag, item)

                #inv drop
                elif choice_list[1] == "drop":
                    item = choice_list[2]
                    bag = inventory.drop(bag, item)

                #inv swap 
                elif choice_list[1] == "swap":
                    item1 = choice_list[2]
                    item2 = choice_list[3]
                    bag = inventory.swap(bag, item1, item2)

                #complex inv
                else:
                    try:
                        start = int(choice_list[1])
                        stop = int(choice_list[2])
                        inventory.inventory(bag, start, stop)
                    except (ValueError, IndexError):
                        print("Invalid command")
            else:
                print("Invalid command")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
