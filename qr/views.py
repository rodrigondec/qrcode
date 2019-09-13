from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from django.views import View
from django.views.generic.list import ListView
from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError

from qr.models import QrCode
from qr.forms import UrlQrCodeForm, FileQrCodeForm


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
    paginate_by = 5


class QrCodeCreateView(View):
    template_name = 'qr/create.html'

    def get(self, request, *args, **kwargs):
        context = {
            'file_form': FileQrCodeForm(),
            'url_form': UrlQrCodeForm()
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {
            'file_form': FileQrCodeForm(),
            'url_form': UrlQrCodeForm()
        }
        if request.POST.get('type'):
            if request.POST.get('type') == 'url':
                form = UrlQrCodeForm(request.POST)
                context['url_form'] = form
            else:
                form = FileQrCodeForm(request.POST, request.FILES)
                context['file_form'] = form
            if form.is_valid():
                qr = form.save(commit=False)
                assert isinstance(qr, QrCode)
                qr.build_image(logo=form.cleaned_data.get('logo'))
                messages.success(request, 'QR Code cadastrado com sucesso!')
                return HttpResponseRedirect('/qr/lista/')
            context['form_errors'] = form.errors
            return render(request, self.template_name, context)
        raise Exception('Não teve um tipo de formulário retornado!')
