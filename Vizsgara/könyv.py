def konyv_hossz(oldal):
    if oldal > 150:
        return True
    else:
        return False
    

cím = input("Ad meg a könyv címét!: ")    
while (cím != " "):
    oldal = int(input("Add meg az oldalainak számát!: "))
    if konyv_hossz(oldal):
        print("A", cím, "hosszú terjedelmű könyv!")
    else:
        print("A", cím, "rövid terjedelmű könyv!")
    cím = input("Cím:")