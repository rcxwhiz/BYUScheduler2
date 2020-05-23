import BYUAPI


def main():
	print("BYU Class Getter API\n")

	selected_year = ""
	selected_semester = ""
	while not selected_year.isdigit():
		selected_year = input("Enter year: ")
	while selected_semester not in BYUAPI.semester_nums.keys():
		selected_semester = input("Enter semester: ").lower()

	BYUAPI.get(selected_year, selected_semester)


if __name__ == "__main__":
	main()
