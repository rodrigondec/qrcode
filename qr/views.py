from django.http import Http404, HttpResponseRedirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError

from qr.models import QrCode, FileQrCode, UrlQrCode
from qr.forms import QrCodeForm, UrlQrCodeForm, FileQrCodeForm


class ResolveQrCodeView(View):
    @staticmethod
    def get(request, pk):
        try:
            qr_code = QrCode.objects.get(id=pk)
        except (QrCode.DoesNotExist, ValidationError):
            raise Http404("Qr Code não existe")
        return redirect(qr_code.resolve())


class QrCodeListView(ListView):
    model = QrCode
    template_name = 'qr/list.html'
    context_object_name = "qrcodes"
    paginate_by = 10


class QrCodeCreateView(View):
    form_class = QrCodeForm
    template_name = 'qr/select_create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            print(form)
            return render(request, self.template_name, {'form': form})

        return render(request, self.template_name, {'form': form})


class ChildQrCodeCreateView(View):
    form_class = {'url': UrlQrCodeForm, 'file': FileQrCodeForm}
    template_name = 'qr/create.html'

    def get(self, request, qr_class, *args, **kwargs):
        form = self.form_class.get(qr_class)()
        return render(request, self.template_name, {'form': form})

    def post(self, request, qr_class, *args, **kwargs):
        form = self.form_class.get(qr_class)(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})
