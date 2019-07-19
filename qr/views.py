from django.http import Http404
from django.views import View
from django.shortcuts import redirect
from django.core.exceptions import ValidationError

from qr.models import QrCode


class GetQrCodeView(View):
    @staticmethod
    def get(request, pk):
        try:
            qr_code = QrCode.objects.get(id=pk)
        except (QrCode.DoesNotExist, ValidationError):
            raise Http404("Qr Code não existe")
        return redirect(qr_code.resolve())
