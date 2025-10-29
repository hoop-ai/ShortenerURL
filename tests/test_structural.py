import re

import pytest

from app import database, models, utils

ALLOWED_CHARACTERS_PATTERN = re.compile(r"^[a-zA-Z0-9]+$")


def test_generate_short_code_uses_url_safe_alphanumerics():
    code = utils.generate_short_code(length=8)
    assert len(code) == 8
    assert ALLOWED_CHARACTERS_PATTERN.match(code)


def test_generate_short_code_allows_length_override():
    code = utils.generate_short_code(length=12)
    assert len(code) == 12


def test_url_model_defaults_clicks_to_zero():
    session = database.SessionLocal()
    try:
        record = models.URL(original_url="https://example.org", short_code="ABC123")
        session.add(record)
        session.commit()
        session.refresh(record)
        assert record.clicks == 0
    finally:
        session.close()


@pytest.mark.parametrize("length", [4, 6, 12])
def test_generate_short_code_produces_variety(length: int):
    samples = {utils.generate_short_code(length=length) for _ in range(50)}
    # Even with randomness, duplicates across 50 samples of size 4 may happen.
    # Assert that we get a reasonable spread by expecting at least half of them to be unique.
    assert len(samples) >= 25
    for sample in samples:
        assert len(sample) == length
        assert ALLOWED_CHARACTERS_PATTERN.match(sample)
