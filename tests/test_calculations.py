import pytest
from app.src.binance_talker import BinancePostInfoConnector


@pytest.mark.parametrize(
    "precision,expected",
    [
        ("1.000000", 0),
        ("0.100000", 1),
        ("0.010000", 2),
        ("0.001000", 3),
        ("0.000100", 4),
        ("0.000010", 5),
        ("0.000001", 6),
    ]
)
def test_precision_calculation(precision: str, expected: int):
    assert BinancePostInfoConnector._convert_precision_to_integer(precision) == expected
