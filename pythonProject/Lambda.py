# f=lambda a:a*a
# result=f(5)
# print(result)
# #ALl expression present in one line only
#
# f=lambda a,b:a+b
# re=f(4,5)
# print(re)

#====filter map reduce=====


#filter function take two argument one is function and other is list

# from functools import reduce
# n=[3,2,4,5,6,8,9,93,22,23,43]
# even=list(filter(lambda num:num%2==0,n))
# odd=list(filter(lambda  num:num%2!=0,n))
#
# #if we want to perform operation on whole list we use map
# doubles=list(map(lambda num:num*2 ,even))
# sum=reduce(lambda a,b:a+b,doubles)
# print('even: ',even)
# print('odd: ',odd)
#
# print('double',doubles)
# print('sum',sum)

#=========decorator===========
#we can change the behaviour of function at runtime
def div(a,b):
    print(a/b)

#func=div function
# def smart_div(func):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#             return func(a,b)
#     return inner
#
# div1=smart_div(div)
# div1(2,4)

#Special Variable
def fun1():
    print('from fun1')

def fun2():
    print('from func2')

def main():
    fun1()
    fun2()

#main function:we use this defination for not calling other module
if __name__=='__main__':
    main()
