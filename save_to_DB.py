import mysql.connector


def saveToDB(st, cat, img_id):
    mydb = mysql.connector.connect(
        host="mysql-project1-barekatainleili-6f3d.aivencloud.com",
        port=21910,
        user="avnadmin",
        password="AVNS_F5ahJN1JZLm9lrSYe2P",
        database="defaultdb"
    )

    mycursor = mydb.cursor()
    query ='UPDATE first_api_advertisement SET state = (%s), category = (%s) WHERE id = (%s)'
    mycursor.execute(query, (st, cat, img_id))
    mydb.commit()
