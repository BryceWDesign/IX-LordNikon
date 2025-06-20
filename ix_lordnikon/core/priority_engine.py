"""
IX-LordNikon Priority Engine

Assigns dynamic priority scores to tasks and goals based on current system state,
external inputs, and strategic importance.
"""

from typing import Dict, Any
import random
import threading

class PriorityEngine:
    def __init__(self):
        self.priorities: Dict[str, float] = {}
        self.lock = threading.Lock()

    def update_priority(self, task: str, factors: Dict[str, Any]):
        with self.lock:
            # Example heuristic combining random and input factors for demo purposes
            base_score = random.uniform(0, 1)
            importance = factors.get("importance", 1.0)
            urgency = factors.get("urgency", 1.0)
            score = base_score * importance * urgency
            self.priorities[task] = score

    def get_priority(self, task: str) -> float:
        with self.lock:
            return self.priorities.get(task, 0.0)

    def get_top_priority(self) -> str:
        with self.lock:
            if not self.priorities:
                return ""
            return max(self.priorities, key=self.priorities.get)

# Example usage
if __name__ == "__main__":
    engine = PriorityEngine()
    engine.update_priority("Expand knowledge base", {"importance": 1.5, "urgency": 1.2})
    engine.update_priority("Security upgrade", {"importance": 2.0, "urgency": 0.9})
    print(f"Top priority: {engine.get_top_priority()}")
