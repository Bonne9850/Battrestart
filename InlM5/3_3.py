import math

a = float(input("Ange längden på sida a: "))
b = float(input("Ange längden på sida b: "))
vinkel_grader = float(input("Ange vinkeln mellan sidorna (i grader): "))

if a > 0 and b > 0 and 0 < vinkel_grader < 180:
    vinkel_rad = math.radians(vinkel_grader)
    c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(vinkel_rad))

    s_a = round(a, 4) # pga floats så att 4.99999 == 5 t ex
    s_b = round(b, 4)
    s_c = round(c, 4)

    print(f"\nTredje sidan (c) är: {c:.2f}")

    if s_a == s_b == s_c:
        print("Resultat: Triangeln är LIKSIDIG (alla sidor är lika).")
    elif s_a == s_b or s_a == s_c or s_b == s_c:
        print("Resultat: Triangeln är LIKBENT (två sidor är lika).")
    else:
        print("Resultat: Triangeln är OLIKSIDIG (alla sidor är olika).")
else:
    print(
        "Fel: Sidorna måste vara större än 0 och vinkeln måste vara mellan 0 och 180 grader."
    )