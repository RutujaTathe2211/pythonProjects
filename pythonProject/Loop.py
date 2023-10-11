#If-else
x=int(input('enter value of x: '))
r=x%2
#Nested if-else
if (r==0):
    print("Even Number")
    if x>5:
        print('Great')
    else:
        print('not great')
else:
    print("Odd number")

#elif program
a=45
if a==1:
    print('1')
elif a==89:
    print('89')
else:
    print('wrong input')

#while loop
i=0
while(i<4):
    print('NTS')
    i+=1

#nested while
i=1
while i<=5:
    #end -used to stay on same line
    print('nts ',end="")
    j=1
    while j<=4:
        print('rocks ',end="")
        j+=1

    i+=1
    print()

#For-loop
# x=['navin',34,5,4,32]
# for i in x:
#     print(i,end=' ')

#go in ascending order
# for i in range(2,21,2):
#     print(i,end=' ')

#go in reverse order
for i in range(20,0,-2):
    print(i,end=" ")