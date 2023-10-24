from src.models.models import Currency, db
from sqlalchemy.exc import IntegrityError

class CurrencyService:
    @staticmethod
    def create_currency(data: dict):
        """
        This is the create_currency method.
        ---
        parameters:
        - data (dict) : The data of the currency to be created.
        responses:
        200:
            description: The currency was successfully created.
        400:
            description: The currency already exists.
        """
        new_currency = Currency(code=data['code'], name=data['name'])
        db.session.add(new_currency)
        try:
            db.session.commit()
            return {'message': 'Currency added successfully!'}, 200
        except IntegrityError:
            db.session.rollback()
            return {'message': 'Currency already exists!'}, 400

    @staticmethod
    def get_currency(id: int):
        """
        This is the get_currency method.
        ---
        parameters:
        - id (int) : The id of the currency to be retrieved.
        responses:
        200:
            description: The currency was successfully retrieved.
        404:
            description: The currency was not found.
        """
        currency = Currency.query.get(id)
        if currency is not None:
            return {'id': currency.currency_id, 'code': currency.code, 'name': currency.name}, 200
        else:
            return {'message': 'Currency not found!'}, 404

    @staticmethod
    def get_all_currencies():
        """
        This is the get_all_currencies method.
        ---
        parameters:
        - None
        responses:
        200:
            description: The currencies were successfully retrieved.
        """
        currencies = Currency.query.all()
        return [{'id': c.currency_id, 'code': c.code, 'name': c.name} for c in currencies], 200

    @staticmethod
    def update_currency(id, data):
        currency = Currency.query.get(id)
        if currency is None:
            return {'message': 'Currency not found!'}, 404

        if 'code' in data:
            currency.code = data['code']
        if 'name' in data:
            currency.name = data['name']

        db.session.commit()
        return {'message': 'Currency updated successfully!'}, 200

    @staticmethod
    def delete_currency(id):
        currency = Currency.query.get(id)
        if currency is None:
            return {'message': 'Currency not found!'}, 404

        db.session.delete(currency)
        db.session.commit()
        return {'message': 'Currency deleted successfully!'}, 200
