text = input("Skriv texten som ska översättas till rövarspråket: \n")

konsonanter = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
resultat = []

for tecken in text:
    if tecken in konsonanter:
        if tecken.isupper():
            resultat.append(tecken + "o" + tecken.lower())
        else:
            resultat.append(tecken + "o" + tecken)
    else:
        resultat.append(tecken)

rovarsprak = "".join(resultat)
print("på rövarspråk:")
print(rovarsprak)

tillbaka = []
i = 0

while i < len(rovarsprak):
    tecken = rovarsprak[i]

    # Kollar om vi har ett mönster av typen konsonant + o + samma konsonant
    if tecken in konsonanter and i + 2 < len(rovarsprak):
        mitten = rovarsprak[i + 1]
        sista = rovarsprak[i + 2]

        if mitten in "oO" and sista.lower() == tecken.lower():
            tillbaka.append(tecken)
            i += 3  # Hoppar över 'o' och den extra konsonanten
            continue

    tillbaka.append(tecken)
    i += 1

print("\nTillbaka till vanlig text:\n" + "".join(tillbaka))