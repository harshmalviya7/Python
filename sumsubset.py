

def helper(nums,n,s,m):
    if s==0:
        return True
    if n==0:
        return False
    if m[n][s]!=-1:
        return m[n][s]
    if nums[n-1]>s:
        m[n][s] = helper(nums, n - 1, s, m)
        return m[n][s]
    else:
        m[n][s] = helper(nums, n - 1, s,m) or helper(nums, n - 1, s - nums[n - 1], m)
        return m[n][s]

nums=[1,2,3,7,8,10]
s=11
m=[[-1 for i in range(s+1)]for j in range(len(nums)+1)]
print(helper(nums,len(nums),s,m))