# test palindromish with pytest

from palindromish import palindromish

def test_nastaran_three():
    assert palindromish("nastaran", 3) == True
