from qrcode.constants import ERROR_CORRECT_H

from decouple import config


QR_LOGO_PERCENTAGE = config('QR_LOGO_PERCENTAGE', default=0.3, cast=float)
QR_VERSION = config('QR_VERSION', default=3, cast=int)
QR_ERROR_CORRECTION_LEVEL = config('QR_CORRECTION', default=ERROR_CORRECT_H, cast=int)
QR_BOX_SIZE = config('QR_BOX_SIZE', default=10, cast=int)
QR_BORDER = config('QR_BORDER', default=4, cast=int)

QR_LABEL_SIZE = 6

LEAFLET_ICON = config('LEAFLET_ICON', default="map-marker-alt")
LEAFLET_SHAPE = config('LEAFLET_SHAPE', default="marker")
LEAFLET_BACKGROUND_COLOR = config('LEAFLET_BACKGROUD_COLOR', default="white")

LEAFLET_COLOR_STEP = config('LEAFLET_COLOR_STEP', default=5, cast=int)
LEAFLET_COLORS = [
    config('LEAFLET_COLOR_1', default='#cc0808'),
    config('LEAFLET_COLOR_2', default='#ccc908'),
    config('LEAFLET_COLOR_3', default='#0fcc08'),
    config('LEAFLET_COLOR_4', default='#0846cc'),
    config('LEAFLET_COLOR_5', default='#b808cc')
]

