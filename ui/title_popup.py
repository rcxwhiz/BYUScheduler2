# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/title_popup.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(382, 189)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.message = QtWidgets.QLabel(Form)
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setWordWrap(True)
        self.message.setObjectName("message")
        self.verticalLayout.addWidget(self.message)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cached_result_button = QtWidgets.QPushButton(Form)
        self.cached_result_button.setObjectName("cached_result_button")
        self.horizontalLayout.addWidget(self.cached_result_button)
        self.download_new_button = QtWidgets.QPushButton(Form)
        self.download_new_button.setObjectName("download_new_button")
        self.horizontalLayout.addWidget(self.download_new_button)
        self.cancel_button = QtWidgets.QPushButton(Form)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.message.setText(_translate("Form", "Fall 2020 has already been downloaded (time). Would you like to use that result or download a new one?"))
        self.cached_result_button.setText(_translate("Form", "Use Cached Result"))
        self.download_new_button.setText(_translate("Form", "Download New Result"))
        self.cancel_button.setText(_translate("Form", "Cancel"))
