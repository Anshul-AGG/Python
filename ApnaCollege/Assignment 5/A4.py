import json

# Step 1: Create dictionary and save to JSON
cities = {"Delhi": 1000000, "Kanpur": 12000, "Lucknow": 1234441}

with open("cities.json", "w") as f:
    json.dump(cities, f, indent=4)

# Step 2: Load and print each city and population
with open("cities.json", "r") as f:
    loaded_cities = json.load(f)

print("Current cities and populations:")
for city, population in loaded_cities.items():
    print(f"{city}: {population}")

# Step 3: Add new city and update JSON
new_city = input("Enter a new city name: ")
new_population = int(input(f"Enter the population of {new_city}: "))
loaded_cities[new_city] = new_population

with open("cities.json", "w") as f:
    json.dump(loaded_cities, f, indent=4)

print(f"\nUpdated cities.json with {new_city}.")
