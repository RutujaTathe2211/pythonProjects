#==========Linear search============

# list=[2,3,4,5,6,7,8,9]
# n=9
# pos=-1
#
# def search(list, n):
#     i=0
#     while i<len(list):
#         if list[i]==n:
#             globals()['pos']=i
#             return True
#         i+=1
#
#     return False
#
#
# if search(list,n):
#     print("found at",pos+1)
# else:
#     print("not found")

#============binary search============
# list=[2,3,4,5,6,7,8,9]
# n=9
# pos=-1
#
# def search(list, n):
#     l=0
#     u=len(list)
#     while l<=u:
#         mid=(l+u)//2
#
#         if list[mid]==n:
#             globals()['pos']=mid
#             return True
#         else:
#             if list[mid]<n:
#                 l=mid+1;
#             else:
#                 u=mid-1;
#     return False
#
# if search(list,n):
#     print("found at",pos+1)
# else:
#     print("not found")

#======bubble sort===========
list=[9,8,7,45,6]


# def sort(list):
#     for i in range(len(list)-1,0,-1):
#         for j in range(i):
#             if list[j]>list[j+1]:
#                 temp=list[j]
#                 list[j]=list[j+1]
#                 list[j+1]=temp
#
# sort(list)
# print(list)

#=============selection sort=================
list=[9,8,7,45,6]


def sort(list):
    for i in range(5):
        minpos=i
        for j in range(i,5):
            if list[j]<list[minpos]:
                minpos=j
        temp=list[i]
        list[i]=list[minpos]
        list[minpos]=temp

sort(list)
print(list)
