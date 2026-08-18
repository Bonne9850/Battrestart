peronnummer = input("Ange personnummer: \n")

pnr_rensat = peronnummer.replace("-", "").replace("+", "")

nast_sista_siffran = int(pnr_rensat[-2])

if nast_sista_siffran % 2 == 0:
    print(f"Personen är en kvinna.")
else:
    print(f"Personen är en man.")