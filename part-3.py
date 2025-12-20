# AND or OR operations in pythons
#AND
if 2+3==5 and 3+4==7:
    print("correct")
else:
    print("Wrong")

#OR
if 2+3==3 or 3+4==7:
    print("correct")
else:
    print("Wrong")

#write an program to count the no of values which are divisible by 2 and 3
li=[1,2,3,4,5,67,9,12,15]
ans=0
for i in li:
    if i%2==0 and i%3==0:
        ans+=1
print(ans)