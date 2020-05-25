import requests
import time
import threading

url1 = "https://search-production.ratemyprofessors.com/solr/rmp/select/?solrformat=true&rows=2&wt=json&q="
url2 = "+AND+schoolid_s%3A135"

max_threads = 10
rest_time = 0.5

sql_cmd = """UPDATE instructors SET found_rmp = ?, avg_rating = ?, avg_helpful = ?, num_ratings = ?, avg_easy_score = ?, avg_clarity_score = ? WHERE person_id = ?;"""


def get_rating(person_id, first_name, last_name, rest_of_name, surname, data_stream):
	url = url1 + first_name.replace(" ", "+") + "+" + last_name.replace(" ", "+") + url2
	response = requests.post(url=url).json()["response"]

	got_data = True
	if response["numFound"] == 0:
		url = url1 + rest_of_name.replace(" ", "+") + "+" + surname.replace(" ", "+") + url2
		response = requests.post(url=url).json()["response"]
		if response["numFound"] == 0:
			got_data = False
	if got_data and response["docs"][0]["total_number_of_ratings_i"] > 0:
		values = (True,
		          response["docs"][0]["averageratingscore_rf"],
		          response["docs"][0]["averagehelpfulscore_rf"],
		          response["docs"][0]["total_number_of_ratings_i"],
		          response["docs"][0]["averageeasyscore_rf"],
		          response["docs"][0]["averageclarityscore_rf"],
		          person_id)
	else:
		values = (False, None, None, None, None, None, person_id)
	data_stream.append(values)


def append_rmp_info(profs, cursor):
	start_time = time.time()
	prof_iter = iter(profs)
	threads = []
	base_threads = threading.active_count()
	data_stream = []

	while True:
		if threading.active_count() - base_threads < max_threads:
			try:
				professor = next(prof_iter)
			except StopIteration:
				break
			new_thread = threading.Thread(target=get_rating, args=(professor[0], professor[1], professor[2], professor[8], professor[9], data_stream))
			new_thread.start()
			threads.append(new_thread)

			if (len(threads) + 1) % 10 == 0:
				elapsed = time.time() - start_time
				seconds_left = elapsed * len(profs) / (len(threads) + 1) - elapsed
				print(f"\rGot Rate My Professor data for {len(threads) + 1}/{len(profs)} instructors... "
				      f"ETA ~{int(seconds_left / 60):02}:{int(seconds_left % 60):02}", end=" " * 15)
		else:
			time.sleep(rest_time)

	for thread in threads:
		thread.join()

	print(f"\rGot Rate My Professor data for {len(profs)} instructors" + " " * 15)

	print("Comitting Rate My Professor data...", end="")
	for data_bit in data_stream:
		cursor.execute(sql_cmd, data_bit)
	print("\rComitted Rate My Professor data       ")
