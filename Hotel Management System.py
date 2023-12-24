import mysql.connector
# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="hotel"
)

cursor = connection.cursor()
# Function to execute queries
def execute_query(query, data=None):
    try:
        cursor.execute(query, data)
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Create tables if not exists
execute_query("""
    CREATE TABLE IF NOT EXISTS customer (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        address VARCHAR(255) NOT NULL,
        phone VARCHAR(15) NOT NULL,
        id_proof VARCHAR(50) NOT NULL,
        id_proof_no VARCHAR(50) NOT NULL,
        total_customer INT NOT NULL
    )
""")

execute_query("""
    CREATE TABLE IF NOT EXISTS room (
        room_no INT AUTO_INCREMENT PRIMARY KEY,
        type VARCHAR(50) NOT NULL,
        status VARCHAR(20) NOT NULL,
        rent INT NOT NULL
    )
""")

execute_query("""
    CREATE TABLE IF NOT EXISTS booking (
        booking_id INT AUTO_INCREMENT PRIMARY KEY,
        room_no INT NOT NULL,
        customer_id INT NOT NULL,
        check_in_date DATE NOT NULL,
        check_out_date DATE NOT NULL,
        FOREIGN KEY (room_no) REFERENCES room(room_no),
        FOREIGN KEY (customer_id) REFERENCES customer(id)
    )
""")

execute_query("""
    CREATE TABLE IF NOT EXISTS bill (
        bill_no INT AUTO_INCREMENT PRIMARY KEY,
        customer_id INT NOT NULL,
        total_amount INT NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customer(id)
    )
""")

execute_query("""
    INSERT INTO room (type, status, rent) VALUES(
        ('Single', 'Free', 1500),
        ('Double', 'Free', 3000),
        ('Suite', 'Free', 6000))""")

def delete_booking_by_room_no(room_no):
    # Check if the booking exists
    execute_query(f"SELECT * FROM booking WHERE room_no = {room_no}")
    booking_info = cursor.fetchone()

    if booking_info:
        # Update room status to Free
        execute_query(f"UPDATE room SET status = 'Free' WHERE room_no = {room_no}")

        # Delete booking record
        execute_query(f"DELETE FROM booking WHERE room_no = {room_no}")

        print("Booking canceled successfully.")
    else:
        print("No booking found for the specified room.")


# Function to insert data into the database
def insert_data(table, data):
    placeholders = ', '.join(['%s'] * len(data))
    columns = ', '.join(data.keys())
    query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
    execute_query(query, tuple(data.values()))

# Function to display options
def display_options(options):
    for key, value in options.items():
        print(f"[{key}] {value}")

while True:
    print("\n" + "*" * 50)
    print("Welcome to Hotel Management System")
    print("*" * 50)
    
    options = {
        1: "Customer Details",
        2: "Room Info",
        3: "Refreshment",
        4: "Bill",
        5: "Exit"
    }

    display_options(options)
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        # Customer Details
        print("\n" + "=" * 50)
        print("Customer Details")
        print("=" * 50)

        # Get customer details
        customer_data = {
            'name': input('Enter Customer Name: '),
            'address': input('Enter Customer Address: '),
            'phone': input('Enter Customer Phone NO: '),
            'id_proof': input('Enter Customer ID(Aadhar/Passport/DL/VoterID): '),
            'id_proof_no': input('Enter Customer ID proof NO: '),
            'total_customer': int(input('Enter number of Members: '))
        }

        # Insert customer data into the database
        insert_data('customer', customer_data)
        print("Customer added successfully!")

    elif choice == 2:
        # Room Info
        print("\n" + "=" * 50)
        print("Room Info")
        print("=" * 50)

        options_room = {
            1: "Room Preview",
            2: "Room Booking",
            3: "Cancel Booking",
            4: "Exit to main menu"
        }

        display_options(options_room)
        choice_room = int(input("Enter your choice: "))

        if choice_room == 1:
            # Room Preview
            execute_query("SELECT * FROM room")
            rooms = cursor.fetchall()
            for room in rooms:
                print(room)

        elif choice_room == 2:
            # Room Booking
            room_no = input('Enter room no to book: ')
            customer_id = input('Enter customer ID: ')
            check_in_date = input('Enter date of occupancy (yyyy-mm-dd): ')
            check_out_date = input('Enter date of leaving (yyyy-mm-dd): ')

            # Check if the room is available
            execute_query(f"SELECT * FROM room WHERE room_no = {room_no} AND status = 'Free'")
            room_status = cursor.fetchone()

            if room_status:
                # Update room status to occupied
                execute_query(f"UPDATE room SET status = 'Occupied' WHERE room_no = {room_no}")

                # Insert booking details into the database
                booking_data = {
                    'room_no': int(room_no),
                    'customer_id': int(customer_id),
                    'check_in_date': check_in_date,
                    'check_out_date': check_out_date
                }
                insert_data('booking', booking_data)

                print(f'Room {room_no} booked successfully for Customer {customer_id}')

            else:
                print(f'Room {room_no} is not available for booking.')

        elif choice_room == 3:
            # Cancel Booking
            room_no_cancel = input("Enter your room number: ")
            delete_booking_by_room_no(room_no_cancel)

        elif choice_room == 4:
            # Exit to main menu
            pass

        else:
            print("Invalid choice!")

    elif choice == 3:
        # Refreshment
        print("\n" + "=" * 50)
        print("Refreshment")
        print("=" * 50)

        options_refreshment = {
            1: "Refreshment Menu",
            2: "Exit to main menu"
        }

        while True:
            display_options(options_refreshment)
            choice_refreshment = int(input("Enter your choice: "))

            if choice_refreshment == 1:
                # Refreshment Menu
                print("\n" + "*" * 50)
                print("Available Food")
                print("*" * 50)

                food_menu = {
                    1: "Tea ---> 10",
                    2: "Coffee ---> 15",
                    3: "Samosa ---> 10",
                    4: "Sandwich ---> 30",
                    5: "Colddrink ---> 20",
                    6: "Pasta ----> 40",
                    7: "Exit to main menu"
                }

                display_options(food_menu)
                choice_food = int(input("Enter your choice: "))

                if choice_food == 7:
                    break

                # Process food order
                print(f"You have ordered: {food_menu[choice_food]}")
                quantity = int(input("Enter Quantity: "))
                total_amount = quantity * int(food_menu[choice_food].split(' ---> ')[1])
                print(f"Your amount for {food_menu[choice_food]}: {total_amount}")

            elif choice_refreshment == 2:
                # Exit to main menu
                break

            else:
                print("Invalid choice!")

    elif choice == 4:
        # Bill
        print("\n" + "=" * 50)
        print("Room Bill")
        print("=" * 50)

        options_bill = {
            1: "Generate Room Bill",
            2: "Exit to main menu"
        }

        display_options(options_bill)
        choice_bill = int(input("Enter your choice: "))

        if choice_bill == 1:
            # Generate Room Bill
            room_no_bill = input("Enter your room number: ")
            customer_id_bill = input("Enter customer ID: ")

            # Check if the booking exists
            execute_query(f"SELECT * FROM booking WHERE room_no = {room_no_bill} AND customer_id = {customer_id_bill}")
            booking_info_bill = cursor.fetchone()

            if booking_info_bill:
                # Get room rent per day
                execute_query(f"SELECT rent FROM room WHERE room_no = {room_no_bill}")
                room_rent = cursor.fetchone()[0]

                # Calculate total amount based on the number of days
                check_in_date_bill = booking_info_bill[3]
                check_out_date_bill = booking_info_bill[4]
                total_days = (check_out_date_bill - check_in_date_bill).days
                total_amount_bill = total_days * room_rent

                # Display bill details
                print(f"Date of Occupancy: {check_in_date_bill}")
                print(f"Date of Leaving: {check_out_date_bill}")
                print(f"Total Payable Days: {total_days}")
                print(f"Room Rent Per Day: {room_rent}")
                print(f"Total Amount: {total_amount_bill}")

                # Update room status to Free
                execute_query(f"UPDATE room SET status = 'Free' WHERE room_no = {room_no_bill}")

                # Delete booking record
                execute_query(f"DELETE FROM booking WHERE room_no = {room_no_bill} AND customer_id = {customer_id_bill}")

                # Insert bill record
                bill_data = {
                    'customer_id': int(customer_id_bill),
                    'total_amount': total_amount_bill
                }
                insert_data('bill', bill_data)

                print("Bill generated successfully.")

            else:
                print("No booking found for the specified room and customer ID.")

        elif choice_bill == 2:
            # Exit to main menu
            pass

        else:
            print("Invalid choice!")

    elif choice == 5:
        # Exit
        print("\n" + "=" * 50)
        print("Thanks For Visiting! Please Come Again.")
        print("=" * 50)
        break

    else:
        print("Invalid choice!")

# Close the cursor and connection
cursor.close()
connection.close()
