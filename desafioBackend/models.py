from django.db import models
from django.core.exceptions import ValidationError
import re
'''
Tabela alunos: id, nome, email
Tabela cursos: id, titulo
Tabela matriculas: id, aluno_id, curso_id, status
'''

def valida_nome(Nome):
        if len(Nome.strip().split()) < 2 or not re.match(r"^[A-Za-zÀ-ÿ\s]+$", Nome):
            raise ValidationError('Nome inválido: o nome possui símbolos e/ou números!')
        
class Aluno(models.Model):
    nome = models.CharField(max_length=100, blank=False, validators=[valida_nome])
    email = models.EmailField(max_length=40, blank=False, unique=True)

    def __str__(self): return self.nome

    
        
class Curso(models.Model):
    titulo = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.titulo
    
class Status_matricula(models.TextChoices):
    ATIVA = 'ativa', 'Ativa'
    CANCELADA = 'cancelada', 'Cancelada'
    CONCLUIDA = 'concluida', 'Concluida'
    
class Matricula(models.Model):
    id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, blank=False)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE, blank=False)
    status = models.CharField(max_length=20, choices=Status_matricula.choices, default=Status_matricula.ATIVA)
