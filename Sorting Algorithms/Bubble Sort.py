def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(1, len(arr) - i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]

arr = [13, 25, 0, -4, 7, -1, 18, 9, -6, 21]
bubble_sort(arr)
print(arr)
