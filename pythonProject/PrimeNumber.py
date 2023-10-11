num=int(input("enter the number: "))
for i in range(2,num):
    if(num%i==0):
        print('Not prime number')
        break
    else:
        print('number is prime')
        break