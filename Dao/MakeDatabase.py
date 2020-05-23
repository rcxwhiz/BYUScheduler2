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
	curriculum_id TEXT NOT NULL,
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
	cirriculum_id TEXT NOT NULL,
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
		department_map = yso[1]["department_map"]

		sql_cmd = """INSERT INTO dept_map VALUES(?, ?);"""
		try:
			cursor.execute(sql_cmd, (dept, department_map[dept]))
		except sqlite3.IntegrityError:
			print(f"Got duplicate: {(dept, department_map[dept])}")
		except:
			print(f"Error adding: {(dept, department_map[dept])}")
	print("\rSaved department map        ")

	print("Saving department list...", end="")
	for dept in semester_result["department_list"].keys():
		department_list = yso[1]["department_list"]

		sql_cmd = """INSERT INTO dept_list VALUES(?, ?);"""
		try:
			cursor.execute(sql_cmd, (dept, department_list[dept]))
		except sqlite3.IntegrityError:
			print(f"Got duplicate: {(dept, department_list[dept])}")
		except:
			print(f"Error adding: {(dept, department_list[dept])}")
	print("\rSaved department list        ")

	print("Saving section types...", end="")
	for section_type in semester_result["section_type_list"]:
		sql_cmd = """INSERT INTO section_types VALUES(?);"""
		try:
			cursor.execute(sql_cmd, (section_type,))
		except sqlite3.IntegrityError:
			print(f"Got duplicate: {(section_type,)}")
		except:
			print(f"Error adding: {(section_type,)}")
	print("\rSaved section types       ")

	print("Saving instructors...", end="")
	for instructor in semester_result["instructor_list"]:
		sql_cmd = """INSERT INTO instructors VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
		try:
			cursor.execute(sql_cmd, [instructor["id"], instructor["first_name"], instructor["last_name"], instructor["sort_name"]] + [None] * 6)
		except sqlite3.IntegrityError:
			print(f'Got duplicate: {[instructor["id"], instructor["first_name"], instructor["last_name"], instructor["sort_name"]] + [None] * 6}')
		except:
			print(f'Error adding: {[instructor["id"], instructor["first_name"], instructor["last_name"], instructor["sort_name"]] + [None] * 6}')
	print("\rSaved instructors       ")

	print("Saving building list...", end="")
	for building in semester_result["building_list"]:
		sql_cmd = """INSERT INTO buildings VALUES(?);"""
		try:
			cursor.execute(sql_cmd, (building["building"],))
		except sqlite3.IntegrityError:
			print(f'Got duplicate: {(building["building"],)}')
		except:
			print(f'Error adding: {(building["building"],)}')
	print("\rSaved building list        ")

	print("Saving course list...", end="")
	for rand_id in classes_result.keys():
		course = classes_result[rand_id]
		curriculum_id = course["curriculum_id"]
		catalog_number = course["catalog_number"]
		catalog_suffix = course["catalog_suffix"]
		dept_name = course["dept_name"]
		full_title = course["full_title"]
		title = course["title"]
		title_code = course["title_code"]

		sql_cmd = """INSERT INTO courses VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
		try:
			cursor.execute(sql_cmd, [curriculum_id + title_code, curriculum_id, catalog_number, catalog_suffix, dept_name, full_title, title, title_code] + [None] * 14)
		except sqlite3.IntegrityError:
			print(f"Got duplicate: {[curriculum_id + title_code, curriculum_id, catalog_number, catalog_suffix, dept_name, full_title, title, title_code] + [None] * 14}")
		except:
			print(f"Error adding: {[curriculum_id + title_code, curriculum_id, catalog_number, catalog_suffix, dept_name, full_title, title, title_code] + [None] * 14}")
	print("\rSaved course list       ")

	i = 1
	for course in section_results:
		for section in course["sections"]:
			availability = section["availability"]
			class_size = availability["class_size"]
			seats_available = availability["seats_available"]
			waitlist_size = availability["waitlist_size"]
			catalog_number = section["catalog_number"]
			catalog_suffix = section["catalog_suffix"]
			credit_hours = section["credit_hours"]
			credit_type = section["credit_type"]
			curriculum_id = section["curriculum_id"]
			dept_name = section["dept_name"]
			end_date = section["end_date"]
			fixed_or_variable = section["fixed_or_variable"]
			honors = section["honors"]
			minimum_credit_hours = section["minimum_credit_hours"]
			mode = section["mode"]
			mode_desc = section["mode_desc"]
			section_number = section["section_number"]
			section_type = section["section_type"]
			start_date = section["start_date"]
			title_code = section["title_code"]
			year_term = section["year_term"]
			sql_cmd = """INSERT INTO sections VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
			try:
				cursor.execute(sql_cmd, (class_size, seats_available, waitlist_size, catalog_number, catalog_suffix, credit_hours, credit_type, curriculum_id, dept_name, end_date, fixed_or_variable, honors, minimum_credit_hours, mode, mode_desc, section_number, section_type, start_date, title_code, year_term))
			except sqlite3.IntegrityError:
				print(f"Got duplicate: {(class_size, seats_available, waitlist_size, catalog_number, catalog_suffix, credit_hours, credit_type, curriculum_id, dept_name, end_date, fixed_or_variable, honors, minimum_credit_hours, mode, mode_desc, section_number, section_type, start_date, title_code, year_term)}")
			except:
				print(f"Error adding: {(class_size, seats_available, waitlist_size, catalog_number, catalog_suffix, credit_hours, credit_type, curriculum_id, dept_name, end_date, fixed_or_variable, honors, minimum_credit_hours, mode, mode_desc, section_number, section_type, start_date, title_code, year_term)}")

			for instructor in section["instructors"]:
				person_id = instructor["person_id"]
				byu_id = instructor["byu_id"]
				net_id = instructor["net_id"]
				surname = instructor["surname"]
				rest_of_name = instructor["rest_of_name"]
				preferred_first_name = instructor["preferred_first_name"]
				phone_number = instructor["phone_number"]
				sql_cmd = """UPDATE instructors SET byu_id = ?, net_id = ?, surname = ?, rest_of_name = ?, preferred_first_name = ?, phone_number = ? WHERE person_id = ?;"""
				cursor.execute(sql_cmd, (byu_id, net_id, surname, rest_of_name, preferred_first_name, phone_number, person_id))

				sql_cmd = """INSERT INTO course_instructors VALUES(?, ?, ?);"""
				try:
					cursor.execute(sql_cmd, (curriculum_id, section_number, person_id))
				except sqlite3.IntegrityError:
					print(f"Got duplicate: {(curriculum_id, section_number, person_id)}")
				except:
					print(f"Error adding: {(curriculum_id, section_number, person_id)}")

			for time in section["times"]:
				begin_time = time["begin_time"]
				building = time["building"]
				end_time = time["end_time"]
				sun = time["sun"]
				mon = time["mon"]
				tue = time["tue"]
				wed = time["wed"]
				thu = time["thu"]
				fri = time["fri"]
				sat = time["sat"]
				room = time["room"]
				sequence_number = time["sequence_number"]

				sql_cmd = """INSERT INTO times VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
				try:
					cursor.execute(sql_cmd, (curriculum_id, section_number, begin_time, building, end_time, fri, mon, room, sat, sequence_number, sun, thu, tue, wed))
				except sqlite3.IntegrityError:
					print(f"Got duplicate: {(curriculum_id, section_number, begin_time, building, end_time, fri, mon, room, sat, sequence_number, sun, thu, tue, wed)}")
				except:
					print(f"Error adding: {(curriculum_id, section_number, begin_time, building, end_time, fri, mon, room, sat, sequence_number, sun, thu, tue, wed)}")

		catalog = course["catalog"]
		curriculum_id = catalog["curriculum_id"]
		credit_hours = catalog["credit_hours"]
		description = catalog["description"]
		effective_date = catalog["effective_date"]
		effective_year_term = catalog["effective_year_term"]
		expired_date = catalog["expired_date"]
		expired_year_term = catalog["expired_year_term"]
		honors_approved = catalog["honors_approved"]
		lab_hours = catalog["lab_hours"]
		lecture_hours = catalog["lecture_hours"]
		note = catalog["note"]
		offered = catalog["offered"]
		prerequisite = catalog["prerequisite"]
		recommended = catalog["recommended"]
		when_taught = catalog["when_taught"]
		sql_cmd = """UPDATE courses SET credit_hours = ?, description = ?, effective_date = ?, effective_year_term = ?, expired_date = ?, expired_year_term = ?, honors_approved = ?, lab_hours = ?, lecture_hours = ?, note = ?, offered = ?, prerequisite = ?, recommended = ?, when_taught = ? WHERE curriculum_id = ?;"""
		try:
			cursor.execute(sql_cmd, (credit_hours, description, effective_date, effective_year_term, expired_date, expired_year_term, honors_approved, lab_hours, lecture_hours, note, offered, prerequisite, recommended, when_taught, curriculum_id))
		except sqlite3.IntegrityError:
			print(f"Got duplicate: {(credit_hours, description, effective_date, effective_year_term, expired_date, expired_year_term, honors_approved, lab_hours, lecture_hours, note, offered, prerequisite, recommended, when_taught, curriculum_id)}")
		except:
			print(f"Error adding: {(credit_hours, description, effective_date, effective_year_term, expired_date, expired_year_term, honors_approved, lab_hours, lecture_hours, note, offered, prerequisite, recommended, when_taught, curriculum_id)}")

		print(f"\rSaved {i}/{len(section_results)} sections...", end="              ")
		i += 1

	print(f"\rSaved {len(section_results)} sections             ")
	print("Commiting changes...", end="")
	connection.commit()
	connection.close()
	print("\rChanges committed")
	print(f"Database entry for {yso[0]} created")
