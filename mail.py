import requests

import mysql.connector


def send_email(status, id):
    # find user mail
	mydb = mysql.connector.connect(
		host="mysql-project1-barekatainleili-6f3d.aivencloud.com",
		port=21910,
		user="avnadmin",
		password="AVNS_F5ahJN1JZLm9lrSYe2P",
		database="defaultdb")

	mycursor = mydb.cursor()
	query = 'SELECT email from first_api_advertisement where id = (%s)'
	mycursor.execute(query, (id,))
	user_email = mycursor.fetchall()
	print(user_email[0][0])
	return requests.post(
		"https://api.mailgun.net/v3/sandboxc303838bc59042d3990485c8f9a7f90e.mailgun.org/messages",
		auth=("api", "eb3f9a6e9cf77cb4f40f0529a5a45f52-48c092ba-847ae5cc"),
		data={"from": "Mailgun Sandbox <postmaster@sandboxc303838bc59042d3990485c8f9a7f90e.mailgun.org>",
			  "to": [user_email[0][0]],
			  "subject": 'Adv status',
			  "text": 'adv id : ' + id + ' has been ' + status})
