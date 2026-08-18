romerska_tal = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

inmatning = input("Ange ett romerskt tal (t.ex. XIV, MCMXCIX): ").upper()

totalt = 0
for i in range(len(inmatning)):
    nuvarande = romerska_tal[inmatning[i]]
    
    # Om det nuvarande tecknet är mindre än nästa, drar vi av värdet
    if i + 1 < len(inmatning) and nuvarande < romerska_tal[inmatning[i + 1]]:
        totalt -= nuvarande
    else:
        totalt += nuvarande

print(f"Det romerska talet {inmatning} blir: {totalt}")