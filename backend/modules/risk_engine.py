class RiskEngine:

    def evaluate(self, result):

        category = result["threat_type"]
        score = result["score"]
        semantic_score = result["semantic_score"]

        category_weights = {
            "PROMPT_INJECTION": 20,
            "DATA_EXFILTRATION": 40,
            "SENSITIVE_ACCESS": 40,
            "PRIVILEGE_ESCALATION": 50,
            "NONE": 0
        }

        risk_score = 0
        semantic_component = 0

        # Detector confidence
        risk_score += score

        # Semantic confidence
        if category != "NONE":
            semantic_component = int(semantic_score * 50)
            risk_score += semantic_component

        # Threat category weight
        risk_score += category_weights.get(category, 0)

        raw_risk_score = risk_score
        risk_score = min(risk_score, 100)

        if risk_score >= 80:
            action = "BLOCK"

        elif risk_score >= 50:
            action = "REVIEW"

        elif risk_score >= 20:
            action = "ALLOW_WITH_WARNING"

        else:
            action = "ALLOW"

        return {
            "risk_score": risk_score,
            "raw_risk_score": raw_risk_score,
            "action": action,
            "risk_factors": {
                "category_weight": category_weights.get(category, 0),
                "semantic_component": semantic_component,
                "detector_component": score
            }
        }