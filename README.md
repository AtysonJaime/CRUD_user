# Cadastro de Usuários - CRUD

![GitHub](https://img.shields.io/badge/Atysonjaime-CRUD__User-9cf)
![GitHub](https://img.shields.io/github/license/atysonjaime/CRUD_User)

> 👤 Projeto fullstack com o intuito de realizar uma simples aplicação para cadastro de usuários. Possibilitando a criação, edição e exclusão. Possue um sistema de login simples, no qual, utiliza o email, cpf ou o pis como forma de acesso para a aréa do usuario.
>
> Projeto proposto como desáfio tecnico para a empresa [PontoTel](https://www.pontotel.com.br/).

![Login Page](/frontend/assets/capa_login.png)

## 💻 Tecnológias

Esse projeto subdivide-se entre backend e frontend. As tecnologias utilizadas podem ser visualizar na tabela abaixo.

| **Backend**                                                    | **Frontend**                                      |
| :------------------------------------------------------------- | :------------------------------------------------ |
| [Python](https://www.python.org)                               | JavaScript e JSON                                 |
| [Django](https://www.djangoproject.com)                        | [Node e NPM](https://nodejs.org/en/)              |
| [Django Rest Framework](https://www.django-rest-framework.org) | [Vue.js](https://vuejs.org)                       |
| [JTW AUTH](https://jwt.io/introduction)                        | [Nuxtjs](https://nuxtjs.org)                      |
|                                                                | [SASS](https://sass-lang.com)                     |
|                                                                | [PUG](https://pugjs.org/api/getting-started.html) |
|                                                                | [Buefy](https://buefy.org)                        |

## 🔧 Build Setup

### Backend

_OBS: é necessario ter o python já instalado em sua maquina._

_OBS2: é necessario ter um arquivo .env na pasta backend/core contendo a SECRET KEY para o banco_

1. Para rodar a parte de back deste projeto, primeiro acesse a parta backend pelo terminal.

2. Após fazer isso, rode o comando:

   ```cmd
   venv\Scripts\activate
   ```

   Para o ambiente virtual ser ativado.

3. Quando ativado, irá aparecer um (venv) na linha de comando do terminal. quando isso acontecer é so seguir os seguintes comandos:

   ```python
   pip install
   ```

   ```python
   python manege.py makemigration
   ```

   ```python
   python manege.py migrate
   ```

   ```python
   python manege.py migrate
   ```

   ```python
   python manege.py runserver
   ```

   Se tudo estiver okay, seu banco estará rodando na porta 8000.

### Frontend

_OBS: é necessario ter o node e npm já instalado em sua maquina._

1. Para rodar a parte de front deste projeto, primeiro acesse a pasta frontend pela terminal.

2. Em seguida, rode os seguintes comandos:

   ```node
   npm install
   ```

   ```node
   npm run dev
   ```

3. Pronto, o projeto frontend estará rodando na porta 3000

## 🚀 Deploy

## 📝 Licença

[MIT License](https://github.com/AtysonJaime/CRUD_user/blob/main/LICENSE) © [Atyson Jaime](https://atysonjaime.github.io)
