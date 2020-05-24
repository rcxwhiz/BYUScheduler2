# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'titleledWLI.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(804, 382)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.big_title = QLabel(self.centralwidget)
        self.big_title.setObjectName(u"big_title")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(36)
        self.big_title.setFont(font)
        self.big_title.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.big_title.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout.addWidget(self.big_title)

        self.name_title = QLabel(self.centralwidget)
        self.name_title.setObjectName(u"name_title")
        font1 = QFont()
        font1.setFamily(u"Arial")
        self.name_title.setFont(font1)
        self.name_title.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout.addWidget(self.name_title)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.semester_label = QLabel(self.centralwidget)
        self.semester_label.setObjectName(u"semester_label")
        self.semester_label.setFont(font1)
        self.semester_label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_2.addWidget(self.semester_label)

        self.semester_picker = QComboBox(self.centralwidget)
        self.semester_picker.addItem("")
        self.semester_picker.addItem("")
        self.semester_picker.addItem("")
        self.semester_picker.addItem("")
        self.semester_picker.setObjectName(u"semester_picker")
        self.semester_picker.setFont(font1)

        self.verticalLayout_2.addWidget(self.semester_picker)

        self.year_label = QLabel(self.centralwidget)
        self.year_label.setObjectName(u"year_label")
        self.year_label.setFont(font1)
        self.year_label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_2.addWidget(self.year_label)

        self.year_picker = QSpinBox(self.centralwidget)
        self.year_picker.setObjectName(u"year_picker")
        self.year_picker.setFont(font1)
        self.year_picker.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.year_picker.setMinimum(2010)
        self.year_picker.setMaximum(2030)

        self.verticalLayout_2.addWidget(self.year_picker)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.make_schedule_button = QPushButton(self.centralwidget)
        self.make_schedule_button.setObjectName(u"make_schedule_button")
        self.make_schedule_button.setFont(font1)

        self.gridLayout_2.addWidget(self.make_schedule_button, 2, 1, 1, 1)

        self.browse_instructor_button = QPushButton(self.centralwidget)
        self.browse_instructor_button.setObjectName(u"browse_instructor_button")
        self.browse_instructor_button.setFont(font1)

        self.gridLayout_2.addWidget(self.browse_instructor_button, 0, 1, 1, 1)

        self.browse_section_button = QPushButton(self.centralwidget)
        self.browse_section_button.setObjectName(u"browse_section_button")
        self.browse_section_button.setFont(font1)

        self.gridLayout_2.addWidget(self.browse_section_button, 2, 0, 1, 1)

        self.browse_course_button = QPushButton(self.centralwidget)
        self.browse_course_button.setObjectName(u"browse_course_button")
        self.browse_course_button.setFont(font1)

        self.gridLayout_2.addWidget(self.browse_course_button, 0, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.big_title.setText(QCoreApplication.translate("MainWindow", u"BYU Scheduler 2", None))
        self.name_title.setText(QCoreApplication.translate("MainWindow", u"By Josh Bedwell", None))
        self.semester_label.setText(QCoreApplication.translate("MainWindow", u"Semester", None))
        self.semester_picker.setItemText(0, QCoreApplication.translate("MainWindow", u"Winter", None))
        self.semester_picker.setItemText(1, QCoreApplication.translate("MainWindow", u"Spring", None))
        self.semester_picker.setItemText(2, QCoreApplication.translate("MainWindow", u"Summer", None))
        self.semester_picker.setItemText(3, QCoreApplication.translate("MainWindow", u"Fall", None))

        self.year_label.setText(QCoreApplication.translate("MainWindow", u"Year", None))
        self.make_schedule_button.setText(QCoreApplication.translate("MainWindow", u"Make Schedule", None))
        self.browse_instructor_button.setText(QCoreApplication.translate("MainWindow", u"Browse Instructors", None))
        self.browse_section_button.setText(QCoreApplication.translate("MainWindow", u"Browse Sections", None))
        self.browse_course_button.setText(QCoreApplication.translate("MainWindow", u"Browse Courses", None))

