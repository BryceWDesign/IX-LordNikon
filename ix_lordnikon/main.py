"""
IX-LordNikon CLI Entry Point

Enables terminal-based queries for cybersecurity and cryptography knowledge.
Outputs results directly to the command line.
"""

import sys
from core.query_processor import IXLordNikonQueryProcessor

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"Your cybersecurity question here\"")
        sys.exit(1)

    query = sys.argv[1]
    processor = IXLordNikonQueryProcessor()
    response = processor.process_query(query)

    print("\n🔐 IX-LordNikon Response 🔐")
    print(response)

if __name__ == "__main__":
    main()
