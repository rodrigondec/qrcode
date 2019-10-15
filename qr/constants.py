from qrcode.constants import ERROR_CORRECT_L

from decouple import config


LOGO_SIZE = config('QR_LOGO_SIZE', default=120, cast=int)
VERSION = config('QR_VERSION', default=3, cast=int)
ERROR_CORRECTION_LEVEL = config('QR_CORRECTION', default=2, cast=int)
BOX_SIZE = config('QR_BOX_SIZE', default=10, cast=int)
BORDER = config('QR_BORDER', default=2, cast=int)

LABEL_SIZE = 6
