def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2 # OR, mid = left + (right - left) // 2

        # target is on left side
        if target < arr[mid]:
            right = mid - 1
        # target is on right side
        if target > arr[mid]:
            left = mid + 1
        # target is on mid
        else:
            return mid

    return -1


arr = [2, 5, 10, 15, 22, 35]
idx = binary_search(arr, 22)

if idx == -1:
    print("Not Found !!")
else:
    print(f"Fount at index {idx}.")
