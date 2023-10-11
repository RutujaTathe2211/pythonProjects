x=int(input("Enter the candies you wants: "))
i=1
av=5
while i<=x:
    if(i>av):
        print("out of stock")
        break

    print("candy")
    i+=1

print("bye")

#Continue:skip remaining line of code
for i in range(1,101):
    #skips the number that divisible by 3 and 5
    if i%3==0 or i%5==0:
        continue
    print(i,end=' ')
print('Bye')

#Pass:when their will be no code then it pass control to else part
for i in range(1,101):
    if i%2!=0:
        pass
    else:
        print(i)


