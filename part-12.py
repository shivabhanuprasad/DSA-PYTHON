#part-12
# different kinds of patterns
'''  *
    ***
   *****
'''
r=10
n=r-1
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    temp=i*2+1
    for i in range(temp):
        print("*",end="")
    print()
#
'''
*
 **
   ***
   '''
r=10
n=r-1
for i in range(r):
    for j in range(i):
        print(" ",end="")
    temp=2*r-1-2*i
    for k in range(temp):
        print("*",end="")
    print()
# reverse+strainght
r=10
n=r-1
for i in range(r-1):
    for j in range(n-i):
        print(" ",end="")
    temp=i*2+1
    for i in range(temp):
        print("*",end="")
    print()
for i in range(r-1,-1,-1):
    for j in range(n-i):
        print(" ",end="")
    temp=i*2+1
    for i in range(temp):
        print("*",end="")
    print()
# another pattern
r=10
n=r-1
for i in range(r-1,-1,-1):
    for j in range(n-i):
        print(" ",end="")
    temp=i*2+1
    for i in range(temp):
        print("*",end="")
    print()
for i in range(1,r):
    for j in range(n-i):
        print(" ",end="")
    temp=i*2+1
    for i in range(temp):
        print("*",end="")
    print()