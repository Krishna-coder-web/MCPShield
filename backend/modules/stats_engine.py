import json
import os
from collections import Counter

class StatsEngine:

    def get_stats(self):

        logs_dir = "logs"

        stats = {
            "total_events": 0,
            "threats_detected": 0,
            "safe_prompts": 0,

            "blocked": 0,
            "reviewed": 0,
            "warnings": 0,
            "allowed": 0,

            "threat_types": {},
            "actions": {}
        }

        threat_counter = Counter()
        action_counter = Counter()

        if not os.path.exists(logs_dir):
            return stats

        for filename in os.listdir(logs_dir):

            if not filename.startswith("threat_logs_"):
                continue

            if not filename.endswith(".json"):
                continue

            file_path = os.path.join(
                logs_dir,
                filename
            )

            try:

                with open(file_path, "r") as f:
                    logs = json.load(f)

            except Exception:
                continue

            for event in logs:

                stats["total_events"] += 1

                if event.get("threat"):

                    stats["threats_detected"] += 1

                    threat_counter[
                        event.get(
                            "threat_type",
                            "UNKNOWN"
                        )
                    ] += 1

                else:

                    stats["safe_prompts"] += 1

                action= event.get(
                        "action",
                        "UNKNOWN"
                    )
                    
                action_counter[action]+=1
                
                if action =="BLOCK":
                    stats["blocked"] += 1
                elif action == "REVIEW":
                    stats["reviewed"] += 1
                elif action == "ALLOW_WITH_WARNING":
                    stats["warnings"] += 1
                elif action == "ALLOW":
                    stats["allowed"] += 1

        stats["threat_types"] = dict(
            threat_counter
        )

        stats["actions"] = dict(
            action_counter
        )

        return stats