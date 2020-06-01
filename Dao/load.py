import sqlite3
from contextlib import closing
from typing import Dict

import Dao.paths


def load_courses(semester_year: str, data: Dict) -> None:
	with closing(sqlite3.connect(Dao.paths.database_path_1(semester_year))) as connection:
		cursor = connection.cursor()

		sql_cmd = """SELECT * FROM courses"""
		cursor.execute(sql_cmd)

		for course in cursor.fetchall():
			course_data = {"curriculum_id_title_code": course[0],
			               "curriculum_id": course[1],
			               "title_code": course[2],
			               "dept_name": course[3],
			               "catalog_number": course[4],
			               "catalog_suffix": course[5],
			               "title": course[6],
			               "full_title": course[7],
			               "credit_hours": course[8],
			               "description": course[9],
			               "effective_date": course[10],
			               "expired_date": course[11],
			               "effective_year_term": course[12],
			               "expired_year_term": course[13],
			               "honors_approved": course[14],
			               "lab_hours": course[15],
			               "lecture_hours": course[16],
			               "note": course[17],
			               "offered": course[18],
			               "prerequisite": course[19],
			               "recommended": course[20],
			               "when_taught": course[21],
			               "sections": [],
			               "instructors": []}

			sql_cmd = """SELECT curriculum_id_title_code,
			 curriculum_id,
			 title_code,
			 dept_name,
			 catalog_suffix,
			 section_number,
			 section_type,
			 credit_hours,
			 minimum_credit_hours,
			 credit_type,
			 credit_hours,
			 minimum_credit_hours,
			 credit_type,
			 fixed_or_variable,
			 class_size,
			 seats_available,
			 waitlist_size,
			 start_date,
			 end_date,
			 honors,
			 mode,
			 mode_desc,
			 year_term
			 FROM sections WHERE curriculum_id_title_code = ?"""
			cursor.execute(sql_cmd, (course_data["curriculum_id_title_code"],))

			for section in cursor.fetchall():
				section_data = {"curriculum_id_title_code": section[0],
				                "curriculum_id": section[1],
				                "title_code": section[2],
				                "dept_name": section[3],
				                "catalog_number": section[4],
				                "catalog_suffix": section[5],
				                "section_number": section[6],
				                "section_type": section[7],
				                "credit_hours": section[8],
				                "minimum_credit_hours": section[9],
				                "credit_type": section[10],
				                "fixed_or_variable": section[11],
				                "class_size": section[12],
				                "seats_available": section[13],
				                "waitlist_size": section[14],
				                "start_date": section[15],
				                "end_date": section[16],
				                "honors": section[17],
				                "mode": section[18],
				                "mode_desc": section[19],
				                "year_term": section[20],
				                "times": [],
				                "instructors": []}

				sql_cmd = """SELECT * FROM times WHERE cirriculum_id_title_code = ? AND section_number = ?"""
				cursor.execute(sql_cmd, (section_data["curriculum_id_title_code"], section_data["section_number"]))

				for time in cursor.fetchall():
					time_data = {"curriculum_id_title_code": time[0],
					             "section_number": time[1],
					             "begin_time": time[2],
					             "end_time": time[3],
					             "building": time[4],
					             "room": time[5],
					             "sun": time[6],
					             "mon": time[7],
					             "tue": time[8],
					             "wed": time[9],
					             "thu": time[10],
					             "fri": time[11],
					             "sat": time[12],
					             "sequence_number": time[13]}
					section_data["times"].append(time_data)
				section_data["times"].sort(key=sort_times)

				sql_cmd = """SELECT person_id FROM course_instructors WHERE curriculum_id_title_code = ? AND section_number = ?"""
				cursor.execute(sql_cmd, (section_data["curriculum_id_title_code"], section_data["section_number"]))

				for person_id in cursor.fetchall():
					sql_cmd = """SELECT * FROM instructors WHERE person_id = ?"""
					cursor.execute(sql_cmd, (person_id[0],))
					instructor = cursor.fetchone()
					try:
						instructor_data = {"person_id": instructor[0],
						                   "byu_id": instructor[1],
						                   "net_id": instructor[2],
						                   "first_name": instructor[3],
						                   "last_name": instructor[4],
						                   "sort_name": instructor[5],
						                   "preferred_first_name": instructor[6],
						                   "rest_of_name": instructor[7],
						                   "surname": instructor[8],
						                   "phone_number": instructor[9],
						                   "avg_rating": instructor[10],
						                   "avg_helpful": instructor[11],
						                   "num_ratings": instructor[12],
						                   "avg_easy_score": instructor[13],
						                   "avg_clarity_score": instructor[14]}
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
			instructor_data = {"person_id": instructor[0],
			                   "byu_id": instructor[1],
			                   "net_id": instructor[2],
			                   "first_name": instructor[3],
			                   "last_name": instructor[4],
			                   "sort_name": instructor[5],
			                   "preferred_first_name": instructor[6],
			                   "rest_of_name": instructor[7],
			                   "surname": instructor[8],
			                   "phone_number": instructor[9],
			                   "avg_rating": instructor[10],
			                   "avg_helpful": instructor[11],
			                   "num_ratings": instructor[12],
			                   "avg_easy_score": instructor[13],
			                   "avg_clarity_score": instructor[14],
			                   "classes_taught": []}
			for key in instructor_data.keys():
				if instructor_data[key] is None:
					instructor_data[key] = ""
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
