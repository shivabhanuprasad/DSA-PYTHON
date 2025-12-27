#part-13

r=4
for i in range(r):
    for j in range(r-i-1):
        print(" ",end="")
    for k in range(i*2+1):
        if k==0 or k==i*2 or i==r-1:
            
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
#reverse one
r=4
for i in range(r-1,-1,-1):
    for j in range(r-i-1):
        print(" ",end="")
    for k in range(i*2+1):
        if k==0 or k==i*2 or i==r-1:
            
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
#pyramid with spaces
r=4
for i in range(r-1):
    for j in range(r-i-1):
        print(" ",end="")
    for k in range(i*2+1):
        if k==0 or k==i*2 or i==r-1:
            
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(r-1,-1,-1):
    for j in range(r-i-1):
        print(" ",end="")
    for k in range(i*2+1):
        if k==0 or k==i*2 :
            
            print("*",end="")
        else:
            print(" ",end="")
    print()
#mpattern
n=6
for i in range(n):
    for j in range(1,i+2):
        print(j,end=" ")
    print()

#reverse pattern of numbers
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i+1,0,-1):
        print(k,end="")
    print()
    
#combined pattern
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i+1,0,-1):
        print(k,end="")
    for l in range(2,i+2):
        print(l,end="")
    print()