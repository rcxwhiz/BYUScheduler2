import os
from datetime import datetime


def database_path(semester, year):
	return database_path_1(semester + "_" + year)


def database_path_1(semester_year):
	return os.path.join("cache", semester_year + ".db")


def check_exists(semester, year):
	return check_exists_1(semester + "_" + year)


def check_exists_1(semester_year):
	return os.path.exists(database_path_1(semester_year))


def check_date(semester, year):
	return check_date_1(semester + "_" + year)


def check_date_1(semester_year):
	return datetime.fromtimestamp(os.path.getmtime(database_path_1(semester_year))).strftime("%B %d, %Y %H:%M:%S")
