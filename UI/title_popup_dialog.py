# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/title_popup_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import Dao
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
	def setupUi(self, DialogIn: QtWidgets.QDialog, semester: str, year: int):
		self.dialog = DialogIn
		self.semester = semester
		self.year = str(year)
		self.semester_year = semester.lower() + "_" + str(year)

		font = QtGui.QFont()
		font.setFamily("Arial")

		self.dialog.setObjectName("Dialog")
		self.dialog.resize(400, 175)
		self.gridLayout = QtWidgets.QGridLayout(self.dialog)
		self.gridLayout.setObjectName("gridLayout")
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")

		self.message = QtWidgets.QLabel(self.dialog)
		self.message.setAlignment(QtCore.Qt.AlignCenter)
		self.message.setWordWrap(True)
		self.message.setObjectName("message")
		self.message.setFont(font)

		self.verticalLayout.addWidget(self.message)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")

		self.cached_result_button = QtWidgets.QPushButton(self.dialog)
		self.cached_result_button.setObjectName("cached_result_button")
		self.cached_result_button.setFont(font)
		self.cached_result_button.setEnabled(False)

		self.horizontalLayout.addWidget(self.cached_result_button)

		self.download_new_button = QtWidgets.QPushButton(self.dialog)
		self.download_new_button.setObjectName("download_new_button")
		self.download_new_button.setFont(font)
		self.download_new_button.setEnabled(False)

		self.horizontalLayout.addWidget(self.download_new_button)

		self.cancel_button = QtWidgets.QPushButton(self.dialog)
		self.cancel_button.setObjectName("cancel_button")
		self.cancel_button.setFont(font)

		self.horizontalLayout.addWidget(self.cancel_button)
		self.verticalLayout.addLayout(self.horizontalLayout)
		self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

		self.retranslateUi()
		QtCore.QMetaObject.connectSlotsByName(self.dialog)

		self.determine_availablilty()

		self.hook_buttons()

	def retranslateUi(self):
		_translate = QtCore.QCoreApplication.translate
		self.dialog.setWindowTitle(_translate("Dialog", "Load Semester Data"))
		self.message.setText(_translate("Dialog", "Loading data..."))
		self.cached_result_button.setText(_translate("Dialog", "Use Cached Result"))
		self.download_new_button.setText(_translate("Dialog", "Download New Result"))
		self.cancel_button.setText(_translate("Dialog", "Cancel"))

	def hook_buttons(self):
		self.cancel_button.clicked.connect(self.cancel_action)

	def cancel_action(self):
		self.dialog.close()

	def determine_availablilty(self):
		if Dao.Paths.check_exists_1(self.semester_year):
			self.message.setText(f"{self.semester} {self.year} is already cached({Dao.Paths.check_date_1(self.semester_year)}). Would you like to use that data or download new data?")
			self.cached_result_button.setEnabled(True)
			self.download_new_button.setEnabled(True)
		else:
			self.message.setText(f"{self.semester} {self.year} is not already cached. Would you like to download new data for this semester?")
			self.download_new_button.setEnabled(True)
