# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/browse_course_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
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

		self.course_horizontal_layout.addWidget(self.course_table)
		self.course_grid_layout.addLayout(self.course_horizontal_layout, 0, 0, 1, 1)
		self.main_window_stacked_widget.addWidget(self.course_page)

	def retranslateUi(self, MainWindow):
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
