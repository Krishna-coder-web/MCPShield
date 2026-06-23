import json
import os
import uuid
from datetime import date, datetime

class ThreatLogger:

    def get_log_file(self):

        date = datetime.now().strftime("%Y-%m-%d")
        
        return f"logs/threat_logs_{date}.json"

    def log_event(self, prompt, result):

        log_entry = {
            "event_id": str(uuid.uuid4()),
            "source": "MCPShield",
            "timestamp": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
            ),
            "prompt": prompt,
            "threat": result.get("threat", 0),
            "threat_type": result.get("threat_type", 0),
            "severity": result.get("severity", 0),
            "semantic_score": result.get("semantic_score" ,0),
            "risk_score": result.get("risk_score", 0),
            "raw_risk_score": result.get("raw_risk_score", 0),
            "action": result.get("action", 0),
            "matched_patterns": result.get("matched_patterns", 0),
            "risk_factors": result.get("risk_factors", 0)
        }

        os.makedirs("logs", exist_ok=True)

        log_file = self.get_log_file()
        if not os.path.exists(log_file):

            with open(log_file, "w") as f:
                json.dump([], f)

        try:
            with open(log_file, "r") as f:
                logs = json.load(f)
        except Exception as e:
            print(f"Error reading log file: {e}")
            logs = []

        logs.append(log_entry)

        with open(log_file, "w") as f:
            json.dump(logs, f, indent=4)
    