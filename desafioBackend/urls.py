from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views


urlpatterns = [
    path('alunos/', views.get_alunos, name='alunos'),
    path('aluno/<int:id>/', views.get_aluno_id),
    path('aluno/criar/', views.create_aluno),
    path('aluno/atualizar/<int:id>/', views.update_aluno),
    path('aluno/deletar/<int:id>/', views.delete_aluno),

    path('cursos/', views.get_cursos, name='cursos'),
    path('curso/<int:id>/', views.get_curso_id),
    path('curso/criar/', views.create_curso),
    path('curso/atualizar/<int:id>/', views.update_curso),
    path('curso/deletar/<int:id>/', views.delete_curso),

    path('matricular/', views.matricular_aluno),
    path('matriculas/curso/<int:id_Curso>/', views.matriculas_curso),
    path('matriculas/aluno/<int:id_Aluno>/', views.matriculas_aluno),
    path('matriculas/cancelar_matricula/<int:id>/', views.cancelar_matricula),
    path('matriculas/concluir_curso/<int:id>/', views.concluir_curso)
]
