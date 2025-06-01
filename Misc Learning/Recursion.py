#Write a recursive function to find the sum of numbers from 1 to n.

def SumofNum(n):
    if n==0:
        return 0
    else:
        return n+ SumofNum(n-1)
print(SumofNum(4))


#Write a recursive function to count down from n to 1.

def Countdown(n):
    if n==0:
        print('done!')
        
    else:
        print(n)
        return Countdown(n-1)
    
Countdown(5)

#Write a recursive function to calculate the factorial of a number n.

def factorial(n):
    if n ==0:
        return 1
    
    else:
        return n* factorial(n-1) 
    
print(factorial(4))