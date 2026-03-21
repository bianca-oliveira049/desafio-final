from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views


urlpatterns = [
    path('alunos/', views.get_alunos, name='alunos'),
    path('aluno/<int:id>/', views.get_aluno_id),
    path('aluno/criar/', views.create_aluno),
    path('aluno/atualizar/<int:id>/', views.update_aluno),
    path('aluno/deletar/<int:id>/', views.delete_aluno)

]
