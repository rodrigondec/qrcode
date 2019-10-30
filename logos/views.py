from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from logos.models import Logo


class LogoListView(LoginRequiredMixin, ListView):
    model = Logo
    template_name = 'logos/list.html'
    context_object_name = "logos"
    paginate_by = 5


class LogoCreateView(LoginRequiredMixin, CreateView):
    model = Logo
    template_name = 'generic/create_update.html'
    fields = ['name', 'image']
    success_url = '/logos/listar/'
    extra_context = {
        'titulo': 'Cadastrar Logo'
    }


class LogoUpdateView(LoginRequiredMixin, UpdateView):
    model = Logo
    template_name = 'generic/create_update.html'
    fields = ['name', 'image']
    success_url = '/logos/listar/'
    extra_context = {
        'titulo': 'Atualizar Logo'
    }
