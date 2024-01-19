print (''' ***********
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir.
**********
''')

sayı=int(input('Sayı:'))

i = 1
toplam = 0
while (i < sayı):
    if (sayı %i == 0):
        toplam += i
    i += 1
    continue
if (toplam == sayı):
    print(sayı,'mükkemmel bir sayıdır.')
else:
    print(sayı,'mükemmel bir sayı değildir')



















