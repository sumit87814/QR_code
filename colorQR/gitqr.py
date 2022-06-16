from ctypes import resize
from ctypes.wintypes import RGB
from gettext import install
from turtle import pos
from matplotlib.pyplot import fill
import qrcode
from PIL import Image
logo = Image.open('download.png')
basewidth=75
wpercent=(basewidth/float(logo.size[0]))
hsize=int((float(logo.size[1])*float(wpercent)))
logo=logo.resize((basewidth,hsize),Image.ANTIALIAS)
qr_big=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr_big.make('https://github.com/sumit87814')
img_qr_big=qr_big.make_image(fill_color="#0b4e39",back_color="black").convert('RGB')
pos=((img_qr_big.size[0] - logo.size[0])//2,(img_qr_big.size[1] - logo.size[1])//2)
img_qr_big.paste(logo,pos)
img_qr_big.save('download_qr.png')
