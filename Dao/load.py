import sqlite3
from contextlib import closing
from typing import Dict

import Dao
import Dao.paths


def load_courses(semester_year: str, data: Dict) -> None:
	with closing(sqlite3.connect(Dao.paths.database_path_1(semester_year))) as connection:
		cursor = connection.cursor()

		sql_cmd = """SELECT * FROM courses"""
		cursor.execute(sql_cmd)

		for course in cursor.fetchall():
			course_data = {"sections": [],
			               "instructors": []}
			for i, key in enumerate(Dao.courses_schema.keys()):
				course_data[key] = course[i]

			sql_cmd = """SELECT * FROM sections WHERE curriculum_id_title_code = ?"""
			cursor.execute(sql_cmd, (course_data["curriculum_id_title_code"],))

			for section in cursor.fetchall():
				section_data = {"times": [],
				                "instructors": []}
				for i, key in enumerate(Dao.sections_schema.keys()):
					section_data[key] = section[i]

				sql_cmd = """SELECT * FROM times WHERE curriculum_id_title_code = ? AND section_number = ?"""
				cursor.execute(sql_cmd, (section_data["curriculum_id_title_code"], section_data["section_number"]))

				for time in cursor.fetchall():
					time_data = {}
					for i, key in enumerate(Dao.times_schema.keys()):
						time_data[key] = time[i]

					section_data["times"].append(time_data)
				section_data["times"].sort(key=sort_times)

				sql_cmd = """SELECT person_id FROM course_instructors WHERE curriculum_id_title_code = ? AND section_number = ?"""
				cursor.execute(sql_cmd, (section_data["curriculum_id_title_code"], section_data["section_number"]))

				for person_id in cursor.fetchall():
					sql_cmd = """SELECT * FROM instructors WHERE person_id = ?"""
					cursor.execute(sql_cmd, (person_id[0],))

					for instructor in cursor.fetchall():
						try:
							instructor_data = {}
							for i, key in enumerate(Dao.instructors_schema.keys()):
								instructor_data[key] = instructor[i]
							section_data["instructors"].append(instructor_data)
						except TypeError:
							pass

				course_data["sections"].append(section_data)
			course_data["sections"].sort(key=sort_sections)

			used_person_ids = set()
			for section in course_data["sections"]:
				for instructor in section["instructors"]:
					if instructor["person_id"] not in used_person_ids:
						course_data["instructors"].append(instructor)
						used_person_ids.add(instructor["person_id"])

			data[course_data["curriculum_id_title_code"]] = course_data


def sort_times(val: Dict) -> int:
	return int(val["sequence_number"])


def sort_sections(val: Dict) -> int:
	return int(val["section_number"])


def load_instructors(semester_year: str, data: Dict) -> None:
	with closing(sqlite3.connect(Dao.paths.database_path_1(semester_year))) as connection:
		cursor = connection.cursor()

		sql_cmd = """SELECT * FROM instructors"""
		cursor.execute(sql_cmd)

		for instructor in cursor.fetchall():
			instructor_data = {"classes_taught": []}
			for i, key in enumerate(Dao.instructors_schema.keys()):
				instructor_data[key] = instructor[i]

			sql_cmd = """SELECT curriculum_id_title_code, section_number FROM course_instructors WHERE person_id = ?"""
			cursor.execute(sql_cmd, (instructor[0],))
			for course in cursor.fetchall():
				sql_cmd = """SELECT catalog_number, catalog_suffix, dept_name FROM sections WHERE curriculum_id_title_code = ? AND section_number = ?"""
				cursor.execute(sql_cmd, course)
				for section in cursor.fetchall():
					suffix = section[1]
					if suffix is None:
						suffix = ""
					class_data = {"course": section[2] + " " + section[0] + suffix,
					              "section": course[1]}

					instructor_data["classes_taught"].append(class_data)
			data[instructor[0]] = instructor_data


def get_class_code(semester_year: str, dept: str, num: str, suffix: str) -> str:
	with closing(sqlite3.connect(Dao.paths.database_path_1(semester_year))) as connection:
		if suffix == "":
			suffix = None

		cursor = connection.cursor()

		sql_cmd = """SELECT curriculum_id_title_code FROM courses WHERE dept_name = ? AND catalog_number = ? AND recommended IS ?"""
		cursor.execute(sql_cmd, (dept.upper(), num, suffix))

		result = cursor.fetchone()
		return result[0] if result is not None else None
