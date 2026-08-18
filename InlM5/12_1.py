MORSE_KOD = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "Å": ".--.-",
    "Ä": ".-.-",
    "Ö": "---.",
    " ": "/",
}

# Omvänd dictionary för att kunna översätta tillbaka
OMVÄND_MORSE = {v: k for k, v in MORSE_KOD.items()}

text = input("Skriv texten som ska översättas till morsekod: \n")

morse_lista = []
for tecken in text.upper():
    if tecken in MORSE_KOD:
        morse_lista.append(MORSE_KOD[tecken])

morse_resultat = " ".join(morse_lista)
print("\nPå morsekod:\n" + morse_resultat)

# Översätt tillbaka från morsekod till text
tillbaka_lista = []
kod_element = morse_resultat.split(" ")

for kod in kod_element:
    if kod in OMVÄND_MORSE:
        tillbaka_lista.append(OMVÄND_MORSE[kod])

print("\nTillbaka till vanlig text:\n" + "".join(tillbaka_lista))