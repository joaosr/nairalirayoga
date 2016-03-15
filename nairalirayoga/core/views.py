from django.shortcuts import render
from nairalirayoga.core.models import Horario, Preco, Professor


def home(request):
    h = Horario.objects.values_list('dia_semana', flat=True).order_by('dia_semana').distinct()
    precos = Preco.objects.all().values()
    professores = Professor.objects.all().values()
    horarios = []
    for i in range(len(h)):
        tmp = {}
        tmp['dia_semana'] = h[i]
        tmp['values'] = Horario.objects.filter(dia_semana=h[i]).values()
        horarios.append(tmp)

    context = {'horarios': horarios, 'precos': precos, 'professores': professores}

    return render(request, 'index.html', context=context)


def gallery(request):
    return render(request, 'gallery.html')
