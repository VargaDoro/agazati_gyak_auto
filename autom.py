from Auto import Auto



   



def beolvas():       
    auto_lista=[]
    with open("auto.txt", "r", encoding="UTF-8" ) as file:
        file.readline()
        kocsi_lista = file.readlines()
        for auto in kocsi_lista:
            autosor_lista=auto.strip().split(":")
            auto_obj=Auto(autosor_lista[0],autosor_lista[1])
            auto_lista.append(auto_obj)
    return auto_lista

def kor(auto):
    print(f"{auto.nev}-{2025-auto.gyartasi_datum}")

def kiir(auto):
    with open("ki.txt", "a", encoding="UTF-8")as file:
        file.write(auto.nev)
        file.write(str(2025-auto.gyartasi_datum)+"\n")
        
def flotta(lista):
    i:int=0
    while i < len(lista):
        i+=1
    with open("ki.txt", "a", encoding="UTF-8")as file:
        file.write(f"Autók száma: {i}")
