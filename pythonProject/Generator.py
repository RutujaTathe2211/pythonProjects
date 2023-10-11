def Topten():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1
       

#return address
#genertors gives iterator
    # yield 1



values=Topten()
print(values.__next__())

for i in values:
    print(i)