import pytest

@pytest.mark.sanity
def test_str01():
    num = 9/4
    s1 = 'I like ' + 'pytest automation'
    assert str(num) == '2.25'
    assert s1 == 'I like pytest automation'
    assert s1 + str(num) == 'I like pytest automation2.25'

@pytest.mark.sanity
def test_str02():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert len(letters) == 24

def test_str03():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[0] == 'a'
    assert letters[-1] == 'z' == letters[25]

@pytest.mark.sanity
@pytest.mark.str
def test_strslice():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[:] == letters
    assert letters[10:] == 'klmnopqrstuvwxyz'
    assert letters[-3:] == 'xyz'
    assert letters[:21:5] == 'afkpu'

def test_strsplit():
    s1 = 'Python,Pytest and Automation'
    assert s1.split() == ['Python,Pytest', 'and', 'Automation']
    assert s1.split(',') == ['Python', 'Pytest and Automation']