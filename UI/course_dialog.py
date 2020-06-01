# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/course_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_Dialog(object):
	def setupUi(self, Dialog, data):
		self.data = data
		Dialog.setObjectName("Dialog")
		Dialog.resize(1200, 640)
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
		self.indi_description_display = QtWidgets.QTextBrowser(Dialog)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.indi_description_display.sizePolicy().hasHeightForWidth())
		self.indi_description_display.setSizePolicy(sizePolicy)
		self.indi_description_display.setMinimumSize(QtCore.QSize(0, 0))
		self.indi_description_display.setMaximumSize(QtCore.QSize(200, 16777215))
		self.indi_description_display.setTextInteractionFlags(
			QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
		self.indi_description_display.setObjectName("indi_description_display")
		self.verticalLayout_2.addWidget(self.indi_description_display)
		self.indi_note_label = QtWidgets.QLabel(Dialog)
		self.indi_note_label.setObjectName("indi_note_label")
		self.verticalLayout_2.addWidget(self.indi_note_label)

		self.indi_note_display = QtWidgets.QTextBrowser(Dialog)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.indi_note_display.sizePolicy().hasHeightForWidth())
		self.indi_note_display.setSizePolicy(sizePolicy)
		self.indi_note_display.setMinimumSize(QtCore.QSize(0, 0))
		self.indi_note_display.setMaximumSize(QtCore.QSize(200, 16777215))
		self.indi_note_display.setTextInteractionFlags(
			QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
		self.indi_note_display.setObjectName("indi_note_display")
		self.verticalLayout_2.addWidget(self.indi_note_display)

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
			["Section Num", "Type", "Instructor", "Start", "End", "Days", "Bldg", "Room", "Start/End", "Class Size",
			 "Seats Avail.", "Waitlist"])
		self.indi_sections_table.setRowCount(len(self.data["sections"]))
		for i, section in enumerate(self.data["sections"]):
			section_num = section["section_number"]
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
				instructor_names.append(instructor["sort_name"])
			self.indi_sections_table.setItem(i, 2, QtWidgets.QTableWidgetItem("\n".join(instructor_names)))
			start = []
			end = []
			days = []
			building = []
			room = []
			for time in section["times"]:
				start.append(self.stamp_to_normal_time(time["begin_time"]))
				end.append(self.stamp_to_normal_time(time["end_time"]))
				days_str = ""
				for key in self.day_keys:
					if time[key] is not None:
						days_str += self.day_keys[key]
				days.append(days_str)
				building.append(time["building"])
				room.append(time["room"])
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

	def stamp_to_normal_time(self, time_in: str) -> str:
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
		suffix = self.data["catalog_suffix"]
		if suffix is None:
			suffix = ""
		Dialog.setWindowTitle(_translate("Dialog", f"{self.data['dept_name']} {self.data['catalog_number']}{suffix}"))
		self.indi_dept_label.setText(_translate("Dialog", f"Dept:\n{self.data['dept_name']}"))
		self.indi_num_label.setText(_translate("Dialog", f"Num:\n{self.data['catalog_number']}"))
		self.indi_credits_label.setText(_translate("Dialog", f"Credits:\n{self.data['credit_hours']}"))
		self.indi_instructors_label.setText(_translate("Dialog", "Instructors"))
		title = self.data["full_title"]
		if title.endswith("."):
			title = title[:-1]
		self.indi_title_label.setText(_translate("Dialog", f"Title:\n{title}"))
		lab_hours = self.data["lab_hours"]
		if "arr" in lab_hours.lower():
			lab_hours = "variable"
		self.indi_lab_hours_label.setText(_translate("Dialog", f"Lab Hours:\n{lab_hours}"))
		lecture_hours = self.data['lecture_hours']
		if "arr" in lecture_hours.lower():
			lecture_hours = "variable"
		self.indi_lecture_hours_label.setText(_translate("Dialog", f"Lecture Hours:\n{lecture_hours}"))
		self.indi_honors_label.setText(_translate("Dialog", f"Honors:\n{self.data['honors_approved']}"))
		self.indi_description_label.setText(_translate("Dialog", "Description"))
		description = self.data["description"]
		if description is None:
			description = ""
		self.indi_description_display.setText(_translate("Dialog", description))
		self.indi_note_label.setText(_translate("Dialog", "Note:"))
		note = self.data["note"]
		if note is None:
			note = ""
		self.indi_note_display.setText(_translate("Dialog", note))
		self.indi_offered_label.setText(_translate("Dialog", f"Offered:\n{self.data['offered']}"))
		self.indi_preqs_label.setText(_translate("Dialog", f"Prerequisites:\n{self.data['prerequisite']}"))
		self.indi_recommended_label.setText(_translate("Dialog", f"Recommended:\n{self.data['recommended']}"))
		self.indi_when_taught_label.setText(_translate("Dialog", f"When Taught:\n{self.data['when_taught']}"))
		self.indi_sections_label.setText(_translate("Dialog", "Sections"))
