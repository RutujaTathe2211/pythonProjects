class computer:
    #method//like constructor         #init method
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        print('init method')

    def config(self):
        print('config is: ',self.cpu,self.ram)

#object of class computer//object creation
#(object(com1) ,cpu, ram)
com1=computer('i5',16)
comp2=computer('i6',18)
print(type(com1))


#acess function of class computer
# computer.config(com1)
# computer.config(comp2)

com1.config()
comp2.config()


