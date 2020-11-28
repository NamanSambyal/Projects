import cv2

import mysql.connector


mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "1234",
	database = "Project"
	)

mycursor = mydb.cursor()


from faces import *
from sign_up import *
from fare calculator import *
from face wallet import *


while(True):

	uid = str(faces())
	print(uid)

	q = "SELECT Name FROM user db WHERE User ID = uid"

	if not mycursor.execute(q):
		sign_up()

	
	else:
			
		q = "SELECT Start_Station FROM user db WHERE User ID = uid"

		mycursor.execute(q)

		start_station = mycursor.fecthall()

		q = "SELECT  End_Station FROM user db WHERE User ID = uid"

		mycursor.execute(q)

		end_station = mycursor.fecthall()

		fare = fare_calculator(start_station, end_station)

		face_wallet(uid, fare)












