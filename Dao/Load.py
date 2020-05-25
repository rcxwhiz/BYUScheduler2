import sqlite3
import Dao.Paths


def load_classes(semester_year):
	data = {}
	connection = sqlite3.connect(Dao.Paths.database_path_1(semester_year))
	cursor = connection.cursor()

	sql_cmd = """SELECT * FROM courses;"""
	cursor.execute(sql_cmd)

	for course in cursor.fetchall():
		data[course[0]] = {"curriculum_id_title_code": course[0],
		                   "curriculum_id": course[1],
		                   "catalog_number": course[2],
		                   "catalog_suffix": course[3],
		                   "dept_name": course[4],
		                   "full_title": course[5],
		                   "title": course[6],
		                   "title_code": course[7],
		                   "credit_hours": course[8],
		                   "description": course[9],
		                   "effective_date": course[10],
		                   "effective_year_term": course[11],
		                   "expired_date": course[12],
		                   "expired_year_term": course[13],
		                   "honors_approved": course[14],
		                   "lab_hours": course[15],
		                   "lecture_hours": course[16],
		                   "note": course[17],
		                   "offered": course[18],
		                   "prerequisite": course[19],
		                   "recommended": course[20],
		                   "when_taught": course[21],
		                   "sections": {}}
	sql_cmd = """SELECT * FROM sections;"""
	cursor.execute(sql_cmd)

	for section in cursor.fetchall():
		section_data = {"class_size": section[1],
		                "seats_available": section[2],
		                "waitlist_size": section[3],
		                "catalog_number": section[4],
		                "catalog_suffix": section[5],
		                "credit_hours": section[6],
		                "credit_type": section[7],
		                "curriculum_id": section[8],
		                "dept_name": section[9],
		                "end_date": section[10],
		                "fixed_or_variable": section[11],
		                "honors": section[12],
		                "minimum_credit_hours": section[13],
		                "mode": section[14],
		                "mode_desc": section[15],
		                "section_number": section[16],
		                "section_type": section[17],
		                "start_date": section[18],
		                "title_code": section[19],
		                "year_term": section[20],
		                "instructors": [],
		                "times": []}

		data[section[0]]["sections"][section[16]] = section_data

	sql_cmd = """SELECT * FROM course_instructors;"""
	cursor.execute(sql_cmd)

	for instructor in cursor.fetchall():
		sql_cmd = """SELECT * FROM instructors WHERE person_id = ?;"""
		cursor.execute(sql_cmd, (instructor[2],))
		data_found = cursor.fetchone()
		if data_found is not None:
			data_to_insert = {"person_id": data_found[0],
			                  "first_name": data_found[1],
			                  "last_name": data_found[2],
			                  "sort_name": data_found[3],
			                  "byu_id": data_found[4],
			                  "net_id": data_found[5],
			                  "phone_number": data_found[6],
			                  "preferred_first_name": data_found[7],
			                  "rest_of_name": data_found[8],
			                  "surname": data_found[9]}
		else:
			data_to_insert = {"person_id": "COULD NOT FIND INSTRUCTOR",
			                  "first_name": "COULD NOT FIND INSTRUCTOR",
			                  "last_name": "COULD NOT FIND INSTRUCTOR",
			                  "sort_name": "COULD NOT FIND INSTRUCTOR",
			                  "byu_id": "COULD NOT FIND INSTRUCTOR",
			                  "net_id": "COULD NOT FIND INSTRUCTOR",
			                  "phone_number": "COULD NOT FIND INSTRUCTOR",
			                  "preferred_first_name": "COULD NOT FIND INSTRUCTOR",
			                  "rest_of_name": "COULD NOT FIND INSTRUCTOR",
			                  "surname": "COULD NOT FIND INSTRUCTOR"}
		data[instructor[0]]["sections"][instructor[1]]["instructors"].append(data_to_insert)

	sql_cmd = """SELECT * FROM times;"""
	cursor.execute(sql_cmd)

	for time in cursor.fetchall():
		time_data = {"begin_time": time[2],
		             "building": time[3],
		             "end_time": time[4],
		             "fri": time[5],
		             "mon": time[6],
		             "room": time[7],
		             "sat": time[8],
		             "sequence_number": time[9],
		             "sun": time[10],
		             "thu": time[11],
		             "tue": time[12],
		             "wed": time[13]}
		data[time[0]]["sections"][time[1]]["times"].append(time_data)
		data[time[0]]["sections"][time[1]]["times"].sort(key=sort_times)


def sort_times(val):
	return val["sequence_number"]


if __name__ == '__main__':
	load_classes("fall_2020")