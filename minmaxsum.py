arr = [1,2,3,4,5]

mini = maxi = s = arr[0]

for x in arr[1:]:
    if mini > x:
        mini = x
    elif maxi < x:
        maxi = x
    s += x

print(s - maxi, s - mini)

