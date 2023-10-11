
from mysql.connector import connect

mydb=connect(host="localhost",user="root",password="Rutuja@123",database="student")

#give cursor to work with the code
mycursor=mydb.cursor()
mycursor.execute("delete from student_details where student_name='Nikita'")
# mycursor.execute("select*from student_details")
#to fetch all data
# result=mycursor.fetchall()
#fetchone-print only one data

for i in mycursor:
    print(i)