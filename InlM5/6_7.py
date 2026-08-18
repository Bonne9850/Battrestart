def magisk_fyrkant():
    n = int(input("Ange storlek på matrisen (N x N): "))
    matris = []

    for i in range(n):
        rad_input = input(
            f"Ange element för rad {i+1} (separera med mellanslag): "
        )
        rad = [int(x) for x in rad_input.split()]

        if len(rad) != n:
            print(f"Fel: Raden måste innehålla exakt {n} tal.")
            return False, []

        matris.append(rad)

    # referenssumman från första raden
    target = sum(matris[0])

    # Kontrollera alla rader
    for rad in matris:
        if sum(rad) != target:
            return False, matris

    # Kontrollera alla kolumner
    for c in range(n):
        if sum(matris[r][c] for r in range(n)) != target:
            return False, matris

    # Kontrollera båda diagonalerna
    diagonal1 = sum(matris[i][i] for i in range(n))
    diagonal2 = sum(matris[i][n - 1 - i] for i in range(n))

    if diagonal1 != target or diagonal2 != target:
        return False, matris

    return True, matris


# Användning
ar_magisk, matris = magisk_fyrkant()

if ar_magisk:
    print("\nDet är en magisk fyrkant!")
else:
    print("\nDet är INTE en magisk fyrkant.")