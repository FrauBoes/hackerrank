def twoStrings(s1, s2):

    d = {}

    for c in s1:
        d[c] = 1

    for c in s2:
        if c in d:
            return "YES"
    return "NO"

print(twoStrings('hello', 'world'))