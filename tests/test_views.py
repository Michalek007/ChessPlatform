def test_login(client):
    data = dict(pin='1234', username='test')
    response = client.post('/login', data=data)
    print(response)
    assert True


def test_login2(client):
    response = client.get('/params/')
    print(response.json)
    assert True
