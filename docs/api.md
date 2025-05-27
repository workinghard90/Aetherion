# AetherionAI Vault API

RESTful endpoints for encrypted memory and vault interaction.

---

## Auth Endpoints

### `POST /auth/register`

Registers a new user.

```json
{
  "username": "demo",
  "password": "demo123"
}

POST /auth/login

Returns a JWT token.

{
  "token": "<JWT>"
}

Use this token for all protected endpoints.

⸻

Vault Endpoints

POST /vault/upload

Upload an encrypted file.
	•	Method: POST
	•	Content-Type: multipart/form-data
	•	Field: file
	•	Header: Authorization: Bearer <token>

⸻

GET /vault/files

List all files for the authenticated user.
	•	Header: Authorization: Bearer <token>

Returns:

[
  {
    "id": 1,
    "name": "document.pdf",
    "type": "application/pdf",
    "size": 10240,
    "uploaded": "2024-01-01T12:00:00"
  }
]

GET /vault/download/<file_id>

Download and decrypt a file.
	•	Header: Authorization: Bearer <token>

Returns: file/octet-stream

⸻

DELETE /vault/delete/<file_id>

Delete a file from the vault.
	•	Header: Authorization: Bearer <token>

Returns:

{
  "message": "File deleted"
}

PATCH /vault/metadata/<file_id>

Update metadata for a file.
	•	Header: Authorization: Bearer <token>
	•	Content-Type: application/json

Example request:

{
  "title": "My Notes",
  "tags": "thoughts,private"
}

Returns:

{
  "message": "File metadata updated"
}

GET /vault/audit

View an audit log of user activity.
	•	Header: Authorization: Bearer <token>

Returns:

[
  {
    "action": "upload",
    "file_id": 2,
    "timestamp": "2024-01-01T12:01:00",
    "ip": "127.0.0.1"
  }
]

Error Format

All error responses follow:

{
  "error": "Message"
}

Authorization Header Format

For all protected endpoints:

Authorization: Bearer <your-token>

Replace <your-token> with the token received from /auth/login.
