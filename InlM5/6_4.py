import random

# Simulerar 9 st uppmätta temperaturvärden (mellan 16.0 och 25.0 °C)
antal_matningar = 100
matvarden = [round(random.uniform(16.0, 25.0), 1) for _ in range(antal_matningar)]

sorterade_varden = sorted(matvarden)
n = len(sorterade_varden)
mitten = n // 2

if n % 2 != 0:
    # Udda antal mätvärden
    median = sorterade_varden[mitten]
else:
    # Jämnt antal mätvärden
    median = (sorterade_varden[mitten - 1] + sorterade_varden[mitten]) / 2

print(f"Uppmätta värden: {matvarden}")
print(f"Sorterade värden: {sorterade_varden}")
print(f"Median: {median}")