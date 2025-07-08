import pytest
from .shapes import Square, Circle
from .utils import area_stats

def test_square_area():
    input_lengths = [1, 1.5, 5]
    expected_values = [1, 2.25, 25]

    for input, expected in zip(input_lengths, expected_values):
        assert Square(input).area() == pytest.approx(expected)