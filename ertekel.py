def elso():
    print("I/A,B:")
    etel:str=str(input("Étel neve: "))
    nev:str=str(input("Étel rendelőjének neve: "))
    ert:int=int(input("Értékelés (1-5): "))
    print("I/C:")
    if ert<0:
        print("Az értékelés nem lehet negatív!")
    elif ert>5:
        print("5 pont feletti értékelés nem elfogadható!")
    else:
        print("Köszönjük az értékelést!")