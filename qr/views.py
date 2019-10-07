from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from django.views import View
from django.views.generic.base import TemplateView, ContextMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError

from qr.models import QrCode, FileQrCode, URLQrCode
from qr.forms import URLQrCodeForm, FileQrCodeForm
from metrics.models import Access


class ResolveQrCodeView(TemplateView):
    template_name = "qr/resolve.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            qr_code = QrCode.objects.get(id=kwargs.get('pk'))
            context['qrcode'] = qr_code
        except (QrCode.DoesNotExist, ValidationError):
            raise Http404("QR Code não existe")
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        Access.from_request(context.get('qrcode'), request)

        return self.render_to_response(context)


class QRCodeListView(ListView):
    model = QrCode
    template_name = 'qr/list.html'
    context_object_name = "qrcodes"
    paginate_by = 5


class QRCodeCreateView(CreateView):
    template_name = 'qr/create.html'

    def get(self, request, *args, **kwargs):
        context = {
            'file_form': FileQrCodeForm(),
            'url_form': URLQrCodeForm()
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {
            'file_form': FileQrCodeForm(),
            'url_form': URLQrCodeForm()
        }
        if request.POST.get('type'):
            if request.POST.get('type') == 'url':
                form = URLQrCodeForm(request.POST)
                context['url_form'] = form
            else:
                form = FileQrCodeForm(request.POST, request.FILES)
                context['file_form'] = form
            if form.is_valid():
                form.save()
                messages.success(request, 'QR Code cadastrado com sucesso!')
                return HttpResponseRedirect('/qr/listar/')
            context['form_errors'] = form.errors
            return render(request, self.template_name, context)
        raise Exception('Não teve um tipo de formulário retornado!')


class QRCodeUpdateView(UpdateView):
    model = QrCode
    template_name = 'generic/create_update.html'

    def get(self, request, *args, **kwargs):
        qr = self.get_object()
        context = {}

        if isinstance(qr, FileQrCode):
            context['form'] = FileQrCodeForm(instance=qr)
            context['titulo'] = 'Atualizar File QR code'
        elif isinstance(qr, URLQrCode):
            context["form"] = URLQrCodeForm(instance=qr)
            context['titulo'] = 'Atualizar URL QR code'
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        qr = self.get_object()
        context = {}
        form = None

        if isinstance(qr, FileQrCode):
            form = FileQrCodeForm(request.POST, request.FILES, instance=qr)
            context['titulo'] = 'Atualizar File QR code'
        elif isinstance(qr, URLQrCode):
            form = URLQrCodeForm(request.POST, instance=qr)
            context['titulo'] = 'Atualizar URL QR code'

        assert isinstance(form, FileQrCodeForm) or isinstance(form, URLQrCodeForm)

        if form.is_valid():
            form.save()
            messages.success(request, 'QR Code atualizado com sucesso!')
            return HttpResponseRedirect('/qr/listar/')

        context['form'] = form
        return render(request, self.template_name, context)
