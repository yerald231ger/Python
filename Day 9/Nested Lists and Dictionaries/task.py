capitals = {
    "USA": "Washington",
    "France": "Paris",
}

travel_log = {
    "USA": ["Washington", "New York"],
    "France": ["Paris", "Lille"],
}

print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"], "E"]

print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille"],
        "number_of_visits": 12,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "number_of_visits": 5,
    }
}
print(travel_log["Germany"]["cities_visited"][2])
