import string
import random
from io import BytesIO

from PIL import Image
import qrcode

from logos.models import Logo
from qr.constants import (QR_LOGO_PERCENTAGE, QR_VERSION,
                          QR_ERROR_CORRECTION_LEVEL, QR_BOX_SIZE, QR_BORDER, QR_LABEL_SIZE)


def _insert_logo_on_img(img, logo):
    img = img.convert('RGB')
    width, height = img.size
    assert width == height

    assert isinstance(logo, Logo)
    logo_img = Image.open(logo.image)

    logo_size = width * QR_LOGO_PERCENTAGE

    # Calculate xmin, ymin, xmax, ymax to put the logo
    xmin = ymin = int((width / 2) - (logo_size / 2))
    xmax = ymax = int((width / 2) + (logo_size / 2))

    logo_img = logo_img.resize((xmax - xmin, ymax - ymin), Image.ANTIALIAS)

    img.paste(logo_img, (xmin, ymin, xmax, ymax))

    return img


def _create_qrcode_img(url):
    qr = qrcode.QRCode(
        version=QR_VERSION,
        error_correction=QR_ERROR_CORRECTION_LEVEL,
        box_size=QR_BOX_SIZE,
        border=QR_BORDER,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    return img


def create_qrcode_io_stream(url, logo):
    img = _create_qrcode_img(url)
    if logo:
        img = _insert_logo_on_img(img, logo)
    stream = BytesIO()
    img.save(stream, format='png')
    return stream.getvalue()


def label_generator(size=QR_LABEL_SIZE, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def get_qrcode_img_path(instance, *args, **kwargs):
    return f'qrcodes/{instance.id}.png'


def get_file_path(instance, filename, *args, **kwargs):
    return f'files/{instance.id}.{filename.split(".")[-1]}'
