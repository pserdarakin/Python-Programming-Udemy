
print('''
*********************************************
Ultra Gelişmiş Hesap Makinesine Hoşgeldiniz.
1. Toplama
2. Çıkarma
3. Çarpma
4. Bölme
5. Üs Alma
6. Faktöriyel Bulma
7. Sinüs Bulma
8. Tanh Bulma
Çıkmak için q'ya basınız.

*********************************************
''' )

from math import*
işlem=int(input('İşlem Seçiniz:'))

while True:

    if (işlem=='q'):
        print('Byeee')
        break
    elif (işlem==1):
        x=int(input('1.Sayıyı Giriniz:'))
        y=int(input('2.Sayıyı Giriniz:'))
        print('',x+y)

    elif (işlem==2):
        x = int(input('1.Sayıyı Giriniz:'))
        y = int(input('2.Sayıyı Giriniz:'))
        print('', x - y)
    elif (işlem == 3):
        x = int(input('1.Sayıyı Giriniz:'))
        y = int(input('2.Sayıyı Giriniz:'))
        print('', x * y)
    elif (işlem == 4):
        x = int(input('1.Sayıyı Giriniz:'))
        y = int(input('2.Sayıyı Giriniz:'))
        print('', x / y)
    elif (işlem == 5):
        x = int(input('Sayıyı Giriniz:'))
        y = int(input('Üssü Giriniz:'))
        print('',pow(x,y))
    elif (işlem== 6):
        x = int(input('Sayıyı Giriniz:'))

        print('',factorial(x))
    elif (işlem==7):
        x = int(input('Sayıyı Giriniz:'))
        print('',sin(x))
    elif (işlem==8):
        x = int(input('Sayıyı Giriniz:'))
        print('',tanh(x))
    else:
        print('Geçersiz İşlem :( ')
        break



























