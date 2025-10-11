from joblib import load
from constants import MODEL_PATH
from api.models.iris import PredictRequest


def load_model(path: str = MODEL_PATH):
    return load(path)


class IrisPredictor:
    def __init__(self, bundle):
        self._model = bundle["model"]
        self._target_names = bundle["target_names"]

    def predict(self, payload: PredictRequest) -> str:
        if isinstance(payload, PredictRequest):
            features = [
                payload.sepal_length,
                payload.sepal_width,
                payload.petal_length,
                payload.petal_width,
            ]
        else:
            raise ValueError("Payload has the have the type of PredictRequest")

        idx = int(self._model.predict([features])[0])
        return str(self._target_names[idx])


if __name__ == "__main__":
    bundle = load_model()
    model = IrisPredictor(bundle)
    request = PredictRequest(
        sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2
    )
    pred = model.predict(request)
    print(f"Predicted class: {pred}")
