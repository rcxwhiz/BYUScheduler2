import requests
import random
import string
import time
import threading

semester_api = "http://saasta.byu.edu/noauth/classSchedule/ajax/getYeartermData.php"
classes_api = "http://saasta.byu.edu/noauth/classSchedule/ajax/getClasses.php"
sections_api = "http://saasta.byu.edu/noauth/classSchedule/ajax/getSections.php"
semester_ids = {"fall": "5", "summer": "4", "spring": "3", "winter": "1"}

# number of threads to use when downloading section info - speeds up downloads
# default: 10
max_threads = 10
# seconds to wait between trying to use another thread to download - reduces CPU usage
# default: 0.5
rest_time = 0.5


def make_id():
	# makes a random session id
	# ex. V0TRBMAJJW497M5Q4AWI
	letters = string.ascii_uppercase + string.digits
	return "".join((random.choice(letters) for _ in range(20)))


def get_section(course, session_id, year, semester, section_responses):
	section_data = {
		"courseId": f"{course['curriculum_id']}-{course['title_code']}",
		"sessionId": session_id, "yearterm": year + semester_ids[semester], "no_outcomes": True}

	section_response = requests.post(url=sections_api, data=section_data).json()
	assert(len(section_response["sections"]) > 0, "Encountered an error getting a section")
	section_responses.append(section_response)


def get(semester, year, output_function=print):
	session_id = make_id()
	output_function(f"Using session id: {session_id}")

	output_function(f"Getting departments for {semester} {year}...")
	semester_response = requests.post(url=semester_api, data={"yearterm": year + semester_ids[semester]}).json()
	assert (len(semester_response["department_list"]) > 0, "There was an error getting that semester")
	output_function(f"Got departments for {semester} {year}" + " " * 15)

	classes_data = {"searchObject[teaching_areas][]": semester_response["department_list"],
	                "searchObject[yearterm]": year + semester_ids[semester],
	                "sessionId": session_id}

	output_function(f"Getting class data...")
	classes_response = requests.post(url=classes_api, data=classes_data).json()
	assert (len(classes_response) > 0, "There was an error getting that semester")
	output_function(f"Got classes" + " " * 15)

	start_time = time.time()
	section_responses = []
	keys = iter(classes_response.keys())
	threads = []
	base_threads = threading.active_count()

	while True:
		if threading.active_count() - base_threads < max_threads:
			try:
				course = classes_response[next(keys)]
			except StopIteration:
				break
			new_thread = threading.Thread(target=get_section, args=(course, session_id, year, semester, section_responses))
			new_thread.start()
			threads.append(new_thread)

			if (len(threads) + 1) % 10 == 0:
				elapsed = time.time() - start_time
				seconds_left = elapsed * len(classes_response) / (len(threads) + 1) - elapsed
				output_function(f"Got sections for {len(threads) + 1}/{len(classes_response)} classes... "
				      f"ETA ~{int(seconds_left / 60):02}:{int(seconds_left % 60):02}")
		else:
			time.sleep(rest_time)

	for thread in threads:
		thread.join()

	output_function(f"Got sections for {len(classes_response)} classes" + " " * 15)

	return semester + "_" + year, semester_response, classes_response, section_responses
