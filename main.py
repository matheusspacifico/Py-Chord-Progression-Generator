from my_libraries.music_keys import *
from my_libraries.progressions import *
from my_libraries.my_functions import *
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
        print("====================================================================")
        print("Please choose a key.")
        print("Type \"check\" if you wish to see all the options available.")
        while True:
            option_key = str(input())
            if option_key == "check":
                print(all_keys_short)
            elif option_key in all_keys_short:
                key_cache = option_key
                return key_to_scale[option_key], key_cache
            else:
                print("Invalid answer! Try again.")
    elif option == 2:
        random_key = random.choice(all_keys_short)
        key_cache = random_key
        return key_to_scale[random_key], key_cache
    
def get_chords(final_key):
    progression = random.choice(test) # using "test" instead of "all_progressions" to test it
    _chords = ""
    for i, chord in enumerate(progression_dict[progression]):
        _chords += final_key[chord-1]
        if i < len(progression) - 1:
            _chords += " "
    _chords = progression_correction(_chords, progression)
    return _chords

def main():
    print("====================================================================")
    print("Would you like to choose a key or let a random one be used?")
    print("[1] - Choose a key")
    print("[2] - Use a random key")
    option = entry_point()
    final_key = chosen_key(option)
    notes, key = final_key
    chords = get_chords(notes)
    print("====================================================================")
    print(f"Key: {key}")
    print(f"Notes: {notes}")
    print(f"Chord progression: {chords}") # adicionar sétimas e dizer se o acorde é menor!!!
    print("====================================================================")
    
if __name__ == "__main__":
    main()