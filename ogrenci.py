class Ogrenci:
    isim = ""
    yas = 0
    sinif = 0
    def __init__(self,isim,yas,sinif):
        self.isim = isim
        self.yas = yas
        self.sinif = sinif
        
    def __repr__(self): 
        return f"İsim: {self.isim} Yaş :{self.yas} Sinif: {self.sinif}" 