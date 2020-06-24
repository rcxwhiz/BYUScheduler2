from PyQt5 import QtCore, QtWidgets

import Model.schedule_core


class SchedulePage:
	def __init__(self, stacked_widget, return_function, data):
		self.core = None
		self.data = data
		page = QtWidgets.QWidget()

		grid_layout_1 = QtWidgets.QGridLayout(page)
		horizontal_layout_1 = QtWidgets.QHBoxLayout()
		vertical_layout_1 = QtWidgets.QVBoxLayout()
		vertical_layout_1.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)

		self.course_list = QtWidgets.QListWidget(page)
		vertical_layout_1.addWidget(self.course_list)

		horizontal_layout_2 = QtWidgets.QHBoxLayout()

		self.course_edit = QtWidgets.QLineEdit(page)
		size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
		size_policy.setHorizontalStretch(0)
		size_policy.setVerticalStretch(0)
		size_policy.setHeightForWidth(self.course_edit.sizePolicy().hasHeightForWidth())
		self.course_edit.setSizePolicy(size_policy)
		self.course_edit.setMaximumSize(QtCore.QSize(120, 16777215))
		horizontal_layout_2.addWidget(self.course_edit)

		add_course_button = QtWidgets.QPushButton("Add Course", page)
		horizontal_layout_2.addWidget(add_course_button)
		vertical_layout_1.addLayout(horizontal_layout_2)
		add_course_button.clicked.connect(self.add_course_action)

		remove_course_button = QtWidgets.QPushButton("Remove Selected Course", page)
		vertical_layout_1.addWidget(remove_course_button)
		remove_course_button.clicked.connect(self.remove_course_action)

		horizontal_layout_3 = QtWidgets.QHBoxLayout()

		clear_classes_button = QtWidgets.QPushButton("Clear Classes")
		horizontal_layout_3.addWidget(clear_classes_button)
		clear_classes_button.clicked.connect(self.clear_classes_action)
		
		self.clear_choices_button = QtWidgets.QPushButton("Clear Choices")
		horizontal_layout_3.addWidget(self.clear_choices_button)
		vertical_layout_1.addLayout(horizontal_layout_3)

		spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		vertical_layout_1.addItem(spacer)
		
		grid_layout_2 = QtWidgets.QGridLayout()

		self.late_classes_button = QtWidgets.QPushButton("Late Classes", page)
		grid_layout_2.addWidget(self.late_classes_button, 0, 0, 1, 1)
		self.least_gaps_button = QtWidgets.QPushButton("Least Gaps", page)
		grid_layout_2.addWidget(self.least_gaps_button, 1, 1, 1, 1)
		self.least_days_button = QtWidgets.QPushButton("Least Days", page)
		grid_layout_2.addWidget(self.least_days_button, 0, 1, 1, 1)
		self.best_professors_button = QtWidgets.QPushButton("Best Professors", page)
		grid_layout_2.addWidget(self.best_professors_button, 0, 2, 1, 1)
		self.early_classes_button = QtWidgets.QPushButton("Early Classes", page)
		grid_layout_2.addWidget(self.early_classes_button, 1, 0, 1, 1)
		self.shortest_days_button = QtWidgets.QPushButton("Shortest Days", page)
		grid_layout_2.addWidget(self.shortest_days_button, 2, 0, 1, 1)
		self.easiest_professors_button = QtWidgets.QPushButton("Easiest Professors", page)
		grid_layout_2.addWidget(self.easiest_professors_button, 1, 2, 1, 1)
		self.smallest_gaps_button = QtWidgets.QPushButton("Smallest Gaps", page)
		grid_layout_2.addWidget(self.smallest_gaps_button, 2, 1, 1, 1)
		self.help_button = QtWidgets.QPushButton("?", page)
		grid_layout_2.addWidget(self.help_button, 2, 2, 1, 1)
		vertical_layout_1.addLayout(grid_layout_2)

		vertical_layout_1.addItem(spacer)

		return_button = QtWidgets.QPushButton("Return to Menu", page)
		return_button.clicked.connect(return_function)
		vertical_layout_1.addWidget(return_button)
		horizontal_layout_1.addLayout(vertical_layout_1)
		vertical_layout_2 = QtWidgets.QVBoxLayout()

		hint_label = QtWidgets.QLabel(
			"Choose all_sections and optimize your schedule until\nthere is only 1 of each section left", page)
		vertical_layout_2.addWidget(hint_label)

		self.table = QtWidgets.QTableWidget(page)
		self.table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
		self.table.setAlternatingRowColors(True)
		self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.table.setColumnCount(2)
		self.table.setHorizontalHeaderLabels(["Course", "Sections"])
		vertical_layout_2.addWidget(self.table)

		horizontal_layout_1.addLayout(vertical_layout_2)
		grid_layout_1.addLayout(horizontal_layout_1, 0, 0, 1, 1)
		stacked_widget.addWidget(page)

	def init_core(self, semester_year):
		self.core = Model.schedule_core.ScheduleCore(semester_year, self.data)

	def add_course_action(self):
		if self.course_edit.text() == "":
			return
		try:
			self.core.add_course(self.course_edit.text().upper())
		except ValueError:
			self.course_edit.setText(f"Can't find {self.course_edit.text()}")
			return
		self.course_edit.clear()
		self.refresh()

	def refresh(self):
		self.core.calculate_possible_schedules()
		self.refresh_list()
		self.refresh_table()

	def remove_course_action(self):
		try:
			self.core.remove_course(self.course_list.itemAt(self.course_list.selectedIndexes()[0].row(),
			                                                self.course_list.selectedIndexes()[0].column()).text())
			self.refresh()
		except IndexError:
			pass

	def clear_classes_action(self):
		self.core.courses.clear()
		self.refresh()

	def clear_choices_action(self):
		print("clearing")

	def refresh_list(self):
		self.course_list.clear()
		for key in self.core.courses.keys():
			self.course_list.addItem(QtWidgets.QListWidgetItem(self.core.courses[key][0]["name"]))

	def refresh_table(self):
		self.table.setRowCount(len(self.core.courses))
		for i, key in enumerate(self.core.courses.keys()):
			self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(self.core.courses[key][0]["name"]))
			used_sections = []
			for section in self.core.courses[key]:
				if section["used"]:
					used_sections.append(str(int(section["data"]["section_number"])))
			self.table.setItem(i, 1, QtWidgets.QTableWidgetItem(", ".join(used_sections)))
