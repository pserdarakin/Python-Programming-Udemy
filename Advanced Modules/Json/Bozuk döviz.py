import requests

from bs4 import BeautifulSoup


url = 'https://www.doviz.com/'


birinci_doviz = input('Birinci Döviz:')
ikinci_doviz = input('İkinci Döviz:')
miktar = float(input('Miktar:'))

response = requests.get(url)
html_iceriği = response.content
soup = BeautifulSoup(html_iceriği,'html.parser')
doviz = (soup.find_all('span',{'class','name'}))
kur = (soup.find_all('span',{'class','value'}))

for dovizler,kurlar in zip(doviz,kur):
    dovizler = dovizler.txt
    kurlar = kurlar.txt
    dovizler = dovizler.strip()
    kurlar = kurlar.strip()
    print(dovizler,':',kurlar)



json_verisi = response.json()
print(json_verisi['rates'][ikinci_doviz] * miktar)


#Printi kaldırıp aktive edebilirsin
#try:
 #   print(json_verisi['rates'][ikinci_doviz]*miktar)
#except KeyError:
 #   sys.stderr.write('Lütfen para birimlerini doğru girin')
  #  sys.stderr.flush()

























