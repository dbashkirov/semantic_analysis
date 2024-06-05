from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from src.model import Model

class InputData(BaseModel):
    text: str

app = FastAPI()
model = Model()


@app.get("/health")
def health():
    return {200: "running"}

@app.get("/predict")
def predict(input_data: InputData):
    res = model.predict(input_data.text)
    return res

