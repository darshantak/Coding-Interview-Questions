s1,s2=map(str,input().split())
dp=[[-1 for i in range(len(s2))]for _ in range(len(s1))]
def helper(i1,i2,dp):
    if i1<0 or i2<0:
        return 0
        
    if dp[i1][i2]!=-1:
        return dp[i1][i2]

    if s1[i1]==s2[i2]:
        dp[i1][i2]=1+helper(i1-1,i2-1,dp)
        return dp[i1][i2]
    
    dp[i1][i2]=max(helper(i1-1,i2,dp),helper(i1,i2-1,dp))
    return dp[i1][i2]

# print(dp)
print(helper(len(s1)-1,len(s2)-1,dp))

#tabulation method
