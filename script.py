from qr.models import QrCode, FileQrCode, UrlQrCode

fqr = QrCode.objects.instance_of(FileQrCode).first()
print(fqr.file.name, fqr.file.url)
fqr.build_image()

furl = QrCode.objects.instance_of(UrlQrCode).first()
print(furl.url)
furl.build_image()


from qr.utils import _create_qrcode_img, insert_logo_on_img

img = _create_qrcode_img('Some Data')
img = insert_logo_on_img(img)
img.save('t.png')