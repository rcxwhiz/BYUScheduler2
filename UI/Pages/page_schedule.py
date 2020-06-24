from PyQt5 import QtCore, QtWidgets


class SchedulePage:
	def __init__(self, stacked_widget, return_function, data):
		self.data = data
		page = QtWidgets.QWidget()

		grid_layout_1 = QtWidgets.QGridLayout(page)
		horizontal_layout_1 = QtWidgets.QHBoxLayout()
		vertical_layout_1 = QtWidgets.QVBoxLayout()
		vertical_layout_1.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)

		course_list = QtWidgets.QListWidget(page)
		vertical_layout_1.addWidget(course_list)

		horizontal_layout_2 = QtWidgets.QHBoxLayout()

		self.course_edit = QtWidgets.QLineEdit(page)
		size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
		size_policy.setHorizontalStretch(0)
		size_policy.setVerticalStretch(0)
		size_policy.setHeightForWidth(self.course_edit.sizePolicy().hasHeightForWidth())
		self.course_edit.setSizePolicy(size_policy)
		self.course_edit.setMaximumSize(QtCore.QSize(120, 16777215))
		horizontal_layout_2.addWidget(self.course_edit)

		self.add_course_button = QtWidgets.QPushButton("Add Course", page)
		horizontal_layout_2.addWidget(self.add_course_button)
		vertical_layout_1.addLayout(horizontal_layout_2)

		self.remove_course_button = QtWidgets.QPushButton("Remove Selected Course", page)
		vertical_layout_1.addWidget(self.remove_course_button)

		horizontal_layout_3 = QtWidgets.QHBoxLayout()

		self.clear_classes_button = QtWidgets.QPushButton("Clear Classes")
		horizontal_layout_3.addWidget(self.clear_classes_button)
		
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

		hint_label = QtWidgets.QLabel("Choose all_sections and optimize your schedule until\nthere is only 1 of each section left", page)
		vertical_layout_2.addWidget(hint_label)

		self.table = QtWidgets.QTableWidget(page)
		self.table.setColumnCount(2)
		self.table.setHorizontalHeaderLabels(["Course", "Sections"])
		vertical_layout_2.addWidget(self.table)

		horizontal_layout_1.addLayout(vertical_layout_2)
		grid_layout_1.addLayout(horizontal_layout_1, 0, 0, 1, 1)
		stacked_widget.addWidget(page)
