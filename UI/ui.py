# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/title.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import UI.title_popup_dialog
import UI.Dialog
import UI.browse_instructor_window
import Dao.Load
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
	def setupUi(self, MainWindowIn: QtWidgets.QMainWindow):
		self.setup_window(MainWindowIn)

		self.setup_title_page()
		self.setup_browse_instructor_page()

		self.finish_setup_window()

	def finish_setup_window(self):
		self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
		self.main_window.setCentralWidget(self.centralwidget)

		self.retranslateUi()
		QtCore.QMetaObject.connectSlotsByName(self.main_window)

		self.hook_buttons()
		self.populate_table()

		self.stackedWidget.setCurrentIndex(0)

	def setup_window(self, MainWindowIn: QtWidgets.QMainWindow):
		self.main_window = MainWindowIn
		self.main_window.setObjectName("MainWindow")
		self.main_window.resize(800, 380)

		self.centralwidget = QtWidgets.QWidget(self.main_window)
		self.centralwidget.setObjectName("centralwidget")

		self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName("gridLayout")

		self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
		self.stackedWidget.setObjectName("stackedWidget")

		self.title_font = QtGui.QFont()
		self.title_font.setFamily("Arial")
		self.title_font.setPointSize(36)
		self.font = QtGui.QFont()
		self.font.setFamily("Arial")

	def setup_title_page(self):
		self.page1 = QtWidgets.QWidget()
		self.page1.setObjectName("page")

		self.gridLayout1 = QtWidgets.QGridLayout(self.page1)
		self.gridLayout1.setObjectName("gridLayout1")

		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")

		self.big_title = QtWidgets.QLabel(self.page1)
		self.big_title.setFont(self.title_font)
		self.big_title.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
		self.big_title.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
		self.big_title.setObjectName("big_title")

		self.verticalLayout.addWidget(self.big_title)

		self.name_title = QtWidgets.QLabel(self.page1)
		self.name_title.setFont(self.font)
		self.name_title.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
		self.name_title.setObjectName("name_title")

		self.verticalLayout.addWidget(self.name_title)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout()
		self.verticalLayout_2.setObjectName("verticalLayout_2")

		self.semester_label = QtWidgets.QLabel(self.page1)
		self.semester_label.setFont(self.font)
		self.semester_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
		self.semester_label.setObjectName("semester_label")

		self.verticalLayout_2.addWidget(self.semester_label)

		self.semester_picker = QtWidgets.QComboBox(self.page1)
		self.semester_picker.setFont(self.font)
		self.semester_picker.setObjectName("semester_picker")
		self.semester_picker.addItems([""] * 4)

		self.verticalLayout_2.addWidget(self.semester_picker)

		self.year_label = QtWidgets.QLabel(self.page1)
		self.year_label.setFont(self.font)
		self.year_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
		self.year_label.setObjectName("year_label")

		self.verticalLayout_2.addWidget(self.year_label)

		self.year_picker = QtWidgets.QSpinBox(self.page1)
		self.year_picker.setFont(self.font)
		self.year_picker.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
		self.year_picker.setMinimum(2010)
		self.year_picker.setMaximum(2030)
		self.year_picker.setValue(2020)
		self.year_picker.setObjectName("year_picker")

		self.verticalLayout_2.addWidget(self.year_picker)
		self.verticalSpacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_2.addItem(self.verticalSpacer)
		self.horizontalLayout.addLayout(self.verticalLayout_2)
		self.gridLayout_2 = QtWidgets.QGridLayout()
		self.gridLayout_2.setObjectName("gridLayout_2")

		self.make_schedule_button = QtWidgets.QPushButton(self.page1)
		self.make_schedule_button.setFont(self.font)
		self.make_schedule_button.setObjectName("make_schedule_button")

		self.gridLayout_2.addWidget(self.make_schedule_button, 2, 1, 1, 1)

		self.browse_instructor_button = QtWidgets.QPushButton(self.page1)
		self.browse_instructor_button.setFont(self.font)
		self.browse_instructor_button.setObjectName("browse_instructor_button")

		self.gridLayout_2.addWidget(self.browse_instructor_button, 0, 1, 1, 1)

		self.browse_section_button = QtWidgets.QPushButton(self.page1)
		self.browse_section_button.setFont(self.font)
		self.browse_section_button.setObjectName("browse_section_button")

		self.gridLayout_2.addWidget(self.browse_section_button, 2, 0, 1, 1)

		self.browse_course_button = QtWidgets.QPushButton(self.page1)
		self.browse_course_button.setFont(self.font)
		self.browse_course_button.setObjectName("browse_course_button")

		self.gridLayout_2.addWidget(self.browse_course_button, 0, 0, 1, 1)

		self.horizontalLayout.addLayout(self.gridLayout_2)
		self.verticalLayout.addLayout(self.horizontalLayout)
		self.gridLayout1.addLayout(self.verticalLayout, 0, 0, 1, 1)
		self.stackedWidget.addWidget(self.page1)

	def setup_browse_instructor_page(self):
		self.data = {}
		self.page2 = QtWidgets.QWidget()
		self.page2.setObjectName("page2")

		self.gridLayout3 = QtWidgets.QGridLayout(self.page2)
		self.gridLayout3.setObjectName("gridLayout3")

		self.horizontalLayout3 = QtWidgets.QHBoxLayout()
		self.horizontalLayout3.setObjectName("horizontalLayout3")

		self.verticalLayout4 = QtWidgets.QVBoxLayout()
		self.verticalLayout4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
		self.verticalLayout4.setObjectName("verticalLayout4")

		self.label5 = QtWidgets.QLabel(self.page2)
		self.label5.setObjectName("label5")
		self.label5.setFont(self.font)

		self.verticalLayout4.addWidget(self.label5)

		self.lineEdit = QtWidgets.QLineEdit(self.page2)

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())

		self.lineEdit.setSizePolicy(sizePolicy)
		self.lineEdit.setObjectName("lineEdit")
		self.lineEdit.setFont(self.font)

		self.verticalLayout4.addWidget(self.lineEdit)

		self.label6 = QtWidgets.QLabel(self.page2)
		self.label6.setObjectName("label6")
		self.label6.setFont(self.font)

		self.verticalLayout4.addWidget(self.label6)

		self.lineEdit_2 = QtWidgets.QLineEdit(self.page2)

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())

		self.lineEdit_2.setSizePolicy(sizePolicy)
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.lineEdit_2.setFont(self.font)

		self.verticalLayout4.addWidget(self.lineEdit_2)

		self.label7 = QtWidgets.QLabel(self.page2)
		self.label7.setObjectName("label7")
		self.label7.setFont(self.font)

		self.verticalLayout4.addWidget(self.label7)

		self.lineEdit_3 = QtWidgets.QLineEdit(self.page2)

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())

		self.lineEdit_3.setSizePolicy(sizePolicy)
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.lineEdit_3.setFont(self.font)

		self.verticalLayout4.addWidget(self.lineEdit_3)

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)

		spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout4.addItem(spacerItem)
		self.horizontalLayout3.addLayout(self.verticalLayout4)

		self.table = QtWidgets.QTableWidget(self.page2)

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())

		self.table.setSizePolicy(sizePolicy)
		self.table.setObjectName("tableView")
		self.table.setFont(self.font)

		self.horizontalLayout3.addWidget(self.table)
		self.gridLayout3.addLayout(self.horizontalLayout3, 0, 0, 1, 1)
		self.stackedWidget.addWidget(self.page2)

	def retranslateUi(self):
		_translate = QtCore.QCoreApplication.translate
		self.main_window.setWindowTitle(_translate("MainWindow", "BYU Scheduler 2"))
		self.big_title.setText(_translate("MainWindow", "BYU Scheduler 2"))
		self.name_title.setText(_translate("MainWindow", "By Josh Bedwell"))
		self.semester_label.setText(_translate("MainWindow", "Semester"))
		self.semester_picker.setItemText(0, _translate("MainWindow", "Winter"))
		self.semester_picker.setItemText(1, _translate("MainWindow", "Spring"))
		self.semester_picker.setItemText(2, _translate("MainWindow", "Summer"))
		self.semester_picker.setItemText(3, _translate("MainWindow", "Fall"))
		self.year_label.setText(_translate("MainWindow", "Year"))
		self.make_schedule_button.setText(_translate("MainWindow", "Make Schedule"))
		self.browse_instructor_button.setText(_translate("MainWindow", "Browse Instructors"))
		self.browse_section_button.setText(_translate("MainWindow", "Browse Sections"))
		self.browse_course_button.setText(_translate("MainWindow", "Browse Courses"))
		self.label5.setText(_translate("MainWindow", "First Name"))
		self.label6.setText(_translate("MainWindow", "Last Name"))
		self.label7.setText(_translate("MainWindow", "Course Taught"))

	def hook_buttons(self):
		self.browse_course_button.clicked.connect(self.browse_course_action)
		self.browse_section_button.clicked.connect(self.browse_section_action)
		self.browse_instructor_button.clicked.connect(self.browse_instructor_action)
		self.make_schedule_button.clicked.connect(self.make_schedule_action)

	def populate_table(self):
		self.table.setColumnCount(7)
		self.table.setRowCount(len(self.data))
		self.table.setHorizontalHeaderLabels(["First Name", "Last Name", "Sort Name", "# Courses Taught", "# RMP Ratings", "RMP Rating", "RMP Difficulty", "HIDDEN"])
		for i, key in enumerate(self.data.keys()):
			self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(self.data[key]["first_name"]))
			self.table.setItem(i, 1, QtWidgets.QTableWidgetItem(self.data[key]["last_name"]))
			self.table.setItem(i, 2, QtWidgets.QTableWidgetItem(self.data[key]["sort_name"]))

			different_classes_taught = set()
			for section in self.data[key]["classes_taught"]:
				different_classes_taught.add(section["course"])
			self.table.setItem(i, 3, QtWidgets.QTableWidgetItem(str(len(different_classes_taught))))

			if self.data[key]["found_rmp"] == 1:
				self.table.setItem(i, 4, QtWidgets.QTableWidgetItem(str(self.data[key]["num_ratings"])))
				self.table.setItem(i, 5, QtWidgets.QTableWidgetItem(str(self.data[key]["avg_rating"])))
				self.table.setItem(i, 6, QtWidgets.QTableWidgetItem(str(self.data[key]["avg_easy_score"])))
			else:
				self.table.setItem(i, 4, QtWidgets.QTableWidgetItem("-"))
				self.table.setItem(i, 5, QtWidgets.QTableWidgetItem("-"))
				self.table.setItem(i, 6, QtWidgets.QTableWidgetItem("-"))
			self.table.setItem(i, 7, QtWidgets.QTableWidgetItem(key))
		self.table.hideColumn(7)
		self.table.setSortingEnabled(True)

	def browse_course_action(self):
		self.data["type"] = "course"
		self.show_popup()

	def browse_section_action(self):
		self.data["type"] = "section"
		self.show_popup()

	def browse_instructor_action(self):
		self.data["type"] = "instructor"
		self.show_popup()

	def make_schedule_action(self):
		self.data["data"] = "schedule"
		self.show_popup()

	def show_popup(self):
		load_decision = ["none"]
		popup_dialog = UI.Dialog.Dialog()
		popup_ui = UI.title_popup_dialog.Ui_Dialog()
		popup_ui.setupUi(popup_dialog, self.semester_picker.currentText(), self.year_picker.value(), load_decision)
		popup_dialog.exec_()

		if load_decision[0] == "load":
			print("going to load cached classes")
			if self.data["type"] == "course":
				# TODO load data
				self.goto_browse_course()
			elif self.data["type"] == "section":
				# TODO load data
				self.goto_browse_section()
			elif self.data["type"] == "instructor":
				data = Dao.Load.load_instructors(self.semester_picker.currentText().lower() + "_" + str(self.year_picker.value()))
				# change_to_instrcutor_view(self.main_window, self, data)
				main_window = QtWidgets.QMainWindow()
				ui = UI.browse_instructor_window.Ui_MainWindow()
				ui.setupUi(main_window, data)
				self.main_window.close()
				main_window.show()

			elif self.data["type"] == "schedule":
				# TODO load data
				self.goto_make_schedule()

	def goto_browse_course(self):
		print("browse course")

	def goto_browse_section(self):
		print("browse section")

	def goto_make_schedule(self):
		print("make schedule")


# def change_to_instrcutor_view(main_window, ui, data):
# 	del main_window
# 	main_window = QtWidgets.QMainWindow()
# 	ui = UI.browse_instructor_window.Ui_MainWindow()
# 	ui.setupUi(main_window, data)
# 	main_window.show()
