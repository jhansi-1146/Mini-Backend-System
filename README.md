# Track 3: Mini Backend System 

# Project Overview:

This project is a lightweight Python-based application designed to manage and analyze student data efficiently.

It provides functionality to:

Store student records
Perform data analysis
Filter students based on criteria
Predict academic outcomes

The system also ensures data persistence using a JSON file, allowing data to be retained across multiple executions.

#  Key Features:

The system is organized into four core functional tracks:

# 1. Student Data Storage
Persistent Storage: Saves student records to a students.json file.

Automatic Loading: Reloads existing data upon startup.

Capacity Management: Includes a safeguard to limit the database to 40 students.

Attributes: Tracks ID, Name, Score, and Attendance.

# 2. Analytics Engine
Calculates class-wide Average Score and Average Attendance.

Identifies the Top Performer and the student with the Lowest Score automatically.

# 3. Filtering System
Provides quick insights by segmenting students into three categories:

High Scorers: Students with a score > 80.

Low Attendance: Students with attendance < 60%.

Pass List: Students who met the minimum passing score (>= 40).

Fail List: Students who did not meet the passing score (< 40).

# 4. Prediction Logic
An intelligent categorization system that labels students based on their performance and attendance:

High Performer: Score >= 70.

Above Average: Score 50–69.

Average Performer: Score 40–49 or attendance 50–59%.

Needs Improvement: Score < 40 or attendance < 50%.

# File Structure:

main.py: The primary application containing the data logic, analytics, and user interface.

test_cases.py: A dedicated script to validate that functions like adding students and prediction logic work correctly.

students.json: (Auto-generated) Stores the student data in a structured format.

# Installation and setup:

Clone the Repository
https://github.com/jhansi-1146/Mini_-Backend_System.git

Prerequisites:
Python 3.x installed on your system.

Running Applications:

1.To start the program and add students to your database:
    python main.py
Follow the on-screen prompts to enter student details. Once finished, the system will display the list, the analysis, and the performance predictions.

2.To verify that the backend logic is functioning as expected:
    python test_cases.py

# Testing Overview:

The test_cases.py script performs the following checks:

Add Student: Verifies if a student object is correctly added to the list.

Predict Result: Ensures the Pass/Fail logic is accurate based on scores.

Performance Level: Tests if the categorization logic (e.g., "High Performer") works for different data sets.

JSON Storage: Confirms that data can be written to and read from a file without corruption.

# Assumptions:

Scores and attendance are provided as numeric values
Passing threshold is set at 40 marks
Maximum number of students is limited to 40
Data is stored locally (no external database)


