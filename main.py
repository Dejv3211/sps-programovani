cislo1 = float(input("zadej číslo: "))
cislo2 = float(input("zadej dalsi cislo: "))
operace = input("co s tím mám dělat: ")

if operace == "scitani":
    print(cislo1 + cislo2) 
elif operace == "odcitani":
    print(cislo1 - cislo2)
elif operace == "nasobeni":
    print(cislo1 * cislo2)
elif operace == "deleni":
    if cislo2 == 0:
        print("nemůžeš dělit nulou")
    else:
        print(cislo1 / cislo2)
else: 
    print("napiš pouze: deleni scitani nasobeni deleni")
    