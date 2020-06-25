#Write an efficient program to find the sum of contiguous subarray 
# within a one-dimensional array of numbers which has the largest sum.

array=list(map(int,input().split()))
max_current=max_sofar=array[0]
for i in range(1,len(array)):
    max_current=max(array[i],max_current+array[i])
    if max_current>max_sofar:
        max_sofar=max_current
    # print(max_current,max_sofar)
print(max_sofar) 