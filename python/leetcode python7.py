numbers = [1, 3, 5, 7, 9, 11]
target = 7

left = 0
right = len(numbers) - 1

while left <= right:
    middle = (left + right) // 2

    if numbers[middle] == target:
        print("Found at index:", middle)
        break
    elif numbers[middle] < target:
        left = middle + 1
    else:
        right = middle - 1