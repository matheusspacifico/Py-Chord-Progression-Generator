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
    return _chords
    