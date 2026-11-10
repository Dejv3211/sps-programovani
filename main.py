jmena = ["Anna", "Bára", "Cyril", "Dana", "Emil"]
print(f"Seznam: {jmena}")
try:
    vstup = int(input(f"Zadej index (0-{len(jmena)-1}): "))
    print(jmena[vstup])
except ValueError:
    print("tohle neni číslo")
except IndexError:
    print("tohle číslo neni v seznamu")

