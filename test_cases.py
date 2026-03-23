import json

from main import add_student, predict_result, performance_level, students



# Test Add Student

def test_add_student():
    students.clear()

    add_student("S1", "Ram", 80, 70)

    if len(students) == 1:
        print("test_add_student passed")
    else:
        print("test_add_student failed")


# Test Predict Result

def test_predict_result():
    if predict_result(80) == "Pass" and predict_result(30) == "Fail":
        print("test_predict_result passed")
    else:
        print("test_predict_result failed")



# Test Performance Level

def test_performance_level():
    s1 = {"score": 30, "attendance": 40}
    s2 = {"score": 85, "attendance": 80}

    if (performance_level(s1) == "Needs Improvement" and
        performance_level(s2) == "High Performer"):
        print("test_performance_level passed")
    else:
        print("test_performance_level failed")



# Test JSON file handling

def test_json_storage():
    students.clear()

    students.append({
        "id": "S1",
        "name": "Ram",
        "score": 80,
        "attendance": 70
    })

    # Save to test file
    with open("test_students.json", "w") as file:
        json.dump(students, file)

    # Clear memory
    students.clear()

    # Load from test file
    with open("test_students.json", "r") as file:
        data = json.load(file)

    if len(data) == 1 and data[0]["name"] == "Ram":
        print("test_json_storage passed")
    else:
        print("test_json_storage failed")



# Run Tests

def run_tests():
    print("Running test cases...\n")

    test_add_student()
    test_predict_result()
    test_performance_level()
    test_json_storage()

    print("\nDone testing!")


# Entry point
if __name__ == "__main__":
    run_tests()