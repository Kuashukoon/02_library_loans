import pytest
from src.library_eligibility import can_borrow


# 3.2 Req 1: under 5 loans and no overdue books -> True
@pytest.mark.parametrize(
    ("active_loans", "overdue_books"),
    [(0, 0), (4, 0)],
)
def test_can_borrow_when_under_limit_and_no_overdue(active_loans, overdue_books):
    assert can_borrow(active_loans, overdue_books) is True


# 3.2 Req 1, 2: exactly 5 loans -> False
def test_cannot_borrow_at_loan_limit():
    # Arrange
    active_loans, overdue_books = 5, 0

    # Act
    result = can_borrow(active_loans, overdue_books)

    # Assert
    assert result is False


# 3.2 Req 2: more than 5 loans -> False
def test_cannot_borrow_above_loan_limit():
    assert can_borrow(6, 0) is False


# 3.2 Req 1, 2: any overdue book -> False
def test_cannot_borrow_with_overdue_books():
    assert can_borrow(0, 1) is False


# 3.2 Req 2: at the limit AND overdue -> False
def test_cannot_borrow_when_both_conditions_fail():
    assert can_borrow(5, 1) is False


# 3.2 Output: result is a Python bool
@pytest.mark.parametrize(
    ("active_loans", "overdue_books"),
    [(0, 0), (5, 0)],
)
def test_can_borrow_returns_bool(active_loans, overdue_books):
    assert type(can_borrow(active_loans, overdue_books)) is bool


# General Req 4: negative active_loans -> ValueError
def test_active_loans_negative_raises_value_error():
    with pytest.raises(ValueError):
        can_borrow(-1, 0)


# General Req 4: negative overdue_books -> ValueError
def test_overdue_books_negative_raises_value_error():
    with pytest.raises(ValueError):
        can_borrow(0, -1)


# General Req 3: non-int active_loans -> TypeError
@pytest.mark.parametrize("active_loans", ["3", 2.5, None])
def test_active_loans_non_int_raises_type_error(active_loans):
    with pytest.raises(TypeError):
        can_borrow(active_loans, 0)


# General Req 3: non-int overdue_books -> TypeError
@pytest.mark.parametrize("overdue_books", ["1", 1.5, None])
def test_overdue_books_non_int_raises_type_error(overdue_books):
    with pytest.raises(TypeError):
        can_borrow(0, overdue_books)


# General Req 2, 3: bool active_loans -> TypeError
@pytest.mark.parametrize("active_loans", [True, False])
def test_active_loans_bool_raises_type_error(active_loans):
    with pytest.raises(TypeError):
        can_borrow(active_loans, 0)


# General Req 2, 3: bool overdue_books -> TypeError
@pytest.mark.parametrize("overdue_books", [True, False])
def test_overdue_books_bool_raises_type_error(overdue_books):
    with pytest.raises(TypeError):
        can_borrow(0, overdue_books)