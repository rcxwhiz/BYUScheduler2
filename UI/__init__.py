import UI.title
import sys
from PyQt5 import QtWidgets, QtCore


def run_ui():
	app = QtWidgets.QApplication([])
	main_window = QtWidgets.QMainWindow()

	ui = UI.title.Ui_MainWindow()
	ui.setupUi(main_window)
	main_window.show()

	sys.exit(app.exec_())
