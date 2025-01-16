import random
import szin
import oszthato
import autom

szin.elso()
szamok=[]
for i in range(50):
    szamok.append(random.randint(1, 100))
oszthato.hettelOszthato(szamok)
auto_lista=autom.beolvas()

'''for i in range(0, len(auto_lista)):
    print("*******")
    print(auto_lista[i].nev)
    print(auto_lista[i].gyartasi_datum)
    print()'''

autom.kor(auto_lista[0])
autom.kiir(auto_lista[1])
autom.flotta(auto_lista)