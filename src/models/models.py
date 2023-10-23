from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Currency(db.Model):
    __tablename__ = 'Currency'
    currency_id = db.Column('currency_id', db.Integer, primary_key=True)
    code = db.Column('code', db.String(10), nullable=False)
    name = db.Column('name', db.String(50), nullable=False)
    from_exchange_rates = db.relationship('ExchangeRate', foreign_keys='ExchangeRate.from_currency_id', backref='from_currency')
    to_exchange_rates = db.relationship('ExchangeRate', foreign_keys='ExchangeRate.to_currency_id', backref='to_currency')

class ExchangeRate(db.Model):
    __tablename__ = 'ExchangeRate'
    exchange_rate_id = db.Column('exchange_rate_id', db.Integer, primary_key=True)
    from_currency_id = db.Column('from_currency_id', db.Integer, db.ForeignKey('Currency.currency_id'), nullable=False)
    to_currency_id = db.Column('to_currency_id', db.Integer, db.ForeignKey('Currency.currency_id'), nullable=False)
    rate = db.Column('rate', db.Float, nullable=False)