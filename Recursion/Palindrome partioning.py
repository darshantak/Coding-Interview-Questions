from operator import index


def partition(ind,s,out):
    if ind==len(s):
        ans.append(out.copy())
    for i in range(ind,len(s)):
        if s[ind:i+1]==s[ind:i+1][::-1]:
            print(s[ind:i+1])
            out.append(s[ind:i+1])
            partition(i+1,s,out)
            out.pop(-1)

ans=[]
partition(0,"aabb",[])
print(ans)