ans=[]
def combSum(ind,arr,target,out):
    if target==0:
        # print(out)
        ans.append(out.copy())
        return
    for i in range(ind,len(arr)):
        if i>ind and arr[i]==arr[i-1]:
            continue
        if arr[i]>target:
            break
        out.append(arr[i])
        combSum(i+1,arr,target-arr[i],out)
        out.pop(-1)

out=[]
combSum(0,[1,1,1,2,2],4,out) 
print(ans)
# ans=[]
# def backtrack(nums,targetLeft,path):
        
#     if targetLeft==0:
#         ans.append(path.copy())
#         return
    
#     for i in range(len(nums)):
#         if i>0 and nums[i]==nums[i-1]:
#             continue
#         if nums[i]>targetLeft:
#             break
#         backtrack(nums[i+1:],targetLeft-nums[i],path+[nums[i]])    
    
# res=[]
# backtrack(sorted([1,1,1,2,2]),4,[])
# print(ans)