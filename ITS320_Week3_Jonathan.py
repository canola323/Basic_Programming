#-------------------------------------------
# Program Name: Weather-Based Outfit Advisor
# Author: Jonathan Canola
# Date: 03/10/2026
#-------------------------------------------
# Pseudocode: 
# 1. Start
# 2. DISPLAY "welcome message"
# 3. WHILE true INPUT("Current temp")
# 4. IF currrentTemp greater less than -5 and 120 store
# 5. ELSE DISPLAY "error" Validate numeric input
# 6. Establish weather tpye options
# 7. WHILE true INPUT("Current weather type")
# 8. IF weatherType is in weatherOptions store 
# 9. ELSE DISPLAY "error"
# 10. WHILE true INPUT("Current wind speed")
# 11. IF windSpeed is greater less than 0 and 150 store
# 12. ELSE DISPLAY "error" Validate numeric input
# 13. DISPLAY "Outfit suggestion"
#-------------------------------------------
# Program Inputs: Weather conditions (temperature, wind speed, weather type).
# Program Outputs: Outfit suggestion based on current weather conditions.
#-------------------------------------------

#Dispalys welcome message
print("Welcome to Your Outfit Adisor!")
#spacing
print(" ")
#Instruct message
print("To get started I will ask you a few question to better assit you.")

print("")

#Loops through and validates user input for numeric input between -5 and 120
while True:
    temperature = input(f"What is the current temperature?: ")
    try:
        currentTemp = float(temperature)
        
        if -5 <= currentTemp <= 120:
            print(f"Okay got it current temperature is {currentTemp} degrees!")
            #exits loop
            break
        else:
            #Displays invalid input message
            print(f"Please enter a valid temperature.")
    #Displays invalid numeric message 
    except ValueError:
        print(f"Invalid input not a numeric value. Please try again!")
#Variable stores options for weather types
weather_options =[f"sunny", "rainy", "snowy", "cloudy"]
#Loops through and validates user input for weather tpye in weather options variable
while True:
    weather_type = input(f"What is the current weather type (e.g., sunny, rainy, snowy)?: ").lower()

    if weather_type in weather_options:
        print(f"Okay got it today is a {weather_type} day!")
        break
    else:
        print(f"Sorry that answer is invalid. Please enter a valid type of weather.")
#Loops through and validates user input for numeric input between 0 and 150
while True:
    wind_speed = input(f"What is the current wind speed?: ")
    try:
        current_speed = float(wind_speed)

        if 0 <= current_speed <= 150:
            print(f"Okay got it current wind speed is {current_speed}mph!")
            break
        else:
            print(f"Please enter a realistic wind speed.")
    except ValueError:
        print(f"Invalid input not a numeric value. Please try again!")

print("")
#Outline
print("-----------------------------------")
#Displays results title
print("Outfit Suggestion Results!")

print("-----------------------------------")
#Selection statment to display suggested outfit based on current conditions
if currentTemp < 40 and wind_speed > 14:
    print(f"Based on current conditions: Coat and scarf is your outfit suggestion.")
elif 40 <= currentTemp <= 70 and weather_type == "sunny":
    print(f"Based on current conditions: Light jacket and jeans is your outfit suggestion.")
elif 5 <= currentTemp <= 60 and weather_type == "snowy":
    print(f"Based on current conditions: Snow suit and snow boots is your outfit suggestion.")
elif 40 <= currentTemp <= 72 and weather_type == "rainy":
    print(f"Based on current conditions: Rain coat and rain boots is your outfit suggestion.")
elif currentTemp > 70 and weather_type == "sunny":
    print(f"Based on current conditions: T-shirt and shorts is your outfit suggestion.")
else:
    print(f"Based on the current conditions the weather seems unpredictable!")

print("------------------------------------")