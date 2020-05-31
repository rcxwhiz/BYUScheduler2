import sys

from PyQt5 import QtWidgets

import UI.main_ui


def run_ui() -> None:
	app = QtWidgets.QApplication([])
	main_window = QtWidgets.QMainWindow()

	ui = UI.main_ui.Ui_MainWindow()
	ui.setup_ui(main_window)
	main_window.show()

	sys.exit(app.exec_())
