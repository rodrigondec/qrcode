from django.contrib import messages
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class PerfilView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'generic/create_update.html'
    fields = ['username', 'email', 'first_name', 'last_name']
    success_url = '/logos/listar/'
    extra_context = {
        'titulo': 'Meu perfil'
    }

    def get_object(self, queryset=None):
        return self.request.user


class MyLogoutView(LogoutView):
    next_page = '/'

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'Você saiu do sistema!')
        return super().dispatch(request, *args, **kwargs)


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'generic/create_update.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        return super().get_context_data(titulo='Mudar senha', **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Sua senha foi alterada com sucesso!')
        return super().form_valid(form)


class MyPasswordResetView(PasswordResetView):
    template_name = 'generic/create_update_without_nav.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        return super().get_context_data(titulo='Resetar senha', **kwargs)

    def form_valid(self, form):
        messages.success(
            self.request,
            'Nós te enviamos por e-mail as instruções para redefinição de sua senha, se existir uma conta com '
            'o e-mail que você forneceu. Você receberá a mensagem em breve.\n '
            'Se você não receber um e-mail, por favor verifique se você digitou o endereço que você usou para '
            'se registrar, e verificar a sua pasta de spam.')
        return super().form_valid(form)


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'generic/create_update_without_nav.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        return super().get_context_data(titulo='Resetar senha', **kwargs)

    def form_valid(self, form):
        messages.success(
            self.request,
            'Sua senha foi definida. Você pode prosseguir e se autenticar agora.')
        return super().form_valid(form)
