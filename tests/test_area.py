import math
import pytest
from geometry import calculate_triangle_area, calculate_circle_area, calculate_arbitrary_shape_area

FLOAT_TOLERANCE: float = 1e-6

def test_circle_area_valid():
    # Arrange
    radius = 2.5
    expected = math.pi * radius ** 2

    # Act
    result = calculate_circle_area(radius)

    # Assert
    assert abs(result - expected) < 1e-6

def test_circle_area_invalid():
    # Arrange
    invalid_rads = [0, -1.0]

    for r in invalid_rads:
        # Act & Assert
        with pytest.raises(ValueError) as excinfo:
            calculate_circle_area(r)
        assert "radius must be a positive" in str(excinfo.value).lower()

def test_triangle_area_valid():
    # Arrange
    sides = (3, 4, 5)
    expected = 6.0

    # Act
    result = calculate_triangle_area(*sides)

    # Assert
    assert abs(result - expected) < 1e-6

def test_triangle_area_invalid():
    # Arrange
    bad_sides = [
        (1, 2, 3),
        (-1, 2, 2),
    ]

    for a, b, c in bad_sides:
        # Act & Assert
        with pytest.raises(ValueError) as excinfo:
            calculate_triangle_area(a, b, c)
        msg = str(excinfo.value).lower()
        assert "must be positive" in msg or "cannot build a triangle" in msg

def test_arbitrary_shape_area_basic():
    # Arrange
    # f(x) = 1
    func = lambda x: 1
    a, b = 0, 2
    expected = 2

    # Act
    result = calculate_arbitrary_shape_area(func, a, b)

    # Assert
    assert abs(result - expected) < 1e-6

def test_arbitrary_shape_area_invalid_limits():
    # Arrange
    func = lambda x: x
    a, b = 2, 1

    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        calculate_arbitrary_shape_area(func, a, b)
    assert "lower limit must be less" in str(excinfo.value).lower()

def test_arbitrary_shape_area_invalid_tolerance():
    # Arrange
    func = lambda x: x
    a, b = 0, 1
    bad_tolerances = [0, -1e-3]

    for tol in bad_tolerances:
        # Act & Assert
        with pytest.raises(ValueError) as excinfo:
            calculate_arbitrary_shape_area(func, a, b, tolerance=tol)
        assert "tolerance must be a positive number" in str(excinfo.value).lower()

def test_arbitrary_shape_area_nan(monkeypatch):
    # Arrange
    def fake_nan(func, a, b): return float('nan'), float('nan')
    monkeypatch.setattr('geometry.area.quad', fake_nan)
    # Act & Assert
    with pytest.raises(ValueError) as excinfo_nan:
        calculate_arbitrary_shape_area(lambda x: x, 0, 1)
    assert "returned nan" in str(excinfo_nan.value).lower()

def test_arbitrary_shape_area_integration_exception(monkeypatch):
    # Arrange
    def fake_exc(func, a, b): raise ZeroDivisionError("division by zero")
    monkeypatch.setattr('geometry.area.quad', fake_exc)

    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        calculate_arbitrary_shape_area(lambda x: x, 0, 1)
    assert "an error occurred during integration" in str(excinfo.value).lower()
