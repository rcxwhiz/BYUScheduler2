import os
import sqlite3


def save(yso, db_name):
	# (yearterm, semester_result, classes_result, [section_result])
	if not os.path.exists(db_name):
		print(f"Could not find {db_name}. Making new database...")
		with open(db_name, "w") as _:
			pass
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	sql_cmd = f"""CREATE TABLE {yso['yearterm']}-buildings (
building TEXT NOT NULL PRIMARY KEY);

CREATE TABLE {yso['yearterm']}-dept_list (
dept_code TEXT NOT NULL PRIMARY KEY,
dept_name TEXT NOT NULL
);

CREATE TABLE {yso['yearterm']}-section_types (
section_type TEXT NOT NULL PRIMARY KEY);

CREATE TABLE {yso['yearterm']}-dept_map (
dept TEXT NOT NULL PRIMARY KEY,
dept_code TEXT NOT NULL);

CREATE TABLE {yso['yearterm']}-instructors (
person_id TEXT NOT NULL PRIMARY KEY,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
sort_name TEXT,
byu_id TEXT,
net_id TEXT,
phone_number TEXT,
preffered_first_name TEXT,
rest_of_name TEXT,
surname TEXT
);

CREATE TABLE {yso['yearterm']}-courses (
curriculum_id TEXT NOT NULL PRIMARY KEY,
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

CREATE TABLE {yso['yearterm']}-sections (
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
instructor_id TEXT,
minimum_credit_hours TEXT,
mode TEXT,
mode_desc TEXT,
section_number TEXT NOT NULL,
section_type TEXT,
start_date TEXT,
title_code TEXT,
year_term TEXT);

CREATE TABLE {yso['yearterm']}-times (
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

	cursor.execute(sql_cmd)

	for dept in yso["semester_result"]["department_map"].keys():
		sql_cmd = f"""INSERT INTO {yso['yearterm']}-dept_map VALUES("{dept}", "{yso['semester_result']['department_map'][dept]}");"""
		cursor.execute(sql_cmd)

	for dept in yso["semester_result"]["department_list"].keys():
		sql_cmd = f"""INSERT INTO {yso['yearterm']}-dept_list VALUES("{dept}", "{yso['semester_result']['department_list'][dept]}");"""
		cursor.execute(sql_cmd)

	for section_type in yso["semester_result"]["section_type_list"]:
		sql_cmd = f"""INSERT INTO {yso['yearterm']}-section_types VALUES("{section_type}");"""
		cursor.execute(sql_cmd)

	for instructor in yso["semester_result"]["instructor_list"]:
		sql_cmd = f"""INSERT INTO {yso['yearterm']}-instructors VALUES("{instructor['id']}", "{instructor['first_name']}", "{instructor['last_name']}", "{instructor['sort_name']}", "", "", "", "", "", "");"""
		cursor.execute(sql_cmd)

	for building in yso["semester_result"]["building_list"]:
		sql_cmd = f"""INSERT INTO {yso['yearterm']}-buildings VALUES("{building['building']}");"""
		cursor.execute(sql_cmd)

	for rand_id in yso["class_result"].keys():
		sql_cmd = f"""INSERT INTO {yso['yearterm']}-courses VALUES("{yso[rand_id]['curriculum_id']}", "{yso[rand_id]['catalog_number']}", "{yso[rand_id]['catalog_suffix']}", "{yso[rand_id]['dept_name']}", "{yso[rand_id]['full_title']}", "{yso[rand_id]['title']}", "{yso[rand_id]['title_code']}", "", "", "", "", "", "", "", "", "", "", "", "", "", "");"""
		cursor.execute(sql_cmd)
