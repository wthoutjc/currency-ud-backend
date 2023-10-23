from flask import Blueprint, request, jsonify, make_response
from src.services.exchange_rate_service import ExchangeRateService

exchange_rate_bp = Blueprint('exchange_rate', __name__)

@exchange_rate_bp.route('/exchange_rate', defaults={"id": None}, methods=['POST', 'GET'])
@exchange_rate_bp.route('/exchange_rate/<int:id>', methods=['GET'])
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
    """
    if request.method == 'POST':
        data = request.get_json()
        response, status_code = ExchangeRateService.create_exchange_rate(data)
        return make_response(jsonify(response), status_code)

    elif request.method == 'GET':
        if id is not None:
            response, status_code = ExchangeRateService.get_exchange_rate(id)
            return make_response(jsonify(response), status_code)
        else:
            response, status_code = ExchangeRateService.get_all_exchange_rates()
            return make_response(jsonify(response), status_code)

    return make_response(jsonify({'message': 'Method not allowed!'}), 405)

# Currency conversion
@exchange_rate_bp.route('/convert', methods=['POST'])
def convert_route():
    data = request.get_json()
    from_currency_id = data['from']
    to_currency_ids = data['to']
    amount = data['amount']
    response, status_code = ExchangeRateService.convert_currency(from_currency_id, to_currency_ids, amount)
    return make_response(jsonify(response), status_code)
