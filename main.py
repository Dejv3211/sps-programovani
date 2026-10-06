muj_list = [
    "Ostrava",
    "Kladno",
    "Praha",
    "Liberec",
    "Opava",
    "České Budějovice",
    "Litoměřice"
]

vstup = int(input("Zadejte index města: "))

for i, mesto in enumerate(muj_list, start=1):
    if i == vstup:
        print(i, mesto,"vybrano")
    else:
        print(i, mesto)