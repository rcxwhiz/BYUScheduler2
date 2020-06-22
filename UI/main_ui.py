from PyQt5 import QtCore, QtWidgets

import UI.Pages.page_course
import UI.Pages.page_instructor
import UI.Pages.page_title
import UI.dialog_course
import UI.dialog_instructor
import UI.dialog_load


class Ui_MainWindow(object):
	# Setup
	# ----------------------------------------------------------------------------------
	def setup_ui(self, MainWindowIn: QtWidgets.QMainWindow) -> None:
		self.setup_window(MainWindowIn)
		self.loaded_data = {}

		self.title_semester_picker, self.title_year_picker = UI.Pages.page_title.add_title_page(
			self.main_window_stacked_widget, self.browse_course_action, self.browse_section_action,
			self.browse_instructor_action, self.make_schedule_action)

		self.instructor_page = UI.Pages.page_instructor.InstructorPage(self.main_window_stacked_widget,
		                                                               self.goto_title_page, self.loaded_data)

		self.course_page = UI.Pages.page_course.CoursePage(self.main_window_stacked_widget, self.goto_title_page,
		                                                   self.loaded_data)

		self.finish_setup_window()

	def setup_window(self, MainWindowIn: QtWidgets.QMainWindow) -> None:
		self.main_window = MainWindowIn

		self.main_window_central_widget = QtWidgets.QWidget(self.main_window)
		self.main_window_grid_layout = QtWidgets.QGridLayout(self.main_window_central_widget)
		self.main_window_stacked_widget = QtWidgets.QStackedWidget(self.main_window_central_widget)

	def finish_setup_window(self) -> None:
		self.main_window_grid_layout.addWidget(self.main_window_stacked_widget, 0, 0, 1, 1)
		self.main_window.setCentralWidget(self.main_window_central_widget)

		QtCore.QMetaObject.connectSlotsByName(self.main_window)

		self.goto_title_page()

	def goto_title_page(self) -> None:
		self.main_window.resize(800, 380)
		self.main_window_stacked_widget.setCurrentIndex(0)
		self.main_window.setWindowTitle("BYU Scheduler 2")
		self.loaded_data.clear()

	def goto_instructor_page(self) -> None:
		self.main_window.resize(1150, 700)
		self.instructor_page.initialize_page()
		self.main_window_stacked_widget.setCurrentIndex(1)
		self.main_window.setWindowTitle("Browse Instructors")

	def goto_browse_course(self) -> None:
		self.main_window.resize(1350, 700)
		self.course_page.initialize_page()
		self.course_page.populate_table()
		self.main_window_stacked_widget.setCurrentIndex(2)
		self.main_window.setWindowTitle("Browse Courses")

	def goto_browse_section(self) -> None:
		print("browse section")

	def goto_make_schedule(self) -> None:
		print("make schedule")

	# Title Functions
	# ----------------------------------------------------------------------------------

	def browse_instructor_action(self) -> None:
		self.loaded_data.clear()
		self.show_popup("instructor")
		if len(self.loaded_data) > 0:
			self.goto_instructor_page()

	def browse_course_action(self) -> None:
		self.loaded_data.clear()
		self.show_popup("course")
		if len(self.loaded_data) > 0:
			self.goto_browse_course()

	def browse_section_action(self) -> None:
		self.show_popup()

	def make_schedule_action(self) -> None:
		self.show_popup()

	def show_popup(self, data_type: str) -> None:
		popup_dialog = QtWidgets.QDialog()
		popup_ui = UI.dialog_load.Ui_Dialog()
		popup_ui.setupUi(popup_dialog,
		                 self.title_semester_picker.currentText(),
		                 self.title_year_picker.value(),
		                 self.loaded_data,
		                 data_type)
		popup_dialog.exec_()
