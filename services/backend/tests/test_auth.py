# services/backend/tests/test_auth.py

def test_register_and_login(client):
    # Register
    res = client.post("/auth/register", json={
        "username": "testuser",
        "password": "secret"
    })
    assert res.status_code == 201

    # Login
    res = client.post("/auth/login", json={
        "username": "testuser",
        "password": "secret"
    })
    assert res.status_code == 200
    assert "token" in res.json
