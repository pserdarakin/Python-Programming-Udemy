from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL,'')

tarih = datetime(2022,12,1)

şu_an = datetime.now()

print(tarih-şu_an)









