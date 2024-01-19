
class Hayvan():
    def __init__(self,solunum = 'sa',beslenme = 'as',ureme='ca',bosaltım ='da',hareket='za'):
        self.solunum = solunum
        self.beslenme = beslenme
        self.ureme = ureme
        self.bosaltım = bosaltım
        self.hareket = hareket

    def bilgilerigoster(self):
        print('Hayvanların Ortak Özellikleri: \n{}\n{}\n{}\n{}\n{}'.format(self.solunum,self.beslenme,self.ureme,self.bosaltım,self.hareket))
class Köpek(Hayvan):
    def __init__(self,solunum,beslenme,ureme,bosaltım,hareket,havlama,sadık):
        super().__init__(solunum,beslenme,ureme,bosaltım,hareket)
        self.havlama = havlama
        self.sadık = sadık
        print('Köpeklere ait spesifik özellikler:{}\n{}\n'.format(self.havlama,self.sadık))
class Kus(Hayvan):
    def __init__(self,solunum,beslenme,ureme,bosaltım,hareket,uçma = 'Uçabilme özelliği',sıçma = 'ustune sıçtığı kisiye loto sansı verir.'):
        super().__init__(solunum,beslenme,ureme,bosaltım,hareket)
        self.uçma = uçma
        self.sıçma = sıçma
        print('Kuslara ait spesifik özellikler: \n{}\n{}'.format(self.uçma,self.sıçma))
class At(Hayvan):
    def __init__(self,solunum,beslenme,ureme,bosaltım,hareket,dörtnala:'Hayvan gibi kosar',bok:'Boku seyrek duser'):
        super().__init__(solunum,beslenme,ureme,bosaltım,hareket)
        self.dörtnala = dörtnala
        self.bok = bok
        print('Atlara ait spesifik özellikler : \n{}\n{}'.format(self.dörtnala,self.bok))

print(''' HAYVANLARA AİT ÖZELLİKLER

1.Hayvanların ortak özellikleri
2.Köpeklere ait spesifik özellikler
3.Kuslara ait spesifik özellikler
4.Atlara ait spesifik özellikler
Çıkmak için 'q' ya basın. 
    
 ''')


while True:
    islem = input('İslem Seçiniz:')

    if (islem == 'q'):
        print('Program sonlandırılıyor..')
        break
    elif (islem == '1'):
        hayvanlar = Hayvan()
        hayvanlar.bilgilerigoster()
    elif (islem == '2'):
        köpekler = Köpek()
        köpekler.bilgilerigoster()
    elif (islem == '3'):
        kuslar = Kus()
        kuslar.bilgilerigoster()
    elif (islem == '4'):
        atlar = At()
        atlar.bilgilerigoster()
    else:
        print('Hatalı islem!')
        break







