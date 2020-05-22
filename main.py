import requests
import random
import string

semester_api = "http://saasta.byu.edu/noauth/classSchedule/ajax/getYeartermData.php"
classes_api = "http://saasta.byu.edu/noauth/classSchedule/ajax/getClasses.php"
semester_nums = {"fall": "5", "summer": "4", "spring": "3", "winter": "1"}
oldSessionId = "V0TRBMAJJW497M5Q4AWI"


def makeId():
	letters = string.ascii_uppercase + string.digits
	return "".join((random.choice(letters) for _ in range(20)))


def main():
	print("BYU Class Getter API\n")

	selected_year = ""
	selected_semester = ""
	while not selected_year.isdigit():
		selected_year = input("Enter year: ")
	while selected_semester not in semester_nums.keys():
		selected_semester = input("Enter semester: ").lower()

	print(f"Getting departments for {selected_semester} {selected_year}...")
	try:
		semester_response = requests.post(url=semester_api, data={"yearterm": selected_year + semester_nums[selected_semester]}).json()
		assert(len(semester_response["department_list"]) > 0)
	except:
		print("There was an error getting that semester")
		return None
	print(f"Got departments for {selected_semester} {selected_year}")

	classes_data = {"searchObject[teaching_areas][]": semester_response["department_list"], "searchObject[yearterm]": selected_year + semester_nums[selected_semester], "sessionId": makeId()}

	print(f"Getting classes for {selected_semester} {selected_year}...")
	try:
		classes_response = requests.post(url=classes_api, data=classes_data).json()
		assert (len(classes_response) > 0)
	except:
		print("There was an error getting that semester")
		return None
	print(f"Got classes for {selected_semester} {selected_year}")

	for i, course in enumerate(classes_response.keys()):
		try:
			print(f"{i + 1}) {classes_response[course]['dept_name']} {classes_response[course]['catalog_number']} - {len(classes_response[course]['sections'])} sections")
		except:
			print("Error printing a class")


if __name__ == "__main__":
	main()
