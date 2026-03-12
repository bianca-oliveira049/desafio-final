from django.contrib import admin
from desafioBackend.models import Aluno, Curso, Matricula

class Alunos(admin.ModelAdmin):
    list_display = ("id", "nome", "email")
    list_display_links = ("id", "nome")
    list_per_page = 20
    search_fields = ("id",)

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ("id", "titulo")
    list_display_links = ("id", "titulo")
    list_per_page = 30
    search_fields = ("id",)

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ("id", "id_aluno", "id_curso")
    list_display_links = ("id", "id_aluno", "id_curso")
    list_per_page = 10
    search_fields = ("id",)

admin.site.register(Matricula, Matriculas)