#print reverse terms n->1
def reverse(i,n):
    if i>n:
        return
    print(n)
    reverse(i,n-1)

#print in reverse terms using backtracking
def reverseBack(i,n):
    if i>n:
        return
    reverseBack(i+1,n)
    print(i)

# reverseBack(1,4)

#print sum using parameterised recursion
def sumPara(i,sum):
    if i<1:
        print(sum)
        return
    sumPara(i-1,sum+i)

sumPara(3,0)

#print sum using functional recursion
def sumFunc(n):
    if n==0:
        return 0
    return sumFunc(n-1)+n

print(sumFunc(3))
 
#check palindrome
def checkPalindrom(i,s):
    if i>=len(s)//2:
        return True
    if s[i]!=s[len(s)-i-1]:
        return False
    return checkPalindrom(i+1,s)

print(checkPalindrom(0,"MAADAM"))

#fibonacci number  
def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
 
print(fibonacci(4)) 


