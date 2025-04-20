from train_operations import display_trains_from_csv
from ticket_operation import create_database, book_ticket, view_tickets
from route_operations import user_search_route

# Initialize the database
create_database()

while True:1
    print("\n====== Train Management System ======")
    print("1️⃣ View Available Trains")
    print("2️⃣ Book Ticket")
    print("3️⃣ View Booked Tickets")
    print("4️⃣ Find Shortest Route")
    print("5️⃣ Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        display_trains_from_csv("train.csv")
    elif choice == '2':
        book_ticket()
    elif choice == '3':
        view_tickets()
    elif choice == '4':
        user_search_route()
    elif choice == '5':
        print(" Exiting Train Management System. Have a great day!")
        break
    else:
        print(" Invalid choice. Please select a valid option.")
