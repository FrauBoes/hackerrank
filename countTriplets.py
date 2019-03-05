def countTriplets(arr, r):
    arr.sort

    count = 0
    triplets = 0

    for x in range(0, len(arr)-2):
        if (count == 0 and arr[x] == 1) or (count == 0 and arr[x] % r == 0):
            count += 1

            for y in range(x+1, len(arr)-1):
                if arr[y] % r == 0 and arr[y] > arr[x]:
                    count += 1

                    for z in range(y+1, len(arr)):
                        if arr[z] % r == 0 and arr[z] > arr[y]:
                            count += 1

                        if count == 3:
                            triplets += 1
                            count = 1
                            break
            count = 0

    return triplets


print(countTriplets([1,2,2,4], 2))

