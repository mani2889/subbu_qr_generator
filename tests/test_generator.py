import os
from qr_generator.generator import generate_qr


def test_generate_qr(tmp_path):
    file_path = tmp_path / "test_qr.png"
    result = generate_qr("https://example.com", file_path)

    assert os.path.exists(result)
    assert result.stat().st_size > 0
