

def findanagrams(l):

    # create set to hold strings found that are anagrams
    res = set()

    # create map to hold strings with their sorted char sequence
    # key: sorted string, value original string
    m = dict()

    for s in l:

        if s in res:
            continue

        else:
            sSorted = "".join(sorted(s))

            if sSorted in m:
                res.add(m[sSorted])
                res.add(s)

            else:
                m[sSorted] = s

    return list(res)


l = ["car", "arc", "night", "right", "bark", "karb", "ignth"]
print(findanagrams(l))
