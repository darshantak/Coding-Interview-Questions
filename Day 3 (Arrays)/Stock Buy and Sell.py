#Stock Buy Sell to Maximize Profit
#The cost of a stock on each day is given in an array, 
# find the max profit that you can make by buying and selling in those days.

array=list(map(int,input().split()))
i=0
while i<len(array)-1:
    while i<len(array)-1 and array[i]>=array[i+1]:
        i+=1
    if i==len(array)-1:
        break
    buy=i
    i+=1
    while i<len(array) and array[i]>=array[i-1]:
        i+=1
    sell=i-1

    print("Buy",buy,"Sell",sell)


