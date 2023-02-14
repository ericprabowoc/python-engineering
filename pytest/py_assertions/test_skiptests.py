import sys
import pytest
pytestmark = pytest.mark.skipif(sys.platform != 'darwin', reason="will run only on Darwin")

const = 9/5
def cent_to_fah(cent=0):
    fah = (cent * const) + 32
    return fah

print(cent_to_fah(38))

@pytest.mark.skip(reason="Skipping for no reason specified")
def test_case01():
    assert type(const) == float

# @pytest.mark.skipif(sys.version_info > (3,6), reason="does not work on py version above 3.6")
@pytest.mark.skipif(cent_to_fah() == 32, reason="default value test, so skipping")
def test_case02():
    assert cent_to_fah() == 32

def test_case02b():
    import sys

    assert sys.version_info > (3,6,1)

@pytest.mark.skipif(pytest.__version__ < '7.3.1', reason='pytest version is less')
def test_case03():
    assert cent_to_fah(38) == 100.4