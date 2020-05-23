import requests
import random
import string
import time
import threading

semester_api = "http://saasta.byu.edu/noauth/classSchedule/ajax/getYeartermData.php"
classes_api = "http://saasta.byu.edu/noauth/classSchedule/ajax/getClasses.php"
sections_api = "http://saasta.byu.edu/noauth/classSchedule/ajax/getSections.php"
semester_nums = {"fall": "5", "summer": "4", "spring": "3", "winter": "1"}
oldSessionId = "V0TRBMAJJW497M5Q4AWI"
max_threads = 10
rest_time = 0.5


def make_id():
	letters = string.ascii_uppercase + string.digits
	return "".join((random.choice(letters) for _ in range(20)))


def get_section(course, session_id, year, semester, section_responses):
	section_data = {
		"courseId": f"{course['curriculum_id']}-{course['title_code']}",
		"sessionId": session_id, "yearterm": year + semester_nums[semester], "no_outcomes": True}
	try:
		section_response = requests.post(url=sections_api, data=section_data).json()
		assert(len(section_response["sections"]) > 0)
		section_responses.append(section_response)
	except:
		print("Encountered an error getting a section")


def get(semester, year):
	session_id = make_id()
	print(f"\nUsing session id: {session_id}")

	print(f"Getting departments for {semester} {year}...", end="")
	try:
		semester_response = requests.post(url=semester_api, data={"yearterm": year + semester_nums[semester]}).json()
		assert (len(semester_response["department_list"]) > 0)
	except:
		print("\nThere was an error getting that semester")
		return None
	print(f"\rGot departments for {semester} {year}                ")

	classes_data = {"searchObject[teaching_areas][]": semester_response["department_list"], "searchObject[yearterm]": year + semester_nums[semester], "sessionId": session_id}

	print(f"Getting class data...", end="")
	try:
		classes_response = requests.post(url=classes_api, data=classes_data).json()
		assert (len(classes_response) > 0)
	except:
		print("\nThere was an error getting that semester")
		return None
	print(f"\rGot classes           ")

	start_time = time.time()
	section_responses = []

	keys = iter(classes_response.keys())
	threads = []
	base_threads = threading.active_count()

	while True:
		if threading.active_count() - base_threads < max_threads:
			try:
				course = classes_response[next(keys)]
			except:
				break
			new_thread = threading.Thread(target=get_section, args=(course, session_id, year, semester, section_responses))
			new_thread.start()
			threads.append(new_thread)

			if (len(threads) + 1) % 10 == 0:
				elapsed = time.time() - start_time
				seconds_left = elapsed * len(classes_response) / (len(threads) + 1) - elapsed
				print(f"\rGot sections for {len(threads) + 1}/{len(classes_response)} classes... ETA ~{int(seconds_left / 60):02}:{round(seconds_left % 60):02}", end="         ")
		else:
			time.sleep(rest_time)

	for thread in threads:
		thread.join()

	print(f"\rGot sections for {len(classes_response)} classes                         ")

	return semester + "_" + year, semester_response, classes_response, section_responses
