a=int(input('Kilonuzu Giriniz(kg):'))
b=float(input('Boyunuzu Giriniz(m):'))

BKİ=(a/(b**2))

if (BKİ<18.5):
    print('Zayıf')
elif (18.5<BKİ<25):
    print('Normal')
elif (25<BKİ<30):
    print('Fazla Kilolu')
else:
    print('Obez')
