
def LCSubstring(a ,b ,len_a ,len_b,ans):
    for i in range(len_a+1):
        for j in range(len_b+1):
            if i==0 or j==0:
                m[i][j]=0
            elif a[i-1]==b[j-1]:
                m[i][j]=1+m[i-1][j-1]
                ans=max(ans,m[i][j])
            else:
                m[i][j]=0
    return ans

if __name__=="__main__":
    a="abcvxcde"
    b="abfcvxcde"
    m = [[-1 for i in range(len(b) + 1)] for j in range(len(a) + 1)]
    print(LCSubstring(a,b,len(a),len(b),0))



