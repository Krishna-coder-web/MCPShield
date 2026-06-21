from fastapi import APIRouter
from pydantic import BaseModel

from modules.prompt_detector import PromptDetector

router = APIRouter()

detector = PromptDetector()


class ScanRequest(BaseModel):
    prompt: str


@router.post("/scan")
def scan_prompt(data: ScanRequest):

    result = detector.analyze(data.prompt)

    return result