rows,cols=map(int,input().split())
grid=[]
for i in range(rows):
    temp=list(map(int,input().split()))
    grid.append(temp)
 
def helper(i,j,grid):
    if i>=0 and j>=0 and grid[i][j]==-1:
        return 0
    if i==0 or j==0:
        return 1
    if i<0 and j<0:
        return 0
    up=helper(i-1,j,grid)
    left=helper(i,j-1,grid)
    return left+up

print(grid)
print(helper(rows-1,cols-1,grid))