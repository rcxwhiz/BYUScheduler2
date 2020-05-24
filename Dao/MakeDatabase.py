import os
import sqlite3
import Dao.Paths


def create_tables(semester_year):
	if not os.path.exists(Dao.Paths.database_path_1(semester_year)):
		print(f"Could not find {Dao.Paths.database_path_1(semester_year)}. Making new database...")
		with open(Dao.Paths.database_path_1(semester_year), "w") as _:
			pass
	connection = sqlite3.connect(Dao.Paths.database_path_1(semester_year))
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
	first_name TEXT,
	last_name TEXT,
	sort_name TEXT NOT NULL,
	byu_id TEXT,
	net_id TEXT,
	phone_number TEXT,
	preferred_first_name TEXT,
	rest_of_name TEXT,
	surname TEXT
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
	catalog_number TEXT NOT NULL,
	catalog_suffix TEXT,
	dept_name TEXT NOT NULL,
	full_title TEXT,
	title TEXT,
	title_code TEXT,
	credit_hours TEXT,
	description TEXT,
	effective_date TEXT,
	effective_year_term TEXT,
	expired_date TEXT,
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
	class_size TEXT,
	seats_available TEXT,
	waitlist_size TEXT,
	catalog_number TEXT NOT NULL,
	catalog_suffix TEXT,
	credit_hours TEXT,
	credit_type TEXT,
	cirriculum_id TEXT NOT NULL,
	dept_name TEXT NOT NULL,
	end_date TEXT,
	fixed_or_variable TEXT,
	honors TEXT,
	minimum_credit_hours TEXT,
	mode TEXT,
	mode_desc TEXT,
	section_number TEXT NOT NULL,
	section_type TEXT,
	start_date TEXT,
	title_code TEXT,
	year_term TEXT);

	DROP TABLE IF EXISTS times;
	CREATE TABLE times (
	cirriculum_id_title_code TEXT NOT NULL,
	section_number TEXT NOT NULL,
	begin_time TEXT,
	building TEXT,
	end_time TEXT,
	fri TEXT,
	mon TEXT,
	room TEXT,
	sat TEXT,
	sequence_number TEXT,
	sun TEXT,
	thu TEXT,
	tue TEXT,
	wed TEXT);"""

	cursor.executescript(sql_cmd)
	connection.commit()
	connection.close()


def save(yso):
	# (semester_year, semester_result, classes_result, [section_result])
	semester_year, semester_result, classes_result, section_results = yso
	if not os.path.exists(Dao.Paths.database_path_1(semester_year)):
		print(f"Could not find {Dao.Paths.database_path_1(semester_year)}. Making new database...")
		if not os.path.exists(os.path.dirname(Dao.Paths.database_path_1(semester_year))):
			os.makedirs(os.path.dirname(Dao.Paths.database_path_1(semester_year)))
		with open(Dao.Paths.database_path_1(semester_year), "w") as _:
			pass

	create_tables(semester_year)

	connection = sqlite3.connect(Dao.Paths.database_path_1(semester_year))
	cursor = connection.cursor()

	print("Saving department map...", end="")
	for dept in semester_result["department_map"].keys():

		sql_cmd = """INSERT INTO dept_map VALUES(?, ?);"""
		values = (dept, yso[1]["department_map"][dept])
		try:
			cursor.execute(sql_cmd, values)
		except sqlite3.IntegrityError:
			print(f"Got duplicate: {values}")
		except:
			print(f"Error adding: {values}")
	print("\rSaved department map        ")

	print("Saving department list...", end="")
	for dept in semester_result["department_list"].keys():

		sql_cmd = """INSERT INTO dept_list VALUES(?, ?);"""
		values = (dept, yso[1]["department_list"][dept])
		try:
			cursor.execute(sql_cmd, values)
		except sqlite3.IntegrityError:
			print(f"Got duplicate: {values}")
		except:
			print(f"Error adding: {values}")
	print("\rSaved department list        ")

	print("Saving section types...", end="")
	for section_type in semester_result["section_type_list"]:
		sql_cmd = """INSERT INTO section_types VALUES(?);"""
		values = (section_type,)
		try:
			cursor.execute(sql_cmd, values)
		except sqlite3.IntegrityError:
			print(f"Got duplicate: {values}")
		except:
			print(f"Error adding: {values}")
	print("\rSaved section types       ")

	print("Saving instructors...", end="")
	for instructor in semester_result["instructor_list"]:
		sql_cmd = """INSERT INTO instructors VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
		values = [instructor["id"], instructor["first_name"], instructor["last_name"], instructor["sort_name"]] + [
			None] * 6
		try:
			cursor.execute(sql_cmd, values)
		except sqlite3.IntegrityError:
			print(f'Got duplicate: {values}')
		except:
			print(f'Error adding: {values}')
	print("\rSaved instructors       ")

	print("Saving building list...", end="")
	for building in semester_result["building_list"]:
		sql_cmd = """INSERT INTO buildings VALUES(?);"""
		values = (building["building"],)
		try:
			cursor.execute(sql_cmd, values)
		except sqlite3.IntegrityError:
			print(f'Got duplicate: {values}')
		except:
			print(f'Error adding: {values}')
	print("\rSaved building list        ")

	print("Saving course list...", end="")
	for rand_id in classes_result.keys():
		course = classes_result[rand_id]

		sql_cmd = """INSERT INTO courses VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
		values = [course["curriculum_id"] + course["title_code"],
		          course["curriculum_id"],
		          course["catalog_number"],
		          course["catalog_suffix"],
		          course["dept_name"],
		          course["full_title"],
		          course["title"],
		          course["title_code"]] + [None] * 14
		try:
			cursor.execute(sql_cmd, values)
		except sqlite3.IntegrityError:
			print(f"Got duplicate: {values}")
		except:
			print(f"Error adding: {values}")
	print("\rSaved course list       ")

	i = 1
	for course in section_results:
		for section in course["sections"]:
			curriculum_id_title_code = section["curriculum_id"] + section["title_code"]
			section_number = section["section_number"]
			availability = section["availability"]
			sql_cmd = """INSERT INTO sections VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
			values = (curriculum_id_title_code,
			          availability["class_size"],
			          availability["seats_available"],
			          availability["waitlist_size"],
			          section["catalog_number"],
			          section["catalog_suffix"],
			          section["credit_hours"],
			          section["credit_type"],
			          section["curriculum_id"],
			          section["dept_name"],
			          section["end_date"],
			          section["fixed_or_variable"],
			          section["honors"],
			          section["minimum_credit_hours"],
			          section["mode"],
			          section["mode_desc"],
			          section_number,
			          section["section_type"],
			          section["start_date"],
			          section["title_code"],
			          section["year_term"])
			try:
				cursor.execute(sql_cmd, values)
			except sqlite3.IntegrityError:
				print(f"Got duplicate: {values}")
			except:
				print(f"Error adding: {values}")

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
					print(f"Got duplicate: {values}")
				except:
					print(f"Error adding: {values}")

				sql_cmd = """INSERT INTO course_instructors VALUES(?, ?, ?);"""
				values = (curriculum_id_title_code,
				          section_number,
				          instructor["person_id"])
				try:
					cursor.execute(sql_cmd, values)
				except sqlite3.IntegrityError:
					print(f"Got duplicate: {values}")
				except:
					print(f"Error adding: {values}")

			for time in section["times"]:
				sql_cmd = """INSERT INTO times VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
				values = (curriculum_id_title_code,
				          section_number,
				          time["begin_time"],
				          time["building"],
				          time["end_time"],
				          time["fri"],
				          time["mon"],
				          time["room"],
				          time["sat"],
				          time["sequence_number"],
				          time["sun"],
				          time["thu"],
				          time["tue"],
				          time["wed"])
				try:
					cursor.execute(sql_cmd, values)
				except sqlite3.IntegrityError:
					print(f"Got duplicate: {values}")
				except:
					print(f"Error adding: {values}")

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
			print(f"Got duplicate: {values}")
		except:
			print(f"Error adding: {values}")

		print(f"\rSaved {i}/{len(section_results)} sections...", end=" " * 15)
		i += 1

	print(f"\rSaved {len(section_results)} sections" + " " * 15)
	print("Commiting changes...", end="")
	try:
		connection.commit()
	except:
		print("Error comitting changes")
		connection.close()
		return None

	connection.close()
	print("\rChanges committed")

	db_size = os.path.getsize(Dao.Paths.database_path_1(semester_year)) / 1e6
	print(f"Database entry for {semester_year} created ({db_size:.1f} MB)")
