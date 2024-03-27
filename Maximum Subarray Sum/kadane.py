def maxSubArrSum(arr):
    sum = 0
    ans = -1e9
    arr_range = []
    left = 0

    for i, n in enumerate(arr):
        sum += n
        #ans = max(ans, sum)
        if sum > ans:
            ans = sum
            arr_range = [left, i]
        if sum < 0:
            sum = 0
            left = i + 1

    return ans, arr_range

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
maximum_sub_array_sum, arr_range = maxSubArrSum(arr)
print(maximum_sub_array_sum)
print(f"The sub array is: {arr[arr_range[0] : arr_range[1]+1]}")
