import math

def primality(n):
    if n < 2:
        return "Not prime"
    elif n <= 3:
        return "Prime"
    elif n % 2 == 0 or n % 3 == 0:
        return "Prime"

    for i in range(5, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return "Not prime"

    return "Prime"

print(primality(997))