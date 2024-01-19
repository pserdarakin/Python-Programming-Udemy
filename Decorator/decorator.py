import time

def zaman(fonk):

    def wrapper(sayılar):
        baslama = time.time()
        sonuç = fonk(sayılar)
        bitis = time.time()

        print(fonk.__name__ + '' + str(bitis-baslama) + 'saniye sürdü.')
        return sonuç
    return wrapper


@zaman
def ortalamabul(sayılar):

    toplam = 0

    for sayı in sayılar:
        toplam+= sayı
    print('Genel Ortalama:',toplam/len(sayılar))

ortalamabul([1,2,3,4,35,647,85,65,77,12330,364357537,555,12,12,120300010501030510350130000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000050])






