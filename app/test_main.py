from app.main import get_human_age

def test_should_return_zero_for_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]

def test_should_return_zero_for_first_14() -> None:
    assert get_human_age(14, 14) == [0, 0]

def test_should_return_one_human_year_after_first_15_years() -> None:
    assert get_human_age(15, 15) == [1, 1]

def test_should_return_one_human_years_after_23_years() -> None:
    assert get_human_age(23, 23) == [1, 1]

def test_should_return_two_human_years_after_24_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_cat_age_after_24_years_should_increase_every_4_years() -> None:
    assert get_human_age(28, 24) == [3, 2]


def test_dog_age_after_24_years_should_increase_every_5_years() -> None:
    assert get_human_age(24, 29) == [2, 3]

def test_cat_age_should_discard_remainder() -> None:
    assert get_human_age(27, 24) == [2, 2]

def test_dog_age_should_discard_remainder() -> None:
    assert get_human_age(24, 28) == [2, 2]