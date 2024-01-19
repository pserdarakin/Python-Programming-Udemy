import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys


mesaj = MIMEMultipart()

mesaj['From'] = 'serdar.jr.python@gmail.com'

mesaj['To'] = 'serdar.jr.python@gmail.com'

mesaj['Subject'] = 'Smtp Mail Gönderme'

yazi = '''

Smtp ile mail gönderiyorum

Serdar AKIN

'''

mesaj_govdesi = MIMEText(yazi,'plain')

mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login('serdar.jr.python@gmail.com','serdar204200')
    mail.sendmail(mesaj['From'],mesaj['To'],mesaj.as_string())
    print('Mail başarıyla gönderildi.')
    mail.close()
except:
    sys.stderr.write('Bir sorun oluştu!')
    sys.stderr.flush()


















