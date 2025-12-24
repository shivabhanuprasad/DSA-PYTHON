# part -10
print("Hell0",end=" ")
print("Shiva",end=" ")
print("Boom")
li=["Hell0","Shiva","Boom"]
for i in range(len(li)):
    print(li[i],end=" ")
print()
#printing patterns (3*3)
rows=3
cols=3
for i in range(rows):
    for j in range (cols):
        print("*",end="-")
    print()

# end - do not ned
rows=3
cols=3
for i in range(rows):
    for j in range (cols):
        print("*",end="")
        if j!=cols-1:
            print("-",end="")
    print()
    
#slept muggu
r=3
c=20
for i in range(r):
    for j in range (c):
        print("*",end="")
        if j!=c-1:
            print("-",end="")
    print()
    
    #straingt
r=15
c=3
for i in range(r):
    for j in range (c):
        print("*",end="")
        if j!=c-1:
            print("-",end="")
    print()