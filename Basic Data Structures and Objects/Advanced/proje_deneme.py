from kütüphane import *

print('''*************************

Kütüphane Programına Hoşgeldiniz.
İşlemler:

1. Kitapları Göster

2.Kitap Sorgula

3.Kitap Ekle

4.Kitap Sil

5.Baskı Yükselt

Çıkmak için 'q' ya basın.
**************************
''')

kütüphane = Kütüphane()


while True:
    işlem = input('Yapacağınız İşlem:')

    if (işlem == 'q'):
        print('Program Sonlandırılıyor...')
        print('Yine Bekleriz...')
        break

    elif (işlem == '1'):
        kütüphane.kitapları_goster()
    elif (işlem == '2'):
        isim=input('Hangi kitabı istiyorsunuz?')
        print('Kitap Sorgulanıyor...')
        time.sleep(2)

        kütüphane.kitap_sorgular(isim)
    elif (işlem == '3'):
        isim = input('Kitap İsmi Giriniz:')
        yazar = input('Yazar:')
        yayınevi = input('Yayınevi:')
        tür = input('Tür:')
        baskı = int(input('Baskı:'))

        yeni_kitap = Kitap(isim,yazar,yayınevi,tür,baskı)

        print('kitap ekleniyor...')

        kütüphane.kitap_ekle(yeni_kitap)

        print('Kitap Eklendi....')
    elif (işlem == '4'):
        isim = input('Hangi kitabı silmek istiyorsunuz :')
        cevap = input('Emin misiniz ?(E/H)')

        if (cevap == 'E'):
            print('kitap siliniyor...')
            time.sleep(2)
            kütüphane.kitap_sil(isim)
            print('kitap silindi...')


    elif (işlem == '5'):
        isim = input('hangi kitabın baskısını yükseltmek istersin?')
        print('Baskı yükseltiliyor.')
        time.sleep(2)

        kütüphane.baskı_yükselt(isim)
        print('Baskı yükseltildi.')

    else:
        print('Geçersiz İşlem...')





















