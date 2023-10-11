#not create object of it
#method only declare not define //at least one abstarctmethod

from abc import ABC,abstractmethod
class computer:

    @abstractmethod
    def process(self):
        pass

class Laptop(computer):
    def process(self):
        print("it's running")

class programmer:
    def work(self,com):
        print('solving bugs')

#if whiteboard is computer then their is compaltion to include abstrct method
class whiteboard(computer):
    def write(self):
        print("it's writing")

prog=programmer()


com1=Laptop()
com1.process()

# com2=whiteboard()
prog.work(com1)

