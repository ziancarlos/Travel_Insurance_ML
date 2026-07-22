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
            "id": prediction.id,
            "prediction_class": prediction.prediction_class,
            "prediction_probability": prediction.prediction_probability,
            **results,
        }
    
    def get_predictions(self):
        predictions = self.repository.get_predictions()

        return [
            {
                "id": prediction.id,
                "prediction_class": prediction.prediction_class,
                "prediction_probability": prediction.prediction_probability,
                "agency": prediction.agency,
                "agency_type": prediction.agency_type,
                "distribution_channel": prediction.distribution_channel,
                "product_name": prediction.product_name,
                "destination": prediction.destination,
                "duration": prediction.duration,
                "net_sales": prediction.net_sales,
                "commission": prediction.commission,
                "age": prediction.age,
                "is_refund": prediction.is_refund,
                "suspected_fraud": prediction.suspected_fraud,
                "commission_rate": prediction.commission_rate,
                "model_version": prediction.model_version,
                "created_at": prediction.created_at,
            }
            for prediction in predictions
        ]