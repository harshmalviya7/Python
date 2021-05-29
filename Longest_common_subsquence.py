def LCS_recurrsion(a,b,i,j):

    if i==0 or j==0:
        return 0

    elif a[i-1]==b[j-1]:
        return 1+LCS_memoization(a,b,i-1,j-1)
    else:
        return max(LCS_memoization(a,b,i-1,j),LCS_memoization(a,b,i,j-1))


def LCS_memoization(a,b,i,j):

    if i==0 or j==0:
        return 0
    elif m[i][j]!=-1:
        return m[i][j]
    elif a[i-1]==b[j-1]:
        m[i][j]=1+LCS_memoization(a,b,i-1,j-1)
        return m[i][j]
    else:
        m[i][j]=max(LCS_memoization(a,b,i-1,j),LCS_memoization(a,b,i,j-1))
        return m[i][j]

if __name__=="__main__":
    a="bd"
    b="abcd"
    m = [[-1 for i in range(len(b) + 1)] for j in range(len(a) + 1)]
    print(LCS_memoization(a,b,len(a),len(b)))

    m = [[-1 for i in range(len(b) + 1)] for j in range(len(a) + 1)]
    print(LCS_recurrsion(a,b,len(a),len(b)))