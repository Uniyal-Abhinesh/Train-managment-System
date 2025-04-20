import sqlite3

def create_database():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            source TEXT,
            destination TEXT
        )
    ''')
    conn.commit()
    conn.close()

def book_ticket():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    source = input("Enter your source station: ")
    destination = input("Enter your destination station: ")

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO tickets (name, age, source, destination) VALUES (?, ?, ?, ?)",
              (name, age, source, destination))
    conn.commit()
    print(f" Ticket booked for {name} from {source} to {destination}.\n")
    conn.close()

    choice = input("Do you want to cancel this ticket? (yes/no): ").lower()
    if choice == "yes":
        cancel_ticket(name)
    else:
        show_train_for_ticket(source, destination)

def cancel_ticket(name=None):
    if not name:
        name = input("Enter the name for ticket cancellation: ")

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("DELETE FROM tickets WHERE name = ?", (name,))
    conn.commit()

    if c.rowcount > 0:
        print(f"Ticket cancelled for {name}.\n")
    else:
        print(f"No ticket found for {name}.\n")
    conn.close()

def show_train_for_ticket(source, destination):
    try:
        with open("train.csv", "r") as file:
            next(file)  # skip header
            for line in file:
                train_name, train_source, train_dest, seats = line.strip().split(",")
                if train_source == source and train_dest == destination:
                    print(f"\n🚆 You are traveling in Train: {train_name} with {seats} available seats.")
                    return
            print("\nNo direct train available for your route.")
    except FileNotFoundError:
        print("Train list file not found.")

def view_tickets():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tickets")
    rows = c.fetchall()

    if rows:
        print("\n🎫 Current Bookings:")
        for row in rows:
            print(row)
    else:
        print("\nNo bookings found.")
    conn.close()
