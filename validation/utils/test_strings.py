from pytest import *
from strings import *

def test_leading_trailing_spaces():
    assert stringHasLeadingOrTrailingSpace("thisisvalid") == True