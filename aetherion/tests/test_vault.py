import io

def get_token(client):
    client.post("/auth/register", json={"username": "a", "password": "a"})
    res = client.post("/auth/login", json={"username": "a", "password": "a"})
    return res.json["token"]

def test_file_upload_and_list(client):
    token = get_token(client)
    headers = {"Authorization": f"Bearer {token}"}
    data = {"file": (io.BytesIO(b"hello world"), "test.txt")}

    res = client.post("/vault/upload", headers=headers, content_type="multipart/form-data", data=data)
    assert res.status_code == 201
