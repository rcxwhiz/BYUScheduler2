# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/instructor_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from typing import Dict

from PyQt5 import QtCore, QtWidgets

import Dao


class Ui_Dialog(object):
	def setupUi(self, Dialog: QtWidgets.QDialog, instructor: Dict) -> None:
		Dialog.setObjectName("Dialog")
		Dialog.resize(400, 402)
		self.gridLayout = QtWidgets.QGridLayout(Dialog)
		self.gridLayout.setObjectName("gridLayout")
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")
		self.first_name_label = QtWidgets.QLabel(Dialog)
		self.first_name_label.setObjectName("first_name_label")
		self.verticalLayout.addWidget(self.first_name_label)
		self.last_name_label = QtWidgets.QLabel(Dialog)
		self.last_name_label.setObjectName("last_name_label")
		self.verticalLayout.addWidget(self.last_name_label)
		self.sort_name_label = QtWidgets.QLabel(Dialog)
		self.sort_name_label.setObjectName("sort_name_label")
		self.verticalLayout.addWidget(self.sort_name_label)
		self.person_id_label = QtWidgets.QLabel(Dialog)
		self.person_id_label.setObjectName("person_id_label")
		self.verticalLayout.addWidget(self.person_id_label)
		self.byu_id_label = QtWidgets.QLabel(Dialog)
		self.byu_id_label.setObjectName("byu_id_label")
		self.verticalLayout.addWidget(self.byu_id_label)
		self.net_id_label = QtWidgets.QLabel(Dialog)
		self.net_id_label.setObjectName("net_id_label")
		self.verticalLayout.addWidget(self.net_id_label)
		self.phone_label = QtWidgets.QLabel(Dialog)
		self.phone_label.setObjectName("phone_label")
		self.verticalLayout.addWidget(self.phone_label)
		self.num_ratings_label = QtWidgets.QLabel(Dialog)
		self.num_ratings_label.setObjectName("num_ratings_label")
		self.verticalLayout.addWidget(self.num_ratings_label)
		self.rating_label = QtWidgets.QLabel(Dialog)
		self.rating_label.setObjectName("rating_label")
		self.verticalLayout.addWidget(self.rating_label)
		self.difficulty_label = QtWidgets.QLabel(Dialog)
		self.difficulty_label.setObjectName("difficulty_label")
		self.verticalLayout.addWidget(self.difficulty_label)
		spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout.addItem(spacerItem)
		self.horizontalLayout.addLayout(self.verticalLayout)
		self.verticalLayout_2 = QtWidgets.QVBoxLayout()
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.label = QtWidgets.QLabel(Dialog)
		self.label.setObjectName("label")
		self.verticalLayout_2.addWidget(self.label)
		self.tableView = QtWidgets.QTableWidget(Dialog)
		self.tableView.setObjectName("tableView")
		self.tableView.setAlternatingRowColors(True)
		self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.verticalLayout_2.addWidget(self.tableView)
		self.horizontalLayout.addLayout(self.verticalLayout_2)
		self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

		self.retranslateUi(Dialog, instructor)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog: QtWidgets.QDialog, instructor: Dict) -> None:
		num_ratings = instructor['num_ratings']
		avg_rating = instructor['avg_rating']
		avg_easy_score = instructor['avg_easy_score']
		if num_ratings == "":
			num_ratings = "Not Found"
		if avg_rating == "":
			avg_rating = "Not Found"
		if avg_easy_score == "":
			avg_easy_score = "Not Found"

		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Instructor Info"))
		self.first_name_label.setText(_translate(f"Dialog", f"First Name:\n{Dao.none_safe(instructor['first_name'])}"))
		self.last_name_label.setText(_translate("Dialog", f"Last Name:\n{Dao.none_safe(instructor['last_name'])}"))
		self.sort_name_label.setText(_translate("Dialog", f"Sort Name:\n{Dao.none_safe(instructor['sort_name'])}"))
		self.person_id_label.setText(_translate("Dialog", f"Person ID:\n{Dao.none_safe(instructor['person_id'])}"))
		self.byu_id_label.setText(_translate("Dialog", f"BYU ID:\n{Dao.none_safe(instructor['byu_id'])}"))
		self.net_id_label.setText(_translate("Dialog", f"NetID:\n{Dao.none_safe(instructor['net_id'])}"))
		self.phone_label.setText(_translate("Dialog", f"Phone Number:\n{Dao.none_safe(instructor['phone_number'])}"))
		self.num_ratings_label.setText(_translate("Dialog", f"Num. RMP Ratings:\n{Dao.none_safe(num_ratings)}"))
		self.rating_label.setText(_translate("Dialog", f"RMP Rating:\n{Dao.none_safe(avg_rating)}"))
		self.difficulty_label.setText(_translate("Dialog", f"RMP Difficulty:\n{Dao.none_safe(avg_easy_score)}"))
		self.label.setText(_translate("Dialog", "Courses Taught:"))

		self.tableView.setColumnCount(2)
		self.tableView.setHorizontalHeaderLabels(["Course", "Section"])
		self.tableView.setRowCount(len(instructor["classes_taught"]))
		for i, course in enumerate(instructor["classes_taught"]):
			self.tableView.setItem(i, 0, QtWidgets.QTableWidgetItem(course["course"]))
			self.tableView.setItem(i, 1, QtWidgets.QTableWidgetItem(course["section"]))
		self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
