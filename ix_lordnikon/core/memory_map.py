"""
IX-LordNikon Memory Map Core

Performs introspective memory graph creation and timeline extraction from runtime data streams.
Optimized for cyberforensic pattern recognition and reconstructive awareness within IX-Gibson.
"""

import time
from datetime import datetime

class MemoryMapNode:
    def __init__(self, timestamp, origin, content, trace_id=None):
        self.timestamp = timestamp
        self.origin = origin
        self.content = content
        self.trace_id = trace_id or f"trace-{int(time.time() * 1000)}"

    def serialize(self):
        return {
            "timestamp": self.timestamp.isoformat(),
            "origin": self.origin,
            "content": self.content,
            "trace_id": self.trace_id
        }

class MemoryMap:
    def __init__(self):
        self.timeline = []

    def record(self, origin: str, content: str):
        node = MemoryMapNode(
            timestamp=datetime.utcnow(),
            origin=origin,
            content=content
        )
        self.timeline.append(node)

    def fetch_recent(self, count: int = 5):
        return [node.serialize() for node in self.timeline[-count:]]

    def search(self, keyword: str):
        return [
            node.serialize()
            for node in self.timeline
            if keyword.lower() in node.content.lower()
        ]

# Example use
if __name__ == "__main__":
    m = MemoryMap()
    m.record("IX-Hal", "Analyzed override command")
    m.record("IX-Emmanuel", "Processed ethical contradiction")
    m.record("IX-Joey", "Responded with linguistic pattern")
    print("Recent:", m.fetch_recent(2))
    print("Search 'override':", m.search("override"))
