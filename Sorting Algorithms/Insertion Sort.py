def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        current = arr[i]
        while j >= 0 and arr[j] > current:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = current

arr = [13, 25, 0, -4, 7, -1, 18, 9, -6, 21]
insertion_sort(arr)
print(arr)
