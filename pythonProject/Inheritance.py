#Multilevel Inheritance
class A:
    def __init__(self):
        print('in a init')
    def feacture1(self):
        print('feacture 1 working')
    def feacture2(self):
        print('feacture 2 working')


#child class-inherit all fecature of A
class B(A):
    def __init__(self):

        #call init method of class A
        super().__init__()
        print("in b init method")

    def feacture3(self):
        print('feacture 3 working')
    def feacture4(self):
        print('feacture 4 working')


class C(A,B):
    #MRO:method can resolve in left to right oreder
    def __init__(self):
        super().__init__()
        print("in c init method")
    #class C(A,B)----multiple inheritance
    def feacture5(self):
        print('feacture 5 working')

# a1=A()
# a1.feacture1()
# a1.feacture2()
#
# b1=B()
# b1.feacture3()
# b1.feacture4()
# b1.feacture1()
# b1.feacture2()

c=C()
# c.feacture5()
# c.feacture1()