#part-7
# incrementing and decrementing the values based on array elements
li = ["--X","X++","X++"]
x=0
for i in range(len(li)):
    temp=li[i]
    if temp=="X++" or temp=="++X":
        x+=1
    else:
        x-=1
print(x)

#Input: address = "1.1.1.1"
#output: address= "1[.]1[.]1[.]1"
s="1.1.1.1"
e=""
for i in range(len(s)):
    if s[i]==".":
        e=e+"[.]"
    else:
        e=e+s[i]
print(e)    
#double for loop
n=4
for i in range(n):
    for j in ['a','b']:
        print(i,j)
        
#identifing the values
jewels="aA"
stones="aaAbc"
count=0
for i in jewels:
    for j in stones:
        if j==i:
            count+=1
print(count)

#another method
jewels="aA"
stones="aaAbc"
count=0
for i in range(len(jewels)):
    for j in range(len(stones)):
        chi=jewels[i]
        chj=stones[j]
        if chi==chj:
            count+=1
print(count)