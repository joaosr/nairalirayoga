from django.shortcuts import render
from nairalirayoga.core.models import Horario, Imagem, Preco, Professor


def home(request):
    h = Horario.objects.values_list('dia_semana', flat=True).order_by('dia_semana').distinct()
    p = Preco.objects.values_list('atividade', flat=True).order_by('atividade').distinct()
    imagens = Imagem.objects.filter(carrosel=True).values().order_by('id')
    nimagens = range(len(imagens))

    professores = Professor.objects.all().values()
    horarios = []
    for i in range(len(h)):
        tmp = {}
        tmp['dia_semana'] = h[i]
        tmp['values'] = Horario.objects.filter(dia_semana=h[i]).values()
        horarios.append(tmp)

    precos = []
    for i in range(len(p)):
        tmp = {}
        tmp['atividade'] = p[i]
        tmp['values'] = Preco.objects.filter(atividade=p[i]).values()
        precos.append(tmp)

    context = {'horarios': horarios,
               'imagens': imagens,
               'nimagens': nimagens,
               'precos': precos,
               'professores': professores}

    return render(request, 'index.html', context=context)


def gallery(request):
    return render(request, 'gallery.html')
