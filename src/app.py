from fastapi import FastAPI
from inference import load_model, IrisPredictor
from api.models.iris import PredictResponse, PredictRequest

app = FastAPI()
_model = IrisPredictor(load_model())


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    pred = _model.predict(request)
    return PredictResponse(prediction=pred)
