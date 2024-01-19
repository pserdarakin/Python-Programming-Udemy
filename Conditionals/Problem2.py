a=int(input('Birinci Sayıyı Giriniz:'))
b=int(input('İkinci Sayıyı Giriniz:'))
c=int(input('Üçüncü Sayıyı Giriniz:'))

if (a>b and a>c):
    print('{}'.format(a))
elif (b>a and b>c):
    print('{}'.format(b))
elif (c>b and c>a):
    print('{}'.format(c))
else:
    print('Düzgün sayı gir lan.')
