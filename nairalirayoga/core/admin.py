from django.contrib import admin
from nairalirayoga.core.models import Horario, Imagem, Preco, Professor, Blog
from pagedown.widgets import AdminPagedownWidget
from django.db.models import TextField

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "created")
    date_hierarchy = 'created'
    list_filter = ('publish',)
    search_fields = ('title', 'body', 'slug')
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {TextField: {'widget': AdminPagedownWidget }}

admin.site.register(Blog, BlogAdmin)

class HorarioModelAdmin(admin.ModelAdmin):
    list_display = ('dia_semana', 'horario', 'local', 'descricao', 'created_at')
    date_hierarchy = 'created_at'
    search_fields = ('dia_semana', 'horario', 'local', 'descricao', 'created_at')
    list_filter = ('dia_semana',)

admin.site.register(Horario, HorarioModelAdmin)

class ImagemModelAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'foto', 'carrosel', 'width_field', 'height_field', 'created_at')
    date_hierarchy = 'created_at'
    search_fields = ('titulo', 'descricao', 'foto', 'carrosel', 'width_field', 'height_field', 'created_at')
    list_filter = ('titulo',)

admin.site.register(Imagem, ImagemModelAdmin)

class PrecoModelAdmin(admin.ModelAdmin):
    list_display = ('valor', 'dias', 'atividade', 'created_at')
    date_hierarchy = 'created_at'
    search_fields = ('valor', 'dias', 'atividade', 'created_at')
    list_filter = ('atividade',)

admin.site.register(Preco, PrecoModelAdmin)

class ProfessorModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'descricao', 'width_field', 'height_field', 'foto', 'created_at')
    date_hierarchy = 'created_at'
    search_fields = ('nome', 'sobrenome', 'descricao', 'foto', 'created_at')
    list_filter = ('nome',)

admin.site.register(Professor, ProfessorModelAdmin)
