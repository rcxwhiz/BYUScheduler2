from PyQt5 import QtCore, QtWidgets

import Dao
import UI.Dialogs.dialog_course


class CoursePage:
	def __init__(self, stacked_widget, return_function, data):
		self.data = data
		page = QtWidgets.QWidget()
		grid_layout_1 = QtWidgets.QGridLayout(page)
		horizontal_layout_1 = QtWidgets.QHBoxLayout()
		vertical_layout_1 = QtWidgets.QVBoxLayout()
		# TODO see if this line has an effect
		vertical_layout_1.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)

		dept_label = QtWidgets.QLabel("Dept", page)
		vertical_layout_1.addWidget(dept_label)

		self.dept_edit = QtWidgets.QLineEdit(page)
		size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		size_policy.setHorizontalStretch(0)
		size_policy.setVerticalStretch(0)
		size_policy.setHeightForWidth(self.dept_edit.sizePolicy().hasHeightForWidth())
		self.dept_edit.setSizePolicy(size_policy)
		vertical_layout_1.addWidget(self.dept_edit)
		self.dept_edit.textChanged.connect(self.filter_table)

		num_label = QtWidgets.QLabel("Course #", page)
		vertical_layout_1.addWidget(num_label)

		self.num_edit = QtWidgets.QLineEdit(page)
		self.num_edit.setSizePolicy(size_policy)
		vertical_layout_1.addWidget(self.num_edit)
		self.num_edit.textChanged.connect(self.filter_table)

		self.credit_hours_check = QtWidgets.QCheckBox("Credit Hours", page)
		vertical_layout_1.addWidget(self.credit_hours_check)
		self.credit_hours_check.stateChanged.connect(self.filter_table)

		self.credit_hour_spinner = QtWidgets.QDoubleSpinBox(page)
		self.credit_hour_spinner.setDecimals(1)
		self.credit_hour_spinner.setSingleStep(0.5)
		vertical_layout_1.addWidget(self.credit_hour_spinner)
		self.credit_hour_spinner.valueChanged.connect(self.filter_table)

		title_label = QtWidgets.QLabel("Title", page)
		vertical_layout_1.addWidget(title_label)

		self.title_edit = QtWidgets.QLineEdit(page)
		self.title_edit.setSizePolicy(size_policy)
		vertical_layout_1.addWidget(self.title_edit)
		self.title_edit.textChanged.connect(self.filter_table)

		instructor_label = QtWidgets.QLabel("Instructor", page)
		vertical_layout_1.addWidget(instructor_label)

		self.instructor_edit = QtWidgets.QLineEdit(page)
		self.instructor_edit.setSizePolicy(size_policy)
		vertical_layout_1.addWidget(self.instructor_edit)
		self.instructor_edit.textChanged.connect(self.filter_table)

		self.lab_hours_check = QtWidgets.QCheckBox("Lab Hours", page)
		vertical_layout_1.addWidget(self.lab_hours_check)
		self.lab_hours_check.stateChanged.connect(self.filter_table)

		self.lab_hours_spinner = QtWidgets.QDoubleSpinBox(page)
		self.lab_hours_spinner.setDecimals(1)
		self.lab_hours_spinner.setSingleStep(0.5)
		vertical_layout_1.addWidget(self.lab_hours_spinner)
		self.lab_hours_spinner.valueChanged.connect(self.filter_table)

		self.lecture_hours_check = QtWidgets.QCheckBox("Lecture Hours", page)
		vertical_layout_1.addWidget(self.lecture_hours_check)
		self.lecture_hours_check.stateChanged.connect(self.filter_table)

		self.lecture_hours_spinner = QtWidgets.QDoubleSpinBox(page)
		self.lecture_hours_spinner.setDecimals(1)
		self.lecture_hours_spinner.setSingleStep(0.5)
		vertical_layout_1.addWidget(self.lecture_hours_spinner)
		self.lecture_hours_spinner.valueChanged.connect(self.filter_table)

		self.honors_check = QtWidgets.QCheckBox("Honors", page)
		vertical_layout_1.addWidget(self.honors_check)
		self.honors_check.stateChanged.connect(self.filter_table)

		description_label = QtWidgets.QLabel("Description", page)
		vertical_layout_1.addWidget(description_label)

		self.description_edit = QtWidgets.QTextEdit(page)
		self.description_edit.setSizePolicy(size_policy)
		self.description_edit.setMaximumSize(QtCore.QSize(120, 16777215))
		vertical_layout_1.addWidget(self.description_edit)
		self.description_edit.textChanged.connect(self.filter_table)

		spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		vertical_layout_1.addItem(spacer)

		return_button = QtWidgets.QPushButton("Return to Menu", page)
		vertical_layout_1.addWidget(return_button)
		horizontal_layout_1.addLayout(vertical_layout_1)
		return_button.clicked.connect(return_function)

		self.table = QtWidgets.QTableWidget(page)
		size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		size_policy.setHorizontalStretch(0)
		size_policy.setVerticalStretch(0)
		size_policy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
		self.table.setSizePolicy(size_policy)
		self.table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
		self.table.setAlternatingRowColors(True)
		self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.table.cellClicked.connect(self.show_course)

		horizontal_layout_1.addWidget(self.table)
		grid_layout_1.addLayout(horizontal_layout_1, 0, 0, 1, 1)
		stacked_widget.addWidget(page)

	def populate_table(self):
		self.table.setColumnCount(9)
		self.table.setRowCount(len(self.data))
		self.table.setHorizontalHeaderLabels(
			["Dept", "Course Num", "Credits", "Title", "# Sections", "# Instructors", "Lab Hours", "Lecture Hours",
			 "HIDDEN"])
		for i, key in enumerate(self.data.keys()):
			self.table.setItem(i, 0,
			                   QtWidgets.QTableWidgetItem(Dao.none_safe(self.data[key]["dept_name"])))
			self.table.setItem(i, 1, QtWidgets.QTableWidgetItem(
				self.data[key]["catalog_number"] + Dao.none_safe(self.data[key]["catalog_suffix"])))
			self.table.setItem(i, 2,
			                   QtWidgets.QTableWidgetItem(Dao.none_safe(self.data[key]["credit_hours"])))
			title = Dao.none_safe(self.data[key]["full_title"])
			if title.endswith("."):
				title = title[:-1]
			self.table.setItem(i, 3, QtWidgets.QTableWidgetItem(title))
			item = QtWidgets.QTableWidgetItem()
			item.setData(QtCore.Qt.DisplayRole, len(self.data[key]["sections"]))
			self.table.setItem(i, 4, item)
			item = QtWidgets.QTableWidgetItem()
			item.setData(QtCore.Qt.DisplayRole, len(self.data[key]["instructors"]))
			self.table.setItem(i, 5, item)
			lab_hours = Dao.none_safe(self.data[key]["lab_hours"])
			try:
				lab_hours = float(lab_hours)
				item = QtWidgets.QTableWidgetItem()
				item.setData(QtCore.Qt.DisplayRole, lab_hours)
				self.table.setItem(i, 6, item)
			except:
				if "arr" in lab_hours.lower():
					lab_hours = "variable"
				self.table.setItem(i, 6, QtWidgets.QTableWidgetItem(lab_hours))
			lecture_hours = Dao.none_safe(self.data[key]["lecture_hours"])
			try:
				lecture_hours = float(lecture_hours)
				item = QtWidgets.QTableWidgetItem()
				item.setData(QtCore.Qt.DisplayRole, lecture_hours)
				self.table.setItem(i, 7, item)
			except:
				if "arr" in lecture_hours.lower():
					lecture_hours = "variable"
				self.table.setItem(i, 7, QtWidgets.QTableWidgetItem(lecture_hours))
			self.table.setItem(i, 8,
			                   QtWidgets.QTableWidgetItem(self.data[key]["curriculum_id_title_code"]))
		self.table.hideColumn(8)
		self.table.setSortingEnabled(True)
		self.table.resizeColumnsToContents()

	def filter_table(self):
		dept_filter = self.dept_edit.text().lower()
		num_filter = self.num_edit.text().lower()
		credit_hours_checked = self.credit_hours_check.isChecked()
		credit_hour_filter = self.credit_hour_spinner.value()
		title_filter = self.title_edit.text().lower()
		instructor_filter = self.instructor_edit.text().lower()
		instructor_parts = instructor_filter.split(" ")
		lab_hour_checked = self.lab_hours_check.isChecked()
		lab_hour_filter = self.lab_hours_spinner.value()
		lecture_hour_checked = self.lecture_hours_check.isChecked()
		lecture_hours_filter = self.lecture_hours_spinner.value()
		honors_checked = self.honors_check.isChecked()
		description_filter = self.description_edit.toPlainText().lower()

		for index in range(self.table.rowCount()):
			show = True
			try:
				if dept_filter != "":
					if dept_filter not in self.table.item(index, 0).text().lower():
						show = False
				if show and num_filter != "":
					if num_filter not in self.table.item(index, 1).text().lower():
						show = False
				if show and credit_hours_checked:
					if credit_hour_filter != float(self.table.item(index, 2).text()):
						show = False
				if show and title_filter != "":
					if title_filter not in self.table.item(index, 3).text().lower():
						show = False
				if show and instructor_filter != "":
					show = False
					found = True
					for instructor in self.data[self.table.item(index, 8).text()]["instructors"]:
						if instructor is not None:
							for part in instructor_parts:
								if part not in instructor["sort_name"].lower():
									found = False
							if found:
								show = True
								break

				if show and lab_hour_checked:
					if lab_hour_filter != float(self.table.item(index, 6).text()):
						show = False
				if show and lecture_hour_checked:
					if lecture_hours_filter != float(self.table.item(index, 7).text()):
						show = False
				if show and honors_checked and (
						self.data[self.table.item(index, 8).text()]["honors_approved"] is None or
						self.data[self.table.item(index, 8).text()]["honors_approved"].lower() == "n"):
					show = False
				if show and description_filter != "":
					if self.data[self.table.item(index, 8).text()][
						"description"] is None or description_filter not in \
							self.data[self.table.item(index, 8).text()]["description"].lower():
						show = False
			except IOError as e:
				print("error sorting")
				print(e)
				show = False

			if show:
				self.table.showRow(index)
			else:
				self.table.hideRow(index)

	def show_course(self, row, column):
		course_dialog = QtWidgets.QDialog()
		course_ui = UI.Dialogs.dialog_course.Ui_Dialog()
		course_ui.setupUi(course_dialog, self.data[self.table.item(row, 8).text()])
		course_dialog.exec_()

	def initialize_page(self):
		self.dept_edit.clear()
		self.num_edit.clear()
		self.title_edit.clear()
		self.instructor_edit.clear()
		self.description_edit.clear()
		self.honors_check.setChecked(False)
		self.description_edit.clear()
