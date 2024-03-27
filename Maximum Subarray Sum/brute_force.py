def maxSubArrSum(arr):
    ans = 0
    arr_range = []

    for left in range(len(arr)):
        for right in range(left, len(arr)):
            sum = 0
            for i in range(left, right + 1):
                sum += arr[i]
            #ans = max(ans, sum)
            if sum > ans:
                ans = sum
                arr_range = [left, right]

    return ans, arr_range

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
maximum_sub_array_sum, arr_range = maxSubArrSum(arr)
print(maximum_sub_array_sum)
print(f"The sub array is: {arr[arr_range[0] : arr_range[1]+1]}")
