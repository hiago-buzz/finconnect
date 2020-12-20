from flask_simplelogin import SimpleLogin
from werkzeug.security import check_password_hash, generate_password_hash
from finconnect.ext.database import db
from finconnect.util.response import format_response
from finconnect.models import User


def verify_login(user):
    """Valida o usuario e senha para efetuar o login"""
    email = user.get("email")
    password = user.get("password")
    if not email or not password:
        return format_response(
            message="Campo email e Senha são Obrigatórios", status_code=403
        )
    existing_user = User.query.filter_by(email=email).first()
    if not existing_user:
        return format_response(
            message="Usuário Não Cadastrado", status_code=400
        )
    if check_password_hash(existing_user.password, password):
        return format_response(
            message="Sucesso ao realizar Login", status_code=200
        )
    return format_response(
            message="Credenciais Invalidas", status_code=403
        )


def create_user(user):
    """Registra um novo usuario caso nao esteja cadastrado"""
    full_name = user.get("full_name")
    birth_date = user.get("birth_date")
    cpf = user.get("cpf")
    email = user.get("email")
    password = user.get("password")
    wage = user.get("wage")

    if User.query.filter_by(email=email).first():
        return False
    else:
        user = User(
            full_name=full_name,
            birth_date=birth_date,
            cpf=cpf,
            email=email,
            password=generate_password_hash(password),
            wage=wage,
        )
        db.session.add(user)
        db.session.commit()
        return user


def init_app(app):
    SimpleLogin(app, login_checker=verify_login)