array=list(map(int,input().split()))
target=int(input())
hash_map={}
for i in range(len(array)):
    temp=target-array[i]
    hash_map[array[i]]=temp

for i,j in hash_map.items():
    if i==j:
        if array.count(i)>1:
            print(i,j)
    elif j in array:
        print(i,j)
        break
    else:
        print("Invalid")