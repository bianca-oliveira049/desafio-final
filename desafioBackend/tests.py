from rest_framework.test import APITestCase
from .models import Aluno, Curso, Matricula
from rest_framework import status

class APIteste(APITestCase):
    def setUp(self):
        self.aluno = Aluno.objects.create(
            nome="Carlos Silva", 
            email="carlos@email.com"
        )
        self.curso = Curso.objects.create(
            titulo="Python para Web"
        )
        self.matricula = Matricula.objects.create(
            id_aluno=self.aluno, 
            id_curso=self.curso, 
            status="ativa"
        )

        self.url_alunos = '/api/alunos/'
        self.url_criar_aluno = '/api/aluno/criar/'
        self.url_cursos = '/api/cursos/'
        self.url_matricular = '/api/matricular/'

    # --- TESTES DE ALUNO ---

    def test_post_aluno_email_duplicado(self):
        data = {
            "nome": "Carlos Segundo", 
            "email": "carlos@email.com"
        }
        response = self.client.post(self.url_criar_aluno, data)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data['dados'])

    def test_get_lista_alunos(self):
        response = self.client.get(self.url_alunos)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # --- TESTES DE MATRÍCULA ---

    def test_post_matricula_valida(self):
        outro_curso = Curso.objects.create(titulo="Outro Curso")
        data = {
            "id_aluno": self.aluno.id,
            "id_curso": outro_curso.id,
            "status": "ativa"
        }
        response = self.client.post(self.url_matricular, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_cancelar_matricula_endpoint(self):
        url = f'/api/matriculas/cancelar_matricula/{self.matricula.id}/'
        
        response = self.client.patch(url)
        
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        
        self.matricula.refresh_from_db()
        self.assertEqual(self.matricula.status, "cancelada")
    
    def test_concluir_curso_endpoint(self):
        url = f'/api/matriculas/concluir_curso/{self.matricula.id}/'
        
        response = self.client.patch(url)
        
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        
        self.matricula.refresh_from_db()
        self.assertEqual(self.matricula.status, "concluida")

    # --- TESTES DE CURSO ---

    def test_post_curso_sem_titulo(self):
        url_criar_curso = '/api/curso/criar/'
        data = {"titulo": ""}
        response = self.client.post(url_criar_curso, data)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)