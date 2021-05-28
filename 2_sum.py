#HASHING leetcode 1. Two Sum
#https://leetcode.com/problems/two-sum/

#return index of value which sums to a given no.
# [ 2, 7, 11, 15 ] , target=9
# return [0,1] as 2+7 gives 9

def two_sum(target,nums):
    hash_table={}

    for i in range(len(nums)):
        complement=target-nums[i]
        if complement not in hash_table:
            hash_table[nums[i]]=i
        else:
            return [hash_table[complement],i]

nums=[2,7,11,15]
target=9
print(two_sum(target,nums)) #[0, 1]