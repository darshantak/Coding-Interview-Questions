# def lcs(x,y):
#     if not x or not y:
#         return ""
#     a,m,b,n=x[0],x[1:],y[0],y[1:]
#     print(x,y)
#     if a==b:
#         return a+lcs(m,n)
#     else:
#         return max(lcs(x,n),lcs(y,m),key=len)
# print(lcs('team','mtama'))
# n=int(input())
# a=list(map(int,input().split()))
# a.insert(0,0)
# i=1
# l=[]
# while a[i]!=0 or i!=len(a)-1:
#     # print(0)
#     if a[i]!=0:
#         temp=[]
#         node=a[a[i]]    
#         initial=a[i]
#         temp.append(i)
#         while node!=initial:
#             temp.append(a.index(node))
#             node=a[node]
#         temp.append(i)
#         for i in temp:
#             a[i]=0
#         l.append(temp)
#         # print(temp)
#     i+=1
#     # print(i,len(a))
#     if i==len(a):
#         break
# for i in l:
#     print(*i)
n = int(input())
arr = [0]
arr += list(map(int, input().split()))
i = 1
visited = []
seq = [[] for i in range(n)]
c = 0
for i in range(1,n+1):
    origin = i
    if i in visited:
        i += 1
    else:
        flag = 1
        while flag:
            seq[c].append(i)
            visited.append(i)
            i = arr[i]
            if i == origin:
                seq[c].append(i)
                c += 1
                flag = 0
        print(seq)
for i in range(0,c):
    for j in seq[i]:
        print(j, end=" ")
    print()
    