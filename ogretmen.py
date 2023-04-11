class Ogretmen:
    isim = ""
    yas = 0
    bolum =""
    def __init__(self,isim,bolum,yas):
        self.isim = isim
        self.yas = yas
        self.bolum = bolum
        
    def __repr__(self): 
        return f"İsim: {self.isim} Yaş: {self.yas} Bölümü: {self.bolum}" 