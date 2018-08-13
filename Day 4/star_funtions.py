#Star Argument Functions

# First - passing tuple

def party(*arg):
    for guest in arg:
        print(guest + " Please come to my party at home")

party()
party('a')
party('a','b','c')
print("----------------------------------------------------------")

# Second - pasing arbitrary and tuple

def party(venue,*guests):
    for guest in guests:
        print(guest + " Please come to my party at home " + venue)

party('a','b')
party('a','b','c')
print("----------------------------------------------------------")

#Third - Dictionary pssing as argument

def show_detail(**kwarg):
    for key in kwarg:
        print("{k}:{v}".format(k=key,v=kwarg[key]))
        #print(key,kwarg[key])

show_detail(name="abc", city="Pune",country="India")
print("----------------------------------------------------------")

#Fourth - Lambda function
sqr = lambda x : x*x
print(sqr(2))

print("----------------------------------------------------------")
ls=range(1,5)
ls_sqr = []

for i in ls:
    ls_sqr.append(i*i)

print(ls)
print(ls_sqr)
print("----------------------------------------------------------")

def sqr(x):
    return x*x
print(sqr(3))
print("----------------------------------------------------------")

def sqr(x):
    return x*x
li=[1,2,3,4]
newli=map(sqr, li)
print(newli)
print("----------------------------------------------------------")

li=[1,2,3,4,5]
newli=map(lambda x: x*x, li)
print(newli)
print("----------------------------------------------------------")

num=[100, 150, 60, 111, 40, 120]
output=map(lambda x:'big' if x>100 else 'small', num)
print(output)

print("----------------------------------------------------------")
x=[1,2,4,5,6]
li1=filter(lambda x : x%2, x)
li2=filter(lambda x : not(x%2), x)
li3=filter(lambda x : x<0, range(-5,5))
print(li1)
print(type(li))
print(li2)
print(li3)

print("----------------------------------------------------------")
#sum
output=reduce(lambda x,y: x+y, [2,3,4,5,6,7])
print(output)
#max
f=lambda a,b: a if (a>b) else b
output=reduce(f,[47,104,42,102,13])
print(output)
#sum with range
output=reduce(lambda x,y: x+y, range(0,101))
print(output)
print("----------------------------------------------------------")
