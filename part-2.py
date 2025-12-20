# DAy-2
# print add,sub,mul,div
first=21
print(first+2) #add
print(first-1) #sub
print(first*2) #mul
print(first/2) #div

# arrays in pythons
a=[4,6,8,9,3]
print(a[0])
print(a[4])
# main important topic is "indices"/"index"
#array can contains values,strings or any values

#to reduce the value of print we use for loop
print(list(range(5))) #range
print(list(range(2,5))) # start and end range
print(list(range(2,5,2))) #skip value
for i in range(5):
    
    print(a[i])

#array values 
li=[1,5,6]
for i in li:
    print("Macha")
    print(i)
    
#counting how many 1 values are there in the given array
ans=0
arr=[1,2,3,4,1,5,6,7,1,2,6,1]
for i in arr:
    if i==1:
        ans=ans+1
print(ans)
