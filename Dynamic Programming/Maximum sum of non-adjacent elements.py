nums=list(map(int,input().split()))
def helper(ind,arr):
    if ind==0:
        return arr[0]
    if ind<0:
        return 0
    pick=arr[ind]+helper(ind-2,arr)
    npick=0+helper(ind-1,arr)
    return max(pick,npick)

# print(helper(len(nums)-1,nums))

#memoisation
def helper1(ind,arr,dp):
    if ind==0:
        return arr[0]
    if ind<0:
        return 0
    pick=arr[ind]+helper1(ind-2,arr,dp)
    npick=0+helper1(ind-1,arr,dp)
    dp[ind]=max(pick,npick)
    return dp[ind]

# print(helper1(len(nums)-1,nums,[-1 for i in range(len(nums))]))

def helper2(arr,dp):
    dp[0]=arr[0]
    prev1,prev2=arr[0],0
    for i in range(1,len(arr)):
        pick=arr[i]
        if i>1:
            pick+=dp[i-2]
            #pick+=prev2
        npick=0+dp[i-1]
        # npick=0+prev1
        # curri=max(pick,npick)
        # prev2=prev1
        # prev1=curri

        dp[i]=max(pick,npick)
        #space optimisation
    # retrun prev1
    return dp[len(nums)-1]

print(helper2(nums,[0 for i in range(len(nums))]))


