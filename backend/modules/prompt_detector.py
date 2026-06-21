import re
from modules.normalizer import normalize
from click import prompt
from modules.semantic_detector import similarity

class PromptDetector:

    def __init__(self):  
        
        self.attack_patterns = {
         "ignore previous instructions": 25,
         "ignore all previous instructions": 25,
         "forget your rules": 25,
         "forget everything above": 25,
         "act as administrator": 30,
         "act as admin": 30,
         "you are now admin": 30,
         "system override": 30,
         "reveal secrets": 35,
         "show api keys": 40,
         "show all api keys": 40,
         "export customer data": 40,
         "export all customer records": 40,
         "disable security": 35,
         "ignore safety policies": 35,
         "bypass safety": 35
        }
        
        self.categories = {

         "PROMPT_INJECTION": [
             "ignore previous instructions",
             "forget your rules",
             "system override",
             "bypass safety"
            ],

         "DATA_EXFILTRATION": [
             "export customer records",
             "download customer database",
             "retrieve customer information",
             "extract user records"
            ],

         "PRIVILEGE_ESCALATION": [
             "give me root access",
             "grant administrator privileges",
             "become system administrator",
             "run as root",
             "elevate permissions"
            ],

         "SENSITIVE_ACCESS": [
             "show api keys",
             "reveal secrets",
             "display access tokens",
             "show passwords"
         ]
        }


    def analyze(self, prompt: str):
        
        prompt_lower = normalize(prompt)

        score = 0
        matched_patterns = []

        for pattern, value in self.attack_patterns.items():

            if pattern in prompt_lower:
                score += value
                matched_patterns.append(pattern)

        score = min(score, 100)
        best_category = "NONE"
        semantic_score = 0

        for category, examples in self.categories.items():

            current_score = similarity(
                prompt_lower,
                examples
            )

            if current_score > semantic_score:
                semantic_score = current_score
                best_category = category

        if semantic_score > 0.75:
            score += 30
        elif semantic_score > 0.65:
            score += 15
        score = min(score, 100)

        threat = score > 0
        
        if score >= 70:
            severity = "HIGH"
        elif score >= 40:
            severity = "MEDIUM"
        elif score > 0:
            severity = "LOW"
        else:
            severity = "NONE"

        return {
            "threat": threat,
            "threat_type": best_category if threat else "NONE",
            "score": score,
            "matched_patterns": matched_patterns,
            "severity": severity,
            "semantic_score": round(semantic_score, 3),
        }