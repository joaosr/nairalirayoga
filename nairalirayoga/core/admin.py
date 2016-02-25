from django.contrib import admin
from nairalirayoga.core.models import Horario

class HorarioModelAdmin(admin.ModelAdmin):
    list_display = ('dia_semana', 'horario', 'local', 'descricao', 'created_at')
    date_hierarchy = 'created_at'
    search_fields = ('dia_semana', 'horario', 'local', 'descricao', 'created_at')
    list_filter = ('dia_semana',)

admin.site.register(Horario, HorarioModelAdmin)