import qrcode
from PIL import Image
qr = qrcode.QRCode(
    version=18,
    box_size=12,
    border=7
)

data="https://www.reddit.com/"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save('text.png')
