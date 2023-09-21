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

#if-elif-else statement will print a specific statement and/or a total price depending on the inputted name
if name == 'James':
    print("\n-Product:", data[0]['product'], "Quantity:", data[0]['quantity'], "Price:", data[0]['price'])
    print("\n-Product:", data[1]['product'], "Quantity:", data[1]['quantity'], "Price:", data[1]['price'])
    total_one = data[0]['quantity'] * data[0]['price'] + data[1]['quantity'] * data[1]['price']
    print(f'\nTotal Sales for {name}: ${total_one:.2f}')
elif name == 'Jack':
    print("\n-Product:", data[2]['product'], "Quantity:", data[2]['quantity'], "Price:", data[2]['price'])
    print("\n-Product:", data[3]['product'], "Quantity:", data[3]['quantity'], "Price:", data[3]['price'])
    total_two = data[2]['quantity'] * data[2]['price'] + data[3]['quantity'] * data[3]['price']
    print(f'\nTotal Sales for {name}: ${total_two:.2f}')
elif name == 'John':
    print("\n-Product:", data[4]['product'], "Quantity:", data[4]['quantity'], "Price:", data[4]['price'])
    total_three = data[4]['quantity'] * data[4]['price']
    print(f'\nTotal Sales for {name}: ${total_three:.2f}')
else:
    print("\nThis person is not in our purchasing database")