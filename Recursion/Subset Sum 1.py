def subSum(ind,arr,s,ans):
    if ind==len(arr):
        ans.append(s)
        return
    subSum(ind+1,arr,s+arr[ind],ans)
    subSum(ind+1,arr,s,ans)

ans=[]
subSum(0,[3,1,2],0,ans)
print(sorted(ans))