while False:
    string = input()
    if string[::-1] == string:
        print(True)
    else:
        print(False)
        
print("Igen"[::-1])