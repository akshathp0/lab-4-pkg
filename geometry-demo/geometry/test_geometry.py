import pytest
import math
from .shapes import Square, Circle
from .utils import area_stats

def test_square_area():
    input_lengths = [1, 1.5, 5]
    expected_values = [1, 2.25, 25]

    for input, expected in zip(input_lengths, expected_values):
        assert Square(input).area() == pytest.approx(expected)

def test_circle_area():
    input_lengths = [1, 1.5, 5]
    expected_values = [math.pi * (1 ** 2),
                        math.pi * (1.5 ** 2), 
                        math.pi * (5 ** 2)
                        ]

    for input, expected in zip(input_lengths, expected_values):
        assert Circle(input).area() == pytest.approx(expected)

def test_square_negative_input():
    input_length = -1
    
    with pytest.raises(ValueError):
        Square(input_length)

def test_circle_negative_input():
    input_length = -1
    
    with pytest.raises(ValueError):
        Circle(input_length)

def test_square_nonnumber_input():
    input_length = "a"

    with pytest.raises(TypeError):
        Square(input_length)

def test_circle_nonnumber_input():
    input_length = "a"

    with pytest.raises(TypeError):
        Circle(input_length)

def test_stats_keys_and_values():
    
    square1 = Square(5)
    circle1 = Circle(5)

    assert isinstance(area_stats(square1, circle1), dict)

    for i in area_stats(square1, circle1).values():
        assert isinstance(i, (int, float))

def test_stats_raises_without_shapes():
    with pytest.raises(ValueError):
        area_stats()