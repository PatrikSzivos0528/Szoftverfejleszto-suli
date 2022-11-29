a = int(input("Elso oldal:"))
b = int(input("Masodik oldal:"))
c = int(input("Harmadik oldal(a legnagyobb):"))

def derekszogu_e():
    if (a**2)+(b**2)==(c**2):
        print("A hámoszög derékszögű")
    else:
        print("A háromszög nem derékszögű")

derekszogu_e()

