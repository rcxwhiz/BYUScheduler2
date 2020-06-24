import itertools

import Dao.load


class ScheduleCore:
	def __init__(self, semester_year):
		self.courses = {}
		self.semester_year = semester_year
		self.data = {}
		Dao.load.load_courses(semester_year, self.data)
		self.possible_schedules = []

	def add_course(self, course_name):
		# TODO fix this using re
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

		self.courses[class_code] = []
		for section in self.data[class_code]["sections"]:
			self.courses[class_code].append({"course": class_code, "data": section, "selected": False, "deselected": False})

	def calculate_possible_schedules(self):
		if len(self.courses) == 0:
			self.possible_schedules = []
		if len(self.courses) == 1:
			self.possible_schedules = list(self.courses.values())[0]

		self.possible_schedules = list(itertools.product(*list(self.courses.values())))
		for schedule in self.possible_schedules:
			for pair in itertools.combinations(schedule, 2):
				if sections_collide(*pair):
					self.possible_schedules.remove(schedule)


def sections_collide(section_1, section_2):
	for meeting_pair in itertools.product(section_1["data"]["times"], section_2["data"]["times"]):
		try:
			if int(meeting_pair[0]["begin_time"]) >= int(meeting_pair[1]["end_time"]) or int(meeting_pair[1]["begin_time"]) >= int(meeting_pair[0]["end_time"]):
				return False
		except ValueError:
			return False
		except TypeError:
			return False
		for day in days:
			if meeting_pair[0][day] is not None and meeting_pair[1][day] is not None:
				print("returning true because of overlapping times and days")
				print(f"sections {meeting_pair[0]['section_number']} and {meeting_pair[1]['section_number']}")
				return True
		return False


days = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]


if __name__ == '__main__':
	test = ScheduleCore("winter_2020")
	test.add_course("math 113")
	test.add_course("chem 105")
	test.calculate_possible_schedules()

	print("done")
