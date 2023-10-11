a=5
b=1

#try with multiple catch block
try:
  print('resource open')
  print(a/b)
  k = int(input("enter number"))
  print(k)

#handle divide by zero error
except ZeroDivisionError as e:
 #e-error message is also print
 print("you can not divide number by zero",e)

#handle invalid input error
except ValueError as e:
 #e-error message is also print
 print("Invalid Input",e)


#handle all other error
except Exception as e:
 print('Exception occur',e)


finally:
 print('resource close')

print("bye")