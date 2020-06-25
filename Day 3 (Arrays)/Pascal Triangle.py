# Write a program to print a pascal triangle 

rows=int(input())

triangle=[[1]]
for i in range(1,rows):
    temp=[1]
    prev_row=triangle[i-1]
    # print(prev_row)
    for j in range(1,i):
        temp.append(prev_row[j]+prev_row[j-1])
        # print(temp)
    temp.append(1)
    triangle.append(temp)


print(triangle)