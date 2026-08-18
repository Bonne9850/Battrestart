input_lista = input("Ange element till listan (separera med komma): ").split(",")
input_tuppel = input("Ange element till tuplen (separera med komma): ").split(",")

lista = [x.strip() for x in input_lista]
tuppel = tuple(x.strip() for x in input_tuppel)

lika = True

if len(lista) != len(tuppel):
    lika = False
else:
    for elem_lista, elem_tuppel in zip(lista, tuppel):
        if elem_lista != elem_tuppel:
            lika = False
            break

if lika:
    print("Listan och tuplen är LIKA.")
else:
    print("Listan och tuplen är OLIKA.")