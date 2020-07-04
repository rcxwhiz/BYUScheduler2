from PyQt5 import QtWidgets


def get_yn_answer(prompt, window):
	reply = QtWidgets.QMessageBox.question(window, '', prompt, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
	return reply == QtWidgets.QMessageBox.Yes
