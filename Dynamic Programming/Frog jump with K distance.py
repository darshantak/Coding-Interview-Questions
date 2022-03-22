from random import randrange
import sys

n,k=map(int,input().split())
heights=list(map(int,input().split()))

dp=[-1 for i in range(n)]
def helper(ind,arr,k,dp):
    if ind==0:
        return 0
    if dp[ind]!=-1:
        return dp[ind]
    mmsteps=sys.maxsize
    for i in range(1,k+1):    
        if ind-i>=0:
            left = helper(ind-i,heights,k,dp)+abs(arr[ind]-arr[ind-i])
            mmsteps=min(mmsteps,left)
            dp[ind]=mmsteps
    # print(mmsteps)
    return dp[ind]

# print(helper(n-1,heights,k,dp))

#tabulation method
def helper1(n,k,arr,dp):
    dp[0]=0
    for i in range(1,len(arr)):
        mmsteps=sys.maxsize
        for j in range(1,k+1):
            if i-j>=0:
                left=dp[i-j]+abs(arr[i]-arr[i-j])
                mmsteps=min(left,mmsteps)
        dp[i]=mmsteps
    return dp[n]
print(helper1(n-1,k,heights,[0 for i in range(n)]))
