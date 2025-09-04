# Step 1: Create a dictionary with student names and their marks
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90,
    "Ethan": 88
}

# Step 2: Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display marks, or show not found message
if student_name in student_marks:
    print(student_name + "'s marks: " + str(student_marks[student_name]))
else:
    print("Student '" + student_name + "' not found in the records.")
