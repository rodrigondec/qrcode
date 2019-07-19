from django.http import HttpResponse
from django.views import View
from django.template import loader
from django.contrib.auth.decorators import login_required


class HomeView(View):
    @staticmethod
    @login_required
    def get(request):
        template = loader.get_template('core/index.html')
        return HttpResponse(template.render({}, request))
