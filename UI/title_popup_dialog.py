# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/title_popup_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import multiprocessing
import threading
from typing import Dict

from PyQt5 import QtCore, QtWidgets

import BYUAPI
import Dao.load
import Dao.make_database
import Dao.paths


class Ui_Dialog(object):
	def setupUi(self, DialogIn: QtWidgets.QDialog, semester: str, year: int, data: Dict, data_type: str) -> None:
		self.dialog = DialogIn
		self.semester = semester
		self.year = str(year)
		self.semester_year = semester.lower() + "_" + str(year)
		self.return_data = data
		self.return_data.clear()
		self.data_type = data_type
		self.manager = multiprocessing.Manager()
		self.message_queue = self.manager.Queue()
		self.kill_queue = self.manager.Queue()
		self.base_threads = threading.active_count()

		self.dialog.setObjectName("Dialog")
		self.dialog.resize(500, 550)
		self.gridLayout = QtWidgets.QGridLayout(self.dialog)
		self.gridLayout.setObjectName("gridLayout")
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")

		self.message = QtWidgets.QPlainTextEdit()
		self.message.setReadOnly(True)
		self.message.setObjectName("message")

		self.verticalLayout.addWidget(self.message)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")

		self.cached_result_button = QtWidgets.QPushButton(self.dialog)
		self.cached_result_button.setObjectName("cached_result_button")
		self.cached_result_button.setEnabled(False)

		self.horizontalLayout.addWidget(self.cached_result_button)

		self.download_new_button = QtWidgets.QPushButton(self.dialog)
		self.download_new_button.setObjectName("download_new_button")
		self.download_new_button.setEnabled(False)

		self.horizontalLayout.addWidget(self.download_new_button)

		self.cancel_button = QtWidgets.QPushButton(self.dialog)
		self.cancel_button.setObjectName("cancel_button")

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

	def retranslateUi(self) -> None:
		_translate = QtCore.QCoreApplication.translate
		self.dialog.setWindowTitle(_translate("Dialog", "Load Semester Data"))
		self.message.setPlainText(_translate("Dialog", "Loading data..."))
		self.cached_result_button.setText(_translate("Dialog", "Use Cached Result"))
		self.download_new_button.setText(_translate("Dialog", "Download New Result"))
		self.cancel_button.setText(_translate("Dialog", "Cancel"))

	def hook_buttons(self) -> None:
		self.cancel_button.clicked.connect(self.cancel_action)
		self.download_new_button.clicked.connect(self.download_action)
		self.cached_result_button.clicked.connect(self.load_action)

	def check_to_close(self) -> None:
		while True:
			try:
				empty = self.kill_queue.empty()
			except BrokenPipeError:
				break
			if empty:
				break
			message = self.kill_queue.get()
			if message == "show cancel":
				self.cancel_button.setEnabled(True)
			if message == "hide cancel":
				self.cancel_button.setEnabled(False)
			if message == "exit":
				self.dialog.close()

	def exit(self) -> None:
		self.dialog.close()

	def cancel_action(self) -> None:
		self.append_message_timer.disconnect()
		self.manager.shutdown()

		assert len(multiprocessing.active_children()) == 0

		self.exit()

	def change_text(self, message: str) -> None:
		self.message_queue.put({"operation": "change", "message": message})

	def append_text(self, message: str) -> None:
		self.message_queue.put({"operation": "append", "message": message})

	def replace_line(self, message: str) -> None:
		self.message_queue.put({"operation": "replace", "message": message})

	def handle_queue(self) -> None:
		while not self.message_queue.empty():
			message = self.message_queue.get()
			if message["operation"] == "change":
				self.apply_change(message["message"])
			elif message["operation"] == "append":
				self.apply_append(message["message"])
			elif message["operation"] == "replace":
				self.apply_replace(message["message"])

	def apply_append(self, message_in: str) -> None:
		self.message.appendPlainText(message_in)

	def apply_change(self, message_in: str) -> None:
		self.message.setPlainText(message_in)

	def apply_replace(self, message_in: str) -> None:
		current_text = self.message.toPlainText().split("\n")
		current_text[-1] = message_in
		self.message.setPlainText("\n".join(current_text))

	def load_action(self) -> None:
		self.download_new_button.setEnabled(False)
		self.cached_result_button.setEnabled(False)
		self.cancel_button.setEnabled(False)

		self.append_text(f"\nLoading {self.semester} {self.year}...")
		self.append_text("This event cannot be cancelled beacuse sqlite3 is incompatible with multi-threading\n")
		if self.data_type == "instructor":
			threading.Thread(target=self.load_work_instructors).start()
		elif self.data_type == "course":
			threading.Thread(target=self.load_work_courses).start()

	def load_work_instructors(self) -> None:
		Dao.load.load_instructors(self.semester_year, self.return_data)
		self.replace_line(f"Loaded {self.semester} {self.year}")
		self.cancel_action()

	def load_work_courses(self) -> None:
		Dao.load.load_courses(self.semester_year, self.return_data)
		self.replace_line(f"Loaded {self.semester} {self.year}")
		self.cancel_action()

	def download_action(self) -> None:
		self.download_new_button.setEnabled(False)
		self.cached_result_button.setEnabled(False)
		self.cancel_button.setEnabled(False)

		self.append_text(f"\nDownloading {self.semester} {self.year}...")
		self.append_text("This will take a few minutes")
		self.append_text("This event cannot be cancelled beacuse sqlite3 is incompatible with multi-threading\n")
		threading.Thread(target=self.download_work).start()

	def download_work(self) -> None:
		try:
			Dao.make_database.save(BYUAPI.get(self.semester.lower(),
			                                  str(self.year),
			                                  append_function=self.append_text,
			                                  replace_function=self.replace_line),
			                       append_function=self.append_text,
			                       replace_function=self.replace_line)
		except Exception as e:
			print("got a downlading error")
			self.append_text(f"\nError getting {self.semester} {self.year} (it might not exist)")
			self.append_text(str(e))
			self.append_text("Please choose another semester")
			self.cancel_button.setEnabled(True)
			return None
		self.load_action()

	def determine_availablilty(self) -> None:
		if Dao.paths.check_exists_1(self.semester_year):
			self.message.setPlainText(
				f"{self.semester} {self.year} is already cached ({Dao.paths.check_date_1(self.semester_year)}). Would you like to use that data or download new data?")
			self.cached_result_button.setEnabled(True)
			self.download_new_button.setEnabled(True)
		else:
			self.message.setPlainText(
				f"{self.semester} {self.year} is not already cached. Would you like to download new data for this semester?")
			self.download_new_button.setEnabled(True)
