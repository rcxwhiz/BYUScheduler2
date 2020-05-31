from PyQt5 import QtCore, QtGui, QtWidgets

import UI.instructor_dialog
import UI.title_popup_dialog


class Ui_MainWindow(object):
	# Setup
	# ----------------------------------------------------------------------------------
	def setup_ui(self, MainWindowIn: QtWidgets.QMainWindow) -> None:
		self.setup_window(MainWindowIn)

		self.setup_title_page()
		self.setup_browse_instructor_page()

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

		self.title_font = QtGui.QFont()
		self.title_font.setFamily("Arial")
		self.title_font.setPointSize(36)
		self.font = QtGui.QFont()
		self.font.setFamily("Arial")

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
		self.title_big_title.setFont(self.title_font)
		self.title_big_title.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
		self.title_big_title.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
		self.title_big_title.setObjectName("big_title")

		self.title_vertical_layout_1.addWidget(self.title_big_title)

		self.title_name = QtWidgets.QLabel(self.title_page)
		self.title_name.setFont(self.font)
		self.title_name.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
		self.title_name.setObjectName("name_title")

		self.title_vertical_layout_1.addWidget(self.title_name)
		self.title_horizontal_layout = QtWidgets.QHBoxLayout()
		self.title_horizontal_layout.setObjectName("horizontalLayout")
		self.title_vertical_layout_2 = QtWidgets.QVBoxLayout()
		self.title_vertical_layout_2.setObjectName("verticalLayout_2")

		self.title_semester_label = QtWidgets.QLabel(self.title_page)
		self.title_semester_label.setFont(self.font)
		self.title_semester_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
		self.title_semester_label.setObjectName("semester_label")

		self.title_vertical_layout_2.addWidget(self.title_semester_label)

		self.title_semester_picker = QtWidgets.QComboBox(self.title_page)
		self.title_semester_picker.setFont(self.font)
		self.title_semester_picker.setObjectName("semester_picker")
		self.title_semester_picker.addItems([""] * 4)

		self.title_vertical_layout_2.addWidget(self.title_semester_picker)

		self.title_year_label = QtWidgets.QLabel(self.title_page)
		self.title_year_label.setFont(self.font)
		self.title_year_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
		self.title_year_label.setObjectName("year_label")

		self.title_vertical_layout_2.addWidget(self.title_year_label)

		self.title_year_picker = QtWidgets.QSpinBox(self.title_page)
		self.title_year_picker.setFont(self.font)
		self.title_year_picker.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
		self.title_year_picker.setMinimum(2010)
		self.title_year_picker.setMaximum(2030)
		self.title_year_picker.setValue(2020)
		self.title_year_picker.setObjectName("year_picker")

		self.title_vertical_layout_2.addWidget(self.title_year_picker)

		self.title_rmp_check = QtWidgets.QCheckBox(self.title_page)
		self.title_rmp_check.setChecked(True)

		self.title_vertical_layout_2.addWidget(self.title_rmp_check)

		self.title_horizontal_layout.addLayout(self.title_vertical_layout_2)
		self.title_grid_layout_2 = QtWidgets.QGridLayout()
		self.title_grid_layout_2.setObjectName("gridLayout_2")

		self.title_schedule_button = QtWidgets.QPushButton(self.title_page)
		self.title_schedule_button.setFont(self.font)
		self.title_schedule_button.setObjectName("make_schedule_button")
		self.title_schedule_button.setEnabled(False)

		self.title_grid_layout_2.addWidget(self.title_schedule_button, 2, 1, 1, 1)

		self.title_instructor_button = QtWidgets.QPushButton(self.title_page)
		self.title_instructor_button.setFont(self.font)
		self.title_instructor_button.setObjectName("browse_instructor_button")

		self.title_grid_layout_2.addWidget(self.title_instructor_button, 0, 1, 1, 1)

		self.title_section_button = QtWidgets.QPushButton(self.title_page)
		self.title_section_button.setFont(self.font)
		self.title_section_button.setObjectName("browse_section_button")
		self.title_section_button.setEnabled(False)

		self.title_grid_layout_2.addWidget(self.title_section_button, 2, 0, 1, 1)

		self.title_course_button = QtWidgets.QPushButton(self.title_page)
		self.title_course_button.setFont(self.font)
		self.title_course_button.setObjectName("browse_course_button")
		self.title_course_button.setEnabled(False)

		self.title_grid_layout_2.addWidget(self.title_course_button, 0, 0, 1, 1)

		self.title_horizontal_layout.addLayout(self.title_grid_layout_2)
		self.title_vertical_layout_1.addLayout(self.title_horizontal_layout)
		self.title_grid_layout_1.addLayout(self.title_vertical_layout_1, 0, 0, 1, 1)
		self.main_window_stacked_widget.addWidget(self.title_page)

	def setup_browse_instructor_page(self) -> None:
		self.loaded_data = {}

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
		self.instructor_first_name_label.setFont(self.font)

		self.instructor_vertical_layout.addWidget(self.instructor_first_name_label)

		self.instructor_first_name_input = QtWidgets.QLineEdit(self.instructor_page)

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.instructor_first_name_input.sizePolicy().hasHeightForWidth())

		self.instructor_first_name_input.setSizePolicy(sizePolicy)
		self.instructor_first_name_input.setObjectName("lineEdit")
		self.instructor_first_name_input.setFont(self.font)

		self.instructor_vertical_layout.addWidget(self.instructor_first_name_input)

		self.instructor_last_name_label = QtWidgets.QLabel(self.instructor_page)
		self.instructor_last_name_label.setObjectName("label6")
		self.instructor_last_name_label.setFont(self.font)

		self.instructor_vertical_layout.addWidget(self.instructor_last_name_label)

		self.instructor_last_name_input = QtWidgets.QLineEdit(self.instructor_page)

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.instructor_last_name_input.sizePolicy().hasHeightForWidth())

		self.instructor_last_name_input.setSizePolicy(sizePolicy)
		self.instructor_last_name_input.setObjectName("lineEdit_2")
		self.instructor_last_name_input.setFont(self.font)

		self.instructor_vertical_layout.addWidget(self.instructor_last_name_input)

		self.instructor_course_label = QtWidgets.QLabel(self.instructor_page)
		self.instructor_course_label.setObjectName("label7")
		self.instructor_course_label.setFont(self.font)

		self.instructor_vertical_layout.addWidget(self.instructor_course_label)

		self.insctructor_course_input = QtWidgets.QLineEdit(self.instructor_page)

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.insctructor_course_input.sizePolicy().hasHeightForWidth())

		self.insctructor_course_input.setSizePolicy(sizePolicy)
		self.insctructor_course_input.setObjectName("lineEdit_3")
		self.insctructor_course_input.setFont(self.font)

		self.instructor_vertical_layout.addWidget(self.insctructor_course_input)

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)

		spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.instructor_vertical_layout.addItem(spacerItem)
		self.instructor_horizontal_layout.addLayout(self.instructor_vertical_layout)

		self.instructor_return_button = QtWidgets.QPushButton(self.instructor_page)
		self.instructor_return_button.setFont(self.font)
		self.instructor_return_button.setObjectName("instructor_return_button")

		self.instructor_vertical_layout.addWidget(self.instructor_return_button)

		self.instructor_table = QtWidgets.QTableWidget(self.instructor_page)

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.instructor_table.sizePolicy().hasHeightForWidth())

		self.instructor_table.setSizePolicy(sizePolicy)
		self.instructor_table.setObjectName("tableView")
		self.instructor_table.setFont(self.font)
		self.instructor_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
		self.instructor_table.setAlternatingRowColors(True)
		self.instructor_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

		self.instructor_horizontal_layout.addWidget(self.instructor_table)
		self.instructor_grid_layout.addLayout(self.instructor_horizontal_layout, 0, 0, 1, 1)
		self.main_window_stacked_widget.addWidget(self.instructor_page)

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
		self.title_rmp_check.setText(_translate("MainWindow", "Include RateMyProfessor Data"))
		self.title_schedule_button.setText(_translate("MainWindow", "Make Schedule"))
		self.title_instructor_button.setText(_translate("MainWindow", "Browse Instructors"))
		self.title_section_button.setText(_translate("MainWindow", "Browse Sections"))
		self.title_course_button.setText(_translate("MainWindow", "Browse Courses"))
		self.instructor_first_name_label.setText(_translate("MainWindow", "First Name"))
		self.instructor_last_name_label.setText(_translate("MainWindow", "Last Name"))
		self.instructor_course_label.setText(_translate("MainWindow", "Course Taught"))
		self.instructor_return_button.setText(_translate("MainWindow", "Return to Menu"))

	def hook_buttons(self) -> None:
		self.title_course_button.clicked.connect(self.browse_course_action)
		self.title_section_button.clicked.connect(self.browse_section_action)
		self.title_instructor_button.clicked.connect(self.browse_instructor_action)
		self.title_schedule_button.clicked.connect(self.make_schedule_action)

		self.instructor_first_name_input.textChanged.connect(self.filter_table)
		self.instructor_last_name_input.textChanged.connect(self.filter_table)
		self.insctructor_course_input.textChanged.connect(self.filter_table)
		self.instructor_table.cellClicked.connect(self.show_instructor)
		self.instructor_return_button.clicked.connect(self.goto_title_page)

	# Common Functions
	# ----------------------------------------------------------------------------------

	def goto_title_page(self) -> None:
		self.main_window.resize(800, 380)
		self.main_window_stacked_widget.setCurrentIndex(0)
		self.main_window.setWindowTitle("BYU Scheduler 2")
		self.loaded_data.clear()

	def goto_instructor_page(self) -> None:
		if self.title_rmp_check.isChecked():
			self.main_window.resize(1150, 700)
		else:
			self.main_window.resize(830, 700)
		self.instructor_first_name_input.clear()
		self.instructor_last_name_input.clear()
		self.insctructor_course_input.clear()
		self.main_window_stacked_widget.setCurrentIndex(1)
		self.main_window.setWindowTitle("Browse Instructors")
		self.populate_table()

	def goto_browse_course(self) -> None:
		print("browse course")

	def goto_browse_section(self) -> None:
		print("browse section")

	def goto_make_schedule(self) -> None:
		print("make schedule")

	# Title Functions
	# ----------------------------------------------------------------------------------

	def browse_instructor_action(self) -> None:
		self.loaded_data.clear()
		self.show_popup()
		if len(self.loaded_data) > 0:
			self.goto_instructor_page()

	def browse_course_action(self) -> None:
		self.show_popup()

	def browse_section_action(self) -> None:
		self.show_popup()

	def make_schedule_action(self) -> None:
		self.show_popup()

	def show_popup(self) -> None:
		popup_dialog = QtWidgets.QDialog()
		popup_ui = UI.title_popup_dialog.Ui_Dialog()
		popup_ui.setupUi(popup_dialog,
		                 self.title_semester_picker.currentText(),
		                 self.title_year_picker.value(),
		                 self.loaded_data,
		                 self.title_rmp_check.isChecked())
		popup_dialog.exec_()

	# Instructor Functions
	# ----------------------------------------------------------------------------------

	def populate_table(self) -> None:
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

			if self.loaded_data[key]["found_rmp"] == 1:
				item = QtWidgets.QTableWidgetItem()
				item.setData(QtCore.Qt.DisplayRole, self.loaded_data[key]["num_ratings"])
				self.instructor_table.setItem(i, 4, item)
				item = QtWidgets.QTableWidgetItem()
				item.setData(QtCore.Qt.DisplayRole, self.loaded_data[key]["avg_rating"])
				self.instructor_table.setItem(i, 5, item)
				item = QtWidgets.QTableWidgetItem()
				item.setData(QtCore.Qt.DisplayRole, self.loaded_data[key]["avg_easy_score"])
				self.instructor_table.setItem(i, 6, item)
			else:
				self.instructor_table.setItem(i, 4, QtWidgets.QTableWidgetItem("-"))
				self.instructor_table.setItem(i, 5, QtWidgets.QTableWidgetItem("-"))
				self.instructor_table.setItem(i, 6, QtWidgets.QTableWidgetItem("-"))
			self.instructor_table.setItem(i, 7, QtWidgets.QTableWidgetItem(key))
		self.instructor_table.hideColumn(7)

		if not self.title_rmp_check.isChecked():
			self.instructor_table.hideColumn(4)
			self.instructor_table.hideColumn(5)
			self.instructor_table.hideColumn(6)

		self.instructor_table.setSortingEnabled(True)
		self.instructor_table.resizeColumnsToContents()

	def filter_table(self) -> None:
		first_filter = self.instructor_first_name_input.text().lower()
		last_filter = self.instructor_last_name_input.text().lower()
		num_filter = self.insctructor_course_input.text().lower()

		for index in range(self.instructor_table.rowCount()):

			show = True
			if first_filter != "":
				if first_filter not in self.instructor_table.item(index, 0).text().lower():
					show = False
			if last_filter != "" and show:
				if last_filter not in self.instructor_table.item(index, 1).text().lower():
					show = False
			if num_filter != "" and show:
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
