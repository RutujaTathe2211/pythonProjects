class car:
    #class variable
    wheels=4

    def __init__(self):
      #define variables //local variable
      # #instance variable
       self.mil=10
       self.com='high'

c1=car()
c2=car()
#we can change value of local variable
c1.mil=20

#chnage value of class variable
car.wheels=8
print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)

