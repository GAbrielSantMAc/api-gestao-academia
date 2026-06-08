# 🏋️ Sistema de Gestão de Academia

API REST desenvolvida utilizando **Python**, **Django** e **Django REST Framework** para gerenciamento de alunos e matrículas em uma academia.

## 📋 Objetivo

Este projeto foi desenvolvido para a disciplina de Desenvolvimento de APIs, com o objetivo de demonstrar a construção de uma API REST completa contendo:

* Models
* Serializers
* Views
* Rotas (URLs)
* Banco de Dados
* Operações CRUD

---

## 🚀 Tecnologias Utilizadas

* Python 3.11
* Django 5.2
* Django REST Framework
* SQLite
* Git
* GitHub

---

## 📊 Estrutura de Dados

### Aluno

| Campo | Tipo    |
| ----- | ------- |
| id    | Integer |
| nome  | String  |
| cpf   | String  |
| email | String  |

### Matrícula

| Campo | Tipo                |
| ----- | ------------------- |
| id    | Integer             |
| plano | String              |
| valor | Decimal             |
| aluno | Foreign Key (Aluno) |

---

## 🔗 Relacionamento

Um aluno pode possuir uma ou mais matrículas.

```text
Aluno
 ├── id
 ├── nome
 ├── cpf
 └── email

Matricula
 ├── id
 ├── plano
 ├── valor
 └── aluno_id
```

---

## 📌 Funcionalidades

### CRUD de Alunos

* Cadastrar aluno
* Listar alunos
* Editar aluno
* Excluir aluno

### CRUD de Matrículas

* Cadastrar matrícula
* Listar matrículas
* Editar matrícula
* Excluir matrícula

---

## 🌐 Rotas da API

### Alunos

```http
/api/alunos/
```

### Matrículas

```http
/api/matriculas/
```

---

## ⚙️ Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/GAbrielSantMAc/api-gestao-academia.git
```

### 2. Entrar na pasta do projeto

```bash
cd academia_projeto
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Executar as migrações

```bash
python manage.py migrate
```

### 5. Iniciar o servidor

```bash
python manage.py runserver
```

O sistema ficará disponível em:

```text
http://127.0.0.1:8000/
```

---

## 🧪 Como Utilizar

### Cadastrar um Aluno

Acesse:

```text
http://127.0.0.1:8000/api/alunos/
```

Preencha:

* nome
* cpf
* email

Clique em **POSTAR**.

---

### Cadastrar uma Matrícula

Acesse:

```text
http://127.0.0.1:8000/api/matriculas/
```

Preencha:

* plano
* valor
* aluno

Clique em **POSTAR**.

---

### Consultar Registros

Basta acessar:

```text
http://127.0.0.1:8000/api/alunos/
```

ou

```text
http://127.0.0.1:8000/api/matriculas/
```

Os dados serão retornados em formato JSON.

---

## 👨‍💻 Autor

Gabriel Santos

Projeto acadêmico desenvolvido para demonstração de APIs REST utilizando Django e Django REST Framework.
