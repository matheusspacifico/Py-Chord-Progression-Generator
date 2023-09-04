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
                match option_key:
                    case "Ab":
                        return a_flat_major
                    case "A":
                        return a_major
                    case "Bb":
                        return b_flat_major
                    case "B":
                        return b_major
                    case "C":
                        return c_major
                    case "Db":
                        return d_flat_major
                    case "D":
                        return d_major
                    case "Eb":
                        return e_flat_major
                    case "E":
                        return e_major
                    case "F":
                        return f_major
                    case "F#":
                        return f_sharp_major
                    case "Gb":
                        return g_flat_major
                    case "G":
                        return g_major
                    case "Am":
                        return a_minor
                    case "Bbm":
                        return b_flat_minor
                    case "Bm":
                        return b_minor
                    case "Cm":
                        return c_minor
                    case "Dm":
                        return d_minor
                    case "Ebm":
                        return e_flat_minor
                    case "Em":
                        return e_minor
                    case "Fm":
                        return f_minor
                    case "Gm":
                        return g_minor
                    case "A#m":
                        return a_sharp_minor
                    case "C#m":
                        return c_sharp_minor
                    case "C#":
                        return c_sharp_major
                    case "D#m":
                        return d_sharp_minor
                    case "F#m":
                        return f_sharp_minor
                    case "F#":
                        return f_sharp_major
                    case "Gb":
                        return g_flat_major
                    case "G#m":
                        return g_sharp_minor
                    case "G#":
                        return g_sharp_major
            else:
                print("Invalid answer! Try again.")
    elif option == 2:
        pass # escrever funcao random()
        
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