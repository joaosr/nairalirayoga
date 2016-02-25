from django.shortcuts import render
from nairalirayoga.core.models import Horario


def home(request):
    h = Horario.objects.values_list('dia_semana', flat=True).distinct()
    horarios = {}
    for i in range(len(h)):
       horarios[h[i]] = Horario.objects.filter(dia_semana=h[i]).values

    return render(request, 'index.html', context=horarios)


def gallery(request):
    return render(request, 'gallery.html')
