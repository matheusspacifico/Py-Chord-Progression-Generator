from my_libraries.music_keys import *
from my_libraries.progressions import *
import random

def entry_point():
    while True:
        try:
            option = int(input())
            valid_entries = [1, 2]
            if option not in valid_entries:
                print("Invalid answer! Try again.")
                print("[1] - Choose a key")
                print("[2] - Use a random key")
            else:
                break
        except ValueError:
            print("Invalid answer! Try again.")
            print("[1] - Choose a key")
            print("[2] - Use a random key")
    return option

def chosen_key(option):
    if option == 1:
        print("===========================================================")
        print("Please choose a key.")
        print("Type \"check\" if you wish to see all the options available.")
        while True:
            option_key = str(input())
            if option_key == "check":
                print(all_keys_short)
            elif option_key in all_keys_short:
                return key_to_scale[option_key]
            else:
                print("Invalid answer! Try again.")
    elif option == 2:
        return random.choice(all_keys)
    
def get_chords(final_key):
    progression = random.choice(all_progressions)
    chords = ""
    for i in progression:
        chords += final_key[i]
        chords += " "
    return chords[:-1]
        
def main():
    print("===========================================================")
    print("Would you like to choose a key or let a random one be used?")
    print("[1] - Choose a key")
    print("[2] - Use a random key")
    option = entry_point()
    final_key = chosen_key(option)
    chords = get_chords(final_key)
    print("===========================================================")
    print(f"Key: {final_key}")
    print(f"Chords: {chords}")
    print("===========================================================")
    
if __name__ == "__main__":
    main()