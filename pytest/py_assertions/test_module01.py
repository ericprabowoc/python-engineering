
def test_a1():
    # assert 5 + 5 == 10
    # assert 5 - 5 == 0
    # assert 5 * 5 == 25
    # assert 5 / 5 == 1
    assert 4 <= 5
    assert 4 != 5

# this is a failed test
def test_a2():
    # assert 9/5 == 1.5, "failed test intentionally"
    assert 0

def test_a3():
    assert "abc" == 'abcd'

def test_a4():
    assert 3-1*4/2 == 1.0

def test_a5():
    assert 1 in divmod(9,5)
    assert 'py' in 'python'