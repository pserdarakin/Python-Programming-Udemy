def mukemmelsayıbulma(sayı):
    toplam=0

    for i in range(1,sayı):
            if (sayı % i == 0):
                toplam+= i
    return toplam == sayı

for i in range(1,10010):
    if (mukemmelsayıbulma(i)):
        print('Mükemmel Sayı:',i)



