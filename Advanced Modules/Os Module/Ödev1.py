import os

for klasör_yolu,klasör_isimleri,dosyalar in os.walk('C:/'):
    for i in dosyalar:
        if i.endswith('.pdf'):
            dosya = open('pdf_dosyaları.txt', 'a')
            b = ('{} Klasör yolu.'.format(klasör_yolu))

            dosya.write(i + b + '\n')

            dosya.close()











