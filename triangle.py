
import math


def is_valid_triangle(a, b, c) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        return False

    
    return (
        a + b > c
        and a + c > b
        and b + c > a
    )


def classify_triangle(a, b, c) -> str:
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    sides = sorted((a, b, c))

    if a == b == c:
        classification = "Equilateral"
    elif a == b or a == c or b == c:
        classification = "Isosceles"
    else:
        classification = "Scalene"

    
    is_right = math.isclose(
        sides[0] ** 2 + sides[1] ** 2,
        sides[2] ** 2,
        rel_tol=1e-9,
        abs_tol=1e-9,
    )

    if is_right:
        return f"Right {classification}"

    return classification
