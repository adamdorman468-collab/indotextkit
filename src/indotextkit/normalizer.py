import json
import os
from typing import Dict

class TextNormalizer:
    """
    A class to normalize non-standard Indonesian words (slang) into formal Indonesian.
    """

    def __init__(self, dictionary_path: str = None):
        if dictionary_path is None:
            # Otomatis cari di folder data root
            base_path = os.path.dirname(os.path.abspath(__file__))
            dictionary_path = os.path.join(base_path, '../../data/slang_dict.json')
        
        self.slang_dict = self._load_dictionary(dictionary_path)

    def _load_dictionary(self, path: str) -> Dict[str, str]:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Dictionary file not found at {path}")

    def normalize_sentence(self, text: str) -> str:
        """
        Replaces slang words with their formal counterparts.
        """
        if not text:
            return ""
            
        words = text.split()
        # Look up word in dictionary, return original word if not found
        normalized_words = [self.slang_dict.get(word.lower(), word) for word in words]
        return ' '.join(normalized_words)