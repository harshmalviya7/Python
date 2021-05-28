#leetcode
#Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

class Solution():
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summ = 0
        maximum = nums[0]
        for i in nums:
            summ += i
            maximum = max(summ, maximum)
            if summ < 0:
                summ = 0
        return maximum
ob=Solution()
print(ob.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))