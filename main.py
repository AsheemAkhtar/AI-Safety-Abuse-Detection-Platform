from mangum import Mangum
from fastapi import FastAPI, Request

from pydantic import BaseModel

from app.model_utils import predict_risk
from app.llm_utils import explain_risk
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    text: str
    threshold: float



@app.post("/analyze")
async def analyze(data: AnalyzeRequest):

    score = predict_risk(data.text)

    label = (
        "HARMFUL"
        if score > data.threshold
        else "SAFE"
    )

    explanation = ""

    if label == "HARMFUL":

        explanation = explain_risk(
            data.text,
            score
        )

    return {
        "risk_score": round(score, 4),
        "label": label,
        "threshold": data.threshold,
        "explanation": explanation
    }

handler = Mangum(app)