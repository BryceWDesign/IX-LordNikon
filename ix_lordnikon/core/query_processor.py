"""
IX-LordNikon Domain-Specific Query Processor

Handles queries related to cybersecurity, cryptography,
and secure communications.
"""

from security_knowledge import SecurityKnowledge

class IXLordNikonQueryProcessor:
    def __init__(self):
        self.knowledge = SecurityKnowledge()

    def process_query(self, query: str) -> str:
        query_lower = query.lower().strip()

        if query_lower.startswith("what is "):
            term = query_lower[8:].strip()
            return self.knowledge.get_fact(term)
        elif "define" in query_lower:
            term = query_lower.split("define")[-1].strip()
            return self.knowledge.get_fact(term)
        elif "explain" in query_lower:
            term = query_lower.split("explain")[-1].strip()
            return self.knowledge.get_fact(term)
        else:
            return (
                "I am IX-LordNikon, your cybersecurity and cryptography specialist. "
                "Ask me to define or explain any security-related concept."
            )

# Example usage
if __name__ == "__main__":
    processor = IXLordNikonQueryProcessor()
    print(processor.process_query("What is encryption?"))
    print(processor.process_query("Define firewall"))
    print(processor.process_query("Explain phishing"))
