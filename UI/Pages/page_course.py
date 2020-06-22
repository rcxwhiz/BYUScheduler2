from PyQt5 import QtCore, QtWidgets


def add_course_page(stacked_widget: QtWidgets.QStackedWidget,
                    filter_action: callable,
                    show_course_action: callable,
                    return_action: callable):
	page = QtWidgets.QWidget()
	grid_layout_1 = QtWidgets.QGridLayout(page)
	horizontal_layout_1 = QtWidgets.QHBoxLayout()
	vertical_layout_1 = QtWidgets.QVBoxLayout()
	# TODO see if this line has an effect
	vertical_layout_1.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)

	dept_label = QtWidgets.QLabel("Dept", page)
	vertical_layout_1.addWidget(dept_label)

	dept_edit = QtWidgets.QLineEdit(page)
	size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
	size_policy.setHorizontalStretch(0)
	size_policy.setVerticalStretch(0)
	size_policy.setHeightForWidth(dept_edit.sizePolicy().hasHeightForWidth())
	dept_edit.setSizePolicy(size_policy)
	vertical_layout_1.addWidget(dept_edit)
	dept_edit.textChanged.connect(filter_action)

	num_label = QtWidgets.QLabel("Course #", page)
	vertical_layout_1.addWidget(num_label)

	num_edit = QtWidgets.QLineEdit(page)
	num_edit.setSizePolicy(size_policy)
	vertical_layout_1.addWidget(num_edit)
	num_edit.textChanged.connect(filter_action)

	credit_hours_check = QtWidgets.QCheckBox("Credit Hours", page)
	vertical_layout_1.addWidget(credit_hours_check)
	credit_hours_check.stateChanged.connect(filter_action)

	credit_hour_spinner = QtWidgets.QDoubleSpinBox(page)
	credit_hour_spinner.setDecimals(1)
	credit_hour_spinner.setSingleStep(0.5)
	vertical_layout_1.addWidget(credit_hour_spinner)
	credit_hour_spinner.valueChanged.connect(filter_action)

	title_label = QtWidgets.QLabel("Title", page)
	vertical_layout_1.addWidget(title_label)

	title_edit = QtWidgets.QLineEdit(page)
	title_edit.setSizePolicy(size_policy)
	vertical_layout_1.addWidget(title_edit)
	title_edit.textChanged.connect(filter_action)

	instructor_label = QtWidgets.QLabel("Instructor", page)
	vertical_layout_1.addWidget(instructor_label)

	instructor_edit = QtWidgets.QLineEdit(page)
	instructor_edit.setSizePolicy(size_policy)
	vertical_layout_1.addWidget(instructor_edit)
	instructor_edit.textChanged.connect(filter_action)

	lab_hours_check = QtWidgets.QCheckBox("Lab Hours", page)
	vertical_layout_1.addWidget(lab_hours_check)
	lab_hours_check.stateChanged.connect(filter_action)

	lab_hours_spinner = QtWidgets.QDoubleSpinBox(page)
	lab_hours_spinner.setDecimals(1)
	lab_hours_spinner.setSingleStep(0.5)
	vertical_layout_1.addWidget(lab_hours_spinner)
	lab_hours_spinner.valueChanged.connect(filter_action)

	lecture_hours_check = QtWidgets.QCheckBox("Lecture Hours", page)
	vertical_layout_1.addWidget(lecture_hours_check)
	lecture_hours_check.stateChanged.connect(filter_action)

	lecture_hours_spinner = QtWidgets.QDoubleSpinBox(page)
	lecture_hours_spinner.setDecimals(1)
	lecture_hours_spinner.setSingleStep(0.5)
	vertical_layout_1.addWidget(lecture_hours_spinner)
	lecture_hours_spinner.valueChanged.connect(filter_action)

	honors_check = QtWidgets.QCheckBox("Honors", page)
	vertical_layout_1.addWidget(honors_check)
	honors_check.stateChanged.connect(filter_action)

	description_label = QtWidgets.QLabel("Description", page)
	vertical_layout_1.addWidget(description_label)

	description_edit = QtWidgets.QTextEdit(page)
	description_edit.setSizePolicy(size_policy)
	description_edit.setMaximumSize(QtCore.QSize(120, 16777215))
	vertical_layout_1.addWidget(description_edit)
	description_edit.textChanged.connect(filter_action)

	spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
	vertical_layout_1.addItem(spacer)

	return_button = QtWidgets.QPushButton("Return to Menu", page)
	vertical_layout_1.addWidget(return_button)
	horizontal_layout_1.addLayout(vertical_layout_1)
	return_button.clicked.connect(return_action)

	table = QtWidgets.QTableWidget(page)
	size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
	size_policy.setHorizontalStretch(0)
	size_policy.setVerticalStretch(0)
	size_policy.setHeightForWidth(table.sizePolicy().hasHeightForWidth())
	table.setSizePolicy(size_policy)
	table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
	table.setAlternatingRowColors(True)
	table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
	table.cellClicked.connect(show_course_action)

	horizontal_layout_1.addWidget(table)
	grid_layout_1.addLayout(horizontal_layout_1, 0, 0, 1, 1)
	stacked_widget.addWidget(page)

	return dept_edit, num_edit, title_edit, instructor_edit, description_edit, honors_check, table, credit_hours_check, credit_hour_spinner, lab_hours_check, lab_hours_spinner, lecture_hours_check, lecture_hours_spinner
