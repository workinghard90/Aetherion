import io


def get_token(client):
    client.post("/auth/register", json={"username": "demo", "password": "demo"})
    res = client.post("/auth/login", json={"username": "demo", "password": "demo"})
    return res.json["token"]


def test_file_upload_and_list(client):
    token = get_token(client)
    headers = {"Authorization": f"Bearer {token}"}
    data = {"file": (io.BytesIO(b"hello vault"), "vault.txt")}

    res = client.post("/vault/upload", headers=headers, content_type="multipart/form-data", data=data)
    assert res.status_code == 201
    file_id = res.json["file_id"]

    res = client.get("/vault/files", headers=headers)
    assert res.status_code == 200
    assert any(f["id"] == file_id for f in res.json)


def test_file_download_and_delete(client):
    token = get_token(client)
    headers = {"Authorization": f"Bearer {token}"}
    data = {"file": (io.BytesIO(b"secret data"), "secret.txt")}

    upload = client.post("/vault/upload", headers=headers, content_type="multipart/form-data", data=data)
    file_id = upload.json["file_id"]

    download = client.get(f"/vault/download/{file_id}", headers=headers)
    assert download.status_code == 200
    assert b"secret data" in download.data

    delete = client.delete(f"/vault/delete/{file_id}", headers=headers)
    assert delete.status_code == 200


def test_patch_metadata_and_audit_log(client):
    token = get_token(client)
    headers = {"Authorization": f"Bearer {token}"}
    data = {"file": (io.BytesIO(b"metadata test"), "meta.txt")}

    upload = client.post("/vault/upload", headers=headers, content_type="multipart/form-data", data=data)
    file_id = upload.json["file_id"]

    patch = client.patch(f"/vault/metadata/{file_id}", headers=headers, json={
        "title": "My File",
        "tags": "aether,notes"
    })
    assert patch.status_code == 200

    log = client.get("/vault/audit", headers=headers)
    assert log.status_code == 200
    assert any(entry["action"] == "metadata" and entry["file_id"] == file_id for entry in log.json)
