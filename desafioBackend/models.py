from django.db import models

'''
Tabela alunos: id, nome, email
Tabela cursos: id, titulo
Tabela matriculas: id, aluno_id, curso_id 
'''

class Aluno(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=40, blank=False)

    def __str__(self): return self.nome

class Curso(models.Model):
    titulo = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.titulo
    
class Matricula(models.Model):
    id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
