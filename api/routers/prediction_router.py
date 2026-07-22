from flask import Blueprint

class PredictionRouter:

    def __init__(self, controller):
        self.controller = controller


    def register(self):

        prediction_bp = Blueprint(
            "predictions",
            __name__
        )

        prediction_bp.add_url_rule(
            "/",
            view_func=self.controller.create_prediction,
            methods=["POST"]
        )

        prediction_bp.add_url_rule(
            "/",
            view_func=self.controller.get_predictions,
            methods=["GET"]
        )

        return prediction_bp