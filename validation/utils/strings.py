from utils.print import *
from static import *


def stringPassesLeadingTrailingSpaceCheck(s):
    if s == "":
        return False
    stripped = s.strip()
    return stripped == s

def stringIsUppercase(s):
    return s.upper() == s

def validateString(colName, value):
    if stringPassesLeadingTrailingSpaceCheck(value) is not True:
      printInvalidSpace(colName, value)
    if stringIsUppercase(value) is not True:
      printInvalidUppercase(colName, value)
    for char in invalid_chars:
      if char in value:
        printInvalidChar(colName, value, char)
