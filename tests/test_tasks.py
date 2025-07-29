def test_task_crud(client):
    client.post('/register', json={'username': 'user', 'password': 'pass'})
    login = client.post('/login', json={'username': 'user', 'password': 'pass'})
    token = login.get_json()['access_token']
    headers = {'Authorization': f'Bearer {token}'}
    response = client.post('/tasks', json={'title': 'New Task'}, headers=headers)
    assert response.status_code == 201