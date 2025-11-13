# GRF Talk - Backend API

API REST desenvolvida com Django e Django Rest Framework para o sistema de chat GRF Talk.

## Tecnologias Utilizadas

- **Python 3.13**
- **Django 4.2** - Framework web
- **Django Rest Framework 3.16** - API REST
- **MySQL** - Banco de dados
- **JWT (Simple JWT)** - Autenticação
- **WebSocket (Socket.IO)** - Comunicação em tempo real
- **CORS Headers** - Suporte a requisições cross-origin

## Funcionalidades

- ✅ Sistema de autenticação com JWT
- ✅ CRUD de usuários
- ✅ Sistema de chats/conversas
- ✅ Envio e gerenciamento de mensagens
- ✅ Upload de anexos (imagens, arquivos)
- ✅ Comunicação em tempo real via WebSocket
- ✅ API RESTful completa

## Pré-requisitos

- Python 3.13+
- MySQL 8.0+
- pip (gerenciador de pacotes Python)

## Instalação

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd back
```

### 2. Crie e ative o ambiente virtual

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados MySQL

Crie um banco de dados MySQL:

```sql
CREATE DATABASE projeto CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 5. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
# Database Configuration
DB_NAME=projeto
DB_USER=root
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=3306
DB_CHARSET=utf8mb4

# Django Settings
SECRET_KEY=django-insecure-a-gnk1b046e!+q@8=y3ctf5g5%2dyx7ou2ti2^rjzq88jpy7ml
DEBUG=True
```

### 6. Execute as migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Crie um superusuário (opcional)

```bash
python manage.py createsuperuser
```

### 8. Inicie o servidor

```bash
python manage.py runserver
```

O servidor estará rodando em `http://127.0.0.1:8000`

## Estrutura do Projeto

```
back/
├── accounts/           # App de autenticação e usuários
├── attachments/        # App de gerenciamento de anexos
├── chats/             # App de chats e mensagens
├── core/              # Configurações do projeto Django
│   ├── settings.py    # Configurações principais
│   ├── urls.py        # Rotas principais
│   └── wsgi.py        # WSGI configuration
├── media/             # Arquivos de mídia (uploads)
├── venv/              # Ambiente virtual Python
├── .env               # Variáveis de ambiente
├── .gitignore         # Arquivos ignorados pelo Git
├── db.sqlite3         # Banco de dados SQLite (desenvolvimento)
├── manage.py          # CLI do Django
├── requirements.txt   # Dependências Python
└── README.md          # Este arquivo
```

## Endpoints da API

### Autenticação

- `POST /api/v1/accounts/sign-up/` - Criar nova conta
- `POST /api/v1/accounts/sign-in/` - Fazer login
- `GET /api/v1/accounts/me/` - Obter dados do usuário autenticado
- `PUT /api/v1/accounts/me/` - Atualizar dados do usuário

### Chats

- `GET /api/v1/chats/` - Listar todos os chats
- `POST /api/v1/chats/` - Criar novo chat
- `DELETE /api/v1/chats/{id}/` - Deletar chat

### Mensagens

- `GET /api/v1/chats/{chat_id}/messages/` - Listar mensagens de um chat
- `POST /api/v1/chats/{chat_id}/messages/` - Enviar mensagem
- `DELETE /api/v1/chats/{chat_id}/messages/{message_id}/` - Deletar mensagem

## Autenticação

A API utiliza **JWT (JSON Web Tokens)** para autenticação. Após fazer login, você receberá um `access_token` que deve ser incluído no header de todas as requisições autenticadas:

```
Authorization: Bearer <seu_access_token>
```

O token tem validade de **7 dias**.

## CORS

O backend está configurado para aceitar requisições de:
- `http://localhost:3000` (Frontend em desenvolvimento)

Para adicionar mais origens, edite o arquivo `core/settings.py`:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3001",
    # Adicione mais origens aqui
]
```

## Desenvolvimento

### Comandos Úteis

```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Iniciar servidor de desenvolvimento
python manage.py runserver

# Iniciar shell do Django
python manage.py shell

# Executar testes
python manage.py test
```

### Admin Panel

Acesse o painel administrativo em `http://127.0.0.1:8000/admin/` com as credenciais do superusuário.

## Produção

⚠️ **Importante:** Antes de fazer deploy para produção:

1. Altere `DEBUG = False` no `settings.py`
2. Gere uma nova `SECRET_KEY` segura
3. Configure `ALLOWED_HOSTS` com seus domínios
4. Use variáveis de ambiente para dados sensíveis
5. Configure um servidor de banco de dados adequado (não use SQLite)
6. Configure arquivos estáticos com `collectstatic`
7. Use um servidor WSGI como Gunicorn ou uWSGI
8. Configure HTTPS

## Troubleshooting

### Erro ao conectar ao MySQL

Certifique-se de que:
- O MySQL está rodando
- As credenciais no `.env` estão corretas
- O banco de dados foi criado
- O pacote `mysqlclient` está instalado

### Erro de CORS

Verifique se a origem do frontend está em `CORS_ALLOWED_ORIGINS` no `settings.py`

### Erro de migração

Execute:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Licença

Este projeto é privado e proprietário.

## Suporte

Para suporte ou dúvidas, entre em contato com a equipe de desenvolvimento.
