n = float(input())
lst = [int(x) for x in input().split()]

pos_fraction = 0
neg_fraction = 0
zero_fraction = 0

for i in lst:
    if i > 0:
        pos_fraction += 1
    elif i < 0:
        neg_fraction += 1
    else:
        zero_fraction += 1

print(format(pos_fraction/n, ".6f"))
print(format(neg_fraction/n, ".6f"))
print(format(zero_fraction/n, ".6f"))

