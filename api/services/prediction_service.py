from schemas.prediction_schema import CreatePredictionRequest
from repositories.prediction_repository import PredictionRepository


class PredictionService:
    def __init__(self, repository):
        self.repository = repository


    def create_prediction(self, data: dict):
        body = CreatePredictionRequest.model_validate(data)

        results = body.model_dump(
            mode="json",
            include={
                "agency",
                "agency_type",
                "distribution_channel",
                "product_name",
                "destination",
                "duration",
                "net_sales",
                "commission",
                "age",
                "is_refund",
                "suspected_fraud",
                "commission_rate",
            }
        )

        prediction = self.repository.make_predictions(results)
        prediction = self.repository.save(results, prediction)

        return {
            **results,
            "prediction": {
                "id": prediction.id,
                "class": prediction.prediction_class,
                "probability": prediction.prediction_probability
            }
        }
    
    def get_predictions(self):
        predictions = self.repository.get_predictions()

        return [
            {
                "id": prediction.id,
                "agency": prediction.agency,
                "agency_type": prediction.agency_type,
                "destination": prediction.destination,
                "prediction_class": prediction.prediction_class,
                "prediction_probability": prediction.prediction_probability
            }
            for prediction in predictions
        ]