from hello import add


def test_add():
    assert add(5.6, 4.7) == 10.3, "the numbers do not add up"
