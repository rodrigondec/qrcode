from qr.models import QrCode
from logos.models import Logo

code = QrCode.objects.first()
logo = Logo.objects.first()

code.build_image(logo)
