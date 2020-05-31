import os
from datetime import datetime


def database_path(semester: str, year: str) -> str:
	return database_path_1(semester + "_" + year)


def database_path_1(semester_year: str) -> str:
	return os.path.join("byu_db_cache", semester_year + ".db")


def check_exists(semester: str, year: str) -> bool:
	return check_exists_1(semester + "_" + year)


def check_exists_1(semester_year: str) -> bool:
	return os.path.exists(database_path_1(semester_year))


def check_date(semester: str, year: str) -> str:
	return check_date_1(semester + "_" + year)


def check_date_1(semester_year: str) -> str:
	return datetime.fromtimestamp(os.path.getmtime(database_path_1(semester_year))).strftime("%d %B %Y %H:%M:%S")
