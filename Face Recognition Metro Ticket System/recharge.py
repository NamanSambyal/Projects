import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "1234",
	database = "Project"
	)

mycursor = mydb.cursor()


def recharge():

	uname = input("Enter Username: ")

	card = input("Enter Credit Card Number: ")


	q = "SELECT User ID FROM user db WHERE Name = uname AND Credit Card No. = card" 

	mycursor.execute(q)

	uid = mycursor.fetchall()

	amount = int(input("Enter the Recharge Amount: "))

	q = "UPDATE face wallet db SET Balance = Balance + amount WHERE User ID = uid"
	
	mycursor.execute(q)
	mycursor.commit()


	print("Face Wallet Balance updated successfully.")

	q = "SELECT Balance FROM face wallet db WHERE User ID = uid"
	
	mycursor.execute(q)
	amount = mycursor.fetchall()

	print("Face Wallet Balance : ", amount)

