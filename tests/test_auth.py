def test_register_and_login(client):
    res = client.post("/auth/register", json={"username": "testuser", "password": "secret"})
    assert res.status_code == 201

    res = client.post("/auth/login", json={"username": "testuser", "password": "secret"})
    assert res.status_code == 200
    assert "token" in res.json
