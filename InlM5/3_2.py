import math

radie = float(input("Ange cirkelns radie: "))

if radie > 0:
    omkrets = 2 * math.pi * radie
    area = math.pi * (radie**2)

    print(f"Cirkelns omkrets: {omkrets:.2f}")
    print(f"Cirkelns area: {area:.2f}")
else:
    print("Fel: Radien måste vara större än 0.")
