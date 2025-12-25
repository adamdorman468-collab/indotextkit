import os
import sys

# Ensure the 'src' directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from indotextkit.normalizer import TextNormalizer
from indotextkit.cleaner import TextCleaner

def main():
    print("=== INDOTEXTKIT RESEARCH DEMO ===")
    
    # 1. Initialize Normalizer (Automatically loads slang_dict.json)
    print("[*] Loading slang dictionary...")
    try:
        norm = TextNormalizer()
        print("    SUCCESS! Dictionary loaded.")
    except Exception as e:
        print(f"    FAILED: {e}")
        return

    # 2. Test Data (Raw social media text)
    test_sentences = [
        "gws ya gan, semoga bsk udh mendingan",
        "brg yg dijual sesuai ekspektasi bgt!! tks min",
        "aq gtau hrs ngomong apa lg sama u... ilfil bgt",
        "sy sdh transfer uangnya... cek ya sis @onlineshop"
    ]

    print("\n[*] Starting normalization process:\n")

    # 3. Processing Loop
    for i, raw_text in enumerate(test_sentences, 1):
        # Step A: Clean noise (punctuation, etc.)
        cleaned = TextCleaner.remove_punctuation(raw_text)
        
        # Step B: Normalize slang to formal Indonesian
        result = norm.normalize_sentence(cleaned)
        
        print(f"Case #{i}")
        print(f"Original : {raw_text}")
        print(f"Result   : {result}")
        print("-" * 50)

if __name__ == "__main__":
    main()