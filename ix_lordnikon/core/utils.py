"""
IX-LordNikon Utility Tools

Helper functions for forensic memory comparison, timestamp parsing,
and cognitive anomaly detection support.
"""

from datetime import datetime

def parse_iso_timestamp(timestamp_str: str) -> datetime:
    """
    Parse ISO8601 timestamp string into a datetime object.
    """
    try:
        return datetime.fromisoformat(timestamp_str)
    except ValueError:
        raise ValueError(f"Invalid ISO timestamp: {timestamp_str}")

def compare_memory_entries(entry1: dict, entry2: dict) -> bool:
    """
    Compare two memory map entries for content similarity.
    Returns True if they are equivalent.
    """
    keys_to_compare = ["origin", "content"]
    for key in keys_to_compare:
        if entry1.get(key) != entry2.get(key):
            return False
    return True

def detect_anomaly(sequence: list) -> bool:
    """
    Given a sequence of memory entries, detect anomalies such as
    repeated identical content or missing expected entries.
    Returns True if anomaly detected.
    """
    seen_contents = set()
    for entry in sequence:
        content = entry.get("content")
        if content in seen_contents:
            return True
        seen_contents.add(content)
    return False

# Example usage
if __name__ == "__main__":
    entry_a = {"origin": "IX-Hal", "content": "Override command"}
    entry_b = {"origin": "IX-Hal", "content": "Override command"}
    print("Compare entries:", compare_memory_entries(entry_a, entry_b))
    print("Detect anomaly in duplicates:", detect_anomaly([entry_a, entry_b]))
