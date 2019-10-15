from qrcode.constants import ERROR_CORRECT_H

from decouple import config


LOGO_PERCENTAGE = config('QR_LOGO_PERCENTAGE', default=0.3, cast=float)
VERSION = config('QR_VERSION', default=3, cast=int)
ERROR_CORRECTION_LEVEL = config('QR_CORRECTION', default=ERROR_CORRECT_H, cast=int)
BOX_SIZE = config('QR_BOX_SIZE', default=10, cast=int)
BORDER = config('QR_BORDER', default=4, cast=int)

LABEL_SIZE = 6
