This is a basic app in flask that registers info on the specified db (check .env for further information).

How it is supposed to work:

The user creates his user through /register and logs in to obtain a token. With a token in "header" he/she can create a project where other users can make a request to participate (/solicitacoes, token needed for user identification). The owner can join a new user to his/her project through 
/integrantes. 

It's possible to list all projects in /projects using method GET.
Further GET routes weren't created, since it's a basic project for demonstration. 

Notes:
1- It includes password hashes in db.
2- Token does not use JWT. 
3- Total of 5 tables in db (users, token, solicitations, participants and projects). 
4- all routes include /api before route. (Example: port/api/register).

---------------------------------------------------------------------------------------------------------------------------------------------------

Procedures to install:

after clone from git, to use the app:

1- delete folder venv

2- on terminal:

python -m ven venv
source venv/bin/activate

pip install flask flask_sqlalchemy flask_migrate environs psycopg2-binary

pip install flask_login

pip install bcrypt	

flask run

use port on insomnia (or other app).

---------------------------------------------------------------------------------------------------------------------------------------------------

blueprints:

POST
port/api/register
port/api/obtain_token (necessary to obtain token, to use next routes)
port/api/projetos	
port/api/integrantes
port/api/solicitacoes

GET
port/api/projetos (lists all projects)

---------------------------------------------------------------------------------------------------------------------------------------------------

LinkedIn: https://www.linkedin.com/in/brunopetinati/






