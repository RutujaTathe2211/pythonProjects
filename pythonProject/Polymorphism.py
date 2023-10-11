# #Duck Typing: one method execute not checking for which class is used for
#
# class pycharm:
#     def execute(self):
#         print('compiling')
#         print('running')
#
# class myEditor:
#     def execute(self):
#         print('spell check')
#         print('convention check')
#         print('compiling')
#         print('running')
#
# class Laptop:
#     def code(self,ide):
#
# #we only check for execute method in any class
#         ide.execute()
#
# ide=myEditor()
#
# lap1=Laptop()
# lap1.code(ide)
#
# #=============Operator overloading=============
# a=5
# b=6
# c='rutuja '
# d='tathe'
# print(int.__add__(a,b))
# print(str.__add__(c,d))

# class Student:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
#
#     def __add__(self, other):
#         m1=self.m1+other.m1
#         m2=self.m2+other.m2
#         s3=Student(m1,m2)
#         return  s3
#
#     def __gt__(self, other):
#         s1=self.m1+other.m1
#         s2=self.m2+other.m2
#         if s1>s2:
#             return True
#         else:
#             return False
#
#
#
#
# s1=Student(23,56)
# s2=Student(50,30)
#
# s3=s1+s2  #converted to Student.__add__(s1,s2) +:call add method
# print(s3.m1)
# print(s3.m2)
#
#
# #if we want to perform operation on any oject we need to create method
# if s1>s2:
#     print('s1 wins')
# else:
#     print('s2 wins')

#=============method overloading=================
# class student:
#     def __init__(self,m1,m2):
#        self.m1=m1
#        self.m2=m2
#
#     def sum(self,a=None,b=None,c=None):
#         s=0
#         #none value replace with other value
#         if(a!=None and b!=None and c!=None):
#            s=a+b+c
#         elif(a!=None and b!=None):
#             s=a+b
#         else:
#             s=a
#
#         return s
#
# s1=student(20,30)
# print(s1.sum(3,2,20))

#=============mthod overriding============
class A:
    def show(self):
        print('in a show')

class B(A):
    #b class override a class show method
    def show(self):
        print('in B show')



a=B()
a.show()
