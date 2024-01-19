import os
from datetime import datetime


for klasör_yolu,klasör_isimleri,dosya_isimler in os.walk(r'C:\Users\asus\Desktop'):
    for i in dosya_isimler:
        if (i.endswith('.txt')):
            print(i)
