# Salah
from models import Course, Student


student_List = []
courses_List = []


def str_ID(list_text):
	long = len(list_text) + 1
	if long <= 9:
		return "000" + str(long)
	elif long <= 99:
		return "00" + str(long)
	elif long <= 999:
		return "0" + str(long)
	return str(long)


def get_students_details(students):
	print("ID|\t\tName|\t\tClass|")
	for s in students:
		print(s.get_student_details())
	print("=============================")


def find_student(students_id, students):
	index = 0
	for s in students:
		if s.student_id == students_id:
			return index
		index += 1
	return -1


def find_course(courses_id, courses):
	index = 0
	for s in courses:
		if s.course_id == courses_id:
			return index
		index += 1
	return -1


def get_courses_list(courses):
	print("ID|\t\tName|\t\tClass|")
	for s in courses:
		print(s.get_course_details())
	print("=============================")


while True:
	try:
		n = int(input("* Select Choice Please * \n1.Add New Student \n2.Remove Student \n3.Edit Student \n4.Display all students \n5.Create new Course \n6.Add Course to student \n0.Exit \n"))
		if n == 1:
			student_name = input("Enter Student Name: ")
			while True:
				student_class = input("Select student class(A-B-C): ")
				if student_class in ("A", "B", "C"):
					break
			student_id = str_ID(student_List)
			student = Student(student_id, student_name, student_class)
			student_List.append(student)
			print("**Student Added Successfully**")

		elif n == 2:
			get_students_details(student_List)
			student_id = input("Enter Student ID: ")
			student_index = find_student(student_id, student_List)
			if student_index == -1:
				print("Student Not Exist :(")
			else:
				student_List.pop(student_index)
				print("Student Removed Successfully :)")
				get_students_details(student_List)

		elif n == 3:
			get_students_details(student_List)
			student_id = input("Enter Student ID: ")
			student_index = find_student(student_id, student_List)
			if student_index == -1:
				print("Student Not Exist :(")
			else:
				student_name = input("Enter Student Name: ")
				while True:
					student_class = input("Select student class(A-B-C): ")
					if student_class in ("A", "B", "C"):
						break
				student_List[student_index].student_name = student_name
				student_List[student_index].student_class = student_class
				print("Student Details Updated Successfully :)")

		elif n == 4:
			get_students_details(student_List)

		elif n == 5:
			course_name = input("Enter Course Name: ")
			while True:
				course_class = input("Select Course Class(A-B-C): ")
				if course_class in ["A", "B", "C"]:
					break
			course_id = str_ID(courses_List)
			course = Course(course_id, course_name, course_class)
			courses_List.append(course)
			print("**Course Created Successfully**")

		elif n == 6:
			get_courses_list(courses_List)
			student_id = input("Enter Student ID: ")
			student_index = find_student(student_id, student_List)
			if student_index == -1:
				print("Student Not Exist :(")
			else:
				course_id = input("Enter Course ID: ")
				course_index = find_course(course_id, courses_List)
				if course_index == -1:
					print("Course Not Exist :(")
				else:
					student_List[student_index].enroll_course(courses_List[course_index])

		elif n == 0:
			print("Good bye :)")
			break
		else:
			print("** You must enter a number from 0 to 6 **")
	except:
		print("** You must enter a number from 0 to 6 **")
