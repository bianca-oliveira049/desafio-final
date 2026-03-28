from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

from desafioBackend.serializers import AlunoSerializer, CursoSerializer, MatriculaSerializer
from desafioBackend.models import Aluno, Curso, Matricula

import json

#CRUD Alunos
@api_view(['GET'])
def get_alunos(request):
    if request.method == 'GET':
        alunos = Aluno.objects.all()

        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH'])
def get_aluno_id(request, id):
    try:
        aluno = Aluno.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET': 
        serializer = AlunoSerializer(aluno)
        return Response(serializer.data)
    
    if request.method == 'PATCH':
        serializer = AlunoSerializer(aluno, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def create_aluno(request):
    novo_aluno = request.data
    serializer = AlunoSerializer(data=novo_aluno)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def update_aluno(request, id):
    try:
        aluno_atualizado = Aluno.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AlunoSerializer(aluno_atualizado, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_aluno(request, id):
    if request.method == 'DELETE':
        try:
            aluno_deletar = Aluno.objects.get(pk=id)
            aluno_deletar.delete()

            return Response(status=status.HTTP_202_ACCEPTED)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
#-----------------------------------------------------------------------------------------------------

#CRUD Cursos
@api_view(['POST'])
def create_curso(request):
    novo_curso = request.data
    serializer = CursoSerializer(data=novo_curso)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_cursos(request):
    if request.method == 'GET':
        cursos = Curso.objects.all()

        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH'])
def get_curso_id(request, id):
    try:
        curso = Curso.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET': 
        serializer = CursoSerializer(curso)
        return Response(serializer.data)
    
    if request.method == 'PATCH':
        serializer = CursoSerializer(curso, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def update_curso(request, id):
    try:
        curso_atualizado = Curso.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CursoSerializer(curso_atualizado, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_curso(request, id):
    if request.method == 'DELETE':
        try:
            curso_deletar = Curso.objects.get(pk=id)
            curso_deletar.delete()

            return Response(status=status.HTTP_202_ACCEPTED)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

#Views para Matriculas
        
@api_view(['POST'])
def matricular_aluno(request):
    nova_matricula = request.data
    serializer = MatriculaSerializer(data=nova_matricula)

    id_aluno = request.data.get('id_aluno')
    id_curso = request.data.get('id_curso')

    if Matricula.objects.filter(id_aluno, id_curso).exists():
        return Response({"Error": "O aluno já está matriculado no curso!"}, status=status.HTTP_400_BAD_REQUEST)
    
    if not Aluno.objects.filter(id_aluno).exists(): 
        return Response({"Error": "Aluno não encontrado!"}, status=status.HTTP_404_NOT_FOUND)
    
    if not Curso.objects.filter(id_curso).exists():
        return Response({"Error": "Curso não encontrado!"}, status=status.HTTP_404_NOT_FOUND)
    
    if Matricula.objects.filter(id_aluno).count() == 5:
        return Response({"Error": "Aluno já possui !"}, status=status.HTTP_404_NOT_FOUND)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def matriculas_curso(request, id_Curso):
    if request.method == 'GET':
        matriculas = Matricula.objects.filter(id_curso = id_Curso)
    
        serializer = MatriculaSerializer(matriculas, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def matriculas_aluno(request, id_Aluno):
    if request.method == 'GET':
        matriculas = Matricula.objects.filter(id_aluno = id_Aluno)
    
        serializer = MatriculaSerializer(matriculas, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)




