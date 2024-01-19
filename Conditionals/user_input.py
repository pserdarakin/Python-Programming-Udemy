print('''
**********************
Kullanıcı Girişi
**********************
''')
sys_kullanıcı_adı='pserdar'
sys_parola='12345'

kullanıcı_adı=input('Kullanıcı adı:')
parola=input('Parola:')

if (kullanıcı_adı == sys_kullanıcı_adı and sys_parola != parola):
    print('Parola Hatalı.')

elif(kullanıcı_adı != sys_kullanıcı_adı and parola==sys_parola):
    print('Kullanıcı Adı Hatalı.')

elif(kullanıcı_adı!= sys_kullanıcı_adı and parola != sys_parola):
    print('Kullanıcı adı ve parola yanlış.')

else:
    print('sisteme başarıyla giriş yapıldı.')













