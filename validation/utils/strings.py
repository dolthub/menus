def stringPassesLeadingTrailingSpaceCheck(s):
    if s == "":
        return False
    stripped = s.strip()
    return stripped == s

def stringIsUppercase(s):
    return s.upper() == s