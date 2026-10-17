
import math

from triangle import is_valid_triangle, classify_triangle


def test_valid_triangle():
    assert is_valid_triangle(3, 4, 5) is True


def test_zero_or_negative_side_is_invalid():
    assert classify_triangle(0, 4, 5) == "Invalid"
    assert classify_triangle(-1, 4, 5) == "Invalid"


def test_degenerate_triangle_is_invalid():

    assert is_valid_triangle(1, 2, 3) is False
    assert classify_triangle(1, 2, 3) == "Invalid"


def test_equilateral_triangle():
    assert classify_triangle(4, 4, 4) == "Equilateral"


def test_isosceles_triangle():
    assert classify_triangle(5, 5, 6) == "Isosceles"


def test_scalene_triangle():
    assert classify_triangle(4, 5, 6) == "Scalene"


def test_right_scalene_triangle():
    assert classify_triangle(3, 4, 5) == "Right Scalene"


def test_right_isosceles_with_non_integer_side():
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"
