# Problem no. 128 leetcode
#https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        a = 0
        for i in nums:
            d[i] = 1

        for i in nums:

            if not d.get(i - 1, 0):
                curr = 1
                no = i
                while (d.get(no + 1, 0)):
                    curr += 1
                    no += 1
                a = max(a, curr)

        return a

ob=Solution()
print(ob.longestConsecutive([100,4,200,1,3,2]))