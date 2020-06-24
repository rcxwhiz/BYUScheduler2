buildings_schema = {"building": "TEXT NOT NULL PRIMARY KEY"}
dept_list_schema = {"dept_code": "TEXT NOT NULL PRIMARY KEY",
                    "dept_name": "TEXT NOT NULL"}
section_types_schema = {"section_type": "TEXT NOT NULL PRIMARY KEY"}
dept_map_schema = {"dept": "TEXT NOT NULL PRIMARY KEY",
                   "dept_code": "TEXT NOT NULL"}
instructors_schema = {"person_id": "TEXT NOT NULL PRIMARY KEY",
                      "byu_id": "TEXT",
                      "net_id": "TEXT",
                      "first_name": "TEXT",
                      "last_name": "TEXT",
                      "sort_name": "TEXT NOT NULL",
                      "preferred_first_name": "TEXT",
                      "rest_of_name": "TEXT",
                      "surname": "TEXT",
                      "phone_number": "TEXT",
                      "avg_rating": "REAL",
                      "avg_helpful": "REAL",
                      "num_ratings": "INTEGER",
                      "avg_easy_score": "REAL",
                      "avg_clarity_score": "REAL"}
course_instructors_schema = {"curriculum_id_title_code": "TEXT NOT NULL",
                             "section_number": "TEXT NOT NULL",
                             "person_id": "TEXT NOT NULL"}
courses_schema = {"curriculum_id_title_code": "TEXT NOT NULL PRIMARY KEY",
                  "curriculum_id": "TEXT NOT NULL",
                  "title_code": "TEXT",
                  "dept_name": "TEXT NOT NULL",
                  "catalog_number": "TEXT NOT NULL",
                  "catalog_suffix": "TEXT",
                  "title": "TEXT",
                  "full_title": "TEXT",
                  "credit_hours": "TEXT",
                  "description": "TEXT",
                  "effective_date": "TEXT",
                  "expired_date": "TEXT",
                  "effective_year_term": "TEXT",
                  "expired_year_term": "TEXT",
                  "honors_approved": "TEXT",
                  "lab_hours": "TEXT",
                  "lecture_hours": "TEXT",
                  "note": "TEXT",
                  "offered": "TEXT",
                  "prerequisite": "TEXT",
                  "recommended": "TEXT",
                  "when_taught": "TEXT"}
sections_schema = {"curriculum_id_title_code": "TEXT NOT NULL",
                   "curriculum_id": "TEXT NOT NULL",
                   "title_code": "TEXT",
                   "dept_name": "TEXT NOT NULL",
                   "catalog_number": "TEXT NOT NULL",
                   "catalog_suffix": "TEXT",
                   "section_number": "TEXT",
                   "section_type": "TEXT",
                   "credit_hours": "TEXT",
                   "minimum_credit_hours": "TEXT",
                   "credit_type": "TEXT",
                   "fixed_or_variable": "TEXT",
                   "class_size": "TEXT",
                   "seats_available": "TEXT",
                   "waitlist_size": "TEXT",
                   "start_date": "TEXT",
                   "end_date": "TEXT",
                   "honors": "TEXT",
                   "mode": "TEXT",
                   "mode_desc": "TEXT",
                   "year_term": "TEXT"}
times_schema = {"curriculum_id_title_code": "TEXT NOT NULL",
                "section_number": "TEXT NOT NULL",
                "begin_time": "TEXT",
                "end_time": "TEXT",
                "building": "TEXT",
                "room": "TEXT",
                "sun": "TEXT",
                "mon": "TEXT",
                "tue": "TEXT",
                "wed": "TEXT",
                "thu": "TEXT",
                "fri": "TEXT",
                "sat": "TEXT",
                "sequence_number": "TEXT"}


def make_table_cmd(schema):
	columns = []
	for key in schema.keys():
		columns.append(key + " " + schema[key])
	return ", ".join(columns)


def none_safe(item):
	return item if item is not None else ""
