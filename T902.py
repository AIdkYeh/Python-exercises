def isPrime(n):
    """判斷n是否為質數"""
    if n<=1:
        print("Not Prime")
    times=0
    for i in range(2,n+1):
        if n%i ==0:
            times+=1
    if times >2:
        print("Not Prime")
    else:
        print("Prime")
    
def primes(n):
    """列出小於n的質數"""
    l=[]
    for i in range (2,n+1):
        t2=0
        for j in range (1,i+1):
            if i%j==0:
                t2+=1
        if t2==2:
            l.append(i)
            
    for j in range(len(l)):
        if j <len(l)-1:
            print(l[j],end=',')
        else:
            print(l[j])
    
x = eval(input()) # 20
isPrime(x)
primes(x)
