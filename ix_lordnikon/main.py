"""
IX-LordNikon CLI Tool

Allows direct terminal-based access to Nikon’s memory tracking,
drift detection, and cognitive sync functions.
"""

import sys
from core.sync_engine import SyncEngine

def main():
    engine = SyncEngine()

    while True:
        print("\n🧠 IX-LordNikon CLI")
        print("1. Ingest event")
        print("2. Check for memory drift")
        print("3. Show recent memory")
        print("4. Exit")

        choice = input("Select option: ").strip()

        if choice == "1":
            source = input("Enter source ID (e.g. IX-Joey): ")
            payload = input("Enter payload content: ")
            hashcode = engine.ingest_event(source, payload)
            print(f"[OK] Ingested with hash: {hashcode}")

        elif choice == "2":
            if engine.detect_drift():
                print("[ALERT] Memory drift detected!")
            else:
                print("[✓] No drift detected.")

        elif choice == "3":
            logs = engine.recent_log()
            for entry in logs:
                print(f"- [{entry['timestamp']}] {entry['origin']}: {entry['content']}")

        elif choice == "4":
            print("Exiting IX-LordNikon CLI.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
