def masodperc_atvaltas(ora, perc, masodperc):
    ido = 0
    ido = ido + ora * 60 * 60
    ido = ido + perc * 60
    ido = ido + masodperc 
    return ido

print(masodperc_atvaltas(7,14,30))