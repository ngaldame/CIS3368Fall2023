import mysql.connector
from mysql.connector import Error


# Create the connection function
def conn_creation(hostname, uname, passwd, dbname):
    connection = None

    try:
        connection = mysql.connector.connect(
            host=hostname,
            user=uname,
            password=passwd,
            database=dbname
        )
        print("The connection is working successfully\n")
    except Error as e:
        print("The connection has failed with error: ", e)
    return connection


# Create a connection object
cn = conn_creation("cis3368hw1.cibekdf7zgry.us-east-1.rds.amazonaws.com", "admin", "Ngg12345", "cis3368hw1db")

# Connect to database and fetch data from the database
personalcursor = cn.cursor(dictionary=True)
seq = "select * from sales"
personalcursor.execute(seq)
rows = personalcursor.fetchall()

# data is a list that will present each row as a dictionary
data = [
    {'id': 1, 'seller': 'James', 'product': 'Pen', 'quantity': 40, 'price': 1.99},
    {'id': 2, 'seller': 'James', 'product': 'Notebook', 'quantity': 23, 'price': 2.98},
    {'id': 3, 'seller': 'Jack', 'product': 'Pencil', 'quantity': 31, 'price': 0.79},
    {'id': 4, 'seller': 'Jack', 'product': 'Marker', 'quantity': 18, 'price': 1.39},
    {'id': 5, 'seller': 'John', 'product': 'Binder', 'quantity': 50, 'price': 1.78},
]

# Print the available sellers and get input to show the selected seller's purchases and total payment
print(rows, "\n\nAvailable sellers:\n")
for row in data:
    print(row['seller'])

name = input("\nEnter the seller's name:\n")
