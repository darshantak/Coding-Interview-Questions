#Given an array of n elements which contains elements from 0 to n-1, 
# with any of these numbers appearing any number of times. 
# Find these repeating numbers in O(n) and using only constant memory space.

array=list(map(int,input().split()))
for i in range(len(array)):
    array[array[i]%len(array)]=array[array[i]%len(array)]+len(array)
    
for i in range(len(array)):
    if array[i]>=len(array)*2:
        print(i)
