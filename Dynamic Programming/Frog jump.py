from os import curdir
import sys
from turtle import left

n=int(input())
heights=list(map(int,input().split()))
dp=[-1 for i in range(n)]
def helper(n,arr,dp):
    if n==0:
        # print()
        return 0
    if dp[n]!=-1:
        return dp[n]

    left=helper(n-1,arr,dp)+abs(arr[n]-arr[n-1]) #when n=1 helper(0)+(arr[1]-arr[0]) 
    right = sys.maxsize
    if n>1:
        right=helper(n-2,arr,dp)+abs(arr[n]-arr[n-2]) #when n=2 helper(0)+(arr[2]-arr[0])
    
    dp[n]=min(left,right)
    return dp[n]

# print(helper(n-1,heights,dp))

#tabulation method
def helper1(n,arr,dp):
    if n==0:
        dp[n]=0
    for i in range(1,len(arr)):
        left=dp[i-1]+abs(arr[i-1]-arr[i])
        right=sys.maxsize
        if i>1:
            right=dp[i-2]+abs(arr[i-2]-arr[i])
        dp[i]=min(left,right)
        
    print(dp)
    return dp[n]
print(helper1(n-1,heights,[0 for i in range(n)]))

#space optimisation
def helper2(n,arr):
    prev1,prev2=0,0
    for i in range(1,len(arr)):
        left=prev1+abs(arr[i-1]-arr[i])
        right=sys.maxsize
        if i>1:
            right=prev2+abs(arr[i-2]-arr[i])
        curri=min(left,right)
        prev2=prev1
        prev1=curri
    return curri

# (helper2(n-1,heights))