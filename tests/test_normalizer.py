import pytest
import os
import json
from src.indotextkit.normalizer import TextNormalizer

# Kita buat dummy dictionary biar test jalan tanpa file asli
@pytest.fixture
def mock_dict_file(tmp_path):
    d = tmp_path / "slang_dict.json"
    content = {"gws": "lekas sembuh", "kpn": "kapan"}
    d.write_text(json.dumps(content))
    return str(d)

def test_normalization_basic(mock_dict_file):
    normalizer = TextNormalizer(dictionary_path=mock_dict_file)
    raw_text = "gws ya kpn main"
    expected = "lekas sembuh ya kapan main"
    assert normalizer.normalize_sentence(raw_text) == expected

def test_normalization_empty():
    # Test kalau dictionary path error, harusnya program handle gracefully?
    # Untuk MVP kita test logic aja dulu
    pass