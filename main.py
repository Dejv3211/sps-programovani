def dvojpozdrav(prvni, druha):
    a = str(print("Ahoj", prvni, "a", druha))
    delka = len(a)
    return len(a)


for prvni in ["Adam", "Bert", "Cyril"]:
    for druha in ["Aneta", "Bára", "Cecílie"]:
        delka = dvojpozdrav(prvni, druha)
        print(f"Pozdrav zabere {delka} znaků.")
