from rest_framework import serializers
from desafioBackend.models import Aluno, Curso, Matricula

class AlunoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class CursoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'