def test_exchange_rate_route(client):
    # Test GET all exchange rates
    response = client.get('/exchange_rate')
    assert response.status_code == 200

    # Test POST new exchange rate
    new_exchange_rate = {'from_currency_id': 1, 'to_currency_id': 2, 'rate': 0.85}
    response = client.post('/exchange_rate', json=new_exchange_rate)
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Exchange rate added successfully!'}

    # Test GET specific exchange rate
    response = client.get('/exchange_rate/1')
    assert response.status_code == 200
    assert response.get_json() == {'id': 1, 'from_currency_id': 1, 'to_currency_id': 2, 'rate': 0.85}
