import json
import os


class HistoryEngine:

    def get_history(self):

        history = []

        logs_dir = "logs"

        if not os.path.exists(logs_dir):
            return history

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

                history.extend(logs)

            except Exception:
                continue

        history.sort(
            key=lambda x: x.get(
                "timestamp",
                ""
            ),
            reverse=True
        )

        return history
    
    def get_recent(self, limit=10):

        history = self.get_history()

        return {
            "count": min(limit, len(history)),
            "events": history[:limit]
        }