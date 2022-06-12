from matplotlib import image
from matplotlib.pyplot import fill
import qrcode
import image
qr= qrcode.QRCode(
    version=10, #10 means the version of the qr code high the number bigger the image and complicated
    box_size=7, #size of the image where the qr code will be dispalyed
    border=5 # it is the white part of the image-- border ina ll sides with white color
) 
data = ("https://www.facebook.com/")


qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("fb_qr.png")