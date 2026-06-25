from modules.stats_engine import StatsEngine
from modules.history_engine import HistoryEngine


class DashboardEngine:

    def __init__(self):

        self.stats_engine = StatsEngine()
        self.history_engine = HistoryEngine()

    def get_dashboard(self):

        stats = self.stats_engine.get_stats()

        recent = self.history_engine.get_recent(
            limit=10
        )

        return {
            "product": "MCPShield",
            "version": "0.5",

            "summary": {
                "total_events":
                    stats["total_events"],

                "threats_detected":
                    stats["threats_detected"],

                "safe_prompts":
                    stats["safe_prompts"],

                "blocked":
                    stats["blocked"],

                "reviewed":
                    stats["reviewed"],

                "warnings":
                    stats["warnings"],

                "allowed":
                    stats["allowed"]
            },

            "threat_types":
                stats["threat_types"],

            "recent_activity":
                recent["events"]
        }