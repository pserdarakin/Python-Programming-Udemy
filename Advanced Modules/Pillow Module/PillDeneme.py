from PIL import Image, ImageFilter

image = Image.open('kelebek.jpg')

image.save('kelebek2.jpg')

image.rotate(180).save('kelebek3.jpg')

image.convert(mode ='L').save('kelebek4.jpeg')

degistir = (480,300)

image.thumbnail(degistir)

image.save('kelebek5.jpg')

image.filter(ImageFilter.GaussianBlur(5)).save('kelebek6.jpg')
kırpılacak_alan = (340,0,950,600)
image2 = Image.open('yoda.jpeg')
image.crop(kırpılacak_alan).save('yoda3.jpg')









