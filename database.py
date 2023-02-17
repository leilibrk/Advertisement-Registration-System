import mysql.connector

mydb = mysql.connector.connect(
    host="mysql-project1-barekatainleili-6f3d.aivencloud.com",
    port=21910,
    user="avnadmin",
    password="AVNS_F5ahJN1JZLm9lrSYe2P",
    database="defaultdb"
)
mycursor = mydb.cursor()
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#   print(x)
mycursor.execute("SELECT * FROM first_api_advertisement")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)