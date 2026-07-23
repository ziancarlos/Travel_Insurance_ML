import requests

class PredictionService:

    def __init__(self, base_url: str, auth_token: str):
        self.base_url = base_url
        self.auth_token = auth_token

    def create_prediction(self, payload: dict):
        response = requests.post(
            f"{self.base_url}/predicts",
            json=payload,
            headers={
                "Authorization": self.auth_token
            },
            timeout=30,
        )

        return response.status_code, response.json()

    def get_predictions(self):
        response = requests.get(
            f"{self.base_url}/predicts",
            headers={
                "Authorization": self.auth_token
            },
            timeout=30,
        )

        return response.status_code, response.json()