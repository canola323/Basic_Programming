#-------------------------------------------
# Program Name: Student Grade Calculator
# Author: Jonathan Canola
# Date: 02/24/2026
#-------------------------------------------
# Pseudocode: 
# 1. Start 
# 2. DISPLAY "welcome message"
# 3. INPUT "ask user for name"
# 4. INPUT "ask user for assignment1"
# 5. INPUT "ask user for assignment2"
# 6. INPUT "ask user for assignment3"
# 7. FLOAT INPUT "ask user for gradeScore1"
# 8. FLOAT INPUT "ask user for gradeScore2"
# 9. FLOAT INPUT "ask user for gradeScore3"
# 10. Add together gradeScore's = totalScore
# 11. Average score = Divide totalScore by number of assignments
# 12. DISPLAY OUTPUT = "title, student name, assignments, grades, total score, average score
# 13. END
#-------------------------------------------
# Program Inputs: Get students name, Get name of 3 assignments, Get Score for 3 assignments
# Program Outputs: Print students name, Print assignment names, Print assignment scores, Print total score, Print average score
#-------------------------------------------



# 1. Welcome message
print("Welcome to the student grading calculator.")

# 2. Gets student information
# Asks user for name using input()
studentName = input("Enter student name: ")

# Asks user for assingment names 
assignment1 = input("Enter first assignment: ")
assignment2 = input("Enter second assignment: ")
assignment3 = input("Enter third assignment: ")

# Gets scores for assignments using input() and converting to float()
gradeScore1 = float(input(f"Please enter score for {assignment1}."))
gradeScore2 = float(input(f"Please enter score for {assignment2}."))
gradeScore3 = float(input(f"Please enter score for {assignment3}."))

# 3. Calculates and retireves students grade
# Gets the total score by adding each assignement score 
totalScore = gradeScore1 + gradeScore2 + gradeScore3
# Gets the average score by dividing the total score by number of assignments.
averageScore = totalScore / 3

# 4. Displays Grade Report
# Using print to display output and f strings to format
print("Student Grade Report")
print(f"Student Name: {studentName}")
print(f"{assignment1} score: {gradeScore1}")
print(f"{assignment2} score: {gradeScore2}")
print(f"{assignment3} score: {gradeScore3}")
print(f"Total Score: {totalScore}")
print(f"Average Score: {averageScore}")