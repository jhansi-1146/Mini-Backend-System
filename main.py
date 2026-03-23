# mini_backend
# problem 1:Store student data
# storing the students 
import json

students = []

def load_students():
    global students
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except:
        students = []
            
#savind the students data in json file
def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


def add_student(id, name, score, attendance):
    if len(students) >= 40:
        print("Cannot add more students (limit reached: 40)")
        return False

    student = {
        "id": id,
        "name": name,
        "score": score,
        "attendance": attendance
    }

    students.append(student)
    return True


# user input for adding students
def input_students():
    while True:
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        score = float(input("Enter student score: "))
        attendance = float(input("Enter student attendance: "))

        success = add_student(id, name, score, attendance)

        if success:
            print("Student added successfully")
        else:
            print("Failed to add student")

        choice = input("Do you want to add another student (yes/no): ")
        if choice.lower() != "yes":
            break


# show students
def show_students():
    print("\n--- Student List ---")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Score: {student['score']}, Attendance: {student['attendance']}")

# problem-2: Analyzing the students data
def analyze_students():
    if len(students)==0:
        print("No students to analyze.")
        return
    total_score=0
    total_attendance=0
    top_student=students[0]
    low_student=students[0]

    for student in students:
        total_score+=student['score']
        total_attendance+=student['attendance']
        if student["score"] > top_student["score"]:
            top_student = student

        if student["score"] < low_student["score"]:
            low_student = student

    average_score=total_score/len(students)
    average_attendance=total_attendance/len(students)

    print(f"\n--- Analysis Results ---")
    print(f"Total Students: {len(students)}")
    print(f"Average Score: {average_score:.2f}")
    print(f"Average Attendance: {average_attendance:.2f}")
    print("Top Student:", top_student["name"])
    print("Lowest Student:", low_student["name"])
    

# problem-3 filter the studentsbased on the score and attendence
def filter_students():
    if len(students) == 0:
        print("No students available")
        return

    print("\n--- Filtering ---")

    print("\nHigh Scorers (score > 80):")
    for s in students:
        if s["score"] > 80:
            print(s["name"])

    print("\nLow Attendance (attendance < 60):")
    for s in students:
        if s["attendance"] < 60:
            print(s["name"])

    print("\nPassed Students (score >= 40):")
    for s in students:
        if s["score"] >= 40:
            print(s["name"])

    print("\nFailed students (score<40):")
    for s in students:
        if s["score"] < 40:
            print(s["name"])

# problem-4:prediction function
def predict_result(score):
    if score >= 40:
        return "Pass"
    else:
        return "Fail"


def performance_level(student):
    if student["score"]<40 or student["attendance"]<50:
        return "Needs Improvement"
    elif student["score"] < 50 or student["attendance"] < 60:
        return "Average Performer"
    elif student["score"] < 70:
        return "Above Average Performer"
    else:
        return "High Performer"


def show_predictions():
    if len(students) == 0:
        print("No students available")
        return

    print("\n--- Predictions ---")

    for s in students:
        result = predict_result(s["score"])
        performance = performance_level(s)

        print(f"{s['name']} -> {result} | {performance}")


# main function
def main():
    load_students()
    input_students()
    save_students()
    print("List of students:")
    show_students()
    analyze_students()
    filter_students()
    show_predictions()



# entry point
if __name__ == "__main__":
    main()