import re

class TextCleaner:
    """
    A class responsible for removing noise from Indonesian text data.
    """

    @staticmethod
    def remove_url(text: str) -> str:
        """Removes URLs starting with http, https, or www."""
        return re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

    @staticmethod
    def remove_punctuation(text: str) -> str:
        """Removes special characters and punctuation."""
        return re.sub(r'[^\w\s]', '', text)

    @staticmethod
    def remove_digits(text: str) -> str:
        """Removes numeric digits from text."""
        return re.sub(r'\d+', '', text)

    @staticmethod
    def clean_all(text: str) -> str:
        """Applies all cleaning methods sequentially."""
        text = TextCleaner.remove_url(text)
        text = TextCleaner.remove_digits(text)
        text = TextCleaner.remove_punctuation(text)
        # Remove extra whitespace
        return re.sub(r'\s+', ' ', text).strip()