arr = [4, 4, 9, 2, 3]

min_value = arr[0]
price = arr[0]

for i in arr[1:]:
    price += i - min(i, min_value)
    if i < min_value:
        min_value = i

print(price)