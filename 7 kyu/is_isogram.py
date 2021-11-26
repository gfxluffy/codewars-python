def is_isogram(string):
    rep = [c for c in string.lower() if string.lower().count(c)!=1]
    if rep:
        return False
    return True