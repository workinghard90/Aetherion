import requests

class OracleService:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    def get_insights(self, prompt: str) -> dict:
        payload = {"prompt": prompt}
        response = requests.post(self.endpoint, json=payload)
        return response.json()
