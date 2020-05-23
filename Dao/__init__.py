import sqlite3
import os
import Dao.MakeDatabase

db_name = "byu_classes.db"


def save(yso):
	MakeDatabase.save(yso, db_name)


def check_exists(yearsemester):
	if not os.path.exists(db_name):
		return False
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()
	cursor.execute(f"""
	SELECT COUNT(*)
	FROM information_schema.tables
	WHERE table_name = '{yearsemester}'""")
	if cursor.fetchone()[0] == 1:
		cursor.close()
		return True
	else:
		cursor.close()
		return False


def get(yearsemester):
	if not os.path.exists(db_name):
		print(f"Could not find {db_name}")
		return None
	connection = sqlite3.connect(db_name)
