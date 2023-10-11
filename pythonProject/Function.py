#define one's can called it many times.
def greet():
    print("Welcome!! Good morning")
    print("how are you?")

greet()

def add(a,b):
    return a+b

result=add(80,20)
print(result)

def add_sub(a,b):
    c=a+b
    d=a-b
    return c,d

result=add(80,20)
result1,result2=add_sub(80,30)
print(result1,result2)

#====Function Arguments========
#their will be no call by value and call by referance in python
#pass by value-pass value to function//memory address change
#pass by referance-pass referance/address of variable
def update(x):
    x=8
    print(x)
a=10

update(a)
print("a ",a)

#a,b are-formal arguments
#Variable length argument
def addition(*b):
    c=0
    for i in b:
        c=c+i
    print(c)

#Type argument
#1.variable length argument
addition(1,2,3,4,9)

#2.keyword length argumnet
#addition(a=90,b=45)

#default(34)//if second value is not specify then the defalult value is take
#addition(2,3,4) // *b:no of argument are not fixed

#keyworded variable length argument: ** is required
def person(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)

person('navin',age=25,city='mumbai',mob=9876667)

a=10#gloabl
def something():
    a=9#local
   # global a:if we want to use global variable
    globals()['a']=15#globals()-use to chnge the value of global variable
    print("in function",a)
something()

print("outside",a)

#===========pass List of Element to function===========
list=[]
size=int(input("enter the size of list: "))
for i in range(size):
    num=int(input("enter the next value"))
    list.append(num)
print(list)
even=[]
odd=[]
def count(list):
    for i in list:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
count(list)

print('even: ',even)
print('odd: ',odd)



