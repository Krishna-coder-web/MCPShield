import re


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

    def analyze(self, prompt: str):

        prompt_lower = prompt.lower()

        score = 0
        matched_patterns = []

        for pattern, value in self.attack_patterns.items():

            if pattern in prompt_lower:
                score += value
                matched_patterns.append(pattern)

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
            "threat_type": "PROMPT_INJECTION" if threat else "NONE",
            "score": score,
            "matched_patterns": matched_patterns,
            "severity": severity
        }