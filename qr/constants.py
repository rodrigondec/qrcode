from qrcode.constants import ERROR_CORRECT_H

from decouple import config


QR_LOGO_PERCENTAGE = config('QR_LOGO_PERCENTAGE', default=0.3, cast=float)
QR_VERSION = config('QR_VERSION', default=3, cast=int)
QR_ERROR_CORRECTION_LEVEL = config('QR_CORRECTION', default=ERROR_CORRECT_H, cast=int)
QR_BOX_SIZE = config('QR_BOX_SIZE', default=10, cast=int)
QR_BORDER = config('QR_BORDER', default=4, cast=int)

QR_LABEL_SIZE = 6
