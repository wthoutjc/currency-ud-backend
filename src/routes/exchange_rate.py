from flask import Blueprint, request, jsonify, make_response
from src.services.exchange_rate_service import ExchangeRateService

# Marshmallow schemas
from src.schemas.exchange_rate_schema import ExchangeRateSchema, ConvertSchema

exchange_rate_bp = Blueprint('exchange_rate', __name__)
exchange_rate_schema = ExchangeRateSchema()
convert_schema = ConvertSchema()

@exchange_rate_bp.route('/exchange_rate', defaults={"id": None}, methods=['POST', 'GET'])
@exchange_rate_bp.route('/exchange_rate/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def exchange_rate_route(id):
    """
    This is the exchange_rate endpoint
    ---
    parameters:
    - id (int) : The id of the exchange_rate to be retrieved.
    responses:
    200:
        description: The exchange_rate was successfully retrieved.
    405:
        description: Method not allowed.
    400:
        description: Bad request.
    404:
        description: The exchange_rate was not found.
    """
    if request.method == 'POST':
        data = request.get_json()

        # Validate the data
        errors = exchange_rate_schema.validate(data)
        if errors:
            return make_response(jsonify(errors), 400)

        response, status_code = ExchangeRateService.create_exchange_rate(data)
        return make_response(jsonify(response), status_code)

    elif request.method == 'GET':
        if id is not None:
            response, status_code = ExchangeRateService.get_exchange_rate(id)
            return make_response(jsonify(response), status_code)
        else:
            response, status_code = ExchangeRateService.get_all_exchange_rates()
            return make_response(jsonify(response), status_code)
    
    elif request.method == 'PUT':
        data = request.get_json()

        # Validate the data
        errors = exchange_rate_schema.validate(data)
        if errors:
            return make_response(jsonify(errors), 400)

        response, status_code = ExchangeRateService.update_exchange_rate(id, data)
        return make_response(jsonify(response), status_code)

    elif request.method == 'DELETE':
        response, status_code = ExchangeRateService.delete_exchange_rate(id)
        return make_response(jsonify(response), status_code)

    return make_response(jsonify({'message': 'Method not allowed!'}), 405)

# Currency conversion
@exchange_rate_bp.route('/convert', methods=['POST'])
def convert_route():
    """
    This is the convert endpoint
    ---
    parameters:
    - from_currency_id (int) : The id of the currency to convert from.
    - to_currency_ids (list) : The ids of the currencies to convert to.
    - amount (float) : The amount to convert.
    responses:
    200:
        description: The conversion was successful.
    400:
        description: Bad request.
    404:
        description: One or more currencies not found.
    """
    data = request.get_json()

    from_currency_id = data['from_currency_id']
    to_currency_ids = data['to_currency_ids']
    amount = data['amount']

    # Validate the data
    errors = convert_schema.validate(data)
    if errors:
        return make_response(jsonify(errors), 400)

    response, status_code = ExchangeRateService.convert_currency(from_currency_id, to_currency_ids, amount)
    return make_response(jsonify(response), status_code)
