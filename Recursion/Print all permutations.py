#approach 1
def printPerm1(arr,out,ans,freq):
    if len(out)==len(arr):
        ans.append(out.copy())
        return 
    for i in range(len(arr)):
        if freq[i]!=1:
            out.append(arr[i])
            freq[i]=1
            printPerm(arr,out,ans,freq)
            freq[i]=0
            out.pop(-1)

# ans=[]
# printPerm1([1,2,3],[],ans,[0,0,0])
# print(ans)

#approach 2
def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]

def printPerm2(ind,arr):
    if ind==len(arr):
        ans.append(arr.copy())
        return
    for i in range(ind,len(arr)):
        swap(arr,i,ind)
        printPerm2(ind+1,arr)
        swap(arr,i,ind)

ans=[]
printPerm2(0,[1,2,3])
print(ans)