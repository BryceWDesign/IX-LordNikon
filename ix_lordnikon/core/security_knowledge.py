"""
IX-LordNikon Core Cybersecurity and Cryptography Knowledge Module

Contains essential definitions and concepts related to cybersecurity,
cryptography, secure communications, and privacy technologies.

Part of the IX-Gibson sibling AI network.
"""

class SecurityKnowledge:
    def __init__(self):
        self.facts = {
            "encryption": "The process of encoding information to prevent unauthorized access.",
            "public key cryptography": "A cryptographic system that uses pairs of keys: public keys which may be disseminated widely, and private keys which are known only to the owner.",
            "symmetric key": "A type of encryption where the same key is used for both encryption and decryption.",
            "asymmetric key": "An encryption system that uses a pair of keys, one public and one private.",
            "hash function": "A function that converts an input into a fixed-size string of bytes, typically for security or data integrity verification.",
            "digital signature": "A mathematical scheme for verifying the authenticity of digital messages or documents.",
            "firewall": "A network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules.",
            "phishing": "A fraudulent attempt to obtain sensitive information by disguising oneself as a trustworthy entity in electronic communication."
        }

    def get_fact(self, term: str) -> str:
        term_lower = term.lower().strip()
        return self.facts.get(term_lower, f"Sorry, I don't yet have information on '{term}'.")

# Example test
if __name__ == "__main__":
    sk = SecurityKnowledge()
    print(sk.get_fact("Encryption"))
    print(sk.get_fact("Digital Signature"))
    print(sk.get_fact("Zero trust"))
