import itertools
import re

import Dao.load


class ScheduleCore:
	def __init__(self, semester_year, data):
		self.courses = {}
		self.semester_year = semester_year
		self.data = data
		self.possible_schedules = []

	def add_course(self, course_name):
		class_code = get_id_from_name(self.semester_year, course_name)
		if class_code is None:
			raise ValueError("course not found")
		if class_code in self.courses.keys():
			return

		self.courses[class_code] = []
		for section in self.data[class_code]["sections"]:
			self.courses[class_code].append(
				{"course": class_code, "name": course_name, "data": section, "selected": False, "deselected": False,
				 "used": False})

	def remove_course(self, course_name):
		class_code = get_id_from_name(self.semester_year, course_name)
		if class_code is None:
			raise ValueError("course not found")
		self.courses.pop(class_code, None)

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
					break

		selected_courses = {}
		deselected_courses = {}
		for course_id in self.courses.keys():
			selected_courses[course_id] = []
			deselected_courses[course_id] = []
			for section in self.courses[course_id]:
				if section["selected"]:
					selected_courses[course_id].append(section)
				elif section["deselected"]:
					deselected_courses[course_id].append(section)

		for course in self.courses.values():
			for section in course:
				section["used"] = False

		schedules_to_remove = []
		for schedule in self.possible_schedules:
			for section in schedule:
				if not self.section_is_usable(section):
					schedules_to_remove.append(schedule)
					break
				else:
					for section_2 in self.courses[section["course"]]:
						if section_2["data"]["section_number"] == section["data"]["section_number"]:
							section_2["used"] = True
							break
		for schedule in schedules_to_remove:
			self.possible_schedules.remove(schedule)

	def section_is_usable(self, section):
		filtered_course = False
		for section in self.courses[section["data"]["curriculum_id_title_code"]]:
			if section["selected"]:
				filtered_course = True
				break
		if filtered_course and not section["selected"]:
			return False
		if section["deselected"]:
			return False
		return True

	def select_section(self, course_name, section_num):
		course_id = get_id_from_name(self.semester_year, course_name)
		for section in self.courses[course_id]:
			if int(section["data"]["section_number"]) == section_num:
				section["selected"] = True

	def deselect_section(self, course_name, section_num):
		course_id = get_id_from_name(self.semester_year, course_name)
		for section in self.courses[course_id]:
			if int(section["data"]["section_number"]) == section_num:
				section["deselected"] = True


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
				return True
		return False


def get_id_from_name(semster_year, course_name):
	found_parts = re.search(course_re, course_name)
	if found_parts is None:
		raise ValueError(f"course '{course_name}' not found")
	return Dao.load.get_class_code(semster_year, found_parts[1], found_parts[2], found_parts[3])


course_re = re.compile(r"([a-zA-Z ]+) ([0-9]+)(.?)")
days = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]


if __name__ == '__main__':
	test = ScheduleCore("winter_2020")
	test.add_course("math 113")
	test.add_course("chem 105")
	test.select_section("chem 105", 1)
	test.calculate_possible_schedules()

	print("done")
