from PyQt5 import QtWidgets, QtCore


class Dialog(QtWidgets.QDialog):
	def __init(self):
		QtWidgets.QDialog.__init__(self)

	def closeEvent(self, event):
		if self.cancel_action():
			event.accept()
		else:
			event.ignore()

	def cancel_action(self):
		print("closing time")
