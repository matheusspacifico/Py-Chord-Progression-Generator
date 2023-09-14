first_progression = [1, 6, 4, 5]
second_progression = [1, 5, 6, 4]
third_progression = [1, 4, 7, 4] # third chord is flat (bVII)
fourth_progression = [2, 5, 1] # second chord has minor seven (V7)
fourth_progression_alternative = [2, 2, 1] # second chord is flat has minor seven (bII7)
fifth_progression = [2, 3, 1] # second chord is flat has augmented fifth (bIII+)
sixth_progression = [7, 5, 1] # first chord is diminished has minor seven (VIIo7)
seventh_progression = [4, 3, 2, 1] # third chord is flat (bII)
eighth_progression = [2, 7, 1] # second chord is flat has minor seven (bVII7)
ninth_progression = [1, 6, 2, 5]
tenth_progression = [1, 5, 7, 4] #third chord is flat (bVII)
eleventh_progression = [6, 2, 5, 1]
twelfth_progression = [1, 5, 6, 5, 3, 5, 1] # third chord is flat (bVI)
twelfth_progression_alternative = [1, 6, 6, 3, 3, 5, 1] # second chord is flat (bVI)
thirteenth_progression = [1, 5, 4, 4, 1, 5, 1, 5]
fourteenth_progression = [1, 5, 1, 7, 3, 2, 1, 5] # 7, 3, 2 are all flat (bVII) (bIII) (bII)
fifteenth_progression = [2, 5, 1]
sixteenth_progression = [5, 3] # all chords have minor seven
seventeenth_progression = [1, 4, 2, 5]
# Omnibus progression <-- parei nesse

# 18th - eighteenth
# 19th - nineteenth
# 20th - twentieth
# 21st - twenty-first
# 22nd - twenty-second
# 23rd - twenty-third
# 24th - twenty-fourth
# 25th - twenty-fifth
# 26th - twenty-sixth
# 27th - twenty-seventh
# 28th - twenty-eighth
# 29th - twenty-ninth
# 30th - thirtieth

all_progressions = [
    "first", "second", "third", "fourth", "fourth_alternative",
    "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"
]

progression_dict = {
    "first": first_progression,
    "second": second_progression,
    "third": third_progression,
    "fourth": fourth_progression,
    "fourth_alternative": fourth_progression_alternative,
    "fifth": fifth_progression,
    "sixth": sixth_progression,
    "seventh": seventh_progression,
    "eighth": eighth_progression,
    "ninth": ninth_progression,
    "tenth": tenth_progression,
    "eleventh": eleventh_progression,
    "twelfth": twelfth_progression,
    "twelfth_alternative": twelfth_progression_alternative,
    "thirteenth": thirteenth_progression,
    "fourteenth": fourteenth_progression,
    "fifteenth": fifteenth_progression,
    "sixteenth": sixteenth_progression,
    "seventeenth": seventeenth_progression
}