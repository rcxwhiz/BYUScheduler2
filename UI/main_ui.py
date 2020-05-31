from PyQt5 import QtCore, QtGui, QtWidgets

import UI.instructor_dialog
import UI.title_popup_dialog


class Ui_MainWindow(object):
	# Setup
	# ----------------------------------------------------------------------------------
	def setup_ui(self, MainWindowIn: QtWidgets.QMainWindow) -> None:
		self.setup_window(MainWindowIn)
		self.loaded_data = {}

		self.setup_title_page()
		self.setup_browse_instructor_page()
		self.setup_browse_course_page()

		self.finish_setup_window()

	def setup_window(self, MainWindowIn: QtWidgets.QMainWindow) -> None:
		self.main_window = MainWindowIn
		self.main_window.setObjectName("MainWindow")

		self.main_window_central_widget = QtWidgets.QWidget(self.main_window)
		self.main_window_central_widget.setObjectName("centralwidget")

		self.main_window_grid_layout = QtWidgets.QGridLayout(self.main_window_central_widget)
		self.main_window_grid_layout.setObjectName("gridLayout")

		self.main_window_stacked_widget = QtWidgets.QStackedWidget(self.main_window_central_widget)
		self.main_window_stacked_widget.setObjectName("stackedWidget")

	def finish_setup_window(self) -> None:
		self.main_window_grid_layout.addWidget(self.main_window_stacked_widget, 0, 0, 1, 1)
		self.main_window.setCentralWidget(self.main_window_central_widget)

		self.retranslate_ui()
		QtCore.QMetaObject.connectSlotsByName(self.main_window)

		self.hook_buttons()

		self.goto_title_page()

	def setup_title_page(self) -> None:
		self.title_page = QtWidgets.QWidget()
		self.title_page.setObjectName("page")

		self.title_grid_layout_1 = QtWidgets.QGridLayout(self.title_page)
		self.title_grid_layout_1.setObjectName("gridLayout1")

		self.title_vertical_layout_1 = QtWidgets.QVBoxLayout()
		self.title_vertical_layout_1.setObjectName("verticalLayout")

		self.title_big_title = QtWidgets.QLabel(self.title_page)
		title_font = QtGui.QFont()
		title_font.setPointSize(36)
		self.title_big_title.setFont(title_font)
		self.title_big_title.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
		self.title_big_title.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
		self.title_big_title.setObjectName("big_title")

		self.title_vertical_layout_1.addWidget(self.title_big_title)

		self.title_name = QtWidgets.QLabel(self.title_page)
		self.title_name.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
		self.title_name.setObjectName("name_title")

		self.title_vertical_layout_1.addWidget(self.title_name)
		self.title_horizontal_layout = QtWidgets.QHBoxLayout()
		self.title_horizontal_layout.setObjectName("horizontalLayout")
		self.title_vertical_layout_2 = QtWidgets.QVBoxLayout()
		self.title_vertical_layout_2.setObjectName("verticalLayout_2")

		self.title_semester_label = QtWidgets.QLabel(self.title_page)
		self.title_semester_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
		self.title_semester_label.setObjectName("semester_label")

		self.title_vertical_layout_2.addWidget(self.title_semester_label)

		self.title_semester_picker = QtWidgets.QComboBox(self.title_page)
		self.title_semester_picker.setObjectName("semester_picker")
		self.title_semester_picker.addItems([""] * 4)

		self.title_vertical_layout_2.addWidget(self.title_semester_picker)

		self.title_year_label = QtWidgets.QLabel(self.title_page)
		self.title_year_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
		self.title_year_label.setObjectName("year_label")

		self.title_vertical_layout_2.addWidget(self.title_year_label)

		self.title_year_picker = QtWidgets.QSpinBox(self.title_page)
		self.title_year_picker.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
		self.title_year_picker.setMinimum(2010)
		self.title_year_picker.setMaximum(2030)
		self.title_year_picker.setValue(2020)
		self.title_year_picker.setObjectName("year_picker")

		self.title_vertical_layout_2.addWidget(self.title_year_picker)

		self.title_spacer = QtWidgets.QLabel(self.title_page)

		self.title_vertical_layout_2.addWidget(self.title_spacer)

		self.title_horizontal_layout.addLayout(self.title_vertical_layout_2)
		self.title_grid_layout_2 = QtWidgets.QGridLayout()
		self.title_grid_layout_2.setObjectName("gridLayout_2")

		self.title_schedule_button = QtWidgets.QPushButton(self.title_page)
		self.title_schedule_button.setObjectName("make_schedule_button")
		self.title_schedule_button.setEnabled(False)

		self.title_grid_layout_2.addWidget(self.title_schedule_button, 2, 1, 1, 1)

		self.title_instructor_button = QtWidgets.QPushButton(self.title_page)
		self.title_instructor_button.setObjectName("browse_instructor_button")

		self.title_grid_layout_2.addWidget(self.title_instructor_button, 0, 1, 1, 1)

		self.title_section_button = QtWidgets.QPushButton(self.title_page)
		self.title_section_button.setObjectName("browse_section_button")
		self.title_section_button.setEnabled(False)

		self.title_grid_layout_2.addWidget(self.title_section_button, 2, 0, 1, 1)

		self.title_course_button = QtWidgets.QPushButton(self.title_page)
		self.title_course_button.setObjectName("browse_course_button")

		self.title_grid_layout_2.addWidget(self.title_course_button, 0, 0, 1, 1)

		self.title_horizontal_layout.addLayout(self.title_grid_layout_2)
		self.title_vertical_layout_1.addLayout(self.title_horizontal_layout)
		self.title_grid_layout_1.addLayout(self.title_vertical_layout_1, 0, 0, 1, 1)
		self.main_window_stacked_widget.addWidget(self.title_page)

	def setup_browse_instructor_page(self) -> None:
		self.instructor_page = QtWidgets.QWidget()
		self.instructor_page.setObjectName("page2")

		self.instructor_grid_layout = QtWidgets.QGridLayout(self.instructor_page)
		self.instructor_grid_layout.setObjectName("gridLayout3")

		self.instructor_horizontal_layout = QtWidgets.QHBoxLayout()
		self.instructor_horizontal_layout.setObjectName("horizontalLayout3")

		self.instructor_vertical_layout = QtWidgets.QVBoxLayout()
		self.instructor_vertical_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
		self.instructor_vertical_layout.setObjectName("verticalLayout4")

		self.instructor_first_name_label = QtWidgets.QLabel(self.instructor_page)
		self.instructor_first_name_label.setObjectName("label5")

		self.instructor_vertical_layout.addWidget(self.instructor_first_name_label)

		self.instructor_first_name_input = QtWidgets.QLineEdit(self.instructor_page)

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.instructor_first_name_input.sizePolicy().hasHeightForWidth())

		self.instructor_first_name_input.setSizePolicy(sizePolicy)
		self.instructor_first_name_input.setObjectName("lineEdit")

		self.instructor_vertical_layout.addWidget(self.instructor_first_name_input)

		self.instructor_last_name_label = QtWidgets.QLabel(self.instructor_page)
		self.instructor_last_name_label.setObjectName("label6")

		self.instructor_vertical_layout.addWidget(self.instructor_last_name_label)

		self.instructor_last_name_input = QtWidgets.QLineEdit(self.instructor_page)

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.instructor_last_name_input.sizePolicy().hasHeightForWidth())

		self.instructor_last_name_input.setSizePolicy(sizePolicy)
		self.instructor_last_name_input.setObjectName("lineEdit_2")

		self.instructor_vertical_layout.addWidget(self.instructor_last_name_input)

		self.instructor_course_label = QtWidgets.QLabel(self.instructor_page)
		self.instructor_course_label.setObjectName("label7")

		self.instructor_vertical_layout.addWidget(self.instructor_course_label)

		self.insctructor_course_input = QtWidgets.QLineEdit(self.instructor_page)

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.insctructor_course_input.sizePolicy().hasHeightForWidth())

		self.insctructor_course_input.setSizePolicy(sizePolicy)
		self.insctructor_course_input.setObjectName("lineEdit_3")

		self.instructor_vertical_layout.addWidget(self.insctructor_course_input)

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)

		spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.instructor_vertical_layout.addItem(spacerItem)
		self.instructor_horizontal_layout.addLayout(self.instructor_vertical_layout)

		self.instructor_return_button = QtWidgets.QPushButton(self.instructor_page)
		self.instructor_return_button.setObjectName("instructor_return_button")

		self.instructor_vertical_layout.addWidget(self.instructor_return_button)

		self.instructor_table = QtWidgets.QTableWidget(self.instructor_page)

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.instructor_table.sizePolicy().hasHeightForWidth())

		self.instructor_table.setSizePolicy(sizePolicy)
		self.instructor_table.setObjectName("tableView")
		self.instructor_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
		self.instructor_table.setAlternatingRowColors(True)
		self.instructor_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

		self.instructor_horizontal_layout.addWidget(self.instructor_table)
		self.instructor_grid_layout.addLayout(self.instructor_horizontal_layout, 0, 0, 1, 1)
		self.main_window_stacked_widget.addWidget(self.instructor_page)

	def setup_browse_course_page(self) -> None:
		self.course_page = QtWidgets.QWidget()
		self.course_page.setObjectName("page3")

		self.course_grid_layout = QtWidgets.QGridLayout(self.course_page)
		self.course_grid_layout.setObjectName("gridLayout")

		self.course_horizontal_layout = QtWidgets.QHBoxLayout()
		self.course_horizontal_layout.setObjectName("horizontalLayout")

		self.course_vertical_layout = QtWidgets.QVBoxLayout()
		self.course_vertical_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
		self.course_vertical_layout.setObjectName("verticalLayout")

		self.course_dept_label = QtWidgets.QLabel(self.course_page)
		self.course_dept_label.setObjectName("course_dept_label")

		self.course_vertical_layout.addWidget(self.course_dept_label)

		self.course_dept_edit = QtWidgets.QLineEdit(self.course_page)

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.course_dept_edit.sizePolicy().hasHeightForWidth())

		self.course_dept_edit.setSizePolicy(sizePolicy)
		self.course_dept_edit.setObjectName("course_dept_edit")

		self.course_vertical_layout.addWidget(self.course_dept_edit)

		self.course_course_num_label = QtWidgets.QLabel(self.course_page)
		self.course_course_num_label.setObjectName("course_course_num_label")

		self.course_vertical_layout.addWidget(self.course_course_num_label)

		self.course_course_num_edit = QtWidgets.QLineEdit(self.course_page)

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.course_course_num_edit.sizePolicy().hasHeightForWidth())

		self.course_course_num_edit.setSizePolicy(sizePolicy)
		self.course_course_num_edit.setObjectName("course_course_num_edit")

		self.course_vertical_layout.addWidget(self.course_course_num_edit)

		self.course_credit_hours_check = QtWidgets.QCheckBox(self.course_page)
		self.course_credit_hours_check.setObjectName("course_credit_hours_check")

		self.course_vertical_layout.addWidget(self.course_credit_hours_check)

		self.course_credit_hour_spinner = QtWidgets.QDoubleSpinBox(self.course_page)
		self.course_credit_hour_spinner.setDecimals(1)
		self.course_credit_hour_spinner.setSingleStep(0.5)
		self.course_credit_hour_spinner.setObjectName("course_credit_hour_spinner")

		self.course_vertical_layout.addWidget(self.course_credit_hour_spinner)

		self.course_title_label = QtWidgets.QLabel(self.course_page)
		self.course_title_label.setObjectName("course_title_label")

		self.course_vertical_layout.addWidget(self.course_title_label)

		self.course_title_edit = QtWidgets.QLineEdit(self.course_page)

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.course_title_edit.sizePolicy().hasHeightForWidth())

		self.course_title_edit.setSizePolicy(sizePolicy)
		self.course_title_edit.setObjectName("course_title_edit")

		self.course_vertical_layout.addWidget(self.course_title_edit)

		self.course_instructor_label = QtWidgets.QLabel(self.course_page)
		self.course_instructor_label.setObjectName("course_instructor_label")

		self.course_vertical_layout.addWidget(self.course_instructor_label)

		self.course_instructor_edit = QtWidgets.QLineEdit(self.course_page)

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.course_instructor_edit.sizePolicy().hasHeightForWidth())

		self.course_instructor_edit.setSizePolicy(sizePolicy)
		self.course_instructor_edit.setObjectName("course_instructor_edit")

		self.course_vertical_layout.addWidget(self.course_instructor_edit)

		self.course_lab_hours_check = QtWidgets.QCheckBox(self.course_page)
		self.course_lab_hours_check.setObjectName("course_lab_hours_check")

		self.course_vertical_layout.addWidget(self.course_lab_hours_check)

		self.course_lab_hours_spinner = QtWidgets.QDoubleSpinBox(self.course_page)
		self.course_lab_hours_spinner.setDecimals(1)
		self.course_lab_hours_spinner.setSingleStep(0.5)
		self.course_lab_hours_spinner.setObjectName("course_lab_hours_spinner")

		self.course_vertical_layout.addWidget(self.course_lab_hours_spinner)

		self.course_lecture_hours_spinner = QtWidgets.QCheckBox(self.course_page)
		self.course_lecture_hours_spinner.setObjectName("course_lecture_hours_spinner")

		self.course_vertical_layout.addWidget(self.course_lecture_hours_spinner)

		self.course_lecture_hours_spinner_2 = QtWidgets.QDoubleSpinBox(self.course_page)
		self.course_lecture_hours_spinner_2.setDecimals(1)
		self.course_lecture_hours_spinner_2.setSingleStep(0.5)
		self.course_lecture_hours_spinner_2.setObjectName("course_lecture_hours_spinner_2")

		self.course_vertical_layout.addWidget(self.course_lecture_hours_spinner_2)

		self.course_honors_check = QtWidgets.QCheckBox(self.course_page)
		self.course_honors_check.setObjectName("course_honors_check")

		self.course_vertical_layout.addWidget(self.course_honors_check)

		self.course_description_label = QtWidgets.QLabel(self.course_page)
		self.course_description_label.setObjectName("course_description_label")

		self.course_vertical_layout.addWidget(self.course_description_label)

		self.course_description_edit = QtWidgets.QTextEdit(self.course_page)

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.course_description_edit.sizePolicy().hasHeightForWidth())

		self.course_description_edit.setSizePolicy(sizePolicy)
		self.course_description_edit.setMaximumSize(QtCore.QSize(120, 16777215))
		self.course_description_edit.setObjectName("course_description_edit")

		self.course_vertical_layout.addWidget(self.course_description_edit)

		spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

		self.course_vertical_layout.addItem(spacerItem)

		self.course_return_to_menu_button = QtWidgets.QPushButton(self.course_page)
		self.course_return_to_menu_button.setObjectName("course_return_to_menu_button")

		self.course_vertical_layout.addWidget(self.course_return_to_menu_button)
		self.course_horizontal_layout.addLayout(self.course_vertical_layout)

		self.course_table = QtWidgets.QTableWidget(self.course_page)

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.course_table.sizePolicy().hasHeightForWidth())

		self.course_table.setSizePolicy(sizePolicy)
		self.course_table.setObjectName("course_table")
		self.course_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
		self.course_table.setAlternatingRowColors(True)
		self.course_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

		self.course_horizontal_layout.addWidget(self.course_table)
		self.course_grid_layout.addLayout(self.course_horizontal_layout, 0, 0, 1, 1)
		self.main_window_stacked_widget.addWidget(self.course_page)

	def retranslate_ui(self) -> None:
		_translate = QtCore.QCoreApplication.translate
		self.title_big_title.setText(_translate("MainWindow", "BYU Scheduler 2"))
		self.title_name.setText(_translate("MainWindow", "By Josh Bedwell"))
		self.title_semester_label.setText(_translate("MainWindow", "Semester"))
		self.title_semester_picker.setItemText(0, _translate("MainWindow", "Winter"))
		self.title_semester_picker.setItemText(1, _translate("MainWindow", "Spring"))
		self.title_semester_picker.setItemText(2, _translate("MainWindow", "Summer"))
		self.title_semester_picker.setItemText(3, _translate("MainWindow", "Fall"))
		self.title_year_label.setText(_translate("MainWindow", "Year"))
		self.title_spacer.setText(_translate("MainWindow", ""))
		self.title_schedule_button.setText(_translate("MainWindow", "Make Schedule"))
		self.title_instructor_button.setText(_translate("MainWindow", "Browse Instructors"))
		self.title_section_button.setText(_translate("MainWindow", "Browse Sections"))
		self.title_course_button.setText(_translate("MainWindow", "Browse Courses"))
		self.instructor_first_name_label.setText(_translate("MainWindow", "First Name"))
		self.instructor_last_name_label.setText(_translate("MainWindow", "Last Name"))
		self.instructor_course_label.setText(_translate("MainWindow", "Course Taught"))
		self.instructor_return_button.setText(_translate("MainWindow", "Return to Menu"))
		self.course_dept_label.setText(_translate("MainWindow", "Dept"))
		self.course_course_num_label.setText(_translate("MainWindow", "Course Number"))
		self.course_credit_hours_check.setText(_translate("MainWindow", "Credit Hours"))
		self.course_title_label.setText(_translate("MainWindow", "Title"))
		self.course_instructor_label.setText(_translate("MainWindow", "Instructor"))
		self.course_lab_hours_check.setText(_translate("MainWindow", "Lab Hours"))
		self.course_lecture_hours_spinner.setText(_translate("MainWindow", "Lecture Hours"))
		self.course_honors_check.setText(_translate("MainWindow", "Honors"))
		self.course_description_label.setText(_translate("MainWindow", "Description"))
		self.course_return_to_menu_button.setText(_translate("MainWindow", "Return to Menu"))

	def hook_buttons(self) -> None:
		self.title_course_button.clicked.connect(self.browse_course_action)
		self.title_section_button.clicked.connect(self.browse_section_action)
		self.title_instructor_button.clicked.connect(self.browse_instructor_action)
		self.title_schedule_button.clicked.connect(self.make_schedule_action)

		self.instructor_first_name_input.textChanged.connect(self.filter_instructor_table)
		self.instructor_last_name_input.textChanged.connect(self.filter_instructor_table)
		self.insctructor_course_input.textChanged.connect(self.filter_instructor_table)
		self.instructor_table.cellClicked.connect(self.show_instructor)
		self.instructor_return_button.clicked.connect(self.goto_title_page)

		self.course_dept_edit.textChanged.connect(self.filter_course_table)
		self.course_course_num_edit.textChanged.connect(self.filter_course_table)
		self.course_credit_hours_check.stateChanged.connect(self.filter_course_table)
		self.course_credit_hour_spinner.valueChanged.connect(self.filter_course_table)
		self.course_title_edit.textChanged.connect(self.filter_course_table)
		self.course_instructor_edit.textChanged.connect(self.filter_course_table)
		self.course_lab_hours_check.stateChanged.connect(self.filter_course_table)
		self.course_lab_hours_spinner.valueChanged.connect(self.filter_course_table)
		self.course_lecture_hours_spinner.stateChanged.connect(self.filter_course_table)
		self.course_lecture_hours_spinner_2.valueChanged.connect(self.filter_course_table)
		self.course_honors_check.stateChanged.connect(self.filter_course_table)
		self.course_description_edit.textChanged.connect(self.filter_course_table)

	# Common Functions
	# ----------------------------------------------------------------------------------

	def goto_title_page(self) -> None:
		self.main_window.resize(800, 380)
		self.main_window_stacked_widget.setCurrentIndex(0)
		self.main_window.setWindowTitle("BYU Scheduler 2")
		self.loaded_data.clear()

	def goto_instructor_page(self) -> None:
		self.main_window.resize(1150, 700)
		self.instructor_first_name_input.clear()
		self.instructor_last_name_input.clear()
		self.insctructor_course_input.clear()
		self.main_window_stacked_widget.setCurrentIndex(1)
		self.main_window.setWindowTitle("Browse Instructors")
		self.populate_instructor_table()

	def goto_browse_course(self) -> None:
		self.main_window.resize(1350, 700)
		self.course_dept_edit.clear()
		self.course_course_num_edit.clear()
		self.course_title_edit.clear()
		self.course_instructor_edit.clear()
		self.course_description_edit.clear()
		self.course_honors_check.setChecked(False)
		self.course_description_edit.clear()
		self.populate_course_table()
		self.main_window_stacked_widget.setCurrentIndex(2)
		self.main_window.setWindowTitle("Browse Courses")

	def goto_browse_section(self) -> None:
		print("browse section")

	def goto_make_schedule(self) -> None:
		print("make schedule")

	# Title Functions
	# ----------------------------------------------------------------------------------

	def browse_instructor_action(self) -> None:
		self.loaded_data.clear()
		self.show_popup("instructor")
		if len(self.loaded_data) > 0:
			self.goto_instructor_page()

	def browse_course_action(self) -> None:
		self.loaded_data.clear()
		self.show_popup("course")
		if len(self.loaded_data) > 0:
			self.goto_browse_course()

	def browse_section_action(self) -> None:
		self.show_popup()

	def make_schedule_action(self) -> None:
		self.show_popup()

	def show_popup(self, data_type: str) -> None:
		popup_dialog = QtWidgets.QDialog()
		popup_ui = UI.title_popup_dialog.Ui_Dialog()
		popup_ui.setupUi(popup_dialog,
		                 self.title_semester_picker.currentText(),
		                 self.title_year_picker.value(),
		                 self.loaded_data,
		                 data_type)
		popup_dialog.exec_()

	# Instructor Functions
	# ----------------------------------------------------------------------------------

	def populate_instructor_table(self) -> None:
		self.instructor_table.setColumnCount(8)
		self.instructor_table.setRowCount(len(self.loaded_data))
		self.instructor_table.setHorizontalHeaderLabels(
			["First Name", "Last Name", "Sort Name", "# Courses Taught", "# RMP Ratings", "RMP Rating",
			 "RMP Difficulty", "HIDDEN"])
		for i, key in enumerate(self.loaded_data.keys()):
			self.instructor_table.setItem(i, 0, QtWidgets.QTableWidgetItem(self.loaded_data[key]["first_name"]))
			self.instructor_table.setItem(i, 1, QtWidgets.QTableWidgetItem(self.loaded_data[key]["last_name"]))
			self.instructor_table.setItem(i, 2, QtWidgets.QTableWidgetItem(self.loaded_data[key]["sort_name"]))

			different_classes_taught = set()
			for section in self.loaded_data[key]["classes_taught"]:
				different_classes_taught.add(section["course"])
			item = QtWidgets.QTableWidgetItem()
			item.setData(QtCore.Qt.DisplayRole, len(different_classes_taught))
			self.instructor_table.setItem(i, 3, item)

			if self.loaded_data[key]["num_ratings"] is None:
				self.instructor_table.setItem(i, 4, QtWidgets.QTableWidgetItem(""))
			else:
				item = QtWidgets.QTableWidgetItem()
				item.setData(QtCore.Qt.DisplayRole, self.loaded_data[key]["num_ratings"])
				self.instructor_table.setItem(i, 4, item)
			if self.loaded_data[key]["avg_rating"] is None:
				self.instructor_table.setItem(i, 5, QtWidgets.QTableWidgetItem(""))
			else:
				item = QtWidgets.QTableWidgetItem()
				item.setData(QtCore.Qt.DisplayRole, self.loaded_data[key]["avg_rating"])
				self.instructor_table.setItem(i, 5, item)
			if self.loaded_data[key]["avg_easy_score"] is None:
				self.instructor_table.setItem(i, 5, QtWidgets.QTableWidgetItem(""))
			else:
				item = QtWidgets.QTableWidgetItem()
				item.setData(QtCore.Qt.DisplayRole, self.loaded_data[key]["avg_easy_score"])
				self.instructor_table.setItem(i, 6, item)

			self.instructor_table.setItem(i, 7, QtWidgets.QTableWidgetItem(key))
		self.instructor_table.hideColumn(7)

		if not self.title_spacer.isChecked():
			self.instructor_table.hideColumn(4)
			self.instructor_table.hideColumn(5)
			self.instructor_table.hideColumn(6)

		self.instructor_table.setSortingEnabled(True)
		self.instructor_table.resizeColumnsToContents()

	def filter_instructor_table(self) -> None:
		first_filter = self.instructor_first_name_input.text().lower()
		last_filter = self.instructor_last_name_input.text().lower()
		num_filter = self.insctructor_course_input.text().lower()

		for index in range(self.instructor_table.rowCount()):

			show = True
			if first_filter != "":
				if first_filter not in self.instructor_table.item(index, 0).text().lower():
					show = False
			if show and last_filter != "":
				if last_filter not in self.instructor_table.item(index, 1).text().lower():
					show = False
			if show and num_filter != "":
				show = False
				for course in self.loaded_data[self.instructor_table.item(index, 7).text()]["classes_taught"]:
					if num_filter in course["course"].lower():
						show = True
						break
			if show:
				self.instructor_table.showRow(index)
			else:
				self.instructor_table.hideRow(index)

	def show_instructor(self, row: int, column: int) -> None:
		instructor_dialog = QtWidgets.QDialog()
		instructor_ui = UI.instructor_dialog.Ui_Dialog()
		instructor_ui.setupUi(instructor_dialog, self.loaded_data[self.instructor_table.item(row, 7).text()])
		instructor_dialog.exec_()

	# Course Functions
	# ----------------------------------------------------------------------------------

	def populate_course_table(self) -> None:
		self.course_table.setColumnCount(9)
		self.course_table.setRowCount(len(self.loaded_data))
		self.course_table.setHorizontalHeaderLabels(
			["Dept", "Course Num", "Credits", "Title", "# Sections", "# Instructors", "Lab Hours", "Lecture Hours",
			 "HIDDEN"])
		for i, key in enumerate(self.loaded_data.keys()):
			self.course_table.setItem(i, 0, QtWidgets.QTableWidgetItem(self.loaded_data[key]["dept_name"]))
			suffix = self.loaded_data[key]["catalog_suffix"]
			if suffix is None:
				suffix = ""
			self.course_table.setItem(i, 1,
			                          QtWidgets.QTableWidgetItem(self.loaded_data[key]["catalog_number"] + suffix))
			self.course_table.setItem(i, 2, QtWidgets.QTableWidgetItem(self.loaded_data[key]["credit_hours"]))
			title = self.loaded_data[key]["full_title"]
			if title.endswith("."):
				title = title[:-1]
			self.course_table.setItem(i, 3, QtWidgets.QTableWidgetItem(title))
			item = QtWidgets.QTableWidgetItem()
			item.setData(QtCore.Qt.DisplayRole, len(self.loaded_data[key]["sections"]))
			self.course_table.setItem(i, 4, item)
			item = QtWidgets.QTableWidgetItem()
			item.setData(QtCore.Qt.DisplayRole, len(self.loaded_data[key]["instructors"]))
			self.course_table.setItem(i, 5, item)
			lab_hours = self.loaded_data[key]["lab_hours"]
			try:
				lab_hours = float(lab_hours)
				item = QtWidgets.QTableWidgetItem()
				item.setData(QtCore.Qt.DisplayRole, lab_hours)
				self.course_table.setItem(i, 6, item)
			except:
				if lab_hours is None:
					lab_hours = ""
				elif "arr" in lab_hours.lower():
					lab_hours = "variable"
				self.course_table.setItem(i, 6, QtWidgets.QTableWidgetItem(lab_hours))
			lecture_hours = self.loaded_data[key]["lecture_hours"]
			try:
				lecture_hours = float(lecture_hours)
				item = QtWidgets.QTableWidgetItem()
				item.setData(QtCore.Qt.DisplayRole, lecture_hours)
				self.course_table.setItem(i, 7, item)
			except:
				if lecture_hours is None:
					lecture_hours = ""
				elif "arr" in lecture_hours.lower():
					lecture_hours = "variable"
				self.course_table.setItem(i, 7, QtWidgets.QTableWidgetItem(lecture_hours))
			self.course_table.setItem(i, 8,
			                          QtWidgets.QTableWidgetItem(self.loaded_data[key]["curriculum_id_title_code"]))
		self.course_table.hideColumn(8)
		self.course_table.setSortingEnabled(True)
		self.course_table.resizeColumnsToContents()

	def filter_course_table(self) -> None:
		dept_filter = self.course_dept_edit.text().lower()
		num_filter = self.course_course_num_edit.text().lower()
		credit_hours_checked = self.course_credit_hours_check.isChecked()
		credit_hour_filter = self.course_credit_hour_spinner.value()
		title_filter = self.course_title_edit.text().lower()
		instructor_filter = self.course_instructor_edit.text().lower()
		instructor_parts = instructor_filter.split(" ")
		lab_hour_checked = self.course_lab_hours_check.isChecked()
		lab_hour_filter = self.course_lab_hours_spinner.value()
		lecture_hour_checked = self.course_lecture_hours_spinner.isChecked()
		lecture_hours_filter = self.course_lecture_hours_spinner_2.value()
		honors_checked = self.course_honors_check.isChecked()
		description_filter = self.course_description_edit.toPlainText().lower()

		for index in range(self.course_table.rowCount()):

			show = True
			try:
				if dept_filter != "":
					if dept_filter not in self.course_table.item(index, 0).text().lower():
						show = False
				if show and num_filter != "":
					if num_filter not in self.course_table.item(index, 1).text().lower():
						show = False
				if show and credit_hours_checked:
					if credit_hour_filter != float(self.course_table.item(index, 2).text()):
						show = False
				if show and title_filter != "":
					if title_filter not in self.course_table.item(index, 3).text().lower():
						show = False
				if show and instructor_filter != "":
					# TODO this is not implimented because instructor storage might change
					i = 1
				if show and lab_hour_checked:
					if lab_hour_filter != float(self.course_table.item(index, 6).text()):
						show = False
				if show and lecture_hour_checked:
					if lecture_hours_filter != float(self.course_table.item(index, 7).text()):
						show = False
				if show and honors_checked and (
						self.loaded_data[self.course_table.item(index, 8).text()]["honors_approved"] is None or
						self.loaded_data[self.course_table.item(index, 8).text()]["honors_approved"].lower() == "n"):
					show = False
				if show and description_filter != "":
					if self.loaded_data[self.course_table.item(index, 8).text()][
						"description"] is None or description_filter not in \
							self.loaded_data[self.course_table.item(index, 8).text()]["description"].lower():
						show = False
			except:
				print("error sorting")
				show = False

			if show:
				self.course_table.showRow(index)
			else:
				self.course_table.hideRow(index)
