#Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

array=list(map(int,input().split()))
i=len(array)-2

while i>=0 and array[i]>array[i+1]:
    i-=1
# print(i)

for j in range(len(array)-1,-1,-1):
    if array[j]>array[i]:
        position=j
        break

array[i],array[position]=array[position],array[i]
# print(array)
array[i+1:]=sorted(array[i+1:])

print(array)