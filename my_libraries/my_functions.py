def progression_correction(_chords, progression):
    if progression == "third":
        spaces = 0
        for i in _chords:
            if spaces == 2:
                _chords = _chords.replace(i, i+"b")
                break
            elif i == " ":
                spaces += 1
    elif progression == "fourth":
        spaces = 0
        for i in range(len(_chords)):
            if _chords[i] == " ":
                spaces += 1
                if spaces == 2:
                    _chords = _chords[:i] + "7" + _chords[i:]
                    break
    elif progression == "fourth_alternative":
        spaces = 0
        for i in range(len(_chords)):
            if _chords[i] == " ":
                _chords = _chords[:i] + " " + _chords[i+1] + "b" + _chords[i+2:]
                break
        for i in range(len(_chords)):
            if _chords[i] == " ":
                spaces += 1
                if spaces == 2:
                    _chords = _chords[:i] + "7" + _chords[i:]
                    break
    elif progression == "fifth":
        spaces = 0
        for i in range(len(_chords)):
            if _chords[i] == " ":
                _chords = _chords[:i] + " " + _chords[i+1] + "b" + _chords[i+2:]
                break
        for i in range(len(_chords)):
            if _chords[i] == " ":
                spaces += 1
                if spaces == 2:
                    _chords = _chords[:i] + "+" + _chords[i:]
                    break
    elif progression == "sixth":
        for i in range(len(_chords)):
            if _chords[i-1] == "°":
                _chords = _chords[:i] + "7" + _chords[i:] 
                break               
            elif _chords[i] == " ":
                _chords = _chords[:i] + "°7" + _chords[i:] 
                break
    elif progression == "seventh":
        spaces = 0
        for i in _chords:
            if spaces == 2:
                _chords = _chords.replace(i, i+"b")
                break
            elif i == " ":
                spaces += 1
    elif progression == "eighth":
        spaces = 0
        for i in range(len(_chords)):
            if _chords[i] == " ":
                _chords = _chords[:i] + " " + _chords[i+1] + "b" + _chords[i+2:]
                break
        for i in range(len(_chords)):
            if _chords[i] == " ":
                spaces += 1
                if spaces == 2:
                    _chords = _chords[:i] + "7" + _chords[i:]
                    break
    return _chords

# ninth_progression = [1, 7, 3, 6, 2, 5, 1, 4, 4, 7, 3, 6, 3, 6, 2, 5, 1, 6] # Its complicated: learn more here https://en.wikipedia.org/wiki/Bird_changes
# tenth_progression = [1, 5, 7, 4] #third chord is flat (bVII)
# eleventh_progression = [6, 2, 5, 1]
# twelfth_progression = [1, 5, 6, 5, 3, 5, 1] # third chord is flat (bVI)
# twelfth_progression_alternative = [1, 6, 6, 3, 3, 5, 1] # second chord is flat (bVI)
# thirteenth_progression = [1, 5, 4, 4, 1, 5, 1, 5]
# fourteenth_progression = [1, 5, 1, 7, 3, 2, 1, 5] # 7, 3, 2 are all flat (bVII) (bIII) (bII)
# fifteenth_progression = [2, 5, 1]
# sixteenth_progression = [5, 3] # all chords have minor seven
# seventeenth_progression = [1, 4, 2, 5]