def getPerm(n,k):
    fact=1
    ans=""
    nums=[i for i in range(1,n+1)]
    n-=1
    while n>0:
        fact=fact*(n)
        n-=1
    k-=1
    # print(nums,fact)
    while True:
        ans+=str(nums[k//fact])
        nums.pop(k//fact)
        # print(ans)
        if len(nums)==0:
            break
        k=k%fact
        fact=fact//len(nums)
    return ans

print(getPerm(4,17))
