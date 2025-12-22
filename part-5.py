# DAY-5
# write a program to print the name based the given no.of times
"""
name="Shiva"
n=3
for i in range(n):
    print(name)
"""
#when we have to write the reusble code we use functions
"""
def fun(s,n):
    for i in range(n):
        print(s)
fun("ka",3)
fun("Shiva",3)
fun("Kashi",3)
"""
# function without parameters without return
# there are 4 possible ways in function
'''
def movies():
    print("INdian Biggest Superstar")
print("Prabhas")
movies()
print("BoxOffice Blast") '''
#function with paramterts with return 
'''
def fun(n):
    print("Hello macha")
    return 2
sh=fun(1)
print(sh)
'''
# write a program to implement table using function

"""
def table(n):
    for i in range(1,11):
        # print(n,"*",i,"=",(n*i))
        # print(str(n)+"*"+str(i)+"="+str(n*i))
        print(f"{n} * {i} = {n*i}")
table(5)
"""
#write a program to check even or odd using functions
def eod(n):
    if n%2==0:
        print("It's a even number")
    else:
        print("it's a odd number")
eod(2)