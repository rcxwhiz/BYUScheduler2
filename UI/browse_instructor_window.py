# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/browse_instructor_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
	def setupUi(self, MainWindowIn, data):
		self.main_window = MainWindowIn
		self.data = data

		font = QtGui.QFont()
		font.setFamily("Arial")

		self.main_window.setObjectName("MainWindow")
		self.main_window.resize(1087, 693)

		self.centralwidget = QtWidgets.QWidget(self.main_window)
		self.centralwidget.setObjectName("centralwidget")

		self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName("gridLayout")

		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")

		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
		self.verticalLayout.setObjectName("verticalLayout")

		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setObjectName("label")
		self.label.setFont(font)

		self.verticalLayout.addWidget(self.label)

		self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())

		self.lineEdit.setSizePolicy(sizePolicy)
		self.lineEdit.setObjectName("lineEdit")
		self.lineEdit.setFont(font)

		self.verticalLayout.addWidget(self.lineEdit)

		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setObjectName("label_2")
		self.label_2.setFont(font)

		self.verticalLayout.addWidget(self.label_2)

		self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())

		self.lineEdit_2.setSizePolicy(sizePolicy)
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.lineEdit_2.setFont(font)

		self.verticalLayout.addWidget(self.lineEdit_2)

		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setObjectName("label_3")
		self.label_3.setFont(font)

		self.verticalLayout.addWidget(self.label_3)

		self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())

		self.lineEdit_3.setSizePolicy(sizePolicy)
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.lineEdit_3.setFont(font)

		self.verticalLayout.addWidget(self.lineEdit_3)

		# self.label_4 = QtWidgets.QLabel(self.centralwidget)
		# self.label_4.setObjectName("label_4")
		# self.label_4.setFont(font)

		# self.verticalLayout.addWidget(self.label_4)

		# self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		# sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())

		# self.lineEdit_4.setSizePolicy(sizePolicy)
		# self.lineEdit_4.setObjectName("lineEdit_4")
		# self.lineEdit_4.setFont(font)

		# self.verticalLayout.addWidget(self.lineEdit_4)

		spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout.addItem(spacerItem)
		self.horizontalLayout.addLayout(self.verticalLayout)

		self.table = QtWidgets.QTableWidget(self.centralwidget)

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())

		self.table.setSizePolicy(sizePolicy)
		self.table.setObjectName("tableView")
		self.table.setFont(font)

		self.horizontalLayout.addWidget(self.table)
		self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
		self.main_window.setCentralWidget(self.centralwidget)

		self.retranslateUi()
		QtCore.QMetaObject.connectSlotsByName(self.main_window)

		self.populate_table()

		print("test")
		self.filter_table()

		print("going to connect filters")
		self.lineEdit.textChanged.connect(self.filter_table)
		self.lineEdit_2.textChanged.connect(self.filter_table)
		self.lineEdit_3.textChanged.connect(self.filter_table)
		self.lineEdit.returnPressed.connect(self.filter_table)
		print("connected filters")

	def retranslateUi(self):
		_translate = QtCore.QCoreApplication.translate
		self.main_window.setWindowTitle(_translate("MainWindow", "Browse Instructors"))
		self.label.setText(_translate("MainWindow", "First Name"))
		self.label_2.setText(_translate("MainWindow", "Last Name"))
		self.label_3.setText(_translate("MainWindow", "Course Taught"))
		# self.label_4.setText(_translate("MainWindow", "Course Num Taught"))

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

	def filter_table(self):
		print("filtering the table")

		for index in range(self.table.rowCount()):
			show = True
			if self.lineEdit.text() != "":
				if self.lineEdit.text() not in self.table.itemAt(index, 0):
					show = False
			if self.lineEdit_2.text() != "" and show:
				if self.lineEdit_2.text() not in self.table.itemAt(index, 1):
					show = False
			if self.lineEdit_3.text() != "" and show:
				show = False
				for course in self.data[self.table.itemAt(index, 7)]["classes_taught"]:
					if self.lineEdit_3.text() in course["course"]:
						show = True
						break
			if show:
				self.table.showRow(index)
				print(f"deciding to show row {index}")
			else:
				self.table.hideRow(index)
				print(f"deciding to hide row {index}")

		print("done filtering the table")
