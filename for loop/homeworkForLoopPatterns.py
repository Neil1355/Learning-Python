#right half triangle 

for i in range (1,6):
    for j in range(1,i+1):
        print("*", end=" ")
    print()
print()

#Left half triangle

k=6
for i in range(1,6):
    for space in range(1,k):
        print(" ",end=" ")
    k=k-1
    for j in range (1,i+1):
        print("*", end=" ")
    print()
print()

# Perfect pyramid

k=4
for i in range(1,10,2):
    for space in range(k):
        print(" ", end=" ")
    k=k-1
    for j in range(0,i):
        print("*", end=" ")
    print()
print()

#perfect pyramid reversed

k=4
for i in range(10,0,-2):
    for space1 in range(k):
        print(" ", end=" ")
    k=k+1
    for j in range(1,i):
        print("*", end=" ")
    print()
    
    
#inverted right half pyramid

for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()
print()

#inverted left half pyramid

k=0
for i in range(5,0,-1):
    for space in range(0,k):
        print(" ", end=" ")
    k=k+1
    for j in range(1,i+1):
        print("*", end=" ")
    print()
print()

#parallelogram

for i in range(0,5):
    for space in range(0,i):
        print(" ", end = " ")
    for j in range(0,5):
        print("*", end=" ")
    print()
print()

#Hollow square

for i in range(0,6):
    for j in range(0,6):
        if i==0 or i==5 or j==0 or j==5:
         print("*", end = " ")
        else:
         print(" ", end = " ")
    print()
print()

#hollow triangle
k = 6  
n=6
for i in range(1, k + 1): 
    for space in range(n):  
        print(" ", end=" ")
    n=n-1

    for j in range(1, i + 1): 
        if j == 1 or j == i or i == k: 
            print("*", end="   ")
        else:  
            print(" ", end="   ")
    print() 