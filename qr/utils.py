import os
from io import BytesIO

from django.conf import settings
from PIL import Image
import qrcode


def _insert_logo_on_img(img):
    img = img.convert('RGB')
    width, height = img.size

    logo_size = 120
    logo_path = os.path.join(settings.STATIC_ROOT, 'imgs/logo.jpg')
    logo = Image.open(logo_path)

    # Calculate xmin, ymin, xmax, ymax to put the logo
    xmin = ymin = int((width / 2) - (logo_size / 2))
    xmax = ymax = int((width / 2) + (logo_size / 2))

    logo = logo.resize((xmax - xmin, ymax - ymin))

    img.paste(logo, (xmin, ymin, xmax, ymax))

    return img


def _create_qrcode_img(url):
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    return img


def create_qrcode_io_stream(url):
    img = _create_qrcode_img(url)
    img = _insert_logo_on_img(img)
    stream = BytesIO()
    img.save(stream, format='png')
    return stream.getvalue()


def get_qrcode_img_path(instance, *args, **kwargs):
    return f'qrcodes/{instance.id}.png'


def get_file_path(instance, filename, *args, **kwargs):
    return f'files/{instance.id}.{filename.split(".")[-1]}'
