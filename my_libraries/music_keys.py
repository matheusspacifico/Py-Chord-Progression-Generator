# Major Keys
a_flat_major = ["Ab", "Bb", "C", "Db", "Eb", "F", "G"]
a_major = ["A", "B", "C#", "D", "E", "F#", "G#"]
b_flat_major = ["Bb", "C", "D", "Eb", "F", "G", "A"]
b_major = ["B", "C#", "D#", "E", "F#", "G#", "A#"]
c_major = ["C", "D", "E", "F", "G", "A", "B"]
d_flat_major = ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C"]
d_major = ["D", "E", "F#", "G", "A", "B", "C#"]
e_flat_major = ["Eb", "F", "G", "Ab", "Bb", "C", "D"]
e_major = ["E", "F#", "G#", "A", "B", "C#", "D#"]
f_major = ["F", "G", "A", "Bb", "C", "D", "E"]
f_sharp_major = ["F#", "G#", "A#", "B", "C#", "D#", "E#"]
g_flat_major = ["Gb", "Ab", "Bb", "Cb", "Db", "Eb", "F"]
g_major = ["G", "A", "B", "C", "D", "E", "F#"]

# Natural Minor Keys (Relative to Major Keys)
a_minor = ["A", "B", "C", "D", "E", "F", "G"]
b_flat_minor = ["Bb", "C", "Db", "Eb", "F", "Gb", "Ab"]
b_minor = ["B", "C#", "D", "E", "F#", "G", "A"]
c_minor = ["C", "D", "Eb", "F", "G", "Ab", "Bb"]
d_minor = ["D", "E", "F", "G", "A", "Bb", "C"]
e_flat_minor = ["Eb", "F", "Gb", "Ab", "Bb", "Cb", "Db"]
e_minor = ["E", "F#", "G", "A", "B", "C", "D"]
f_minor = ["F", "G", "Ab", "Bb", "C", "Db", "Eb"]
g_minor = ["G", "A", "Bb", "C", "D", "Eb", "F"]

# Additional Keys (Enharmonic Equivalents)
a_sharp_minor = ["A#", "B#", "C#", "D#", "E#", "F#", "G#"]
c_sharp_major = ["C#", "D#", "E#", "F#", "G#", "A#", "B#"]
c_sharp_minor = ["C#", "D#", "E", "F#", "G#", "A", "B"]
d_flat_major = ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C"]
d_sharp_minor = ["D#", "E#", "F#", "G#", "A#", "B", "C#"]
f_sharp_major = ["F#", "G#", "A#", "B", "C#", "D#", "E#"]
g_flat_minor = ["Gb", "Ab", "Bbb", "Cb", "Db", "Ebb", "Fb"]
g_sharp_minor = ["G#", "A#", "B", "C#", "D#", "E", "F#"]

# Keys that didn't fit
f_sharp_minor = ["F#", "G#", "A", "B", "C#", "D", "E"]
g_sharp_major = ["G#", "A#", "C", "Db", "Eb", "F", "G"]

# Every key listed
all_keys = [
    a_flat_major, a_major, b_flat_major, b_major, c_major, d_flat_major, d_major,
    e_flat_major, e_major, f_major, f_sharp_major, g_flat_major, g_major, a_minor,
    b_flat_minor, b_minor, c_minor, d_minor, e_flat_minor, e_minor, f_minor, g_minor,
    a_sharp_minor, c_sharp_major, c_sharp_minor, d_flat_major, d_sharp_minor,
    f_sharp_major, g_flat_minor, g_sharp_minor
]

all_keys_short = ["Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "F#", "Gb", "G",
        "Am", "Bbm", "Bm", "Cm", "Dm", "Ebm", "Em", "Fm", "Gm", 
        "A#m", "C#m", "C#", "Db", "D#m", "F#m", "F#", "Gb", "G#m", "G#"]

key_to_scale = {
    "Ab": a_flat_major,
    "A": a_major,
    "Bb": b_flat_major,
    "B": b_major,
    "C": c_major,
    "Db": d_flat_major,
    "D": d_major,
    "Eb": e_flat_major,
    "E": e_major,
    "F": f_major,
    "F#": f_sharp_major,
    "Gb": g_flat_major,
    "G": g_major,
    "Am": a_minor,
    "Bbm": b_flat_minor,
    "Bm": b_minor,
    "Cm": c_minor,
    "Dm": d_minor,
    "Ebm": e_flat_minor,
    "Em": e_minor,
    "Fm": f_minor,
    "Gm": g_minor,
    "A#m": a_sharp_minor,
    "C#m": c_sharp_minor,
    "C#": c_sharp_major,
    "D#m": d_sharp_minor,
    "F#m": f_sharp_minor,
    "G#m": g_sharp_minor,
    "G#": g_sharp_major,
}
