# Largest subarray with 0 sum
# https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1
def maxLen(n, arr):
    # Code here

    d = {}
    summ = 0
    count = 0
    for i in range(len(arr)):

        summ += arr[i]
        if arr[i] == 0 and count == 0:
            count = 1
        if summ == 0:
            count = i + 1
        if summ in d:
            count = max(count, i - d[summ])

        else:
            d[summ] = i

    return count

arr=[15,-2,2,-8,1,7,10,23]
n=len(arr)

print(maxLen(n, arr))