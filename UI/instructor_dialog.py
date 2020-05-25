# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/instructor_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
	def setupUi(self, DialogIn):
		self.dialog = DialogIn

		font = QtGui.QFont()
		font.setFamily("Arial")

		self.dialog.setObjectName("Dialog")
		self.dialog.resize(400, 300)
		self.gridLayout = QtWidgets.QGridLayout(self.dialog)
		self.gridLayout.setObjectName("gridLayout")
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")

		self.first_name_label = QtWidgets.QLabel(self.dialog)
		self.first_name_label.setObjectName("first_name_label")
		self.first_name_label.setFont(font)

		self.verticalLayout.addWidget(self.first_name_label)

		self.last_name_label = QtWidgets.QLabel(self.dialog)
		self.last_name_label.setObjectName("last_name_label")
		self.last_name_label.setFont(font)

		self.verticalLayout.addWidget(self.last_name_label)

		self.sort_name_label = QtWidgets.QLabel(self.dialog)
		self.sort_name_label.setObjectName("sort_name_label")
		self.sort_name_label.setFont(font)

		self.verticalLayout.addWidget(self.sort_name_label)

		self.person_id_label = QtWidgets.QLabel(self.dialog)
		self.person_id_label.setObjectName("person_id_label")
		self.person_id_label.setFont(font)

		self.verticalLayout.addWidget(self.person_id_label)

		self.byu_id_label = QtWidgets.QLabel(self.dialog)
		self.byu_id_label.setObjectName("byu_id_label")
		self.byu_id_label.setFont(font)

		self.verticalLayout.addWidget(self.byu_id_label)

		self.net_id_label = QtWidgets.QLabel(self.dialog)
		self.net_id_label.setObjectName("net_id_label")
		self.net_id_label.setFont(font)

		self.verticalLayout.addWidget(self.net_id_label)

		self.phone_label = QtWidgets.QLabel(self.dialog)
		self.phone_label.setObjectName("phone_label")
		self.phone_label.setFont(font)

		self.verticalLayout.addWidget(self.phone_label)

		self.num_ratings_label = QtWidgets.QLabel(self.dialog)
		self.num_ratings_label.setObjectName("num_ratings_label")
		self.num_ratings_label.setFont(font)

		self.verticalLayout.addWidget(self.num_ratings_label)

		self.rating_label = QtWidgets.QLabel(self.dialog)
		self.rating_label.setObjectName("rating_label")
		self.rating_label.setFont(font)

		self.verticalLayout.addWidget(self.rating_label)

		self.difficulty_label = QtWidgets.QLabel(self.dialog)
		self.difficulty_label.setObjectName("difficulty_label")
		self.difficulty_label.setFont(font)

		self.verticalLayout.addWidget(self.difficulty_label)
		spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout.addItem(spacerItem)
		self.horizontalLayout.addLayout(self.verticalLayout)
		self.verticalLayout_2 = QtWidgets.QVBoxLayout()
		self.verticalLayout_2.setObjectName("verticalLayout_2")

		self.label = QtWidgets.QLabel(self.dialog)
		self.label.setObjectName("label")
		self.label.setFont(font)

		self.verticalLayout_2.addWidget(self.label)

		self.tableView = QtWidgets.QTableView(self.dialog)
		self.tableView.setObjectName("tableView")
		self.tableView.setFont(font)

		self.verticalLayout_2.addWidget(self.tableView)
		self.horizontalLayout.addLayout(self.verticalLayout_2)
		self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

		self.retranslateUi()
		QtCore.QMetaObject.connectSlotsByName(self.dialog)

	def retranslateUi(self):
		_translate = QtCore.QCoreApplication.translate
		self.dialog.setWindowTitle(_translate("Dialog", "Dialog"))
		self.first_name_label.setText(_translate("Dialog", "First Name: ---"))
		self.last_name_label.setText(_translate("Dialog", "Last Name: ---"))
		self.sort_name_label.setText(_translate("Dialog", "Sort Name: ---"))
		self.person_id_label.setText(_translate("Dialog", "Person ID: ---"))
		self.byu_id_label.setText(_translate("Dialog", "BYU ID: ---"))
		self.net_id_label.setText(_translate("Dialog", "NetID: ---"))
		self.phone_label.setText(_translate("Dialog", "Phone Number: ---"))
		self.num_ratings_label.setText(_translate("Dialog", "Num. RMP Ratings: ---"))
		self.rating_label.setText(_translate("Dialog", "RMP Rating: ---"))
		self.difficulty_label.setText(_translate("Dialog", "RMP Difficulty: ---"))
		self.label.setText(_translate("Dialog", "Courses Taught:"))
