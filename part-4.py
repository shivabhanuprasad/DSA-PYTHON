# DAY-4
# write a program to implement reverse of a string
s="ABCD"
ans=" "
for i in range(3,-1,-1):
    ans=ans+s[i]
print(ans)

# reversing aa list
li=[5,8,9,1,0,2,3,2]
n=len(li)
for i in range(n-1,-1,-1):
    print(li[i])
    
#use the n term for reversing a string
sh="SHIVA"
le=len(sh)
ans=" "
for i in range(le-1,-1,-1):
    ans=ans+sh[i]
print(ans)

#check wheather the given string is palindrome
a="madam"
b=""
lena=len(a)
for i in range(lena-1,-1,-1):
    b=b+a[i]
if a==b:
    print("Yes,it's a palindrome")
else:
    print("NO, it's not a plaindrome")
#boolean data type
a=True
b=False
print(a,b)

#use another logic to check plaindrome
s="abccbd"
n=len(s)//2 # first half
mu=len(s)  # secondhalf
valid=True
for i in range(n):
    l=s[i]  #left value
    r=s[mu-1-i]  #right value
    if l!=r:     #checking
        valid=False
        break    #stopping the iteration
if valid:
    print("yes")
else:
    print("no")
#clearly understanding the break concept
for i in range(10):
    print(i)
    if i==3:
        break
