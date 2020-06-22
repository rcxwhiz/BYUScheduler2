from PyQt5 import QtCore, QtGui, QtWidgets


def add_title_page(stacked_widget: QtWidgets.QStackedWidget,
                   course_button_action: callable,
                   instructor_button_action: callable,
                   schedule_button_action: callable):

	page = QtWidgets.QWidget()

	grid_layout_1 = QtWidgets.QGridLayout(page)
	vertical_layout_1 = QtWidgets.QVBoxLayout()

	big_title = QtWidgets.QLabel("BYU Scheduler 2", page)
	title_font = QtGui.QFont()
	title_font.setPointSize(36)
	big_title.setFont(title_font)
	big_title.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
	big_title.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
	vertical_layout_1.addWidget(big_title)

	name = QtWidgets.QLabel("By Josh Bedwell", page)
	name.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
	vertical_layout_1.addWidget(name)

	horizontal_layout_1 = QtWidgets.QHBoxLayout()
	vertical_layout_2 = QtWidgets.QVBoxLayout()

	semester_label = QtWidgets.QLabel(page)
	semester_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
	vertical_layout_2.addWidget(semester_label)

	semester_picker = QtWidgets.QComboBox(page)
	semester_picker.addItems(["Winter", "Spring", "Summer", "Fall"])
	vertical_layout_2.addWidget(semester_picker)

	year_label = QtWidgets.QLabel("Year", page)
	year_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
	vertical_layout_2.addWidget(year_label)

	year_picker = QtWidgets.QSpinBox(page)
	year_picker.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
	year_picker.setRange(2010, 2030)
	year_picker.setValue(2020)
	vertical_layout_2.addWidget(year_picker)

	spacer = QtWidgets.QLabel(page)
	spacer.setText("")
	vertical_layout_2.addWidget(spacer)

	horizontal_layout_1.addLayout(vertical_layout_2)
	grid_layout_2 = QtWidgets.QGridLayout()

	schedule_button = QtWidgets.QPushButton("Make Schedule", page)
	schedule_button.clicked.connect(schedule_button_action)
	grid_layout_2.addWidget(schedule_button, 2, 1, 1, 1)

	instructor_button = QtWidgets.QPushButton("Browse Instructors", page)
	instructor_button.clicked.connect(instructor_button_action)
	grid_layout_2.addWidget(instructor_button, 0, 1, 1, 1)

	course_button = QtWidgets.QPushButton("Browse Courses", page)
	course_button.clicked.connect(course_button_action)
	grid_layout_2.addWidget(course_button, 0, 0, 1, 1)

	horizontal_layout_1.addLayout(grid_layout_2)
	vertical_layout_1.addLayout(horizontal_layout_1)
	grid_layout_1.addLayout(vertical_layout_1, 0, 0, 1, 1)

	stacked_widget.addWidget(page)

	return semester_picker, year_picker
