# Student and Course Management System

A simple Python script for managing students and courses.

## Introduction

This Python script provides a console-based application for managing students and courses. It allows users to perform various actions such as adding new students, removing students, editing student details, creating new courses, and enrolling students in courses.

## Features

- Add new students with details including name and class.
- Remove students from the list.
- Edit student details such as name and class.
- Display a list of all students along with their details.
- Create new courses with details including name and class.
- Enroll students in courses based on their class compatibility.

## Usage

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using the following command:
5. Follow the on-screen instructions to perform various actions.

## Code Overview

The script consists of two classes, `Course` and `Student`, that model courses and students, respectively. It provides a simple console-based interface to interact with these entities.

### Class: Course

- `course_id`: The unique identifier for the course.
- `course_name`: The name of the course.
- `course_class`: The class for which the course is intended.

### Class: Student

- `student_id`: The unique identifier for the student.
- `student_name`: The name of the student.
- `student_class`: The class to which the student belongs.
- `courses_list`: A list of courses the student is enrolled in.

## Usage Examples

1. Adding a new student:

   ```
   * Select Choice Please *
   1. Add New Student
   2. Remove Student
   3. Edit Student
   4. Display all students
   5. Create new Course
   6. Add Course to student
   0. Exit
   Choice: 1

   Enter Student Name: John Doe
   Select student class(A-B-C): A
   **Student Added Successfully**
   ```

2. Creating a new course:

   ```
   * Select Choice Please *
   1. Add New Student
   2. Remove Student
   3. Edit Student
   4. Display all students
   5. Create new Course
   6. Add Course to student
   0. Exit
   Choice: 5

   Enter Course Name: Math
   Select Course Class(A-B-C): B
   **Course Created Successfully**
   ```

3. Enrolling a student in a course:

   ```
   * Select Choice Please *
   1. Add New Student
   2. Remove Student
   3. Edit Student
   4. Display all students
   5. Create new Course
   6. Add Course to student
   0. Exit
   Choice: 6

   ID|            Name|            Class|
   0001            John Doe        A
   0002            Jane Smith      B
   =============================
   Enter Student ID: 0001
   ID|            Name|            Class|
   0001            Math            B
   =============================
   ```

## Requirements

- Python 3.x

## Author

- Salah El-Din Abu Saif

## License

This project is licensed under the [MIT License](https://github.com/salahsaeed19/university-system-project).

