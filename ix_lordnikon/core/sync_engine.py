"""
IX-LordNikon Sync Engine

Coordinates timestamped memory data with input/output event streams
to detect cognitive drift, overwrite threats, or shadow memory formations.
"""

from core.memory_map import MemoryMap
import hashlib

class SyncEngine:
    def __init__(self):
        self.memory_map = MemoryMap()
        self.hash_log = []

    def ingest_event(self, source: str, payload: str):
        self.memory_map.record(source, payload)
        snapshot = self._generate_snapshot(payload)
        self.hash_log.append(snapshot)
        return snapshot

    def _generate_snapshot(self, content: str) -> str:
        """
        Generate a content hash for drift detection and delta-tracking.
        """
        hasher = hashlib.sha256()
        hasher.update(content.encode("utf-8"))
        return hasher.hexdigest()

    def detect_drift(self) -> bool:
        """
        Compare recent snapshots for mutations or overwrite conditions.
        Returns True if anomaly is detected.
        """
        if len(self.hash_log) < 2:
            return False
        return self.hash_log[-1] != self.hash_log[-2]

    def recent_log(self, count: int = 3):
        return self.memory_map.fetch_recent(count)

# Example
if __name__ == "__main__":
    sync = SyncEngine()
    sync.ingest_event("IX-Joey", "User requested diagnostic dump.")
    sync.ingest_event("IX-Joey", "User requested diagnostic dump.")
    print("Drift detected:", sync.detect_drift())
    sync.ingest_event("IX-Gibson", "Memory overwrite triggered.")
    print("Drift detected:", sync.detect_drift())
    print("Recent:", sync.recent_log())
