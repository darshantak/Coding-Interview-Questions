n=int(input())
days=[]
for _ in range(n):
    tasks=list(map(int,input().split()))
    days.append(tasks)

def helper(day,last_task):
    if day==0:
        maxi=0
        for i in range(3):
            if i!=last_task:
                maxi=max(maxi,days[day][i])
        return maxi
    maxi=0
    for i in range(3):
        if i!=last_task:
            points=days[day][i]+helper(day-1,i)
            maxi=max(maxi,points)
        
    return maxi

# print(helper(len(days)-1,3))

#memoisation
def helper1(ind,last_task,dp):
    if ind==0:
        maxi=0
        for i in range(3):
            if i!=last_task:
                maxi=max(maxi,days[ind][i])
        dp[ind][i]=maxi
        return dp[ind][i]
    if dp[ind][last_task]!=-1:
        return dp[ind][last_task]
    maxi=0

    for i in range(3):
        if i!=last_task:
            points=days[ind][i]+helper1(ind-1,i,dp)
            maxi=max(maxi,points)
        dp[ind][last_task]=maxi
    print(dp)
    return dp[ind][last_task]

 
dp=[[-1 for i in range(4)]]*len(days)
print(helper1(len(days)-1,3,dp))
# print(dp)

