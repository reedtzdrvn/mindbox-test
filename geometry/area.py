import math
from typing import Callable, Union
from scipy.integrate import quad

Number = Union[int, float]

def calculate_circle_area(radius: Number) -> float:
    """
    Calculate the area of a circle given its radius.

    :param radius: Radius of the circle. Must be > 0.
    :return: Area of the circle.
    :raises ValueError: If radius is not positive.
    """
    if radius <= 0:
        raise ValueError('Radius must be a positive number')
    
    return math.pi * radius ** 2

def calculate_triangle_area(a: Number, b: Number, c: Number) -> float:
    """
    Calculate the area of a triangle given its three sides using Heron's formula.

    :param a: Length of side a. Must be > 0.
    :param b: Length of side b. Must be > 0.
    :param c: Length of side c. Must be > 0.
    :return: Area of the triangle.
    :raises ValueError: If any side is non-positive or sides cannot form a triangle.
    """
    if any(side <= 0 for side in (a, b, c)):
        raise ValueError('All sides must be positive numbers')
    
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise ValueError('Cannot build a triangle with these sides')
    
    # Heron's formula
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def calculate_arbitrary_shape_area(
    func: Callable[[float], float],
    a: Number,
    b: Number,
    tolerance: float = 1e-6
) -> float:
    """
    Calculates the area under a given function between two limits.

    :param func: Function f(x) to integrate
    :param a: Lower limit of integration
    :param b: Upper limit of integration
    :param tolerance: Maximum acceptable integration error (default 1e-6)
    :return: Area under the curve
    :raises ValueError: If the integration fails, inputs are invalid, or error is too large
    """
    if a >= b:
        raise ValueError("The lower limit must be less than the upper limit.")
    
    if tolerance <= 0:
        raise ValueError("Tolerance must be a positive number.")
    
    try:
        result, error = quad(func, a, b)
    except Exception as e:
        raise ValueError(f"An error occurred during integration: {e}")

    if math.isnan(result) or math.isnan(error):
        raise ValueError("Integration returned NaN (Not a Number).")

    if error > tolerance:
        raise ValueError(f"Integration error is too large: {error:.2e} (tolerance: {tolerance:.2e})")

    return abs(result)
