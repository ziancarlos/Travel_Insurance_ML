import pandas as pd
from constants.prediction_constant import COLUMN_MAPPING
from flask import g
from models.prediction import Prediction

class PredictionRepository:
    def __init__(self, model, version):
        self.model = model
        self.version = version
        
    def make_predictions(self, data):
        df = pd.DataFrame([data])

        df.rename(columns=COLUMN_MAPPING, inplace=True)

        prediction = self.model.predict(df)[0]
        prediction_probability = self.model.predict_proba(df)[0][1]

        return  {
            "prediction": int(prediction),
            "probability": float(prediction_probability)
        }
        
    def save(self, data, predictions):
        prediction = Prediction(
            agency=data["agency"],
            agency_type=data["agency_type"],
            distribution_channel=data["distribution_channel"],
            product_name=data["product_name"],
            destination=data["destination"],

            duration=data["duration"],
            net_sales=data["net_sales"],
            commission=data["commission"],
            age=data["age"],

            is_refund=data["is_refund"],
            suspected_fraud=data["suspected_fraud"],

            commission_rate=data["commission_rate"],

            prediction_class=predictions["prediction"],
            prediction_probability=predictions["probability"],
            model_version=self.version
        )
        
        g.db.add(prediction)
        g.db.commit()
        g.db.refresh(prediction)
        
        return prediction
    
    def get_predictions(self):
        db = g.db

        return db.query(Prediction).all()