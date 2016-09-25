# -*- coding: utf-8 -*-
from django.views import generic
from django.shortcuts import render
from django.views import generic
from nairalirayoga.core.models import Horario, Imagem, Preco, Professor, Blog


def home(request):
    days_ord = ['Seg', 'Ter', 'Quar', 'Qui', 'Sex', 'Sáb', 'Dom']
    h_tmp = Horario.objects.values_list('dia_semana', flat=True).order_by('dia_semana').distinct()
    h = []
    for key in days_ord:
        if key in h_tmp:
            h.append(key)

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

class BlogPost(generic.DetailView):
    model = Blog
    template_name = "post.html"


class BlogIndex(generic.ListView):
    queryset = Blog.objects.published()
    template_name = "blog.html"
    paginate_by = 3
