import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "1234",
	database = "Project"
	)

mycursor = mydb.cursor()


def fare_calculator(start_station, end_station):
	
	q = "SELECT Fare FROM station db where Station ID = start_station"
    mycursor.execute(q)
	
	f1 = mycursor.fecthall()

	q = "SELECT Fare FROM station db where Station ID = end_station"
    mycursor.execute(q)

    f2 = mycursor.fecthall() 

    fare = f2 - f1

    if(fare<0):
    	fare  = -fare


    return fare



