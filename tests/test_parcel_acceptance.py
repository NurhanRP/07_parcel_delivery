import pytest
from src.parcel_acceptance import is_parcel_accepted


@pytest.mark.parametrize("weight, length", [
    (1, 1),          # Lower boundaries
    (5000, 100),     # Nominal values
    (20000, 200),    # Upper boundaries (exposes bug)
])
def test_valid_parcel_dimensions_returns_true(weight, length):
    # Arrange
    weight_grams = weight
    length_cm = length

    # Act
    result = is_parcel_accepted(weight_grams, length_cm)

    # Assert
    assert result is True


@pytest.mark.parametrize("weight, length", [
    (0, 100),        # Zero weight boundary
    (5000, 0),       # Zero length boundary
    (20001, 100),    # Exceeds max weight
    (5000, 201),     # Exceeds max length
])
def test_outside_acceptance_limits_returns_false(weight, length):
    # Arrange
    weight_grams = weight
    length_cm = length

    # Act
    result = is_parcel_accepted(weight_grams, length_cm)

    # Assert
    assert result is False


@pytest.mark.parametrize("weight, length", [
    (-1, 100),       # Negative weight
    (5000, -1),      # Negative length
])
def test_negative_dimensions_raises_value_error(weight, length):
    # Arrange
    weight_grams = weight
    length_cm = length

    # Act and Assert
    with pytest.raises(ValueError):
        is_parcel_accepted(weight_grams, length_cm)


@pytest.mark.parametrize("weight, length", [
    ("500", 100),    # String weight
    (5000, 100.5),   # Float length
    (True, 100),     # Boolean weight
    (5000, False),   # Boolean length
])
def test_invalid_dimension_data_type_raises_type_error(weight, length):
    # Arrange
    weight_grams = weight
    length_cm = length

    # Act and Assert
    with pytest.raises(TypeError):
        is_parcel_accepted(weight_grams, length_cm)