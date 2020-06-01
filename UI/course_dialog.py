# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/course_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


import re

from PyQt5 import QtCore, QtWidgets

import Dao


class Ui_Dialog(object):
	def setupUi(self, Dialog, data):
		self.data = data
		Dialog.setObjectName("Dialog")
		Dialog.resize(1200, 850)
		self.gridLayout = QtWidgets.QGridLayout(Dialog)
		self.gridLayout.setObjectName("gridLayout")
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout()
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.indi_dept_label = QtWidgets.QLabel(Dialog)
		self.indi_dept_label.setObjectName("indi_dept_label")
		self.verticalLayout_2.addWidget(self.indi_dept_label)
		self.indi_num_label = QtWidgets.QLabel(Dialog)
		self.indi_num_label.setObjectName("indi_num_label")
		self.verticalLayout_2.addWidget(self.indi_num_label)
		self.indi_credits_label = QtWidgets.QLabel(Dialog)
		self.indi_credits_label.setObjectName("indi_credits_label")
		self.verticalLayout_2.addWidget(self.indi_credits_label)
		self.indi_title_label = QtWidgets.QLabel(Dialog)
		self.indi_title_label.setObjectName("indi_title_label")
		self.verticalLayout_2.addWidget(self.indi_title_label)
		self.indi_lab_hours_label = QtWidgets.QLabel(Dialog)
		self.indi_lab_hours_label.setObjectName("indi_lab_hours_label")
		self.verticalLayout_2.addWidget(self.indi_lab_hours_label)
		self.indi_lecture_hours_label = QtWidgets.QLabel(Dialog)
		self.indi_lecture_hours_label.setObjectName("indi_lecture_hours_label")
		self.verticalLayout_2.addWidget(self.indi_lecture_hours_label)
		self.indi_honors_label = QtWidgets.QLabel(Dialog)
		self.indi_honors_label.setObjectName("indi_honors_label")
		self.verticalLayout_2.addWidget(self.indi_honors_label)
		self.indi_description_label = QtWidgets.QLabel(Dialog)
		self.indi_description_label.setObjectName("indi_description_label")
		self.verticalLayout_2.addWidget(self.indi_description_label)
		# self.indi_description_display = QtWidgets.QLabel(Dialog)
		# self.indi_description_display.setObjectName("indi_description_display")
		# self.verticalLayout_2.addWidget(self.indi_description_display)
		self.indi_note_label = QtWidgets.QLabel(Dialog)
		self.indi_note_label.setObjectName("indi_note_label")
		self.verticalLayout_2.addWidget(self.indi_note_label)

		# self.indi_note_display = QtWidgets.QLabel(Dialog)
		# self.indi_note_display.setObjectName("indi_note_display")
		# self.verticalLayout_2.addWidget(self.indi_note_display)

		self.indi_offered_label = QtWidgets.QLabel(Dialog)
		self.indi_offered_label.setObjectName("indi_offered_label")
		self.verticalLayout_2.addWidget(self.indi_offered_label)
		self.indi_preqs_label = QtWidgets.QLabel(Dialog)
		self.indi_preqs_label.setObjectName("indi_preqs_label")
		self.verticalLayout_2.addWidget(self.indi_preqs_label)
		self.indi_recommended_label = QtWidgets.QLabel(Dialog)
		self.indi_recommended_label.setObjectName("indi_recommended_label")
		self.verticalLayout_2.addWidget(self.indi_recommended_label)
		self.indi_when_taught_label = QtWidgets.QLabel(Dialog)
		self.indi_when_taught_label.setObjectName("indi_when_taught_label")
		self.verticalLayout_2.addWidget(self.indi_when_taught_label)
		spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_2.addItem(spacerItem)
		self.horizontalLayout.addLayout(self.verticalLayout_2)
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")
		self.indi_sections_label = QtWidgets.QLabel(Dialog)
		self.indi_sections_label.setObjectName("indi_sections_label")
		self.verticalLayout.addWidget(self.indi_sections_label)
		self.indi_sections_table = QtWidgets.QTableWidget(Dialog)
		self.indi_sections_table.setObjectName("indi_sections_table")
		self.indi_sections_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
		self.indi_sections_table.setAlternatingRowColors(True)
		self.indi_sections_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.verticalLayout.addWidget(self.indi_sections_table)
		self.indi_instructors_label = QtWidgets.QLabel(Dialog)
		self.indi_instructors_label.setObjectName("indi_instructors_label")
		self.verticalLayout.addWidget(self.indi_instructors_label)
		self.indi_instructors_table = QtWidgets.QTableWidget(Dialog)
		self.indi_instructors_table.setObjectName("indi_instructors_table")
		self.indi_instructors_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
		self.indi_instructors_table.setAlternatingRowColors(True)
		self.indi_instructors_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.verticalLayout.addWidget(self.indi_instructors_table)
		self.horizontalLayout.addLayout(self.verticalLayout)
		self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

		self.day_keys = {"sun": "Su", "mon": "M", "tue": "Tu", "wed": "W", "thu": "Th", "fri": "F", "sat": "Sa"}

		self.indi_sections_table.setColumnCount(12)
		self.indi_sections_table.setHorizontalHeaderLabels(
			["Section", "Type", "Instructor", "Start", "End", "Days", "Bldg", "Room", "Start/End", "Class Size",
			 "Seats Avail.", "Waitlist"])
		self.indi_sections_table.setRowCount(len(self.data["sections"]))
		for i, section in enumerate(self.data["sections"]):
			section_num = Dao.none_safe(section["section_number"])
			try:
				section_num = int(section_num)
				item = QtWidgets.QTableWidgetItem()
				item.setData(QtCore.Qt.DisplayRole, section_num)
				self.indi_sections_table.setItem(i, 0, item)
			except:
				self.indi_sections_table.setItem(i, 0, QtWidgets.QTableWidgetItem(section_num))
			self.indi_sections_table.setItem(i, 1, QtWidgets.QTableWidgetItem(section["section_type"]))
			instructor_names = []
			for instructor in section["instructors"]:
				instructor_names.append(Dao.none_safe(instructor["sort_name"]))
			self.indi_sections_table.setItem(i, 2, QtWidgets.QTableWidgetItem("\n".join(instructor_names)))
			start = []
			end = []
			days = []
			building = []
			room = []
			for time in section["times"]:
				start.append(Dao.none_safe(self.stamp_to_normal_time(time["begin_time"])))
				end.append(Dao.none_safe(self.stamp_to_normal_time(time["end_time"])))
				days_str = ""
				for key in self.day_keys:
					if time[key] is not None:
						days_str += self.day_keys[key]
				days.append(Dao.none_safe(days_str))
				building.append(Dao.none_safe(time["building"]))
				room.append(Dao.none_safe(time["room"]))
			self.indi_sections_table.setItem(i, 3, QtWidgets.QTableWidgetItem("\n".join(start)))
			self.indi_sections_table.setItem(i, 4, QtWidgets.QTableWidgetItem("\n".join(end)))
			self.indi_sections_table.setItem(i, 5, QtWidgets.QTableWidgetItem("\n".join(days)))
			self.indi_sections_table.setItem(i, 6, QtWidgets.QTableWidgetItem("\n".join(building)))
			self.indi_sections_table.setItem(i, 7, QtWidgets.QTableWidgetItem("\n".join(room)))
			self.indi_sections_table.setItem(i, 8, QtWidgets.QTableWidgetItem(
				f"{section['start_date']}/{section['end_date']}"))
			self.indi_sections_table.setItem(i, 9, QtWidgets.QTableWidgetItem(section["class_size"]))
			self.indi_sections_table.setItem(i, 10, QtWidgets.QTableWidgetItem(section["seats_available"]))
			self.indi_sections_table.setItem(i, 11, QtWidgets.QTableWidgetItem(section["waitlist_size"]))
		self.indi_sections_table.resizeColumnsToContents()
		self.indi_sections_table.resizeRowsToContents()
		self.indi_instructors_table.setSortingEnabled(True)

		self.indi_instructors_table.setColumnCount(6)
		self.indi_instructors_table.setHorizontalHeaderLabels(
			["Sections", "First Name", "Last Name", "# RMP Ratings", "RMP Rating", "RMP Difficulty"])
		self.indi_instructors_table.setRowCount(len(self.data["instructors"]))
		for i, instructor in enumerate(self.data["instructors"]):
			sections_taught = []
			for section in self.data["sections"]:
				for section_instructor in section["instructors"]:
					if section_instructor["person_id"] == instructor["person_id"]:
						sections_taught.append(section["section_number"].lstrip("0"))
						break
			self.indi_instructors_table.setItem(i, 0, QtWidgets.QTableWidgetItem(", ".join(sections_taught)))
			self.indi_instructors_table.setItem(i, 1, QtWidgets.QTableWidgetItem(instructor["first_name"]))
			self.indi_instructors_table.setItem(i, 2, QtWidgets.QTableWidgetItem(instructor["last_name"]))
			try:
				item = QtWidgets.QTableWidgetItem()
				item.setData(QtCore.Qt.DisplayRole, int(instructor["num_ratings"]))
				self.indi_instructors_table.setItem(i, 3, item)
			except:
				self.indi_instructors_table.setItem(i, 3, QtWidgets.QTableWidgetItem(instructor["num_ratings"]))
			try:
				item = QtWidgets.QTableWidgetItem()
				item.setData(QtCore.Qt.DisplayRole, float(instructor["avg_rating"]))
				self.indi_instructors_table.setItem(i, 4, item)
			except:
				self.indi_instructors_table.setItem(i, 4, QtWidgets.QTableWidgetItem(instructor["avg_rating"]))
			try:
				item = QtWidgets.QTableWidgetItem()
				item.setData(QtCore.Qt.DisplayRole, float(instructor["avg_easy_score"]))
				self.indi_instructors_table.setItem(i, 5, item)
			except:
				self.indi_instructors_table.setItem(i, 5, QtWidgets.QTableWidgetItem(instructor["avg_easy_score"]))

	def stamp_to_normal_time(self, time_in: str) -> str:
		if time_in is None:
			return ""
		num_time = int(time_in)
		if num_time >= 1200:
			ampm = "PM"
		else:
			ampm = "AM"
		if num_time >= 1300:
			num_time -= 1200
		time = str(num_time)
		return f"{time[:-2]}:{time[-2:]} {ampm}"

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog",
		                                 f"{self.data['dept_name']} {self.data['catalog_number']}{Dao.none_safe(self.data['catalog_suffix'])}"))
		self.indi_dept_label.setText(_translate("Dialog", f"Dept:\n{self.data['dept_name']}"))
		self.indi_num_label.setText(_translate("Dialog", f"Num:\n{self.data['catalog_number']}"))
		self.indi_credits_label.setText(_translate("Dialog", f"Credits:\n{Dao.none_safe(self.data['credit_hours'])}"))
		self.indi_instructors_label.setText(_translate("Dialog", "Instructors:"))
		self.indi_title_label.setText(
			_translate("Dialog", f"Title:\n{line_breaker(Dao.none_safe(self.data['full_title']).rstrip('.'))}"))
		lab_hours = Dao.none_safe(self.data["lab_hours"])
		if "arr" in lab_hours.lower():
			lab_hours = "variable"
		self.indi_lab_hours_label.setText(_translate("Dialog", f"Lab Hours:\n{lab_hours}"))
		lecture_hours = Dao.none_safe(self.data['lecture_hours'])
		if "arr" in lecture_hours.lower():
			lecture_hours = "variable"
		self.indi_lecture_hours_label.setText(_translate("Dialog", f"Lecture Hours:\n{lecture_hours}"))
		self.indi_honors_label.setText(_translate("Dialog", f"Honors:\n{Dao.none_safe(self.data['honors_approved'])}"))
		self.indi_description_label.setText(
			_translate("Dialog", f"Description:\n{line_breaker(Dao.none_safe(self.data['description']))}"))
		# self.indi_description_display.setText(_translate("Dialog", Dao.none_safe(self.data['description'])))
		self.indi_note_label.setText(_translate("Dialog", f"Note:\n{line_breaker(Dao.none_safe(self.data['note']))}"))
		# self.indi_note_display.setText(_translate("Dialog", Dao.none_safe(self.data['note'])))
		self.indi_offered_label.setText(
			_translate("Dialog", f"Offered:\n{line_breaker(Dao.none_safe(self.data['offered']))}"))
		self.indi_preqs_label.setText(
			_translate("Dialog", f"Prerequisites:\n{line_breaker(Dao.none_safe(self.data['prerequisite']))}"))
		self.indi_recommended_label.setText(
			_translate("Dialog", f"Recommended:\n{line_breaker(Dao.none_safe(self.data['recommended']))}"))
		self.indi_when_taught_label.setText(
			_translate("Dialog", f"When Taught:\n{line_breaker(Dao.none_safe(self.data['when_taught']))}"))
		self.indi_sections_label.setText(_translate("Dialog", "Sections"))


link_re = re.compile(r"(<[aA].*?>)(.*?)(</[aA]>)")


def line_breaker(line: str, width: int = 45) -> str:
	while True:
		match = re.search(link_re, line)
		if match is not None:
			print(f"replacing a match {''.join(match.groups())} to {match.group(2)}")
			line = line.replace("".join(match.groups()), match.group(2))
			print(f"new line:\n{line}")
		else:
			break

	lines = []
	while len(line) > 0:
		if len(line) < width:
			lines.append(line)
			break
		break_point = -1
		for i in range(width, 0, -1):
			if line[i] == " " or line[i] == "\n":
				break_point = i
				break
		if break_point == -1:
			lines.append(line[:width - 1] + "-")
			line = line[width - 1:]
		else:
			lines.append(line[:break_point])
			line = line[break_point:]
	return "\n".join(lines)
