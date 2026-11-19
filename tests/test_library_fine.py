import pytest
from src.library_fine import calculate_fine


# 3.1 Req 1: fine is 50 cents per overdue day
@pytest.mark.parametrize(
    ("days_overdue", "expected_fine"),
    [(1, 50), (10, 500)],
)
def test_fine_is_50_cents_per_day(days_overdue, expected_fine):
    assert calculate_fine(days_overdue) == expected_fine


# 3.1 Req 2: zero overdue days -> zero fine
def test_fine_zero_days_is_zero():
    # Arrange
    days_overdue = 0

    # Act
    result = calculate_fine(days_overdue)

    # Assert
    assert result == 0


# 3.1 Req 2: no maximum fine
@pytest.mark.parametrize(
    ("days_overdue", "expected_fine"),
    [(11, 550), (100, 5000)],
)
def test_fine_has_no_maximum(days_overdue, expected_fine):
    assert calculate_fine(days_overdue) == expected_fine


# 3.1 Output: fine is returned as an int
def test_fine_returns_int():
    assert type(calculate_fine(3)) is int


# General Req 4: negative days -> ValueError
def test_fine_negative_days_raises_value_error():
    with pytest.raises(ValueError):
        calculate_fine(-1)


# General Req 3: non-int -> TypeError
@pytest.mark.parametrize("days_overdue", ["5", 2.5, None])
def test_fine_non_int_raises_type_error(days_overdue):
    with pytest.raises(TypeError):
        calculate_fine(days_overdue)


# General Req 2, 3: bool is not a valid int -> TypeError
@pytest.mark.parametrize("days_overdue", [True, False])
def test_fine_bool_raises_type_error(days_overdue):
    with pytest.raises(TypeError):
        calculate_fine(days_overdue)