import pytest
from person import Person


def test_person_givenname():
    p = Person("John", "1234", 100.0)
    assert p.givenname == "John"
    p.givenname = "Jane"
    assert p.givenname == "Jane"


def test_person_password():
    p = Person("John", "1234", 100.0)
    assert p.password == "1234"
    p.password = "5678"
    assert p.password == "5678"


def test_person_balance():
    p = Person("John", "1234", 100.0)
    assert p.balance == 100.0
    p.balance = 200.0
    assert p.balance == 200.0


def test_person_balance_exception():
    p = Person("John", "1234", 100.0)
    with pytest.raises(ValueError):
        p.balance = "abc"
    assert p.balance == -1.0
