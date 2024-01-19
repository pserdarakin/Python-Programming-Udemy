a=input('Üçgen mi Dörtgen mi:')
b=input('1.Kenar:')
c=input('2.Kenar:')
d=input('3.Kenar:')
e=input('4.Kenar:')

if ('a=Dörtgen' and 'b=c=d=e'):
    print('Kare')
elif ('a=Dörtgen' and ('b=c or d=e or b=e or c=e')):
    print('Dikdörtgen')

