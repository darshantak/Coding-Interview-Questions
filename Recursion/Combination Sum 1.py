ans=[]
def combSum(i,candidates,out,target,ans):
    if i==len(candidates):
        if target==0:
            print(*out)
            ans.append(out.copy())
            # print(ans)
        return
    if candidates[i]<=target:
        out.append(candidates[i])
        combSum(i,candidates,out,target-candidates[i],ans)
        out.pop(-1)
    combSum(i+1,candidates,out,target,ans)

combSum(0,[2,3,6,7],[],7,ans)
#the ans array is storing the reference of ds object.So, when ds changes in further recursions, 
#the referenced  values in ans array also changes. So, I did ans.append(ds.copy()).
#Storing a copy for ds array so that I don’t lose that particular combination.