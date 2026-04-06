from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import numpy as np

# Initialize FastAPI App
app = FastAPI(
    title="FraudGuard AI Engine API",
    description="Backend API for Credit Card Fraud Detection",
    version="1.0.0"
)

# Define the data validation model using Pydantic
class TransactionData(BaseModel):
    amount: float
    time: float
    v1: float
    v2: float
    features: dict[str, float] = {}

class PredictionResponse(BaseModel):
    is_fraud: bool
    risk_score: float

@app.get("/")
def read_root():
    return {"status": "FastAPI Backend is fully operational!"}

@app.post("/predict", response_model=PredictionResponse)
def predict_fraud(transaction: TransactionData):
    try:
        # TODO: Once your ML model is ready, load it here
        # import joblib
        # model = joblib.load("random_forest.pkl")
        # prediction = model.predict([[transaction.v1, transaction.v2, ...]])

        # MOCK ML LOGIC temporarily replicating what we had in Streamlit
        amount = transaction.amount
        v1 = transaction.v1
        
        is_fraud = bool(amount > 1000 or v1 > 1.5)
        
        if is_fraud:
            risk_score = float(np.random.uniform(85.0, 99.9))
        else:
            risk_score = float(np.random.uniform(0.1, 15.0))
            
        return PredictionResponse(
            is_fraud=is_fraud, 
            risk_score=risk_score
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    # Runs the server locally on port 8000
    uvicorn.run("backend:app", host="0.0.0.0", port=8000, reload=True)
