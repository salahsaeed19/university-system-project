class Course:

	def __init__(self, course_id, course_name, course_class):
		self.course_id = course_id
		self.course_name = course_name
		self.course_class = course_class

	def get_course_details(self):
		print(str(self.course_id) + "\t" + self.course_name + "\t\t" + self.course_class)


class Student:

	def __init__(self, student_id, student_name, student_class):
		self.student_id = student_id
		self.student_name = student_name
		self.student_class = student_class
		self.courses_list = []

	def enroll_course(self, course):
		if self.student_class == course.course_class:
			for i in self.courses_list:
				if course.course_id == i.course_id:
					print("Course Already Enrolled ;)")
					return
			self.courses_list.append(course)
			print("Course Enrolled Successful :)")
		else:
			# course.list_of_course.append(course)
			print("Invalid Course Class :(")

	def get_student_details(self):
		print(str(self.student_id) + " \t" + self.student_name + "\t\t" + self.student_class)
		if len(self.courses_list) == 0:
			print("Courses List Empty ")
			return
		print("Courses List >>> ")
		for course in self.courses_list:
			print(course.course_name)
