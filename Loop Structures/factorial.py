print(''' ***************
Faktöriyel Bulma Programı

Çıkmak için q'ya basın.

****************

''')

while True:
    sayı = input('sayı:')
    if (sayı == 'q'):
        print('Program Sonlandırılıyor.')
        break
    else:
        sayı=int(sayı)

        faktoriyel = 1

        for i in range (2,sayı+1):
            print('Faktöriyel',faktoriyel,'i:',i)
            faktoriyel *= i
        print('Faktöriyel ',faktoriyel)

