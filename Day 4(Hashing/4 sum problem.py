array=list(map(int,input().split()))
X=int(input())
hash_map={}
for i in range(len(array)):
    for j in range(i+1,len(array)):
        hash_map[array[i]+array[j]]=[i,j]

flag=0
for i in range(len(array)):
    for j in range(i+1,len(array)):
        summ=array[i]+array[j]

        if X-summ in hash_map:
            temp=hash_map[X-summ]
            if temp[0]!=i and temp[0]!=j and temp[1]!=i and temp[1]!=j:
                flag=1
                print(array[i],array[j],array[temp[0]],array[temp[1]])   
    if flag:
        break