
def knapsack(W,wt,val,n):
    if n==0 or W==0:
        return 0

    if m[n][W]!=-1:
        return m[n][W]

    if wt[n-1]>W:
        m[n][W]=knapsack(W,wt,val,n-1)
        return m[n][W]
    else:
        m[n][W]=max(val[n-1]+knapsack(W-wt[n-1],wt,val,n-1),knapsack(W,wt,val,n-1))
        return m[n][W]






val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
m=[[-1 for i in range(W+1)] for j in range(n+1)]

print(knapsack(W,wt,val,n))  #220