import mysql.connector as sql
from datetime import date
import tabulate as tb

# Connect to MySQL
con = sql.connect(host="localhost", user="root", passwd="123456", auth_plugin="mysql_native_password")
cur = con.cursor()

# Create Database
cur.execute("CREATE DATABASE IF NOT EXISTS ticket_booking")
cur.execute("USE ticket_booking")

# Create Customers Table
cur.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        c_id INT PRIMARY KEY,
        c_name VARCHAR(100),
        c_address VARCHAR(100),
        c_aadhar VARCHAR(20),
        c_contact VARCHAR(15),
        email VARCHAR(100)
    );
""")

# Create Booking Table
cur.execute("""
    CREATE TABLE IF NOT EXISTS booking (
        B_id INT PRIMARY KEY,
        c_id INT,
        start_location VARCHAR(100),  
        stop_location VARCHAR(100),
        date_of_booking DATE DEFAULT (CURDATE()),  -- Auto-set to today's date
        date_of_journey DATE,
        FOREIGN KEY (c_id) REFERENCES customers(c_id) ON DELETE CASCADE
    );
""")

# Function to show customers
def show_customers():
    cur.execute("SELECT * FROM customers;")
    data = cur.fetchall()
    print(tb.tabulate(data, headers=["c_id", "c_name", "c_address", "c_aadhar", "c_contact", "email"]))

# Function to add a customer
def add_customer():
    c_id = int(input("Enter Customer ID: "))
    c_name = input("Enter Customer Name: ")
    c_address = input("Enter Customer Address: ")
    c_aadhar = input("Enter Aadhar Number: ")
    c_contact = input("Enter Contact Number: ")
    email = input("Enter Email: ")

    command = f"INSERT INTO customers VALUES ('{c_id}', '{c_name}', '{c_address}', '{c_aadhar}', '{c_contact}', '{email}');"
    cur.execute(command)
    con.commit()
    print("Customer added successfully!")

# Function to delete a customer
def delete_customer(c_id):
    command = f"DELETE FROM customers WHERE c_id = '{c_id}';"
    cur.execute(command)
    con.commit()
    print(f"Customer with ID {c_id} deleted successfully!")

# Function to update customer details
def update_customer(c_id):
    print("\nWhich field do you want to update?")
    print("1: Name")
    print("2: Address")
    print("3: Aadhar Number")
    print("4: Contact Number")
    print("5: Email")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        field = "c_name"
        new_value = input("Enter new Name: ")
    elif choice == 2:
        field = "c_address"
        new_value = input("Enter new Address: ")
    elif choice == 3:
        field = "c_aadhar"
        new_value = input("Enter new Aadhar Number: ")
    elif choice == 4:
        field = "c_contact"
        new_value = input("Enter new Contact Number: ")
    elif choice == 5:
        field = "email"
        new_value = input("Enter new Email: ")
    else:
        print("Invalid choice! Returning to menu.")
        return

    command = f"UPDATE customers SET {field} = '{new_value}' WHERE c_id = '{c_id}';"
    cur.execute(command)
    con.commit()
    print(f"{field} updated successfully!")

# Function to show bookings
def show_bookings():
    cur.execute("SELECT * FROM booking;")
    data = cur.fetchall()
    print(tb.tabulate(data, headers=["B_id", "c_id", "start_location", "stop_location", "date_of_booking", "date_of_journey"]))

# Function to add a booking
def add_booking():
    B_id = int(input("Enter Booking ID: "))
    c_id = int(input("Enter Customer ID: "))
    start_location = input("Enter Start Location: ")
    stop_location = input("Enter Stop Location: ")
    date_of_journey = input("Enter Date of Journey (YYYY-MM-DD): ")

    today = date.today()
    command = f"INSERT INTO booking VALUES ('{B_id}', '{c_id}', '{start_location}', '{stop_location}', '{today}', '{date_of_journey}');"
    cur.execute(command)
    con.commit()
    print("Booking added successfully!")

# Function to delete a booking
def delete_booking(B_id):
    command = f"DELETE FROM booking WHERE B_id = '{B_id}';"
    cur.execute(command)
    con.commit()
    print(f"Booking with ID {B_id} deleted successfully!")

# Function to update a booking
def update_booking(B_id):
    print("\nWhich field do you want to update?")
    print("1: Start Location")
    print("2: Stop Location")
    print("3: Date of Journey")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        field = "start_location"
        new_value = input("Enter new Start Location: ")
    elif choice == 2:
        field = "stop_location"
        new_value = input("Enter new Stop Location: ")
    elif choice == 3:
        field = "date_of_journey"
        new_value = input("Enter new Date of Journey (YYYY-MM-DD): ")
    else:
        print("Invalid choice! Returning to menu.")
        return

    command = f"UPDATE booking SET {field} = '{new_value}' WHERE B_id = '{B_id}';"
    cur.execute(command)
    con.commit()
    print(f"{field} updated successfully!")

# Menu-driven program
while True:
    print("\n----------------------------")
    print("\tCUSTOMER MANAGEMENT")
    print("----------------------------")
    print("1: Show Customers")
    print("2: Add Customer")
    print("3: Delete Customer")
    print("4: Update Customer Details")

    print("\n----------------------------")
    print("\tBOOKING MANAGEMENT")
    print("----------------------------")
    print("5: Show Bookings")
    print("6: Add Booking")
    print("7: Delete Booking")
    print("8: Update Booking Details")

    print("\n0: Exit")
    print("----------------------------")

    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        show_customers()
    elif choice == 2:
        add_customer()
    elif choice == 3:
        c_id = int(input("Enter Customer ID to delete: "))
        delete_customer(c_id)
    elif choice == 4:
        c_id = int(input("Enter Customer ID to update: "))
        update_customer(c_id)
    elif choice == 5:
        show_bookings()
    elif choice == 6:
        add_booking()
    elif choice == 7:
        B_id = int(input("Enter Booking ID to delete: "))
        delete_booking(B_id)
    elif choice == 8:
        B_id = int(input("Enter Booking ID to update: "))
        update_booking(B_id)
    elif choice == 0:
        print("Thank You!")
        break
    else:
        print("Invalid choice, please try again.")
