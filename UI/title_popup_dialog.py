# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/title_popup_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import Dao
import BYUAPI
from typing import List
import multiprocessing
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
	def setupUi(self, DialogIn: QtWidgets.QDialog, semester: str, year: int, load_decision: List[str]):
		self.dialog = DialogIn
		self.semester = semester
		self.year = str(year)
		self.semester_year = semester.lower() + "_" + str(year)
		self.load_decision = load_decision
		self.download_thread = None
		self.message_queue = multiprocessing.Manager().list()

		font = QtGui.QFont()
		font.setFamily("Arial")

		self.dialog.setObjectName("Dialog")
		self.dialog.resize(500, 550)
		self.gridLayout = QtWidgets.QGridLayout(self.dialog)
		self.gridLayout.setObjectName("gridLayout")
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")

		self.message = QtWidgets.QPlainTextEdit()
		self.message.setReadOnly(True)
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

		self.append_message_timer = QtCore.QTimer()
		self.append_message_timer.timeout.connect(self.handle_queue)
		log_update_interval = 200
		self.append_message_timer.start(log_update_interval)

		self.dialog.cancel_action = self.cancel_action

	def retranslateUi(self):
		_translate = QtCore.QCoreApplication.translate
		self.dialog.setWindowTitle(_translate("Dialog", "Load Semester Data"))
		self.message.setPlainText(_translate("Dialog", "Loading data..."))
		self.cached_result_button.setText(_translate("Dialog", "Use Cached Result"))
		self.download_new_button.setText(_translate("Dialog", "Download New Result"))
		self.cancel_button.setText(_translate("Dialog", "Cancel"))

	def hook_buttons(self):
		self.cancel_button.clicked.connect(self.cancel_action)
		self.download_new_button.clicked.connect(self.download_action)
		self.cached_result_button.clicked.connect(self.load_action)

	def cancel_action(self):
		self.load_decision[0] = "cancel"
		if self.download_thread is not None:
			self.download_thread.terminate()
			self.download_thread.join()
		self.dialog.close()

	def change_text(self, message):
		self.message_queue.append({"operation": "change", "message": message})

	def append_text(self, message):
		self.message_queue.append({"operation": "append", "message": message})

	def replace_line(self, message):
		self.message_queue.append({"operation": "replace", "message": message})

	def handle_queue(self):
		for message in self.message_queue:
			if message["operation"] == "change":
				self.apply_change(message["message"])
			elif message["operation"] == "append":
				self.apply_append(message["message"])
			elif message["operation"] == "replace":
				self.apply_replace(message["message"])
		self.message_queue[:] = []

	def apply_append(self, message_in):
		self.message.appendPlainText(message_in)

	def apply_change(self, message_in):
		self.message.setPlainText(message_in)

	def apply_replace(self, message_in):
		current_text = self.message.toPlainText().split("\n")
		current_text[-1] = message_in
		self.message.setPlainText("\n".join(current_text))

	def load_action(self):
		self.load_decision[0] = "load"
		self.dialog.close()

	def download_action(self):
		self.load_decision[0] = "download"
		self.download_new_button.setEnabled(False)
		self.cached_result_button.setEnabled(False)
		self.download_thread = multiprocessing.Process(target=downloader, args=(self.semester.lower(), self.year, self.append_text, self.replace_line, self.load_decision))
		self.download_thread.start()

	def determine_availablilty(self):
		if Dao.Paths.check_exists_1(self.semester_year):
			self.message.setPlainText(f"{self.semester} {self.year} is already cached ({Dao.Paths.check_date_1(self.semester_year)}). Would you like to use that data or download new data?")
			self.cached_result_button.setEnabled(True)
			self.download_new_button.setEnabled(True)
		else:
			self.message.setPlainText(f"{self.semester} {self.year} is not already cached. Would you like to download new data for this semester?")
			self.download_new_button.setEnabled(True)


def downloader(semester, year, append_function, replace_function, outcome):
	append_function("")
	append_function(f"Downloading {semester} {year}...")
	append_function("This will take a few minutes\n")
	try:
		Dao.MakeDatabase.save(BYUAPI.get(semester, str(year), append_function=append_function, replace_function=replace_function), append_function=append_function, replace_function=replace_function)
		outcome[0] = "load"
	except Exception as e:
		append_function(f"\nError getting {semester} {year} (it might not exist)")
		append_function("Please choose another semester")
		outcome[0] = "Error"
