#Break is necessary for forElse loop
num=[10,2,3,4,50,55,6,7,8]
for i in num:
    if i%5==0:
        print(i)
        break
else:
    print("not found")