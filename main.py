from colorama import init, Fore, Back, Style
import random
init()

loop = True
word_list = ["crown", "build", "logic", "plane", "focus", "money", "plant", "plate", "pound", "other", "input", "horse", "green", "group", "beans", "guide", "layer", "mayor", "lunch", "limit", "model", "point", "scope", "score", "title", "total", "world"]
while loop:
    print(Back.WHITE + Fore.BLACK + "Start a new game? (y/quit)" + Style.RESET_ALL)
    command = input()
    if command == "quit":
        loop = False
    elif command == "y":
        inner_loop = 0
        word = random.choice(word_list)
        print("Enter a word")

        while inner_loop < 6:

            attempt = input()

            # Game logic
            output = ""
            for i in range(word.__len__()):
                if attempt[i] == word[i]:
                    output = output + Back.RED + attempt[i] + Back.RESET
                elif attempt[i] in word:
                    output = output + Back.YELLOW + attempt[i] + Back.RESET
                else:
                    output = output + attempt[i] + Back.RESET
            print(output)
            if word == attempt:
                print("Congrats")
                inner_loop = inner_loop + 6 # Reset game

            inner_loop = inner_loop + 1
