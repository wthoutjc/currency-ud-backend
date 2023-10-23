from flask import Blueprint, request, jsonify, make_response

# Services
from src.services.currency_service import CurrencyService

currency_bp = Blueprint('currency', __name__)

@currency_bp.route('/currency', defaults={"id": None}, methods=['POST', 'GET'])
@currency_bp.route('/currency/<int:id>', methods=['GET'])
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
    """
    if request.method == 'POST':
        data = request.get_json()
        response, status_code = CurrencyService.create_currency(data)
        return make_response(jsonify(response), status_code)

    elif request.method == 'GET':
        if id is not None:
            response, status_code = CurrencyService.get_currency(id)
            return make_response(jsonify(response), status_code)
        else:
            response, status_code = CurrencyService.get_all_currencies()
            return make_response(jsonify(response), status_code)

    return make_response(jsonify({'message': 'Method not allowed!'}), 405)