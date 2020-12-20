from finconnect.ext.database import db
from sqlalchemy_serializer import SerializerMixin
from finconnect.util import date


class User(db.Model, SerializerMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(140))
    birth_date = db.Column(db.String(10))
    cpf = db.Column(db.String(11))
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(512))
    wage = db.Column(db.String(20))
    status = db.Column("active", db.Boolean, default=True)
    createAt = db.Column(db.String(20), default=date.date_now())
    editAt = db.Column(db.String(20), default=None)


class Debts(db.Model, SerializerMixin):
    __tablename__ = "debts"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    due_date = db.Column(db.Integer)
    name = db.Column(db.String(140))
    init_date = db.Column(db.String(10))
    end_date = db.Column(db.String(10))
    status = db.Column("active", db.Boolean, default=True)
    createAt = db.Column(db.String(20), default=date.date_now())
    editAt = db.Column(db.String(20), default=None)

    user = db.relationship("User", foreign_keys=user_id)


class PaymentHistory(db.Model, SerializerMixin):
    __tablename__ = "payment_history"
    id = db.Column(db.Integer, primary_key=True)
    debts_id = db.Column(db.Integer, db.ForeignKey("debts.id"))
    payment_day = db.Column(db.Integer)
    status = db.Column("active", db.Boolean, default=True)
    createAt = db.Column(db.String(20), default=date.date_now())
    editAt = db.Column(db.String(20), default=None)

    debts = db.relationship("Debts", foreign_keys=debts_id)


class Extra(db.Model, SerializerMixin):
    __tablename__ = "extra"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    name = db.Column(db.String(140))
    init_date = db.Column(db.String(10))
    end_date = db.Column(db.String(10))
    status = db.Column("active", db.Boolean, default=True)
    createAt = db.Column(db.String(20), default=date.date_now())
    editAt = db.Column(db.String(20), default=None)

    user = db.relationship("User", foreign_keys=user_id)