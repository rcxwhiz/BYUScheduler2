import os


def database_path(semester, year):
	return os.path.join("cache", semester + "_" + year + ".db")


def database_path(semester_year):
	return os.path.join("cache", semester_year + ".db")


def check_exists(semester, year):
	return os.path.exists(database_path(semester, year))


def check_exists(semester_year):
	return os.path.exists(database_path(semester_year))


def check_date(semester, year):
	return os.path.getmtime(database_path(semester, year))


def check_date(semester_year):
	return os.path.getmtime(database_path(semester_year))
