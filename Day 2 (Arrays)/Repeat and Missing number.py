#Given an unsorted array of size n. Array elements are in the range from 1 to n. 
# One number from set {1, 2, …n} is missing and one number occurs twice in the array. 
# Find these two numbers.

array=list(map(int,input().split()))
count=[0]*(len(array)+1)

for i in array:
    count[i]+=1
x,y=0,0
for i in range (1,len(count)):
    if count[i]==0:
        x=i
    if count[i]>1:
        y=i

print(x,y)