rows,cols=map(int,input().split())
def helper(i,j):
    if i==0 or j==0:
        return 1
    if i<0 or j<0:
        return 0
    up=helper(i-1,j)
    left=helper(i,j-1)
    return up+left

# print(helper(rows-1,cols-1))

#memoization
def helper1(i,j,dp):
    if i==0 and j==0:
        return 1
    if i<0 or j<0:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]

    up=helper1(i-1,j,dp)
    left=helper1(i,j-1,dp)

    dp[i][j]=up+left

    return dp[i][j]

dp=[[0 for i in range(cols)] for j in range(rows)] 
# print(helper1(rows-1,cols-1,dp))

def helper2(i,j,dp):
    for i in range(rows):
        for j in range(cols):
            if i==0 and j==0: 
                dp[0][0]=1
            else:
                up,left=0,0
                if i>0:
                    up=dp[i-1][j]
                if j>0:
                    left=dp[i][j-1]
                dp[i][j]=up+left
    return dp[i][j]

print(helper2(rows-1,cols-1,dp))