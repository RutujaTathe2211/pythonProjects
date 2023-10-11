# num=[2,3,4,5,7,8,9]
#
# # for i in num:
# #     print(i)
#
# #=========iterator============
# it=iter(num)
# # print(it.__next__())
# # print(it.__next__())
#
# for i in num:
#     print(i)

#======create own iterator===============
class TopTen:
    def __init__(self):
        self.num=1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num<=10:
            val = self.num
            self.num += 1
            return val

        else:
            raise StopIteration


values=TopTen()

print(values.__next__())
print(values.__next__())

#if we found values in first then it not be repeated
for i in values:
    print(i)