idezet = """Távolság és hosszú távollét minden barátságnak kárára van, bármily kelletlenül valljuk is be. Az emberek ugyanis, még legkedvesebb barátaink is, ha sokáig nem látjuk őket, évek múltán lassanként elvont fogalmakká asznak, miáltal részvétünk irányukban mindinkább pusztán értelmivé, sőt hagyományszerűvé válik. Eleven és mély érzésünk csak azokat illeti, kik szemünk előtt vannak - legyenek azok bár csupán kedves állataink."""

szavak = (idezet).split()
def a_sazvak_szama(szavak):
    darab = 0
    for i in szavak:
        if szavak == 10:
            darab += 1
    return szavak

print(a_sazvak_szama(szavak))