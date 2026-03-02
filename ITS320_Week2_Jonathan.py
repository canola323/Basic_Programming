#-------------------------------------------
# Program Name: Travel Itinerary Organizer
# Author: Jonathan Canola
# Date: 03/02/2025
#-------------------------------------------
# Pseudocode: 
# 1. Start
# 2. DISPLAY "welcome message"
# 3. DISPLAY "Intro"
# 4. Create empty destination list
# 5. BOOLEAN variable set to true
# 6. WHILE loop variable 
# 7. INPUT "name for city"
# 8. INPUT "name for country"
# 9. INPUT "duration in city"
# 10. INPUT "budget for city"
# 11. IF "days" and "budget" are digits then days and budget = int
# 12. Create dictionary for input data
# 13. Store dictionary in destinations list
# 14. DISPLAY successfully stored ELSE DISPLAY error 
# 15. DISPLAY "more destinations message? (yes/no)"
# 16. DISPLAY "travel itinerary"
#-------------------------------------------
# Program Inputs: Gets city name, country, duration at destination, budget
# Program Outputs: Formatted travel itinerary from input data
#-------------------------------------------

# Welcome message
print(f"Welcome to your Travel Itinerary Organizer!")
# Leaves a blank line
print("")
# Intro
print(f"To get started we will ask you a few qestions about your travel plans.")

# Creates empty lsit for destinations
destinations = []
# Variable to tell the loop to stop
moreDestinations = True

# Loop through destination data for itinerary till complete
while moreDestinations:
    cityName = input("\nEnter the name of the city for the destination: ")
    country = input("Enter the name of the country for the city: ")
    cityDays = input("Enter duration of days spend in city: ")
    cityBudget = input("Enter the allocated budget for city: ")

    # If input for days and budget arnt integers send back error message
    if cityDays.isdigit() and cityBudget.isdigit():
        days = int(cityDays)
        budget = int(cityBudget)

        # Store input data together per destination
        itineraryData = {
            "city": cityName,
            "country": country,
            "duration": cityDays,
            "budget": cityBudget 
        }
        # Adds stored input data to destinations list
        destinations.append(itineraryData)
        # Let user know destination was added 
        print(f"Destination {cityName} added to itinerary.")
    else:
        print("Error in entry: Destination not saved!")
    # Asks user if they want to add another destination if not stops loop
    addMore = input("Would you like to add another destination? (yes/no): ")
    if addMore == "no":
        moreDestinations = False

# Displays travel itinerary from user input
print("\nTravel Itinerary")
print(" ")

for trip in destinations:
    print(f"City: {trip['city']}")
    print(f"Country: {trip['country']}")
    print(f"Duration of Stay: {trip['duration']} days")
    print(f"Allocated Budget: ${trip['budget']}")
    print()