import math

inmatning = input("Ange vektorns komponenter (separera med mellanslag): ")
vektor = [float(x) for x in inmatning.split()]

kvadratsumma = sum(x**2 for x in vektor)
langd = math.sqrt(kvadratsumma)

print(f"\nVektor: {vektor}")
print(f"Matematisk längd: {langd:.2f}")