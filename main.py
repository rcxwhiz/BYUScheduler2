import BYUAPI
import Dao.MakeDatabase
import Dao.Paths
import UI


def get_db_terminal():
	year = ""
	semester = ""
	while not year.isdigit():
		year = input("Enter year: ")
	while semester not in BYUAPI.semester_ids.keys():
		semester = input("Enter semester: ").lower()

	download_semester = True
	if Dao.Paths.check_exists(semester, year):
		answer = ""
		while answer != "y" and answer != "n":
			answer = input(f"{semester}_{year} is already cached ({Dao.Paths.check_date(semester, year)}) Use that result? (y/n) ").lower()
		download_semester = answer == "n"

	if download_semester:
		try:
			Dao.MakeDatabase.save(True, BYUAPI.get(semester, year))
		except BaseException as e:
			print(f"Error getting {semester} {year}: {str(e)}")


if __name__ == "__main__":
	print("Start BYU Class Getter API\n")
	UI.run_ui()
