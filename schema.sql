CREATE TABLE IF NOT EXISTS trains (
    train_id INTEGER PRIMARY KEY AUTOINCREMENT,
    train_name TEXT NOT NULL,
    source TEXT NOT NULL,
    destination TEXT NOT NULL,
    seats INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    passenger_name TEXT NOT NULL,
    train_id INTEGER NOT NULL,
    seat_no INTEGER NOT NULL,
    FOREIGN KEY (train_id) REFERENCES trains(train_id)
);
