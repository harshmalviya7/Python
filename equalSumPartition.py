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


nums=[1,5,11,5]
sum=sum(nums)
if sum%2==0:

    m=[[-1 for j in range((sum//2)+1)]for i in range(len(nums)+1)]
    print(helper(nums,len(nums),sum//2,m))
else:
    print("No")