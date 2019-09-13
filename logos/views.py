from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from django.views import View
from django.views.generic.list import ListView
from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError

from logos.models import Logo


class LogoListView(ListView):
    model = Logo
    template_name = 'logos/list.html'
    context_object_name = "logos"
    paginate_by = 5
