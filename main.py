import BYUAPI
import Dao


def main():
	print("BYU Class Getter API\n")

	year = ""
	semester = ""
	while not year.isdigit():
		year = input("Enter year: ")
	while semester not in BYUAPI.semester_nums.keys():
		semester = input("Enter semester: ").lower()

	if Dao.Paths.check_exists(semester, year):
		answer = ""
		while answer != "y" and answer != "n":
			answer = input(f"{semester}_{year} is already cached ({Dao.Paths.check_date(semester, year)}) Use that result? (y/n) ").lower()
		if answer == "y":
			print("loading semester")
		if answer == "n":
			test = BYUAPI.get(semester, year)
			Dao.MakeDatabase.save(test)
	else:
		test = BYUAPI.get(semester, year)
		Dao.MakeDatabase.save(test)


if __name__ == "__main__":
	main()
