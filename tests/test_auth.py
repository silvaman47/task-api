def test_register(client):
    response = client.post('/register', json={'username': 'user', 'password': 'pass'})
    assert response.status_code == 201