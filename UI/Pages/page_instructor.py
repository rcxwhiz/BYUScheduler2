from PyQt5 import QtCore, QtGui, QtWidgets


def add_instructor_page(stacked_widget: QtWidgets.QStackedWidget,
                        filter_table_action: callable,
                        show_instructor_action: callable,
                        return_button_action: callable) -> (QtWidgets.QLineEdit, QtWidgets.QLineEdit, QtWidgets.QLineEdit, QtWidgets.QTableWidget):
	page = QtWidgets.QWidget()

	grid_layout_1 = QtWidgets.QGridLayout(page)

	horizontal_layout_1 = QtWidgets.QHBoxLayout()

	vertical_layout_1 = QtWidgets.QVBoxLayout()
	vertical_layout_1.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)

	first_name_label = QtWidgets.QLabel(page)
	first_name_label.setText("First Name")
	vertical_layout_1.addWidget(first_name_label)

	first_name_input = QtWidgets.QLineEdit(page)
	size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
	size_policy.setHorizontalStretch(0)
	size_policy.setVerticalStretch(0)
	size_policy.setHeightForWidth(first_name_input.sizePolicy().hasHeightForWidth())
	first_name_input.setSizePolicy(size_policy)
	first_name_input.textChanged.connect(filter_table_action)
	vertical_layout_1.addWidget(first_name_input)

	last_name_label = QtWidgets.QLabel(page)
	last_name_label.setText("Last Name")
	vertical_layout_1.addWidget(last_name_label)

	last_name_input = QtWidgets.QLineEdit(page)
	last_name_input.setSizePolicy(size_policy)
	last_name_input.textChanged.connect(filter_table_action)
	vertical_layout_1.addWidget(last_name_input)

	course_label = QtWidgets.QLabel(page)
	course_label.setText("Course Taught")
	vertical_layout_1.addWidget(course_label)

	course_input = QtWidgets.QLineEdit(page)
	course_input.setSizePolicy(size_policy)
	course_input.textChanged.connect(filter_table_action)
	vertical_layout_1.addWidget(course_input)

	spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
	vertical_layout_1.addItem(spacer)
	horizontal_layout_1.addLayout(vertical_layout_1)

	return_button = QtWidgets.QPushButton(page)
	return_button.setText("Return to Menu")
	return_button.clicked.connect(return_button_action)
	vertical_layout_1.addWidget(return_button)

	table = QtWidgets.QTableWidget(page)
	size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
	size_policy.setHorizontalStretch(0)
	size_policy.setVerticalStretch(0)
	size_policy.setHeightForWidth(table.sizePolicy().hasHeightForWidth())
	table.setSizePolicy(size_policy)
	table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
	table.setAlternatingRowColors(True)
	table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
	table.cellClicked.connect(show_instructor_action)

	horizontal_layout_1.addWidget(table)
	grid_layout_1.addLayout(horizontal_layout_1, 0, 0, 1, 1)
	stacked_widget.addWidget(page)

	return first_name_input, last_name_input, course_input, table
