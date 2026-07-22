from flask import Flask, Blueprint
from config.load_env import get_env
from werkzeug.exceptions import (
    HTTPException
)
from middlewares.error_middleware import (
    handle_http_exception,
    validation_exception,
    ise_exception
)
from middlewares.db_middleware import (
    create_db_session,
    close_db_session
)
from middlewares.auth_middleware import validate_token
from pydantic import ValidationError
from repositories.prediction_repository import PredictionRepository
from services.prediction_service import PredictionService
from controllers.prediction_controller import PredictionController
from routers.prediction_router import PredictionRouter
import joblib

env = get_env()
API_PORT=int(env.getenv("API_PORT", 3000))
DEBUG_MODE = env.getenv("DEBUG", "True").lower() == "true"
MODEL_LOCATION = "ml_models/tuned_gradient_boost_v1.0.joblib"


app = Flask(__name__)
app.json.sort_keys = False

api_bp = Blueprint("api", __name__)

model = joblib.load(MODEL_LOCATION)
prediction_repository = PredictionRepository(model, "tuned_gradient_boost_v1.0")
prediction_service = PredictionService(prediction_repository)
prediction_controller = PredictionController(prediction_service)
prediction_router = PredictionRouter(prediction_controller)
prediction_bp = prediction_router.register()


app.before_request(
    validate_token
)
app.before_request(
    create_db_session
)
app.teardown_request(close_db_session)

api_bp.register_blueprint(
    prediction_bp,
    url_prefix="/predicts"
)
app.register_blueprint(
    api_bp,
    url_prefix="/api"
)


app.errorhandler(HTTPException)(handle_http_exception)
app.errorhandler(ValidationError)(validation_exception)
app.errorhandler(Exception)(ise_exception)

if __name__ == "__main__":
    
    app.run(
        host="0.0.0.0",
        port=API_PORT,
        debug=DEBUG_MODE,
    )