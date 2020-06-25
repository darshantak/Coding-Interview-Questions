array=list(map(int,input().split()))
X=0
hm,max_len,current_sum={},0,0
for i in range(len(array)):
    if array[i]==0 and max_len==0:
        max_len=1

    current_sum+=array[i]
    if current_sum==0:
        max_len=i+1
    
    if current_sum in hm:
        max_len=max(max_len,i-hm[current_sum])
    else:
        hm[current_sum]=i

print(max_len)
