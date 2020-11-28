import cv2
import shutil, os

import mysql.connector


mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "1234",
	database = "Project"
	)

mycursor = mydb.cursor()

from recharge import *

def sign_up():
	
	print("Enter Name: ")
	name = input()

	print("Enter Aadhar Card number: ")
	aadhar = int(input())

	print("Enter Phone Number: ")
	phn = int(input())

	print("Enter Credit Card No.: ")
	crn = int(input())

	while True:

		print("Enter User ID: ")
		uid = input()

		q = "SELECT * from user db WHERE User ID = uid"

		if mycursor.execute(q):
			print("User ID taken. Enter other user id.") 
			

		else:
			break

	q = "INSERT INTO user db (User ID, Name, Phone No., Aadhar No., Credit Card No.) VALUES (uid, name, phn, aadhar, crn)"

	mycursor.execute(q)

	mycursor.commit()

	print("LOOK IN THE CAMERA.")


	# captures 5 images of the passenger to use as test case.


	camera = cv2.VideoCapture(0)
	for i in range(5):
	    
	    return_value, image = camera.read()
	    cv2.imwrite('uid'+str(i)+'.png', image)

	del(camera)


	files = ['1.png', '2.png', '3.png', '4.png', '5.png']

	for f in files:
	    shutil.move(f, uid)

	source = 'C:/Users/nd_xing/Desktop/Project/uid'

	dest = ''

	shutil.move(source, dest) 

	print("Press Y if you wish to recharge or Press N: ")
	ch = input()

	if ch == 'Y' or ch == 'y':
		recharge()



sign_up()



			
