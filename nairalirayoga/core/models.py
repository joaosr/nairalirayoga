# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse


class Horario(models.Model):
    SEGUNDA = 'Seg'
    TERCA = 'Ter'
    QUARTA = 'Quar'
    QUINTA = 'Qui'
    SEXTA = 'Sex'
    SABADO = 'Sáb'
    DOMINGO = 'Sex'
    DAYS_OF_WEEK = (
        (SEGUNDA, 'Segunda-feira'),
        (TERCA, 'Terça-feira'),
        (QUARTA, 'Quarta-feira'),
        (QUINTA, 'Quinta-feira'),
        (SEXTA, 'Sexta-feira'),
        (SABADO, 'Sábado'),
        (DOMINGO, 'Domingo'),
    )

    dia_semana = models.CharField('Dia da semana', max_length=4, choices=DAYS_OF_WEEK)
    horario = models.TimeField('Horário')
    local = models.TextField('Endereço')
    descricao = models.TextField('Descrição')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'horários'
        verbose_name = 'horário'

    def __str__(self):
        return self.dia_semana

class Preco(models.Model):
    D1 = '1x por semana'
    D2 = '2x por semana'
    D3 = '3x por semana'
    D4 = '4x por semana'
    D5 = '5x por semana'
    D6 = '6x por semana'
    D7 = '7x por semana'
    DX = 'Aula livre'
    DAYS = (
        (D1, D1),
        (D2, D2),
        (D3, D3),
        (D4, D4),
        (D5, D5),
        (D6, D6),
        (D7, D7),
        (DX, DX),
    )
    AT1 = 'Aula de Yoga'
    ATIVIDADES = (
        (AT1, AT1),
    )
    valor = models.FloatField('Preço')
    dias = models.CharField('Dias por semana', max_length=13, choices=DAYS)
    atividade = models.CharField('Atividade', max_length=50, choices=ATIVIDADES)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Preços'
        verbose_name = 'Preço'

    def __str__(self):
        return self.atividade

def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)

class Professor(models.Model):
    nome = models.CharField('Nome', max_length=20)
    sobrenome = models.CharField('Sobrenome', max_length=20)
    descricao = models.TextField('Descrição')
    foto = models.ImageField('Foto', upload_to=upload_location,
                             null=True,
                             blank=True,
                             height_field="height_field",
                             width_field="width_field",
                             default='no-img-professor.png')
    height_field = models.IntegerField('Largura', default=0)
    width_field = models.IntegerField('Altura', default=0)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Professores'
        verbose_name = 'Professor'

    def __str__(self):
        return self.nome + " " + self.sobrenome

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})

class Imagem(models.Model):
    titulo = models.CharField('Título', max_length=50)
    descricao = models.TextField('Descrição')
    foto = models.ImageField('Foto', upload_to=upload_location,
                             null=True,
                             blank=True,
                             height_field="height_field",
                             width_field="width_field",
                             default='no-img-professor.png')
    carrosel = models.BooleanField('No Carrosel')
    height_field = models.IntegerField('Largura', default=0)
    width_field = models.IntegerField('Altura', default=0)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Imagens'
        verbose_name = 'Imagem'

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})