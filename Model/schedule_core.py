import Dao.load


class ScheduleCore:
	def __init__(self, semester_year):
		self.courses = {}
		self.semester_year = semester_year
		self.data = {}
		Dao.load.load_courses(semester_year, self.data)
		self.possible_schedules = []

	def add_course(self, course_name):
		dept = course_name.split(" ")[0]
		num = ""
		suffix = ""
		switch = True
		for ch in course_name.split(" ")[1]:
			if switch and ch.isnumeric():
				num += ch
			else:
				switch = False
				if not ch.isnumeric():
					suffix += ch
				else:
					break

		class_code = Dao.load.get_class_code(self.semester_year, dept, num, suffix)
		if class_code is None:
			raise ValueError("course not found")
		if class_code in self.courses.keys():
			return

		self.courses[class_code] = {"all_sections": self.data[class_code]["sections"], "selected_sections": [],
		                            "deselected_sections": []}

	def calculate_possible_schedules(self):
