from qr.models import QrCode, FileQrCode, UrlQrCode

fqr = QrCode.objects.instance_of(FileQrCode).first()
print(fqr.file.name, fqr.file.url)
fqr.build_img()

furl = QrCode.objects.instance_of(UrlQrCode).first()
print(furl.url)
furl.build_img()
