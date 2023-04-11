from ogrenci import Ogrenci
from ogretmen import Ogretmen

ogretmenList = []
ogrenciList = []

def addOgrenci(ogrenci):
        ogrenciList.append(ogrenci)

def addOgretmen(ogretmen):
        ogretmenList.append(ogretmen)

def showOgretmenList():
    print(f"Öğretmenler : {ogretmenList}")
    
def showOgrenciList():
    print(f"Öğrenciler  : {ogrenciList}")


ogretmen1 = Ogretmen("Halit","Python",25)
ogretmen2 = Ogretmen("Engin","Java",37)

ogrenci1 = Ogrenci("Buse",24, "7-c")
ogrenci2 = Ogrenci("Lara ",23,"12-a")
addOgretmen(ogretmen1)
addOgretmen(ogretmen2)

addOgrenci(ogrenci1)
addOgrenci(ogrenci2)
showOgretmenList()
showOgrenciList()


