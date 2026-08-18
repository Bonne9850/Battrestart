# Comviq mannen

antal_min = int(input("Hur många minuter ska du prata i telefon, yäni?"))

if antal_min <= 33:
    print("Då ska du ha ett kontantabonnemang")
elif antal_min > 33 and antal_min < 66:
    print("I sådana fall lönar sig Normal mest")
else:
    print("Du behöver ett PLUSabonnemang bror")