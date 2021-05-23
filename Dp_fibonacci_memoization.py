import time
import sys
sys.setrecursionlimit(1500)
memo={}
def fib_recurrsion(n,m={}):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        num=fib_recurrsion(n-1,m)+fib_recurrsion(n-2,m)

        return num
def fib_memoization(n,m={}):
    if n in memo:
        return memo[n]
    elif n==1 or n==0:
        return n

    else:
        num=fib_memoization(n-1,m)+fib_memoization(n-2,m)
    m[n]=num
    return num
# s=time.time()
# fib_recurrsion(1000,memo)
# print("Recursion time: ",time.time()-s)

s=time.time()
print(fib_memoization(3,memo))
print("Memoization: ",time.time()-s)