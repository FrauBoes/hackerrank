# Find max sum of all possible hourglasses in 2D-array
# Hourglass format = 3-1-3
# Int values <= 9 and >= -9


def maxHourglass(arr):

    max_sum = -63
    row_length = len(arr)
    col_length = len(arr[0])

    for i in range(row_length - 2):
        for j in range(col_length - 2):

            top = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]

            mid = arr[i + 1][j + 1]

            bottom = arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]

            hourglass = top + mid + bottom

        if hourglass > max_sum:
            max_sum = hourglass

    return max_sum


a = [[1,1,1,0,0,0], [0,1,0,0,0,0], [1,1,1,0,0,0], [0,0,2,4,4,0], [0,0,0,2,0,0], [0,0,1,2,4,0]]
print(maxHourglass(a))
