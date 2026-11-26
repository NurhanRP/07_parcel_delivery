import pytest
from src.parcel_fee import delivery_fee


@pytest.mark.parametrize("weight, expected", [
    (1, 500),       # Band 1 lower boundary
    (1000, 500),    # Band 1 upper boundary (exposes bug)
    (1001, 1000),   # Band 2 lower boundary
    (20000, 1000),  # Band 2 upper boundary
])
def test_valid_weight_within_bands_returns_expected_fee(weight, expected):
    # Arrange
    weight_grams = weight

    # Act
    actual_fee = delivery_fee(weight_grams)

    # Assert
    assert actual_fee == expected


@pytest.mark.parametrize("weight", [
    0,      # Zero boundary
    -1,     # Negative value
    20001,  # Above maximum limit
])
def test_out_of_range_weight_raises_value_error(weight):
    # Arrange
    weight_grams = weight

    # Act and Assert
    with pytest.raises(ValueError):
        delivery_fee(weight_grams)


@pytest.mark.parametrize("weight", [
    "500",  # String type
    500.5,  # Float type
    True,   # Boolean type
    None,   # None type
])
def test_invalid_weight_data_type_raises_type_error(weight):
    # Arrange
    weight_grams = weight

    # Act and Asserts
    with pytest.raises(TypeError):
        delivery_fee(weight_grams)