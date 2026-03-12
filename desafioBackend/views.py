from django.shortcuts import render
from rest_framework import viewsets
from desafioBackend.serializers import AlunoSerializer, CursoSerializer, MatriculaSerializer
from desafioBackend.models import Aluno, Curso, Matricula

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer