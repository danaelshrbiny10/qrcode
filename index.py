import qrcode
# from PIL import Image
import os


img = qrcode.make('https://www.linkedin.com/in/dana-elshrbiny-b600701b2/')
img.save('img.png')


os.system('img.png')
# Image.open('img.png').show()