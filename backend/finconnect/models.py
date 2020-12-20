  
from pydaria.ext.database import db
from sqlalchemy_serializer import SerializerMixin


class User(db.Model, SerializerMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(140))
    birth_date = db.Column(db.Date())
    cpf = db.Column(db.String(11))
    email = db.Column(db.String(50))
    password = db.Column(db.String(512))
    wage = db.Column(db.Numeric())
    status = db.Column(db.Enum('A', 'I'))
    createAt =db.Column(db.DateTime())
    editAt =db.Column(db.DateTime())

class Debts(db.Model, SerializerMixin):
    __tablename__ = 'debts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    due_date = db.Column(db.Integer)
    name = db.Column(db.String(140))
    init_date = db.Column(db.DateTime())
    end_date = db.Column(db.DateTime())
    status = db.Column(db.Enum('A', 'I'))
    createAt =db.Column(db.DateTime())
    editAt =db.Column(db.DateTime())

class PaymentHistory(db.Model, SerializerMixin):
    __tablename__ = 'payment_history'
    id = db.Column(db.Integer, primary_key=True)
    debts_id = db.Column(db.Integer, db.ForeignKey('debts.id'))
    payment_day = db.Column(db.Integer)
    status = db.Column(db.Enum('A', 'I'))
    createAt =db.Column(db.DateTime())
    editAt =db.Column(db.DateTime())

class Extra(db.Model, SerializerMixin):
    __tablename__ = 'extra'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(140))
    init_date = db.Column(db.DateTime())
    end_date = db.Column(db.DateTime())
    status = db.Column(db.Enum('A', 'I'))
    createAt =db.Column(db.DateTime())
    editAt =db.Column(db.DateTime())

