from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from metrics.models import Access
from qr.models import QrCode


@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qrcodes'] = QrCode.objects.all()
        context['access_list'] = Access.objects.all()

        context['timeline'] = Access.get_formated_timeline_count()
        for attr_name in ['os', 'device', 'browser']:
            context[f'{attr_name}_count'] = Access.get_formated_value_count(attr_name)
        return context
