n = int(input())
arr = []

for x in range(n):
    arr.append(input())

for x in arr:
    print(x[0:: 2] + ' ' + x[1:: 2])

