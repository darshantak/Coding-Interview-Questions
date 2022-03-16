def subSum(ind,arr,out):
    ans.append(out.copy())
    for i in range(ind,len(arr)):
        if i>ind and arr[i]==arr[i-1]:
            continue
        out.append(arr[i])
        subSum(i+1,arr,out)
        out.pop(-1)
        
ans,out=[],[]
subSum(0,[1,2,2],out)
print(ans)