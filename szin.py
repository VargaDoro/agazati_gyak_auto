def elso():
    print("Első feladat:")
    szin:str=str(input("Kérek egy színkeverési módszert: "))
    kod=(input("Kérem a kódot: "))
    felt1:bool=(szin=="HEX" and len(kod)==6)
    felt2:bool=(szin == "RGB" and len(kod) >=5 and len(kod)<=11)
    felt3:bool=(szin == "HSL" and 7<=len(kod)<=13)
    if felt1 or felt2 or felt3:
        print("Megfeleő hossz")
    elif szin!="HEX" or "RGB" or "HSL":
        print("Bonyolult kiszámolni")
    else:
        print("Nem megfeleő hossz")


"""  elif szin == "RGB" and len(kod) >=5 and len(kod)<=11:
        print("Megfeleő hossz")
    elif szin == "HSL" and 7<=len(kod)<=13:
        print("Megfeleő hossz") """
    

