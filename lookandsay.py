
# # Look and Say
# To generate a member of the sequence from the previous member, read off the digits of the previous member, counting the number of digits in groups of the same digit. For example:
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# 1211 is read off as "one 1, one 2, then two 1s" or 111221.
# 111221 is read off as "three 1s, two 2s, then one 1" or 312211.
#
# Problem:
#         Given some integer n. Determine the nth term in the "look and say" sequence.
#
#         example:
#             for n=4, the 4th term in the sequence is 1211.

def num(n):
    if n==1:
        return 1
    if n==2:
        return 11
    s="11"
    for j in range(n-2):
        count=1
        s+="$"
        temp=""
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                count+=1
            else:
                temp=temp+str(count)+s[i]
                count=1
        s=temp


    return temp
s="1"
n=4 #term
print(num(n))