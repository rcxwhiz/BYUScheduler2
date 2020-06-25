import itertools
import re

import Dao.load


class ScheduleCore:
	def __init__(self, semester_year, data):
		self.courses = {}
		self.semester_year = semester_year
		self.data = data
		self.schedules = []
		self.new_courses = []

	def add_course(self, course_name):
		print(f"adding {course_name}")
		class_code = get_id_from_name(self.semester_year, course_name)
		if class_code is None:
			raise ValueError("course not found")
		if class_code in self.courses.keys():
			return

		self.new_courses.append(
			{"course": class_code, "name": course_name, "sections": self.data[class_code]["sections"],
			 "used_sections": set()})

	def remove_course(self, course_name):
		class_code = get_id_from_name(self.semester_year, course_name)
		if class_code is None:
			raise ValueError("course not found")
		self.courses.pop(class_code)
		self.new_courses = list(self.courses.values())
		self.courses = {}
		self.calculate_possible_schedules()

	def calculate_possible_schedules(self):
		# go through all the built up new courses to add
		for new_course in self.new_courses:
			# get ready to see all the new schedules we can make with this new course
			new_schedules = []
			# go through all all the sections of this course to see which we can add
			for section in new_course["sections"]:
				# go through our old schedules to see which of them are compatible with this new section
				if len(self.schedules) > 0:
					for bit in self.schedules:
						# add the new section to the old schedule
						old_schedule = bit.copy()
						old_schedule.append(section)
						add_this_schedule = True
						for pair in itertools.combinations(old_schedule, 2):
							if sections_collide(*pair):
								add_this_schedule = False
								break
						# determined if there are any conflicts in this schedule
						if add_this_schedule:
							# if there are no conflicts add this to what will be our new list of schedules
							new_schedules.append(old_schedule)
				elif len(self.courses) == 0:
					new_schedules.append([section])
			self.courses[new_course["course"]] = new_course
			# set the official schedules to these newly found ones so that we can determine which sections from the
			# next class are compatible
			self.schedules = new_schedules
		self.new_courses.clear()

		for course in self.courses.values():
			course["used_sections"] = set()

		for schedule in self.schedules:
			for section in schedule:
				self.courses[section["curriculum_id_title_code"]]["used_sections"].add(int(section["section_number"]))

		for course in self.courses.values():
			course["used_sections"] = sorted(course["used_sections"])

	def deselect_section(self, course_name, section_num):
		new_schedules = []
		for old_schedule in self.schedules:
			to_add = True
			for section in old_schedule:
				if section["name"] == course_name.upper() and section["data"]["section_number"] == int(section_num):
					to_add = False
					break
			if to_add:
				new_schedules.append(old_schedule)
		self.schedules = new_schedules


def sections_collide(section_1, section_2):
	for meeting_pair in itertools.product(section_1["times"], section_2["times"]):
		try:
			if int(meeting_pair[0]["begin_time"]) >= int(meeting_pair[1]["end_time"]) or int(
					meeting_pair[1]["begin_time"]) >= int(meeting_pair[0]["end_time"]):
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
	data = {}
	Dao.load.load_courses("winter_2020", data)
	test = ScheduleCore("winter_2020", data)
	test.add_course("math 113")
	test.add_course("chem 105")
	test.calculate_possible_schedules()

	print("done")
