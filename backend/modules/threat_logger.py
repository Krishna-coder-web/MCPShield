import json
import os
import uuid
from datetime import datetime

class ThreatLogger:

    LOG_FILE = "logs/threat_logs.json"
    try:
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

            if not os.path.exists(self.LOG_FILE):

                with open(self.LOG_FILE, "w") as f:
                    json.dump([], f)

            try:
                with open(self.LOG_FILE, "r") as f:
                    logs = json.load(f)
            except Exception as e:
                print(f"Error reading log file: {e}")
                logs = []

            logs.append(log_entry)

            with open(self.LOG_FILE, "w") as f:
                json.dump(logs, f, indent=4)
    except Exception as e:
        print(f"Error in ThreatLogger: {e}")