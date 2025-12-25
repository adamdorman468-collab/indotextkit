# IndoTextKit: Indonesian Text Preprocessing Library

![Tests](https://github.com/adamdorman468-collab/indotextkit/actions/workflows/testing.yml/badge.svg)
![License](https://img.shields.io/github/license/adamdorman468-collab/indotextkit)
![Python Versions](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue)

**IndoTextKit** is a lightweight and modular Python library for preprocessing and normalizing Indonesian text. It is designed to bridge the gap between formal Indonesian language tools and the noisy, slang-heavy text commonly found on social media platforms such as Twitter/X, Instagram, and WhatsApp.

---

## 🔥 Key Features

- **Slang Normalization**  
  Converts non-standard or colloquial words (e.g., *“yg”*, *“gk”*, *“baper”*) into formal Indonesian using a curated dictionary of **4,000+ entries**.

- **Noise Cleaning**  
  Efficiently removes URLs, mentions, hashtags, punctuation, and other noise elements typically found in real-world NLP datasets.

- **Modular Design**  
  Use only the components you need—such as the `TextCleaner` or the `TextNormalizer`.

- **Zero External Dependencies**  
  Built entirely using Python’s standard library. (`pytest` required only for development/testing)

---

## 📦 Installation

Clone the repository and install the package:

```bash
git clone https://github.com/adamdorman468-collab/indotextkit.git
cd indotextkit
pip install .
```

---

## 🚀 Quick Usage

### 1. Slang Normalization

```python
from indotextkit.normalizer import TextNormalizer

# Initialize the normalizer (auto-load dictionary)
normalizer = TextNormalizer()

text = "gws ya bro, ntar kita main lagi"
normalized_text = normalizer.normalize_sentence(text)

print(normalized_text)
# Output: "lekas sembuh ya bro, nanti kita main lagi"
```

---

### 2. Noise Cleaning

```python
from indotextkit.cleaner import TextCleaner

raw_text = "Promo gila!! Klik http://bit.ly/xyz @shopee_id #diskon"
clean_text = TextCleaner.clean_all(raw_text)

print(clean_text)
# Output: "Promo gila Klik diskon"
```

---

## 📚 Dataset Sources

This library incorporates:

- **Colloquial Indonesian Lexicon** (Salsabila et al., 2018)  
- Community-maintained dictionaries of slang, abbreviations, and modern neologisms

---

## 🧪 Running Tests

Before submitting a pull request or making changes, run the test suite:

```bash
pytest
```

---

## 🤝 Contributing

Contributions are welcome!  
If you'd like to add new slang mappings, improve normalization logic, or enhance documentation:

1. Fork the repo  
2. Create a feature branch  
3. Make your changes  
4. Submit a Pull Request  

Please ensure all tests pass before submitting.

---

## 📄 License

This project is licensed under the **MIT License** — see the full license text below.

```
MIT License

Copyright (c) 2025 Adam Dorman

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```