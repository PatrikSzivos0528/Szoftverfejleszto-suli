#a,

def orakra_valtas(masodperc):
    ido = masodperc // 3600
    return ido

print(orakra_valtas(9010))

#b, 

def percekre_valtas(masodperc, perc):
    ido = masodperc % 3600 //60 
    return ido

print(percekre_valtas(9010 , 0))

#c,

def masodpercekre_valtas(masodperc, perc, ora):
    ido = masodperc % 3600 % 60 
    return ido

print(masodpercekre_valtas(9010 , 0 , 0))