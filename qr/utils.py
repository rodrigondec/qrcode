from io import BytesIO

import qrcode


def create_qrcode_img(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    return img


def create_qrcode_io_stream(url):
    img = create_qrcode_img(url)
    stream = BytesIO()
    img.save(stream, format='png')
    return stream.getvalue()


def get_qrcode_img_path(instance, *args, **kwargs):
    return f'qrcodes/{instance.id}.png'


def get_file_path(instance, filename, *args, **kwargs):
    return f'files/{instance.id}.{filename.split(".")[1]}'
