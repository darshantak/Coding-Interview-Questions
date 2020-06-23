# Given a set of time intervals in any order, 
# merge all overlapping intervals into one and output the result which should have only mutually exclusive intervals

intervals=[]
for i in range(int(input())):
    a=list(map(int,input().split()))
    intervals.append(a)


intervals.sort(key=lambda x: x[0])
i=1
while i<len(intervals):
    if intervals[i][0]<=intervals[i-1][1]:
        intervals[i-1][0]=min(intervals[i-1][0],intervals[i][0])
        intervals[i-1][1]=max(intervals[i-1][1],intervals[i][1])

        intervals.pop(i)

    else:
        i+=1

print(intervals)



