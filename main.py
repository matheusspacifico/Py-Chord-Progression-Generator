from my_libraries.music_keys import *
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
        
def main():
    print("===========================================================")
    print("Would you like to choose a key or let a random one be used?")
    print("[1] - Choose a key")
    print("[2] - Use a random key")
    option = entry_point()
    final_key = chosen_key(option)
    print(final_key)
    
if __name__ == "__main__":
    main()