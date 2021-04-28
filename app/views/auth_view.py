from flask import Blueprint, render_template, request, current_app, redirect, url_for
from app.models.usuarios_model import UsuariosModel
from http import HTTPStatus
from flask_login import login_user

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        

        session = current_app.db.session
    
        email_f = request.form.get('email')
        senha_f = request.form.get('senha')

        find_user = UsuariosModel.query.filter_by(email=email_f).first()
        
        if find_user and find_user.senha == senha_f:
            next_url= request.args.get('next')
            login_user(find_user, False)
            if next_url and next_url.startswith('/'):
                next_url = url_for('auth.login')
            
            if not next_url:
                next_url = url_for('bp_home.home')
            return redirect(next_url)  
        else:
            return "<p> Senha ou usuário incorretos </p>" 


@bp.route('/signup', methods=['GET','POST'])
def signup():
  if request.method == 'GET':
    return render_template("signup.html")
  
  session = current_app.db.session

  nome = (request.form.get("nome"))
  email = (request.form.get("email"))
  senha = (request.form.get("senha"))
  tecnologias = (request.form.get("tecnologia"))
  idiomas = (request.form.get("idiomas"))
  bio = (request.form.get("bio"))

  usuario = UsuariosModel(nome=nome,email=email,senha=senha,tecnologias=tecnologias,idiomas=idiomas, bio=bio)

  session.add(usuario)
  session.commit()      

  return "<h1> Cadastrado </h1>"  
