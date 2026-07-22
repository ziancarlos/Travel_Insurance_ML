from flask.views import MethodView
from flask import request


class PredictionController(MethodView):
    def __init__(self, service):
        self.service = service

    def create_prediction(self):
        data = request.get_json()

        results = self.service.create_prediction(data)

        return {
            "message": "Succcessfully Created A Predictions",
            "data": results
        }, 200


    def get_predictions(self):
        results = self.service.get_predictions()

        return {
            "message": "Successfully fetched predictions",
            "data": results
        }, 200