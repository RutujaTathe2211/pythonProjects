# def fibonacci(n):
#     t1=0
#     t2=1
#     count=0
#     print(t1,end=' ')
#     print(t2,end=' ')
#     for i in range(2,n):
#        t3=t1+t2
#        print(t3,end=' ')
#        t1=t2
#        t2=t3
#
# fibonacci(10)

#Factorial-Number
#n=6
def fact(n):
    fact=1
   # range()-exclude last variable value
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
fact(5)