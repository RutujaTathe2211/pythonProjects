from numpy import *

#====Different way to create array-array(),linspace()
#logspace(),arange(),zeros(),ones()
#
# #1. in numpy we not need to provide type of array
# arr=array([1,2,3,4,55,43,2])
# # #using linspace():0-start,16-not exclueded (end part),10(breake into different part
# arr1=linspace(0,16,20)
# print(arr1)
#
# #using logspace()
# ls=logspace(1,40,5)
# #used to get the bvalue of 4 th element
# print("%2f" %ls[4])
#
# print(ls)
#
# #using zeros:all elemnet of array will zero
# arr2=zeros(5)
# print(arr2)
#
# #using ones:all elemnet of array is one
# arr3=ones(5)
# print(arr3)
#
# #Addition of array
# a1=array([2,3,45,78,11])
# a2=array([3,4,5,2,11])
# # a3=a1+a2
# # print(a3)
# print(concatenate([a1,a2]))
#
# #using numpy we can find value of sin,cos,log,sqrt
# a4=array([4,9,16,25,36])
# print(log(a4))
# print(sin(a4))
# print(sqrt(a4))
# print(cos(a4))
#
# #======================copying array===================
# # 1.address is same
# # a5=a1
# # print(a5)
#
# #2.shallow copy-both the array are dependent on each other
# a5=a1.view()
# print(a5)
#
# #3.deep copy-both array independent on each other
# # a5=a1.copy()
# # print(a5)
#
# #used to get the address of an array
# print(id(a5))
# print(id(a1))

#===========multidimensional array===============
# array1=array([
# [1,2,3,9,6,7,3,0],
# [4,5,6,3,4,5,6,7]
# ])
# #to get the dimension
# print(array1.ndim)#get dimension
# print(array1.dtype)#get type os array
# print(array1.shape)#get no of rows and column
# print(array1.size)#get the element count
#
# #to convert multidimension  to one dimansion
# # array2=array1.flatten()
# # print(array2)
#
# #to convert one dimension to multi-dimensional
# array2=array1.reshape(4,4)
# print(array2)

#matrix operation
m1=matrix('6,5;4,3;8,9;7,6')
m2=matrix('6,5;4,3;8,9;7,6')
m3=m1+m2
print(m3)
print(m1)
print(m1.min())#minimum element
print(m1.max())#maximum element

