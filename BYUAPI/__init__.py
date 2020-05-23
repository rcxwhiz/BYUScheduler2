import requests
import random
import string

semester_api = "http://saasta.byu.edu/noauth/classSchedule/ajax/getYeartermData.php"
classes_api = "http://saasta.byu.edu/noauth/classSchedule/ajax/getClasses.php"
sections_api = "http://saasta.byu.edu/noauth/classSchedule/ajax/getSections.php"
semester_nums = {"fall": "5", "summer": "4", "spring": "3", "winter": "1"}
oldSessionId = "V0TRBMAJJW497M5Q4AWI"


def make_id():
	letters = string.ascii_uppercase + string.digits
	return "".join((random.choice(letters) for _ in range(20)))


def get(year, semester):
	print(f"Getting departments for {semester} {year}...")
	try:
		semester_response = requests.post(url=semester_api, data={"yearterm": year + semester_nums[semester]}).json()
		assert (len(semester_response["department_list"]) > 0)
	except:
		print("There was an error getting that semester")
		return None
	print(f"Got departments for {semester} {year}")

	classes_data = {"searchObject[teaching_areas][]": semester_response["department_list"], "searchObject[yearterm]": year + semester_nums[semester], "sessionId": make_id()}

	print(f"Getting class data...")
	try:
		classes_response = requests.post(url=classes_api, data=classes_data).json()
		assert (len(classes_response) > 0)
	except:
		print("There was an error getting that semester")
		return None
	print(f"Got classes")

	section_responses = []
	print("Getting section data...")
	for rand_id in classes_response.keys():
		section_data = {
			"courseId": f"{classes_response[rand_id]['curriculum_id']}-{classes_response[rand_id]['title_code']}",
			"sessionId": make_id(), "yearterm": year + semester_nums[semester], "no_outcomes": True}
		section_response = requests.post(url=sections_api, data=section_data)
		if len(section_response["sections"]) > 0:
			section_responses.append(section_response)
	print("Got sections")

	return year + semester_nums[semester], semester_response, classes_response, section_responses
