def test_currency_route(client):
    # Test GET all currencies
    response = client.get('/currency')
    assert response.status_code == 200

    # Test POST new currency
    new_currency = {'code': 'EUR', 'name': 'Euro'}
    response = client.post('/currency', json=new_currency)
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Currency added successfully!'}

    # Test GET specific currency
    response = client.get('/currency/1')
    assert response.status_code == 200
    assert response.get_json() == {'id': 1, 'code': 'EUR', 'name': 'Euro'}
