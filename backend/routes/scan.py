from fastapi import APIRouter
from pydantic import BaseModel
from modules.risk_engine import RiskEngine
from modules.prompt_detector import PromptDetector
from modules.threat_logger import ThreatLogger

router = APIRouter()

detector = PromptDetector()
risk_engine = RiskEngine()
threat_logger = ThreatLogger()

class ScanRequest(BaseModel):
    prompt: str


@router.post("/scan")
def scan_prompt(data: ScanRequest):

    result = detector.analyze(data.prompt)

    decision = risk_engine.evaluate(result)

    result.update(decision)
    
    threat_logger.log_event(data.prompt, result)

    return result