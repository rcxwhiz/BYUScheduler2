from PyQt5 import QtCore, QtWidgets

import Dao
import UI.dialog_instructor


class InstructorPage:
	def __init__(self, stacked_widget, return_function, data):
		self.data = data
		page = QtWidgets.QWidget()

		grid_layout_1 = QtWidgets.QGridLayout(page)

		horizontal_layout_1 = QtWidgets.QHBoxLayout()

		vertical_layout_1 = QtWidgets.QVBoxLayout()
		vertical_layout_1.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)

		first_name_label = QtWidgets.QLabel("First Name", page)
		vertical_layout_1.addWidget(first_name_label)

		self.first_name_input = QtWidgets.QLineEdit(page)
		size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		size_policy.setHorizontalStretch(0)
		size_policy.setVerticalStretch(0)
		size_policy.setHeightForWidth(self.first_name_input.sizePolicy().hasHeightForWidth())
		self.first_name_input.setSizePolicy(size_policy)
		self.first_name_input.textChanged.connect(self.filter_table)
		vertical_layout_1.addWidget(self.first_name_input)

		last_name_label = QtWidgets.QLabel("Last Name", page)
		vertical_layout_1.addWidget(last_name_label)

		self.last_name_input = QtWidgets.QLineEdit(page)
		self.last_name_input.setSizePolicy(size_policy)
		self.last_name_input.textChanged.connect(self.filter_table)
		vertical_layout_1.addWidget(self.last_name_input)

		course_label = QtWidgets.QLabel("Course Taught", page)
		vertical_layout_1.addWidget(course_label)

		self.course_input = QtWidgets.QLineEdit(page)
		self.course_input.setSizePolicy(size_policy)
		self.course_input.textChanged.connect(self.filter_table)
		vertical_layout_1.addWidget(self.course_input)

		spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		vertical_layout_1.addItem(spacer)
		horizontal_layout_1.addLayout(vertical_layout_1)

		return_button = QtWidgets.QPushButton("Return to Menu", page)
		return_button.clicked.connect(return_function)
		vertical_layout_1.addWidget(return_button)

		self.table = QtWidgets.QTableWidget(page)
		size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		size_policy.setHorizontalStretch(0)
		size_policy.setVerticalStretch(0)
		size_policy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
		self.table.setSizePolicy(size_policy)
		self.table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
		self.table.setAlternatingRowColors(True)
		self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.table.cellClicked.connect(self.show_instructor)

		horizontal_layout_1.addWidget(self.table)
		grid_layout_1.addLayout(horizontal_layout_1, 0, 0, 1, 1)
		stacked_widget.addWidget(page)

	def initialize_table(self):
		self.table.setColumnCount(8)
		self.table.setRowCount(len(self.data))
		self.table.setHorizontalHeaderLabels(
			["First Name", "Last Name", "Sort Name", "# Courses Taught", "# RMP Ratings", "RMP Rating",
			 "RMP Difficulty", "HIDDEN"])
		for i, key in enumerate(self.data.keys()):
			self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(Dao.none_safe(self.data[key]["first_name"])))
			self.table.setItem(i, 1, QtWidgets.QTableWidgetItem(Dao.none_safe(self.data[key]["last_name"])))
			self.table.setItem(i, 2, QtWidgets.QTableWidgetItem(Dao.none_safe(self.data[key]["sort_name"])))

			different_classes_taught = set()
			for section in self.data[key]["classes_taught"]:
				different_classes_taught.add(section["course"])
			item = QtWidgets.QTableWidgetItem()
			item.setData(QtCore.Qt.DisplayRole, len(different_classes_taught))
			self.table.setItem(i, 3, item)

			try:
				item = QtWidgets.QTableWidgetItem()
				item.setData(QtCore.Qt.DisplayRole, self.data[key]["num_ratings"])
				self.table.setItem(i, 4, item)
			except:
				self.table.setItem(i, 4, QtWidgets.QTableWidgetItem(
					Dao.none_safe(self.data[key]["num_ratings"])))

			try:
				item = QtWidgets.QTableWidgetItem()
				item.setData(QtCore.Qt.DisplayRole, self.data[key]["avg_rating"])
				self.table.setItem(i, 5, item)
			except:
				self.table.setItem(i, 5, QtWidgets.QTableWidgetItem(
					Dao.none_safe(self.data[key]["avg_rating"])))

			try:
				item = QtWidgets.QTableWidgetItem()
				item.setData(QtCore.Qt.DisplayRole, self.data[key]["avg_easy_score"])
				self.table.setItem(i, 6, item)
			except:
				self.table.setItem(i, 5, QtWidgets.QTableWidgetItem(
					Dao.none_safe(self.data[key]["avg_easy_score"])))

			self.table.setItem(i, 7, QtWidgets.QTableWidgetItem(key))
		self.table.hideColumn(7)

		self.table.setSortingEnabled(True)
		self.table.resizeColumnsToContents()

	def filter_table(self):
		first_filter = self.first_name_input.text().lower()
		last_filter = self.last_name_input.text().lower()
		num_filter = self.course_input.text().lower()

		for index in range(self.table.rowCount()):

			show = True
			if first_filter != "":
				if first_filter not in self.table.item(index, 0).text().lower():
					show = False
			if show and last_filter != "":
				if last_filter not in self.table.item(index, 1).text().lower():
					show = False
			if show and num_filter != "":
				show = False
				for course in self.data[self.table.item(index, 7).text()]["classes_taught"]:
					if num_filter in course["course"].lower():
						show = True
						break
			if show:
				self.table.showRow(index)
			else:
				self.table.hideRow(index)

	def show_instructor(self, row, column):
		instructor_dialog = QtWidgets.QDialog()
		instructor_ui = UI.dialog_instructor.Ui_Dialog()
		instructor_ui.setupUi(instructor_dialog, self.data[self.table.item(row, 7).text()])
		instructor_dialog.exec_()

	def initialize_page(self):
		self.first_name_input.clear()
		self.last_name_input.clear()
		self.course_input.clear()
		self.initialize_table()
