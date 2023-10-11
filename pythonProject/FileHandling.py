#open file //r:read
f=open('mydata','r')

#to read the data from file
# print(f.read())

f1=open('abc','w') #  w:write data in file
# f.write("something data are present in this file")
#
# f=open('abc','a') #a :append
# f.write("\nmy name is rutuja")

#to read data from file mydata
# for data in f:
#     print(data)

#to copy the data to abc file
# for data in f:
#     f1.write(data)

#when we work with binart data then we open file in binary format
# 'rb'

img=open("Img_6309.png","rb")
copyimg=open("myimage.png","wb")

for i in img:
    copyimg.write(i)

#commemnts in python
# for single line commnet : # is used
# for documentation comment: '''   ''' : is used //they are not ignored

#python is compiled as well as interpreted language
