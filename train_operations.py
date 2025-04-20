import csv

trains = []

import csv

def display_trains_from_csv(csv_file):
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            print(f"Train: {row[0]}, From: {row[1]}, To: {row[2]}, Seats: {row[3]}")

def view_trains():
    for train in trains:
        print(f"{train['TrainName']} | {train['Source']} → {train['Destination']} | Seats: {train['Seats']}")
