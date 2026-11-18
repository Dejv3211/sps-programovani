a = int(input("cislo1 "))
b = int(input("cislo2 "))

while not (a == 0 or b == 0):
    if a > b:
        c = b // a
        b = b - (a*c)
    else:
        c = a // b
        a = a - (b*c)
        continue
if b == 0:
    print("nejvetsi delitel je B")
else:
    print("nejvetsi delitel je A")
        
