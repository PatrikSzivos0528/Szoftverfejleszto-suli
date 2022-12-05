def osszehasonlitas(a,b):
    if a > b:
        return 1
    elif a < b:
        return -1
    elif a == b:
        return 0
    else:
        return False
    
print(osszehasonlitas(5, 4))
print(osszehasonlitas(7, 7))
print(osszehasonlitas(2, 3))
print(osszehasonlitas(42, 1))

