import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
# i=0
# def greet():
#     global i
#     i+=1
#     print('hello',i)
#     greet()#infinite loop
# greet()

#Factorial using recursion
def fact(n):
    if(n==0):
        return 1
    return n* fact(n-1)

result=fact(5)
print(result)