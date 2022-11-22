Hónap = ["január", "február", "március", "április", "május", "juniús", "julius", "augusztus", "szeptember", "oktober", "november", "december"]

a = input("Ez a hónap hány napos? Kérlek írd be a hónap nevét: ")

if a == ("január"):
    print(31)
elif a == ("február"):
    print(28)
elif a == ("március"):
    print(31)
elif a == ("április"):
    print(31)
elif a == ("május"):
    print(31)
elif a == ("juniús"):
    print(31)
elif a == ("julus"):
    print(31)
elif a == ("augusztus"):
    print(31)
elif a == ("szeptember"):
    print(30)
elif a == ("oktober"):
    print(31)
elif a == ("november"):
    print(30)
elif a == ("december"):
    print(31)
else:
    print("None")
    
    