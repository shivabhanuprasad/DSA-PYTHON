#part-11
#square box pattern
rows=5
cols=5
for i in range(rows):
    for j in range(cols):
        if i==0 or i==rows-1 or j==0 or j==cols-1:
            print("*",end="")
        else:
            print(" ",end="")
        if j!=cols-1:
            print(" ",end="")
    print()
    
#scale box pattern
r=4
c=10
for i in range(r):
    for j in range(c):
        if i==0 or i==r-1 or j==0 or j==c-1:
            print("*",end=" ")
    if j!=c-1:
        print(" ",end="")
    print()
    
#bike stand pattern
r=16
c=5
c1=r-1
for i in range(r):
    for j in range(c1-i):
        print("-",end="")
    for k in range(c):
        print("*",end="")
    print()
#another bike stand pattern
r= 16
c=5
for i in range(r):
    for j in range(i):
        print(" ",end="")
    for k in range(c):
        print("*",end="")
    print()
        