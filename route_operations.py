from collections import defaultdict
import heapq
import random
import csv

def shortest_path(graph, start, end):
    if start not in graph or end not in graph:
        return None  # either station not in graph

    queue = [(0, start)]
    distances = {start: 0}

    while queue:
        current_distance, current_station = heapq.heappop(queue)

        if current_station == end:
            return current_distance

        for neighbor, distance in graph.get(current_station, []):
            new_distance = current_distance + distance
            if neighbor not in distances or new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))

    return None  # no path found

def get_random_train(csv_file):
    trains = []
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            trains.append(row["Train Name"])
    if trains:
        return random.choice(trains)
    else:
        return "No Train Available"

def user_search_route():
    graph = {
        "Delhi": [("Mumbai", 10)],
        "Mumbai": [("Pune", 5)],
        "Chennai": [("Hyderabad", 7)],
        "Hyderabad": [("Pune", 6)],
        "Kolkata": [("Pune", 12)]
    }

    source = input("Enter source station: ")
    destination = input("Enter destination station: ")

    distance = shortest_path(graph, source, destination)
    if distance is not None:
        print(f"✅ Shortest distance from {source} to {destination} is: {distance} units.")
        print(f"🚄 Booking confirmed on route: {source} ➝ {destination}")
    else:
        print(f"❌ No direct or connecting route from {source} to {destination}.")
        random_train = get_random_train("train.csv")
        print(f"🎫 But don't worry — you’ve been booked on {random_train} instead!")

