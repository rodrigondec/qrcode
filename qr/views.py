import traceback

from django.http import Http404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError

from qr.models import QrCode, FileQrCode, URLQrCode, VideoQrCode
from qr.forms import URLQrCodeForm, FileQrCodeForm, VideoQrCodeForm, CHOICES, FORM_CLASSES
from metrics.models import Access


class ResolveQrCodeView(TemplateView):
    template_name = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            qr_code = QrCode.objects.get(label=kwargs.get('id'))
            context['qrcode'] = qr_code
            self.template_name = qr_code.resolve_template()
        except (QrCode.DoesNotExist, ValidationError) as e:
            traceback.print_exc()
            raise Http404("QR Code não existe")
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        Access.from_request(context.get('qrcode'), request)

        return self.render_to_response(context)


class QRCodeListView(LoginRequiredMixin, ListView):
    model = QrCode
    template_name = 'qr/list.html'
    context_object_name = "qrcodes"
    paginate_by = 5


class QRCodeCreateView(LoginRequiredMixin, CreateView):
    template_name = 'qr/create.html'
    success_url = reverse_lazy('qr_listar')

    def get_context_data(self, **kwargs):
        context = {
            f'{FileQrCode.type()}_form': FileQrCodeForm(),
            f'{URLQrCode.type()}_form': URLQrCodeForm(),
            f'{VideoQrCode.type()}_form': VideoQrCodeForm()
        }

        _type = None
        if kwargs.get('form'):
            form = kwargs.get('form')
            _type = form.data.get('type')
            context[f'{_type}_form'] = form

        if kwargs.get('request'):
            request = kwargs.get('request')
            _type = request.POST.get('type')
            context[f'{_type}_form'] = FORM_CLASSES.get(f'{_type}')(request.POST, request.FILES)

        context['form'] = context.get(f'{_type}_form')

        return context

    def post(self, request, *args, **kwargs):
        _type = request.POST.get('type')
        if _type in [choice[0] for choice in CHOICES]:
            context = self.get_context_data(request=request)

            form = context.get('form')
            if form.is_valid():
                messages.success(request, 'QR Code cadastrado com sucesso!')
                return self.form_valid(form)
            return self.form_invalid(form)
        raise Exception('Não teve um tipo de formulário retornado!')


class QRCodeUpdateView(LoginRequiredMixin, UpdateView):
    model = QrCode
    template_name = 'generic/create_update.html'
    success_url = reverse_lazy('qr_listar')

    def get_context_data(self, **kwargs):
        qr = self.get_object()

        context = {
            'titulo': f'Atualizar {qr.type()} QR Code',
            'form': FORM_CLASSES.get(qr.type())(instance=qr)
        }

        if kwargs.get('form'):
            context['form'] = kwargs.get('form')

        if kwargs.get('request'):
            request = kwargs.get('request')
            context['form'] = FORM_CLASSES.get(qr.type())(request.POST, request.FILES, instance=qr)

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(request=request)

        form = context.get('form')
        if form.is_valid():
            messages.success(request, 'QR Code atualizado com sucesso!')
            return self.form_valid(form)
        return self.form_invalid(form)
