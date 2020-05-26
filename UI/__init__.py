import UI.ui
import sys
from PyQt5 import QtWidgets, QtCore


def run_ui():
	app = QtWidgets.QApplication([])
	main_window = QtWidgets.QMainWindow()

	ui = UI.ui.Ui_MainWindow()
	ui.setup_ui(main_window)
	main_window.show()

	sys.exit(app.exec_())
