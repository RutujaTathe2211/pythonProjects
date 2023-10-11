class student:
    #static variable     #class variable
    school='Jspm'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

        #object of inner class assign to outer class variable //inner class is present within outer class so we need to call outer class first
        self.lap=self.Laptop()

        #instance method-we use self //it works with object
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    # if we want to use class variable then cls used
    # for instance variable -self is used
    # to create class method-@classmethod decorator used

    @classmethod
    def getSchool(cls):
        return cls.school

#Static method-we use @staticmethod decorator
    @staticmethod
    def info():
        print('This is student class...in abc module')

    # def get_m1(self):
    #     return self.m1
    #
    # def set_m1(self,value):
    #     self.m1=value

    #=========Inner class===============
    class Laptop:
        def __init__(self):
            self.brand='Hp'
            self.cpu='i5'
            self.ram=8

        def show(self):
            print(self.brand,self.ram,self.cpu)


s1=student(23,43,43)
s2=student(32,22,11)

print(s1.avg())
print(s2.avg())
print(student.getSchool())
print(student.info())

#if we want to fetch the brand value of inside class then we use
lap1=s1.lap
lap2=s2.lap
print(lap1)
print(lap2)

#to print the show method of inner class
print(s1.lap.show())

# object of inner class
# lap1=student.Laptop()