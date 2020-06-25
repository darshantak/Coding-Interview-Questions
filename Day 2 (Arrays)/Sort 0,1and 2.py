# Given an array A[] consisting 0s, 1s and 2s. The task is to write a function that sorts the given array. 
# The functions should put all 0s first, then all 1s and all 2s in last.

array=list(map(int,input().split()))
low,mid=0,0
high=len(array)-1

while mid<=high:
    if array[mid]==0:
        array[low],array[mid]=array[mid],array[low]
        mid+=1
        low+=1
    elif array[mid]==1:
        mid+=1
    else:
        array[high],array[mid]=array[mid],array[high]
        high-=1
        
print(*array)
