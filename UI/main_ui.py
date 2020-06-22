from PyQt5 import QtCore, QtWidgets

import Dao
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

		# items = UI.Pages.page_instructor.add_instructor_page(self.main_window_stacked_widget,
		#                                                      self.filter_instructor_table,
		#                                                      self.show_instructor,
		#                                                      self.goto_title_page)
		# self.instructor_first_name_input = items[0]
		# self.instructor_last_name_input = items[1]
		# self.instructor_course_input = items[2]
		# self.instructor_table = items[3]
		self.instructor_page = UI.Pages.page_instructor.InstructorPage(self.main_window_stacked_widget,
		                                                               self.goto_title_page, self.loaded_data)

		items = UI.Pages.page_course.add_course_page(self.main_window_stacked_widget, self.filter_course_table,
		                                             self.show_course, self.goto_title_page)
		self.course_dept_edit = items[0]
		self.course_course_num_edit = items[1]
		self.course_title_edit = items[2]
		self.course_instructor_edit = items[3]
		self.course_description_edit = items[4]
		self.course_honors_check = items[5]
		self.course_table = items[6]
		self.course_credit_hours_check = items[7]
		self.course_credit_hours_spinner = items[8]
		self.course_lab_hours_check = items[9]
		self.course_lab_hours_spinner = items[10]
		self.course_lecture_hours_check = items[11]
		self.course_lecture_hours_spinner = items[12]

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
		self.course_dept_edit.clear()
		self.course_course_num_edit.clear()
		self.course_title_edit.clear()
		self.course_instructor_edit.clear()
		self.course_description_edit.clear()
		self.course_honors_check.setChecked(False)
		self.course_description_edit.clear()
		self.populate_course_table()
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

	def populate_course_table(self) -> None:
		self.course_table.setColumnCount(9)
		self.course_table.setRowCount(len(self.loaded_data))
		self.course_table.setHorizontalHeaderLabels(
			["Dept", "Course Num", "Credits", "Title", "# Sections", "# Instructors", "Lab Hours", "Lecture Hours",
			 "HIDDEN"])
		for i, key in enumerate(self.loaded_data.keys()):
			self.course_table.setItem(i, 0,
			                          QtWidgets.QTableWidgetItem(Dao.none_safe(self.loaded_data[key]["dept_name"])))
			self.course_table.setItem(i, 1, QtWidgets.QTableWidgetItem(
				self.loaded_data[key]["catalog_number"] + Dao.none_safe(self.loaded_data[key]["catalog_suffix"])))
			self.course_table.setItem(i, 2,
			                          QtWidgets.QTableWidgetItem(Dao.none_safe(self.loaded_data[key]["credit_hours"])))
			title = Dao.none_safe(self.loaded_data[key]["full_title"])
			if title.endswith("."):
				title = title[:-1]
			self.course_table.setItem(i, 3, QtWidgets.QTableWidgetItem(title))
			item = QtWidgets.QTableWidgetItem()
			item.setData(QtCore.Qt.DisplayRole, len(self.loaded_data[key]["sections"]))
			self.course_table.setItem(i, 4, item)
			item = QtWidgets.QTableWidgetItem()
			item.setData(QtCore.Qt.DisplayRole, len(self.loaded_data[key]["instructors"]))
			self.course_table.setItem(i, 5, item)
			lab_hours = Dao.none_safe(self.loaded_data[key]["lab_hours"])
			try:
				lab_hours = float(lab_hours)
				item = QtWidgets.QTableWidgetItem()
				item.setData(QtCore.Qt.DisplayRole, lab_hours)
				self.course_table.setItem(i, 6, item)
			except:
				if "arr" in lab_hours.lower():
					lab_hours = "variable"
				self.course_table.setItem(i, 6, QtWidgets.QTableWidgetItem(lab_hours))
			lecture_hours = Dao.none_safe(self.loaded_data[key]["lecture_hours"])
			try:
				lecture_hours = float(lecture_hours)
				item = QtWidgets.QTableWidgetItem()
				item.setData(QtCore.Qt.DisplayRole, lecture_hours)
				self.course_table.setItem(i, 7, item)
			except:
				if "arr" in lecture_hours.lower():
					lecture_hours = "variable"
				self.course_table.setItem(i, 7, QtWidgets.QTableWidgetItem(lecture_hours))
			self.course_table.setItem(i, 8,
			                          QtWidgets.QTableWidgetItem(self.loaded_data[key]["curriculum_id_title_code"]))
		self.course_table.hideColumn(8)
		self.course_table.setSortingEnabled(True)
		self.course_table.resizeColumnsToContents()

	# TODO put this in the class
	def filter_course_table(self) -> None:
		dept_filter = self.course_dept_edit.text().lower()
		num_filter = self.course_course_num_edit.text().lower()
		credit_hours_checked = self.course_credit_hours_check.isChecked()
		credit_hour_filter = self.course_credit_hours_spinner.value()
		title_filter = self.course_title_edit.text().lower()
		instructor_filter = self.course_instructor_edit.text().lower()
		instructor_parts = instructor_filter.split(" ")
		lab_hour_checked = self.course_lab_hours_check.isChecked()
		lab_hour_filter = self.course_lab_hours_spinner.value()
		lecture_hour_checked = self.course_lecture_hours_check.isChecked()
		lecture_hours_filter = self.course_lecture_hours_spinner.value()
		honors_checked = self.course_honors_check.isChecked()
		description_filter = self.course_description_edit.toPlainText().lower()

		for index in range(self.course_table.rowCount()):
			show = True
			try:
				if dept_filter != "":
					if dept_filter not in self.course_table.item(index, 0).text().lower():
						show = False
				if show and num_filter != "":
					if num_filter not in self.course_table.item(index, 1).text().lower():
						show = False
				if show and credit_hours_checked:
					if credit_hour_filter != float(self.course_table.item(index, 2).text()):
						show = False
				if show and title_filter != "":
					if title_filter not in self.course_table.item(index, 3).text().lower():
						show = False
				if show and instructor_filter != "":
					show = False
					found = True
					for instructor in self.loaded_data[self.course_table.item(index, 8).text()]["instructors"]:
						if instructor is not None:
							for part in instructor_parts:
								if part not in instructor["sort_name"].lower():
									found = False
							if found:
								show = True
								break

				if show and lab_hour_checked:
					if lab_hour_filter != float(self.course_table.item(index, 6).text()):
						show = False
				if show and lecture_hour_checked:
					if lecture_hours_filter != float(self.course_table.item(index, 7).text()):
						show = False
				if show and honors_checked and (
						self.loaded_data[self.course_table.item(index, 8).text()]["honors_approved"] is None or
						self.loaded_data[self.course_table.item(index, 8).text()]["honors_approved"].lower() == "n"):
					show = False
				if show and description_filter != "":
					if self.loaded_data[self.course_table.item(index, 8).text()][
						"description"] is None or description_filter not in \
							self.loaded_data[self.course_table.item(index, 8).text()]["description"].lower():
						show = False
			except IOError as e:
				print("error sorting")
				print(e)
				show = False

			if show:
				self.course_table.showRow(index)
			else:
				self.course_table.hideRow(index)

	def show_course(self, row: int, column: int) -> None:
		course_dialog = QtWidgets.QDialog()
		course_ui = UI.dialog_course.Ui_Dialog()
		course_ui.setupUi(course_dialog, self.loaded_data[self.course_table.item(row, 8).text()])
		course_dialog.exec_()
