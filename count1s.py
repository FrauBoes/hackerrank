n = '524275'

# bn = str(bin(n))
# count = 0
# count2 = 0
#
# for c in bn[2:]:
#     if c == '1':
#         count += 1
#         if count > count2:
#             count2 = count
#     else:
#         count = 0
#
# print(max(count, count2))

# One-liner
print(len(max(bin(int(n))[2:].split("0"))))

