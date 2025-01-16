def elso():
    print("Első feladat:")
    szin:str=str(input("Kérek egy színkeverési módszert: "))
    kod=(input("Kérem a kódot: "))
    if szin=="HEX" and len(kod)==6 or szin == "RGB" and len(kod) == 5 or 6 or 7 or 8 or 9 or 10 or 11 or szin == "HSL" and len(kod)==7 or 8 or 9 or 10 or 11 or 12 or 13:
        print("Megfeleő hossz")
    elif szin!="HEX" or "RGB" or "HSL":
        print("Bonyolult kiszámolni")
    else:
        print("Nem megfeleő hossz")
    

