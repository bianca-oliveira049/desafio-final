# Desafio Final Backend - PD

## Link da APi:
[https://desafio-final-rjeb.onrender.com](https://desafio-final-rjeb.onrender.com)

## Tecnologias e Ferramentas
* **Linguagem:** Python 3.14.2
* **Framework:** Django 6.0.3 / Django Rest Framework
* **Base de Dados:** PostgreSQL (Produção) / SQLite (Desenvolvimento)
* **Documentação:** Swagger (drf-yasg)
* **Deploy:** Render
* **Servidor de Aplicação:** Gunicorn
* **Gestão de Estáticos:** WhiteNoise

## Funcionalidades Principais
* **Alunos:** CRUD completo, validação de nome e garantia de e-mails únicos.
* **Cursos:** CRUD completo, com garantia de nome não vazio.
* **Matrículas:** Controle de inscrições com estados (Ativa, Cancelada, Concluída).
* **Documentação:** Interface interativa para testes de endpoints via Swagger.

## Como Rodar o Projeto Localmente

### 1. Clonar o Repositório
```bash
git clone [https://github.com/bianca-oliveira049/desafio-final.git](https://github.com/bianca-oliveira049/desafio-final.git)
cd desafio-final
```
## 2. Configurar ambiente virtual
```
python -m venv venv
*No Windows:*
.\venv\Scripts\activate
*No Linux/Mac:*
source venv/bin/activate
```
### 3. Instalar dependências
```
pip install -r requirements.txt
```
### 4. Executar migrações e iniciar
```
python manage.py migrate
python manage.py runserver
```
## Endpoints disponíveis
* 'api/alunos/' - Listar alunos
* 'api/aluno/<int:id>/' - Procurar aluno por id
* 'api/aluno/criar/' - Criar aluno
* 'api/aluno/atualizar/<int:id>/' -  Atualizar dados de aluno
* 'api/aluno/deletar/<int:id>/' - Deletar aluno

* 'api/cursos/' - Listar cursos
* 'api/curso/<int:id>/' - Procurar curso por id
* 'api/curso/criar/' - Criar curso
* 'api/curso/atualizar/<int:id>/' - Atualizar dados de curso
* 'api/curso/deletar/<int:id>/' - Deletar curso

* 'api/matricular/' - Criar matrícula
* 'api/matriculas/curso/<int:id_Curso>/' - Listar matrículas de um curso
* 'api/matriculas/aluno/<int:id_Aluno>/' - Listar matrículas de um aluno
* 'api/matriculas/cancelar_matricula/<int:id>/' - Cancelar matrícula
* 'api/matriculas/concluir_curso/<int:id>/' - Concluir matrícula

* 'swagger/' - Acessar documentação
