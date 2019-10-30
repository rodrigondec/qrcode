from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView, PasswordResetView


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
