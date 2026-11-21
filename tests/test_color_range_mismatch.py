import pytest
import math
from media import color_range_mismatch as mod

CASES = [
    ("range", 'm.read_range("") == "limited"'),
    ("matrix_hd", 'm.matrix_for(1080, "bt709") == "bt709"'),
    ("matrix_sd", 'm.matrix_for(480, "bt709") == "bt601"'),
    ("up", 'm.upsample("nearest") == "bilinear"'),
    ("bits", 'm.bitdepth(10) == 10'),
    ("once", 'm.once(1) is True'),
    ("hdr", 'm.hdr_range("pq") == "full"'),
    ("subtitle", 'm.subtitle_after(True) is True'),
    ("thumb", 'm.thumbnail(True) is True'),
    ("tag", 'm.write_tag("limited") == "limited"'),
    ("order", 'm.order(True) is True'),
    ("clamp", 'm.clamp_code(300, 16, 235) == 235'),
    ("name", 'm.matrix_name("bt2020") == "bt2020"'),
    ("span", 'm.span(True) == (16, 235)'),
    ("full", 'm.is_full("full") is True')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
