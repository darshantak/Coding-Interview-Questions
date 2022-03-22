starting_time=list(map(int,input().split()))
finish_time=list(map(int,input().split()))
starting_time=[x for _,x in sorted(zip(finish_time,starting_time))]
finish_time.sort()
n=1
temp=finish_time[0]
schedule=[1]
while n<len(starting_time):
    if starting_time[n]>temp:
        # print(starting_time[n],finish_time[n-1])
        schedule.append(n+1)
        temp=finish_time[n]
    n+=1
print(*schedule)
