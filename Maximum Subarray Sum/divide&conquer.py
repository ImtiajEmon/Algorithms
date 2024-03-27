def maxSubArrSum(arr):
    if len(arr) == 1:
        return arr[0]

    mid = len(arr)//2

    lss = maxSubArrSum(arr[:mid])
    rss = maxSubArrSum(arr[mid:])

    sum = 0
    left_sum, right_sum = -1e9, -1e9

    #for left sum
    for i in range(mid-1, -1, -1):
        sum += arr[i]
        left_sum = max(sum, left_sum)

    #for right sum
    sum = 0
    for i in range(mid, len(arr), 1):
        sum += arr[i]
        right_sum = max(sum, right_sum)

    return max(lss, rss, left_sum+right_sum)

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
maximum_sub_array_sum = maxSubArrSum(arr)
print(maximum_sub_array_sum)
#print(f"The sub array is: {arr[arr_range[0] : arr_range[1]+1]}")
