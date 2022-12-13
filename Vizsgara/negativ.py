a = int(input("Adj meg egy sztámot: "))
b = int(input("Add meg a második számot: "))

if a>0 and b >0:
    print("A két szám közül egyik se negatív!")
elif a>0 and b<0:
    print("A két szám közül az egyik negatív!")
elif a<0 and b>0:
    print("A két szám közül az egyik negatív!")
else:
    print("Mindkét szám negatív")