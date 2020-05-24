# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/title.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import UI.title_popup_dialog
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
	def setupUi(self, MainWindowIn: QtWidgets.QMainWindow):
		self.main_window = MainWindowIn

		self.main_window.setObjectName("MainWindow")
		self.main_window.resize(800, 380)

		self.centralwidget = QtWidgets.QWidget(self.main_window)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName("gridLayout")
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")

		title_font = QtGui.QFont()
		title_font.setFamily("Arial")
		title_font.setPointSize(36)
		other_font = QtGui.QFont()
		other_font.setFamily("Arial")

		self.big_title = QtWidgets.QLabel(self.centralwidget)
		self.big_title.setFont(title_font)
		self.big_title.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
		self.big_title.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
		self.big_title.setObjectName("big_title")

		self.verticalLayout.addWidget(self.big_title)

		self.name_title = QtWidgets.QLabel(self.centralwidget)
		self.name_title.setFont(other_font)
		self.name_title.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
		self.name_title.setObjectName("name_title")

		self.verticalLayout.addWidget(self.name_title)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout()
		self.verticalLayout_2.setObjectName("verticalLayout_2")

		self.semester_label = QtWidgets.QLabel(self.centralwidget)
		self.semester_label.setFont(other_font)
		self.semester_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
		self.semester_label.setObjectName("semester_label")

		self.verticalLayout_2.addWidget(self.semester_label)

		self.semester_picker = QtWidgets.QComboBox(self.centralwidget)
		self.semester_picker.setFont(other_font)
		self.semester_picker.setObjectName("semester_picker")
		self.semester_picker.addItems([""] * 4)

		self.verticalLayout_2.addWidget(self.semester_picker)

		self.year_label = QtWidgets.QLabel(self.centralwidget)
		self.year_label.setFont(other_font)
		self.year_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
		self.year_label.setObjectName("year_label")

		self.verticalLayout_2.addWidget(self.year_label)

		self.year_picker = QtWidgets.QSpinBox(self.centralwidget)
		self.year_picker.setFont(other_font)
		self.year_picker.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
		self.year_picker.setMinimum(2010)
		self.year_picker.setMaximum(2030)
		self.year_picker.setValue(2020)
		self.year_picker.setObjectName("year_picker")

		self.verticalLayout_2.addWidget(self.year_picker)
		self.horizontalLayout.addLayout(self.verticalLayout_2)
		self.gridLayout_2 = QtWidgets.QGridLayout()
		self.gridLayout_2.setObjectName("gridLayout_2")

		self.make_schedule_button = QtWidgets.QPushButton(self.centralwidget)
		self.make_schedule_button.setFont(other_font)
		self.make_schedule_button.setObjectName("make_schedule_button")

		self.gridLayout_2.addWidget(self.make_schedule_button, 2, 1, 1, 1)

		self.browse_instructor_button = QtWidgets.QPushButton(self.centralwidget)
		self.browse_instructor_button.setFont(other_font)
		self.browse_instructor_button.setObjectName("browse_instructor_button")

		self.gridLayout_2.addWidget(self.browse_instructor_button, 0, 1, 1, 1)

		self.browse_section_button = QtWidgets.QPushButton(self.centralwidget)
		self.browse_section_button.setFont(other_font)
		self.browse_section_button.setObjectName("browse_section_button")

		self.gridLayout_2.addWidget(self.browse_section_button, 2, 0, 1, 1)

		self.browse_course_button = QtWidgets.QPushButton(self.centralwidget)
		self.browse_course_button.setFont(other_font)
		self.browse_course_button.setObjectName("browse_course_button")

		self.gridLayout_2.addWidget(self.browse_course_button, 0, 0, 1, 1)

		self.horizontalLayout.addLayout(self.gridLayout_2)
		self.verticalLayout.addLayout(self.horizontalLayout)
		self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
		self.main_window.setCentralWidget(self.centralwidget)

		self.retranslateUi()
		QtCore.QMetaObject.connectSlotsByName(self.main_window)

		self.hook_buttons()

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

	def hook_buttons(self):
		self.browse_course_button.clicked.connect(self.show_popup)
		self.browse_section_button.clicked.connect(self.show_popup)
		self.browse_instructor_button.clicked.connect(self.show_popup)
		self.make_schedule_button.clicked.connect(self.show_popup)

	def show_popup(self):
		popup_dialog = QtWidgets.QDialog()
		popup_ui = UI.title_popup_dialog.Ui_Dialog()
		popup_ui.setupUi(popup_dialog)
		popup_dialog.exec_()
