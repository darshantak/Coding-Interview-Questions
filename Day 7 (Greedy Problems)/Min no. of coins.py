denominations=list(map(int,input().split()))
v=int(input())
numOfCoins=[float("inf") for i in range(v+1)]
numOfCoins[0]=0
for denom in denominations:
    for coins in range(v+1):
        numOfCoins[coins]=min(numOfCoins[coins],1+numOfCoins[coins-denom])

print(numOfCoins[-1])

