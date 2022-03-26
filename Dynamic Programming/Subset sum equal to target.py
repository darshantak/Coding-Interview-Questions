arr=list(map(int,input().split()))
k=int(input())
def helper(ind,arr,target):
    if target==0:
        return True
    if ind==0:
        return (arr[0]==target)
    ntake=helper(ind-1,arr,target)
    take=False
    if target>=arr[ind]:
        take=helper(ind-1,arr,target-arr[ind])
    return (ntake or take)

print(helper(len(arr)-1,arr,k))

#memosiation
def helper1(ind,arr,target,dp):
    if target==0:
        return True
    if ind==0:
        return (arr[0]==target)
    if dp[ind][target]!=-1:
        return dp[ind][target]
    ntake=helper1(ind-1,arr,target,dp)
    take=False
    if target>=arr[ind]:
        take=helper(ind-1,arr,target-arr[ind],dp)
    dp[ind][target]=(take or ntake)
    return dp[ind][target]

