from flask_simplelogin import SimpleLogin
from werkzeug.security import check_password_hash, generate_password_hash
from finconnect.ext.database import db
from finconnect.models import User
from finconnect.util import date_now


def verify_login(user):
    """Valida o usuario e senha para efetuar o login"""
    email = user.get("email")
    password = user.get("password")
    if not email or not password:
        return False
    existing_user = User.query.filter_by(email=email).first()
    if not existing_user:
        return False
    if check_password_hash(existing_user.password, password):
        return True
    return False


def create_user(user):
    """Registra um novo usuario caso nao esteja cadastrado"""
    full_name = user.full_name
    birth_date = user.birth_date
    cpf = user.cpf
    email = user.email
    password = user.password
    wage = user.wage
    status = "A"
    createAt = date_now()

    if User.query.filter_by(email=email).first():
        raise RuntimeError(f"{email} já esta cadastrado")
    user = User(
        full_name=full_name,
        birth_date=birth_date,
        cpf=cpf,
        email=email,
        password=generate_password_hash(password),
        wage=wage,
        status=status,
        createAt=createAt,
    )
    db.session.add(user)
    db.session.commit()
    return user


def init_app(app):
    SimpleLogin(app, login_checker=verify_login)