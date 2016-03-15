from django.contrib import admin
from nairalirayoga.core.models import Horario, Preco, Professor

class HorarioModelAdmin(admin.ModelAdmin):
    list_display = ('dia_semana', 'horario', 'local', 'descricao', 'created_at')
    date_hierarchy = 'created_at'
    search_fields = ('dia_semana', 'horario', 'local', 'descricao', 'created_at')
    list_filter = ('dia_semana',)

admin.site.register(Horario, HorarioModelAdmin)

class PrecoModelAdmin(admin.ModelAdmin):
    list_display = ('valor', 'dias', 'atividade', 'created_at')
    date_hierarchy = 'created_at'
    search_fields = ('valor', 'dias', 'atividade', 'created_at')
    list_filter = ('atividade',)

admin.site.register(Preco, PrecoModelAdmin)

class ProfessorModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'descricao', 'foto', 'created_at')
    date_hierarchy = 'created_at'
    search_fields = ('nome', 'sobrenome', 'descricao', 'foto', 'created_at')
    list_filter = ('nome',)

admin.site.register(Professor, ProfessorModelAdmin)
