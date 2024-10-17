# Function to determine grade based on the score
def calculate_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    elif 50 <= score <= 59:
        return "E"
    else:
        return "Fail"

# Loop to take input for multiple students and display their grades
def grade_students():
    num_students = int(input("Enter the number of students: "))
    for i in range(num_students):
        score = int(input(f"Enter the score for student {i+1}: "))
        grade = calculate_grade(score)
        print(f"Student {i+1}'s grade: {grade}")
        
grade_students()

