class ScheduleCore:
	def __init__(self):
		self.courses = []

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

