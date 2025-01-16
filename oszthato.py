def hettelOszthato(lista):
    print(f"A lista elemei: {lista}")
    db:int=0
    i:int=0
    while i < len(lista):
        if lista[i]%7==0:
            db+=1
        i+=1
    print(f"A listában {db} db héttel osztható szám van.")
