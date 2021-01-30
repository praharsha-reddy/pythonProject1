import mysql.connector as a
mydb =a.connect(host="localhost",user="root",passwd="rupesh799")
print(mydb)
if(mydb):
    print("connection successful")
else:
    print("connection unsuccessfull")