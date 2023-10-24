from src.models.models import ExchangeRate, Currency, db
from sqlalchemy.exc import IntegrityError

class ExchangeRateService:
    @staticmethod
    def create_exchange_rate(data: dict):
        """
        This is the create_exchange_rate method.
        ---
        parameters:
        - data (dict) : The data of the exchange_rate to be created.
        responses:
        200:
            description: The exchange_rate was successfully created.
        400:
            description: The exchange_rate already exists.
        """
        new_exchange_rate = ExchangeRate(from_currency_id=data['from_currency_id'], to_currency_id=data['to_currency_id'], rate=data['rate'])
        db.session.add(new_exchange_rate)
        try:
            db.session.commit()
            return {'message': 'Exchange rate added successfully!'}, 200
        except IntegrityError:
            db.session.rollback()
            return {'message': 'Exchange rate already exists!'}, 400

    @staticmethod
    def get_exchange_rate(id: int):
        """
        This is the get_exchange_rate method.
        ---
        parameters:
        - id (int) : The id of the exchange_rate to be retrieved.
        responses:
        200:
            description: The exchange_rate was successfully retrieved.
        404:
            description: The exchange_rate was not found.
        """
        exchange_rate = ExchangeRate.query.get(id)
        if exchange_rate is not None:
            return {
                'id': exchange_rate.exchange_rate_id, 
                'from_currency_id': exchange_rate.from_currency_id, 
                'to_currency_id': exchange_rate.to_currency_id, 
                'rate': exchange_rate.rate}, 200
        else:
            return {'message': 'Exchange rate not found!'}, 404

    @staticmethod
    def get_all_exchange_rates():
        """
        This is the get_all_exchange_rates method.
        ---
        parameters:
        - None
        responses:
        200:
            description: The exchange_rates were successfully retrieved.
        """
        exchange_rates = ExchangeRate.query.all()
        return [{
            'id': er.exchange_rate_id, 
            'from_currency_id': er.from_currency_id, 
            'to_currency_id': er.to_currency_id, 
            'rate': er.rate} for er in exchange_rates], 200

    @staticmethod
    def update_exchange_rate(id: int, data: dict):
        """
        This is the update_exchange_rate method.
        ---
        parameters:
        - id (int) : The id of the exchange_rate to be updated.
        - data (dict) : The data of the exchange_rate to be updated.
        responses:
        200:
            description: The exchange_rate was successfully updated.
        404:
            description: The exchange_rate was not found.
        """
        exchange_rate = ExchangeRate.query.get(id)
        if exchange_rate is None:
            return {'message': 'Exchange rate not found!'}, 404

        if 'from_currency_id' in data:
            exchange_rate.from_currency_id = data['from_currency_id']
        if 'to_currency_id' in data:
            exchange_rate.to_currency_id = data['to_currency_id']
        if 'rate' in data:
            exchange_rate.rate = data['rate']

        db.session.commit()
        return {'message': 'Exchange rate updated successfully!'}, 200

    @staticmethod
    def delete_exchange_rate(id: int):
        """
        This is the delete_exchange_rate method.
        ---
        parameters:
        - id (int) : The id of the exchange_rate to be deleted.
        responses:
        200:
            description: The exchange_rate was successfully deleted.
        404:
            description: The exchange_rate was not found.
        """
        exchange_rate = ExchangeRate.query.get(id)
        if exchange_rate is None:
            return {'message': 'Exchange rate not found!'}, 404

        db.session.delete(exchange_rate)
        db.session.commit()
        return {'message': 'Exchange rate deleted successfully!'}, 200
    
    @staticmethod
    def convert_currency(from_currency_id: int, to_currency_ids: list, amount: float):
        """
        This is the convert_currency method.
        ---
        parameters:
        - from_currency_id (int) : The id of the currency to convert from.
        - to_currency_ids (list) : The ids of the currencies to convert to.
        - amount (float) : The amount to convert.
        responses:
        200:
            description: The conversion was successful.
        404:
            description: One or more currencies not found.
        """
        from_currency = Currency.query.get(from_currency_id)
        if from_currency is None:
            return {'message': 'From currency not found!'}, 404

        to_currencies = Currency.query.filter(Currency.currency_id.in_(to_currency_ids)).all()
        if len(to_currencies) != len(to_currency_ids):
            return {'message': 'One or more to currencies not found!'}, 404

        conversions = []
        for to_currency in to_currencies:
            exchange_rate = ExchangeRate.query.filter_by(from_currency_id=from_currency_id, to_currency_id=to_currency.currency_id).first()
            if exchange_rate is None:
                return {'message': f'Exchange rate from {from_currency.code} to {to_currency.code} not found!'}, 404

            converted_amount = amount * exchange_rate.rate
            conversions.append({
                'from': from_currency.code,
                'to': to_currency.code,
                'amount': converted_amount,
            })

        return conversions, 200
