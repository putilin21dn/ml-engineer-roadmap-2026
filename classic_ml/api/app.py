from fastapi import Body, Depends, FastAPI

from api.schemas import PredictRequest, PredictResponse, ChurnFeatures
from scripts.predict import predict 
import uvicorn
import pandas as pd

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict", response_model=PredictResponse)
def predict_request(request: PredictRequest):
    rows = request.model_dump()["features"]
    X = pd.DataFrame(rows)
    predictions = predict(X).tolist()
    return PredictResponse(predictions=predictions)

def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()