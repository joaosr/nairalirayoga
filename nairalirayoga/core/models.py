from django.db import models


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