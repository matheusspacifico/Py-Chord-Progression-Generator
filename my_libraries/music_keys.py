# Major Keys
a_flat_major = ["Ab", "Bbm", "Cm", "Db", "Eb", "Fm", "G°"]
a_major = ["A", "Bm", "C#m", "D", "E", "F#m", "G#°"]
b_flat_major = ["Bb", "Cm", "Dm", "Eb", "F", "Gm", "A°"]
b_major = ["B", "C#m", "D#m", "E", "F#", "G#m", "A#°"]
c_major = ["C", "Dm", "Em", "F", "G", "Am", "B°"]
d_flat_major = ["Db", "Ebm", "Fm", "Gb", "Ab", "Bbm", "C°"]
d_major = ["D", "Em", "F#m", "G", "A", "Bm", "C#°"]
e_flat_major = ["Eb", "Fm", "Gm", "Ab", "Bb", "Cm", "D°"]
e_major = ["E", "F#m", "G#m", "A", "B", "C#m", "D#°"]
f_major = ["F", "Gm", "Am", "Bb", "C", "Dm", "E°"]
f_sharp_major = ["F#", "G#m", "A#m", "B", "C#", "D#m", "E#°"]
g_flat_major = ["Gb", "Abm", "Bbm", "Cb", "Db", "Ebm", "F°"]
g_major = ["G", "Am", "Bm", "C", "D", "Em", "F#°"]

# Natural Minor Keys (Relative to Major Keys)
a_minor = ["Am", "B°", "C", "Dm", "Em", "F", "G"]
b_flat_minor = ["Bbm", "C°", "Db", "Ebm", "Fm", "Gb", "Ab"]
b_minor = ["Bm", "C#°", "D", "Em", "F#m", "G", "A"]
c_minor = ["Cm", "D°", "Eb", "Fm", "Gm", "Ab", "Bb"]
d_minor = ["Dm", "E°", "F", "Gm", "Am", "Bb", "C"]
e_flat_minor = ["Ebm", "F°", "Gb", "Abm", "Bbm", "Cb", "Db"]
e_minor = ["Em", "F#°", "G", "Am", "Bm", "C", "D"]
f_minor = ["Fm", "G°", "Ab", "Bbm", "Cm", "Db", "Eb"]
g_minor = ["Gm", "A°", "Bb", "Cm", "Dm", "Eb", "F"]

# Additional Keys (Enharmonic Equivalents)
a_sharp_minor = ["A#m", "B#°", "C#", "D#m", "E#m", "F#", "G#"]
c_sharp_major = ["C#", "D#m", "E#m", "F#", "G#", "A#m", "B#°"]
c_sharp_minor = ["C#m", "D#°", "E", "F#m", "G#m", "A", "B"]
d_flat_major = ["Db", "Ebm", "Fm", "Gb", "Ab", "Bbm", "C°"]
d_sharp_minor = ["D#m", "E#°", "F#", "G#m", "A#m", "B", "C#"]
f_sharp_major = ["F#", "G#m", "A#m", "B", "C#", "D#m", "E#°"]
g_flat_minor = ["Gbm", "Ab°", "Bbb", "Cbm", "Dbm", "Ebb", "Fb"]
g_sharp_minor = ["G#m", "A#°", "B", "C#m", "D#m", "E", "F#"]

# Keys that didn't fit
f_sharp_minor = ["F#m", "G#°", "A", "Bm", "C#m", "D", "E"]
g_sharp_major = ["G#", "A#m", "Cm", "Db", "Eb", "Fm", "G°"]

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