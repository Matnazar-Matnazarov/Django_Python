from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from django.views.generic import TemplateView,ListView,DetailView,CreateView
from .models import Izoh_011,Muzqaymoqlar,Hodimlar_00
class home_sahifa(TemplateView):
    template_name = 'home.html'
class izoh_sahifa(DetailView):
    model = Izoh_011
    template_name ='izohlar.html'
class model_sahifa(ListView):
    model = Izoh_011
    template_name = 'malumot_muzqaymoq.html'
class Muzqaymoq_s(ListView):
    model = Muzqaymoqlar
    template_name = 'muzqaymoq_sahifa.html'
class Hodim(ListView):
    model = Hodimlar_00
    template_name = 'hodimlar.html'
class hodim_button(DetailView):
    model = Hodimlar_00
    template_name = 'hodimlar_malumot.html'
class Hodim_add(CreateView):
    model = Hodimlar_00
    template_name ="hodim_add_h.html"
    fields = ['ism','familiya','tel_raqam','ish_boshlagan_sana','ishlagan_kunlar_soni','belgilangan_narx','karta','Bank_Tranzit','bank_mfo']
class muzqaymoq_t(DetailView):
    model = Muzqaymoqlar
    template_name = 'muzqaymoq_mal.html'