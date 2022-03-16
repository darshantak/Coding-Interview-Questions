#print all the subsequences in an array
def solve():
    out=[]
    def subsequence(i,arr,out,a):
        if i==len(arr):
            a.append(out)
            print(a)
            # print(*out)
            return
        out.append(arr[i])
        subsequence(i+1,arr,out,a) #Take
        out.pop(-1)
        subsequence(i+1,arr,out,a) #Not Take
    subsequence(0,[3,1,2],out,[])
    # print(a)

solve()

# print(ans)
#print all the subsequence whose sum is equal to k
def sumSub(i,arr,out,s,k):
    if i==len(arr):
        if s==k:
            print(out)
        return 
    # print(s,i,len(arr))
    out.append(arr[i])
    s+=arr[i]
    sumSub(i+1,arr,out,s,k)
    out.pop(-1)
    s-=arr[i]
    sumSub(i+1,arr,out,s,k)
out=[]
# sumSub(0,[1,2,1],out,0,2)


#print any 1 subsequence whose sum is equal to k
def sumSub(i,arr,out,s,k):
    if i==len(arr):
        if s==k:
            print(out)
            return True
        return False
    out.append(arr[i])
    s+=arr[i]
    if sumSub(i+1,arr,out,s,k)==True:
        return True
    out.pop(-1)
    s-=arr[i]
    if sumSub(i+1,arr,out,s,k)==True:
        return True
    return False


i,s,k,out=0,0,5,[]
# sumSub(i,[1,2,1],out,s,k)

#count the subsequences whose sum is k
def countSub(i,arr,s,k):
    if i==len(arr):
        if s==k:
            return 1
        return 0
    s+=arr[i]
    l=countSub(i+1,arr,s,k)
    s-=arr[i]
    r=countSub(i+1,arr,s,k)
    return l+r
s,k=0,2
# print(countSub(i,[1,2,1],s,k))
    