# backend/oracle.py

import os
import requests

class OracleService:
    def __init__(self):
        # Read the endpoint and API key from env
        self.endpoint = os.getenv("ORACLE_ENDPOINT", "").strip()
        self.api_key = os.getenv("OPENAI_API_KEY", "").strip()

    def get_insights(self, prompt: str) -> dict:
        """
        Calls OpenAI’s Chat Completions API. Returns the JSON response.
        Expects:
          - ORACLE_ENDPOINT=https://api.openai.com/v1/chat/completions
          - OPENAI_API_KEY=<your-openai-key>
        """
        if not self.endpoint:
            return {"error": "Oracle endpoint not configured"}

        if not self.api_key:
            return {"error": "OpenAI API key not configured"}

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Construct payload for Chat Completions
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        try:
            response = requests.post(self.endpoint, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            # Return the error in JSON form
            return {"error": str(e), "status_code": getattr(e.response, "status_code", None)}
