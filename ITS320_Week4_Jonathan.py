#-------------------------------------------
# Program Name: Voting Registration System
# Author: Jonathan Canola
# Date:03/14/2026
#-------------------------------------------
# Pseudocode:
# 1. Start
# 2. Display welcome message
# 3. Create candidate list
# 4. Create empty voter dictionary
# 5. Create Main Menu loop
# 6. Display options in menu to register voter, display registerd voters, search for voter, and exit program
# 7. Create Register New Voter loop 
# 8. INPUT voter age
# 9. INPUT voter candidate choice
# 10. INPUT voter ID
# 11. Store voter in dictionary
# 12. DISPLAY message to exit to register voter loop
# 13. Create Display Rigisterd Voter loop
# 14. DISPLAYS registered voters if stored is voters dictionary
# 15. Create Voter Search loop
# 16. INPUT voter ID
# 17. IF valid ID DISPLAY voter if not ERROR message
# 18. Create EXIT loop
# 19. DISPLAY goodbye message and exit main menu loop
#-------------------------------------------
# Program Inputs: Voter age, candidate choice, id
# Program Outputs: Voter data 
#-------------------------------------------

# Displays welcome message
print(" Welcome to the Voting Registration System. ")
# spacing
print(" ")
# List of possible candidates
candidate_options = ["Alice", "Bob", "Charlie"]\
# Empty voters dictionary
voters = []

main_menu = True
# Main loop for voter program 
while main_menu:
    # Displays options for main menu
    print("MAIN MENU")
    print("1. Register New Voter")
    print("2. Display All Registered Voters")
    print("3. Search for a Voter")
    print("4. Exit ")
    # Asks user select which option to jump to
    option = input("Select an option: ").strip()
    # Option 1 contains voter registration questions   
    if option == "1":
        while True:
            print("ENTER NEW VOTER")
            print("--------------------------------")
            # Holds voter info to be put in dictionary
            current_voter = {}
            # Voter Age
            age_completed = False   
            while not age_completed:
                # Asks user for age
                voter_age = input("Enter your age: ").strip()
                # Validates user input is a number 
                if voter_age.isdigit():
                    age = int(voter_age)
                    # Vealidates that input is between 18 and 120 if so save input if not return error message
                    if 18 <= age <= 120:
                        current_voter["age"] = age
                        age_completed = True
                    else:
                        print("Error: Please enter valid age minimum requirment of 18.")
                else:
                    print("Error. Please enter a valid age.")
            # Voter Candidate Choice
            candidate_completed = False
            while not candidate_completed:
                # Asks user for candidate selection
                voter_candidate = input("Enter candidate selection: ").capitalize().strip()
                # Validates user input is in the candidate list, if so saves input if not displays error message
                if voter_candidate in candidate_options:
                    candidate = voter_candidate
                    current_voter["candidate"] = candidate
                    candidate_completed = True
                else:
                    print("Error: please enter valid candidate.")
            # Voter ID
            id_completed = False
            while not id_completed:
                # Asks user to create voter ID 
                voter_id = input("Create a unique voter ID. Enter atleast 8 characters minimum: ").strip()
                # Validates user input if alpha numerical if not prints error message
                if voter_id.isalnum():
                    id = voter_id
                    # Validates user input is between 8 to 15 characters if not prints error message  
                    if 8 <= len(id) <= 15:
                        current_voter["id"] = id
                        id_completed = True
                    else:
                        print("Error: Please create voter ID between 8 and 15 characters. ")
                else:
                    print("Error: Please enter valid voter ID.")

            # Saves voters info to voter dictionary    
            voters.append(current_voter)
            print("Registered Successfully!")
            # Asks user if they want to start voter loop over to register new voter if not exit to main menu
            action = input("Do you want to add another voter? Enter 'No' to finish or 'Yes' to add another: ").lower().strip()
            if action == "no":
                break
    # Option 2 displays registered voters       
    elif option == "2":   
        # If not voters registered displays error message
        if not voters:
            print("\nError: No voters registered.")
        else:
            print(" ")
            # Displays registered voters 
            print("\nRegistered Voters")
            print(f"\n{'Voter ID':<15} | {'Age':<5} | {'Candidate'}")
            # Creates a 50 dash boarder
            print("-" * 50 )
            for voter in voters:
                print(f"{voter['id']:<15} | {voter['age']:<5} | {voter['candidate']}")
    # Option 3 allows user to search for registered voters by ID
    elif option == "3":
        # Asks user for voter ID
        find_id = input("Enter Voter ID: ").strip()
        id_found = False
        for voter in voters:
            # Searches for ID in voters dictionary if found dispays voter if not displays error message
            if voter['id'] == find_id:
                # Creates a 60 dash boarder 
                print("-" * 60)
                print(f"Registered Voter: ID: {voter['id']} | Age: {voter['age']} | Candidate: {voter['candidate']}")
                print("-" * 60)
                id_found = True
                break
        if not id_found:
            print("Error: ID not found.")
    # Option 4 exits program with goodbye message
    elif option == "4":
        print("-" * 50)
        print("Exited program. Goodbye!")
        print("-" * 50)
        main_menu = False
    # Dispalys error message if selection from main menu is invalid 
    else:
        print("Error: Please enter valid selection.")