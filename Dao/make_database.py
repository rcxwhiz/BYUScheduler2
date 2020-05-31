import os
import sqlite3
from typing import Callable, Tuple

import Dao.paths
import RateMyProfessorAPI


def create_tables(semester_year: str, output_function: Callable) -> None:
	if not os.path.exists(Dao.paths.database_path_1(semester_year)):
		output_function(f"Could not find {Dao.paths.database_path_1(semester_year)}. Making new database...")
		with open(Dao.paths.database_path_1(semester_year), "w") as _:
			pass
	connection = sqlite3.connect(Dao.paths.database_path_1(semester_year))
	cursor = connection.cursor()

	sql_cmd = """
	DROP TABLE IF EXISTS buildings;
	CREATE TABLE buildings (
	building TEXT NOT NULL PRIMARY KEY);

	DROP TABLE IF EXISTS dept_list;
	CREATE TABLE dept_list (
	dept_code TEXT NOT NULL PRIMARY KEY,
	dept_name TEXT NOT NULL
	);

	DROP TABLE IF EXISTS section_types;
	CREATE TABLE section_types (
	section_type TEXT NOT NULL PRIMARY KEY);
	
	DROP TABLE IF EXISTS dept_map;
	CREATE TABLE dept_map (
	dept TEXT NOT NULL PRIMARY KEY,
	dept_code TEXT NOT NULL);

	DROP TABLE IF EXISTS instructors;
	CREATE TABLE instructors (
	person_id TEXT NOT NULL PRIMARY KEY,
	byu_id TEXT,
	net_id TEXT,
	first_name TEXT,
	last_name TEXT,
	sort_name TEXT NOT NULL,
	preferred_first_name TEXT,
	rest_of_name TEXT,
	surname TEXT,
	phone_number TEXT,
	avg_rating REAL,
	avg_helpful REAL,
	num_ratings INTEGER,
	avg_easy_score REAL,
	avg_clarity_score REAL
	);

	DROP TABLE IF EXISTS course_instructors;
	CREATE TABLE course_instructors (
	curriculum_id_title_code TEXT NOT NULL,
	section_number TEXT NOT NULL,
	person_id TEXT NOT NULL);

	DROP TABLE IF EXISTS courses;
	CREATE TABLE courses (
	curriculum_id_title_code TEXT NOT NULL PRIMARY KEY,
	curriculum_id TEXT NOT NULL,
	title_code TEXT,
	dept_name TEXT NOT NULL,
	catalog_number TEXT NOT NULL,
	catalog_suffix TEXT,
	title TEXT,
	full_title TEXT,
	credit_hours TEXT,
	description TEXT,
	effective_date TEXT,
	expired_date TEXT,
	effective_year_term TEXT,
	expired_year_term TEXT,
	honors_approved TEXT,
	lab_hours TEXT,
	lecture_hours TEXT,
	note TEXT,
	offered TEXT,
	prerequisite TEXT,
	recommended TEXT,
	when_taught TEXT
	);

	DROP TABLE IF EXISTS sections;
	CREATE TABLE sections (
	curriculum_id_title_code TEXT NOT NULL,
	curriculum_id TEXT NOT NULL,
	title_code TEXT,
	dept_name TEXT NOT NULL,
	catalog_number TEXT NOT NULL,
	catalog_suffix TEXT,
	section_number TEXT NOT NULL,
	section_type TEXT,
	credit_hours TEXT,
	minimum_credit_hours TEXT,
	credit_type TEXT,
	fixed_or_variable TEXT,
	class_size TEXT,
	seats_available TEXT,
	waitlist_size TEXT,
	start_date TEXT,
	end_date TEXT,
	honors TEXT,
	mode TEXT,
	mode_desc TEXT,
	year_term TEXT);

	DROP TABLE IF EXISTS times;
	CREATE TABLE times (
	cirriculum_id_title_code TEXT NOT NULL,
	section_number TEXT NOT NULL,
	begin_time TEXT,
	end_time TEXT,
	building TEXT,
	room TEXT,
	sun TEXT,
	mon TEXT,
	tue TEXT,
	wed TEXT,
	thu TEXT,
	fri TEXT,
	sat TEXT,
	sequence_number TEXT);"""

	cursor.executescript(sql_cmd)
	connection.commit()
	connection.close()


def save(yso: Tuple, use_rmp: bool, append_function: Callable = print, replace_function: Callable = print) -> None:
	semester_year, semester_result, classes_result, section_results = yso
	if not os.path.exists(Dao.paths.database_path_1(semester_year)):
		append_function(f"Could not find {Dao.paths.database_path_1(semester_year)}. Making new database...")
		if not os.path.exists(os.path.dirname(Dao.paths.database_path_1(semester_year))):
			os.makedirs(os.path.dirname(Dao.paths.database_path_1(semester_year)))
		with open(Dao.paths.database_path_1(semester_year), "w") as _:
			pass

	create_tables(semester_year, append_function)

	connection = sqlite3.connect(Dao.paths.database_path_1(semester_year))
	cursor = connection.cursor()

	append_function("Saving department map...")
	for dept in semester_result["department_map"].keys():

		sql_cmd = """INSERT INTO dept_map VALUES(?, ?);"""
		values = (dept, yso[1]["department_map"][dept])
		try:
			cursor.execute(sql_cmd, values)
		except sqlite3.IntegrityError:
			append_function(f"Got duplicate: {values}")
		except:
			append_function(f"Error adding: {values}")
	replace_function("Saved department map")

	append_function("Saving department list...")
	for dept in semester_result["department_list"].keys():

		sql_cmd = """INSERT INTO dept_list VALUES(?, ?);"""
		values = (dept, yso[1]["department_list"][dept])
		try:
			cursor.execute(sql_cmd, values)
		except sqlite3.IntegrityError:
			append_function(f"Got duplicate: {values}")
		except:
			append_function(f"Error adding: {values}")
	replace_function("Saved department list")

	append_function("Saving section types...")
	for section_type in semester_result["section_type_list"]:
		sql_cmd = """INSERT INTO section_types VALUES(?);"""
		values = (section_type,)
		try:
			cursor.execute(sql_cmd, values)
		except sqlite3.IntegrityError:
			append_function(f"Got duplicate: {values}")
		except:
			append_function(f"Error adding: {values}")
	replace_function("Saved section types")

	append_function("Saving instructors...")
	for instructor in semester_result["instructor_list"]:
		sql_cmd = """INSERT INTO instructors VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
		values = [instructor["id"], None, None, instructor["first_name"], instructor["last_name"],
		          instructor["sort_name"]] + [None] * 9
		try:
			cursor.execute(sql_cmd, values)
		except sqlite3.IntegrityError:
			append_function(f'Got duplicate: {values}')
		except:
			append_function(f'Error adding: {values}')
	replace_function("Saved instructors")

	append_function("Saving building list...")
	for building in semester_result["building_list"]:
		sql_cmd = """INSERT INTO buildings VALUES(?);"""
		values = (building["building"],)
		try:
			cursor.execute(sql_cmd, values)
		except sqlite3.IntegrityError:
			append_function(f"Got duplicate: {values}")
		except:
			append_function(f"Error adding: {values}")
	replace_function("Saved building list")

	append_function("Saving course list...")
	for rand_id in classes_result.keys():
		course = classes_result[rand_id]

		sql_cmd = """INSERT INTO courses VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
		values = [course["curriculum_id"] + course["title_code"],
		          course["curriculum_id"],
		          course["title_code"],
		          course["dept_name"],
		          course["catalog_number"],
		          course["catalog_suffix"],
		          course["title"],
		          course["full_title"]
		          ] + [None] * 14
		try:
			cursor.execute(sql_cmd, values)
		except sqlite3.IntegrityError:
			append_function(f"Got duplicate: {values}")
		except:
			append_function(f"Error adding: {values}")
	replace_function("Saved course list")

	for i, course in enumerate(section_results):
		for section in course["sections"]:
			curriculum_id_title_code = section["curriculum_id"] + section["title_code"]
			section_number = section["section_number"]
			availability = section["availability"]
			sql_cmd = """INSERT INTO sections VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
			values = (curriculum_id_title_code,
			          section["curriculum_id"],
			          section["title_code"],
			          section["dept_name"],
			          section["catalog_number"],
			          section["catalog_suffix"],
			          section_number,
			          section["section_type"],
			          section["credit_hours"],
			          section["minimum_credit_hours"],
			          section["credit_type"],
			          section["fixed_or_variable"],
			          availability["class_size"],
			          availability["seats_available"],
			          availability["waitlist_size"],
			          section["start_date"],
			          section["end_date"],
			          section["honors"],
			          section["mode"],
			          section["mode_desc"],
			          section["year_term"])
			try:
				cursor.execute(sql_cmd, values)
			except sqlite3.IntegrityError:
				append_function(f"Got duplicate: {values}")
			except:
				append_function(f"Error adding: {values}")

			for instructor in section["instructors"]:
				sql_cmd = """UPDATE instructors SET byu_id = ?, net_id = ?, surname = ?, rest_of_name = ?, preferred_first_name = ?, phone_number = ? WHERE person_id = ?;"""
				values = (instructor["byu_id"],
				          instructor["net_id"],
				          instructor["surname"],
				          instructor["rest_of_name"],
				          instructor["preferred_first_name"],
				          instructor["phone_number"],
				          instructor["person_id"])
				try:
					cursor.execute(sql_cmd, values)
				except sqlite3.IntegrityError:
					append_function(f"Got duplicate: {values}")
				except:
					append_function(f"Error adding: {values}")

				sql_cmd = """INSERT INTO course_instructors VALUES(?, ?, ?);"""
				values = (curriculum_id_title_code,
				          section_number,
				          instructor["person_id"])
				try:
					cursor.execute(sql_cmd, values)
				except sqlite3.IntegrityError:
					append_function(f"Got duplicate: {values}")
				except:
					append_function(f"Error adding: {values}")

			for time in section["times"]:
				sql_cmd = """INSERT INTO times VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
				values = (curriculum_id_title_code,
				          section_number,
				          time["begin_time"],
				          time["end_time"],
				          time["building"],
				          time["room"],
				          time["sun"],
				          time["mon"],
				          time["tue"],
				          time["wed"],
				          time["thu"],
				          time["fri"],
				          time["sat"],
				          time["sequence_number"])
				try:
					cursor.execute(sql_cmd, values)
				except sqlite3.IntegrityError:
					append_function(f"Got duplicate: {values}")
				except:
					append_function(f"Error adding: {values}")

		catalog = course["catalog"]
		sql_cmd = """UPDATE courses SET credit_hours = ?, description = ?, effective_date = ?, effective_year_term = ?, expired_date = ?, expired_year_term = ?, honors_approved = ?, lab_hours = ?, lecture_hours = ?, note = ?, offered = ?, prerequisite = ?, recommended = ?, when_taught = ? WHERE curriculum_id = ?;"""
		values = (catalog["credit_hours"],
		          catalog["description"],
		          catalog["effective_date"],
		          catalog["effective_year_term"],
		          catalog["expired_date"],
		          catalog["expired_year_term"],
		          catalog["honors_approved"],
		          catalog["lab_hours"],
		          catalog["lecture_hours"],
		          catalog["note"],
		          catalog["offered"],
		          catalog["prerequisite"],
		          catalog["recommended"],
		          catalog["when_taught"],
		          catalog["curriculum_id"])
		try:
			cursor.execute(sql_cmd, values)
		except sqlite3.IntegrityError:
			append_function(f"Got duplicate: {values}")
		except:
			append_function(f"Error adding: {values}")

		replace_function(f"Saved {i + 1}/{len(section_results)} sections...")

	replace_function(f"Saved {len(section_results)} sections")

	if use_rmp:
		sql_cmd = """SELECT * FROM instructors;"""
		cursor.execute(sql_cmd)
		profs = cursor.fetchall()
		RateMyProfessorAPI.append_rmp_info(profs, cursor, append_function, replace_function)

	append_function("Commiting changes...")
	cursor.close()
	try:
		connection.commit()
	except BaseException as e:
		append_function("Error committing changes")
		connection.close()
		raise e

	connection.close()
	replace_function("Changes committed")

	db_size = os.path.getsize(Dao.paths.database_path_1(semester_year)) / 1e6
	append_function(f"Database entry for {semester_year} created ({db_size:.1f} MB)")
