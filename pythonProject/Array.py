from array import *
vals=array('i',[2,3,45,677,3,43,33,23])

#typecode-take the values from vals//when we don't know type
newArray=array(vals.typecode,(a*a for a in vals))
print(vals)

#size of array and memory address
print(vals.buffer_info())

#reverse the array
vals.reverse()
print(vals)

#print second element of reverserd array
print(vals[1])

for i in newArray:
    print(i)

# arr=array('f',[1.2,1.3,4.5,5.5])
# print(arr)

#===============Take array value from user================

arr=array('i',[])
n=int(input("enter size of array:"))
for i in range(n):
    x = int(input("enter the value "))
    #used to add values in array
    arr.append(x)
print(arr)

val=int(input("enter the value you want to serach"))
k=0
for e in arr:
    if e==val:
        print(k)

    k+=1

#using function
print("----using function------")
print(arr.index(val))
