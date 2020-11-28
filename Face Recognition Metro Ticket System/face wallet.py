import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "1234",
	database = "Project"
	)

mycursor = mydb.cursor()


def face_wallet(u_id, fare):

	q = "UPDATE face wallet db SET Balance = Balance - fare WHERE User ID = u_id"

	mycursor.execute(q)
	mycursor.commit()

	print("Rs ", fare, " deducted from Face Wallet.")


	q = "SELECT Balance FROM face wallet db WHERE User ID = u_id"

	mycursor.execute(q)

	amt = mycursor.fetchall()

	print("Face Wallet Balance: ", amt)


	if amt<20:
		print("Your Face Wallet Amount is low.")

		print("Enter Y if you wish to Recharge your Face wallet or else Enter N ")

		ch = input()

		if(ch == 'Y' or ch == 'y'):

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

			bal = mycursor.fetchall()



			print("Updated Face Wallet Balance : ", bal )