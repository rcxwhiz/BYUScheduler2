from PyQt5 import QtWidgets


class Dialog(QtWidgets.QDialog):
	def __init(self):
		QtWidgets.QDialog.__init__(self)

	def closeEvent(self, event):
		print("entering parent close event")
		if self.cancel_action():
			print("close event accepted")
			event.accept()
		else:
			print("close event ignored")
			event.ignore()

	def cancel_action(self):
		print("closing time")
