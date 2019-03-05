import math
import os
import random
import re
import sys


# Complete the maxCircle function below.
def maxCircle(queries):
    circles = set(frozenset(queries[0]))
    output = [2]
    max_size = 2

    for pair in queries[1:]:

        for s in circles:

            if pair[0] in s or pair[1] in s:
                s.add(pair[1])
                s.add(pair[0])

                if len(s) > max_size:
                    max_size = len(s)

        circles.append(set(pair))

        print(circles)

        for x in range(0, len(circles)):
            c2 = circles[:x] + circles[x+1:]
            print(x, c2)

            for s2 in c2:

                if not circles[x].isdisjoint(s2):
                    circles[x] = circles[x].union(s2)

                    if len(circles[x]) > max_size:
                        max_size = len(circles[x])

        output.append(max_size)

    return output


print(maxCircle([[1, 2], [3, 4], [1, 3], [5, 7], [5, 6], [7, 4]]))
