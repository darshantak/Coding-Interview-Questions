#We are given two sorted array. 
# We need to merge these two arrays such that the initial numbers (after complete sorting) are in the first array and 
# the remaining numbers are in the second array. 
#Extra space allowed in O(1).

#Time O(len(array1)*len(array2))
#Space O(1)

array1=list(map(int,input().split()))
array2=list(map(int,input().split()))

for i in range(len(array2)-1,-1,-1):
    greatest=array1[-1]
    j=len(array1)-2
    while j>=0 and array1[j]>=array2[i]:
        array1[j+1]=array1[j]
        j-=1

    if j!=len(array1)-2 or array2[i]<greatest:
        array1[j+1]=array2[i]
        array2[i]=greatest

print(*array1)
print(*array2)

