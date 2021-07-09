from pytest import *
from strings import *

def test_leading_trailing_spaces():
    assert stringPassesLeadingTrailingSpaceCheck("thisisvalid") == True