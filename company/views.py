from re import template
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Idioma,Frase

class Home (LoginRequiredMixin, generic.TemplateView):
    template_name= 'company/home.html'
    login_url= 'company:login'

class IdiomaList(generic.ListView):
    template_name = "company/idiomas.html"
    model = Idioma
    context_object_name="obj"



class FraseList(generic.ListView):
    template_name = "company/frases.html"
    model = Frase
    context_object_name="obj"

    def get_queryset(self):
        qs = Frase.objects.all()
        idioma_id = self.request.GET.get("lang")
        if idioma_id:
            qs = qs.filter(idioma__id=idioma_id)
        return qs
