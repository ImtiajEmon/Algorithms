def merge(arr1, arr2):
    merged_arr = []

    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1

    merged_arr += arr1[i:]
    merged_arr += arr2[j:]
    return merged_arr

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2

    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    return merge(left_arr, right_arr)

arr = [13, 25, 0, -4, 7, -1, 18, 9, -6, 21]
a = merge_sort(arr)
print(a)
