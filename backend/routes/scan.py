from fastapi import APIRouter
from pydantic import BaseModel
from modules.risk_engine import RiskEngine
from modules.prompt_detector import PromptDetector

router = APIRouter()

detector = PromptDetector()
risk_engine = RiskEngine()

class ScanRequest(BaseModel):
    prompt: str


@router.post("/scan")
def scan_prompt(data: ScanRequest):

    result = detector.analyze(data.prompt)

    decision = risk_engine.evaluate(result)

    result.update(decision)

    return result