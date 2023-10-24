from flask import Blueprint, request, jsonify, make_response

# Services
from src.services.currency_service import CurrencyService

# Marshmallow schemas
from src.schemas.currency_schema import CurrencySchema

currency_bp = Blueprint('currency', __name__)
currency_schema = CurrencySchema()

@currency_bp.route('/currency', defaults={"id": None}, methods=['POST', 'GET'])
@currency_bp.route('/currency/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def currency_route(id: int):
    """
    This is the currency endpoint
    ---
    parameters:
    - id (int) : The id of the currency to be retrieved.
    responses:
    200:
        description: The currency was successfully retrieved.
    405:
        description: Method not allowed.
    404:
        description: The currency was not found.
    400:
        description: Bad request.
    """
    if request.method == 'POST':
        data = request.get_json()

        # Validate the data
        errors = currency_schema.validate(data)
        if errors:
            return make_response(jsonify(errors), 400)

        response, status_code = CurrencyService.create_currency(data)
        return make_response(jsonify(response), status_code)

    elif request.method == 'GET':
        if id is not None:
            response, status_code = CurrencyService.get_currency(id)
            return make_response(jsonify(response), status_code)
        else:
            response, status_code = CurrencyService.get_all_currencies()
            return make_response(jsonify(response), status_code)

    elif request.method == 'PUT':
        data = request.get_json()

        # Validate the data
        errors = currency_schema.validate(data)
        if errors:
            return make_response(jsonify(errors), 400)
        
        response, status_code = CurrencyService.update_currency(id, data)
        return make_response(jsonify(response), status_code)

    elif request.method == 'DELETE':
        response, status_code = CurrencyService.delete_currency(id)
        return make_response(jsonify(response), status_code)
    
    return make_response(jsonify({'message': 'Method not allowed!'}), 405)