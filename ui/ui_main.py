# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1066, 786)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnConn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnConn.sizePolicy().hasHeightForWidth())
        self.btnConn.setSizePolicy(sizePolicy)
        self.btnConn.setObjectName("btnConn")
        self.horizontalLayout_3.addWidget(self.btnConn)
        self.btnDisconn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDisconn.sizePolicy().hasHeightForWidth())
        self.btnDisconn.setSizePolicy(sizePolicy)
        self.btnDisconn.setObjectName("btnDisconn")
        self.horizontalLayout_3.addWidget(self.btnDisconn)
        self.labConn = QtWidgets.QLabel(self.centralwidget)
        self.labConn.setMinimumSize(QtCore.QSize(200, 0))
        self.labConn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.labConn.setObjectName("labConn")
        self.horizontalLayout_3.addWidget(self.labConn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabVal = QtWidgets.QWidget()
        self.tabVal.setObjectName("tabVal")
        self.gridLayout = QtWidgets.QGridLayout(self.tabVal)
        self.gridLayout.setContentsMargins(20, 0, 20, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.edtOrderTyp = QtWidgets.QLineEdit(self.tabVal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtOrderTyp.sizePolicy().hasHeightForWidth())
        self.edtOrderTyp.setSizePolicy(sizePolicy)
        self.edtOrderTyp.setMinimumSize(QtCore.QSize(200, 25))
        self.edtOrderTyp.setObjectName("edtOrderTyp")
        self.gridLayout.addWidget(self.edtOrderTyp, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tabVal)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.edtTyp = QtWidgets.QLineEdit(self.tabVal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtTyp.sizePolicy().hasHeightForWidth())
        self.edtTyp.setSizePolicy(sizePolicy)
        self.edtTyp.setMinimumSize(QtCore.QSize(200, 25))
        self.edtTyp.setObjectName("edtTyp")
        self.gridLayout.addWidget(self.edtTyp, 5, 1, 1, 1)
        self.edtOrderSpec = QtWidgets.QLineEdit(self.tabVal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtOrderSpec.sizePolicy().hasHeightForWidth())
        self.edtOrderSpec.setSizePolicy(sizePolicy)
        self.edtOrderSpec.setMinimumSize(QtCore.QSize(200, 25))
        self.edtOrderSpec.setObjectName("edtOrderSpec")
        self.gridLayout.addWidget(self.edtOrderSpec, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tabVal)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tabVal)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 8, 0, 1, 1)
        self.cmbClass = QtWidgets.QComboBox(self.tabVal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbClass.sizePolicy().hasHeightForWidth())
        self.cmbClass.setSizePolicy(sizePolicy)
        self.cmbClass.setMinimumSize(QtCore.QSize(200, 25))
        self.cmbClass.setObjectName("cmbClass")
        self.gridLayout.addWidget(self.cmbClass, 8, 1, 1, 1)
        self.cmbSn = QtWidgets.QComboBox(self.tabVal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbSn.sizePolicy().hasHeightForWidth())
        self.cmbSn.setSizePolicy(sizePolicy)
        self.cmbSn.setMinimumSize(QtCore.QSize(200, 25))
        self.cmbSn.setObjectName("cmbSn")
        self.gridLayout.addWidget(self.cmbSn, 9, 1, 1, 1)
        self.edtVc = QtWidgets.QLineEdit(self.tabVal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtVc.sizePolicy().hasHeightForWidth())
        self.edtVc.setSizePolicy(sizePolicy)
        self.edtVc.setMinimumSize(QtCore.QSize(200, 25))
        self.edtVc.setObjectName("edtVc")
        self.gridLayout.addWidget(self.edtVc, 7, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tabVal)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 7, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tabVal)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 9, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tabVal)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 10, 0, 1, 1)
        self.btnCount = QtWidgets.QPushButton(self.tabVal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCount.sizePolicy().hasHeightForWidth())
        self.btnCount.setSizePolicy(sizePolicy)
        self.btnCount.setMinimumSize(QtCore.QSize(100, 25))
        self.btnCount.setObjectName("btnCount")
        self.gridLayout.addWidget(self.btnCount, 11, 1, 1, 1)
        self.sbAmount = QtWidgets.QSpinBox(self.tabVal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbAmount.sizePolicy().hasHeightForWidth())
        self.sbAmount.setSizePolicy(sizePolicy)
        self.sbAmount.setMinimumSize(QtCore.QSize(0, 25))
        self.sbAmount.setObjectName("sbAmount")
        self.gridLayout.addWidget(self.sbAmount, 10, 1, 1, 1)
        self.btnClear = QtWidgets.QPushButton(self.tabVal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnClear.sizePolicy().hasHeightForWidth())
        self.btnClear.setSizePolicy(sizePolicy)
        self.btnClear.setMinimumSize(QtCore.QSize(100, 25))
        self.btnClear.setObjectName("btnClear")
        self.gridLayout.addWidget(self.btnClear, 14, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tabVal)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.edtSpec = QtWidgets.QLineEdit(self.tabVal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtSpec.sizePolicy().hasHeightForWidth())
        self.edtSpec.setSizePolicy(sizePolicy)
        self.edtSpec.setMinimumSize(QtCore.QSize(200, 25))
        self.edtSpec.setObjectName("edtSpec")
        self.gridLayout.addWidget(self.edtSpec, 6, 1, 1, 1)
        self.edtInfo = QtWidgets.QTextEdit(self.tabVal)
        self.edtInfo.setObjectName("edtInfo")
        self.gridLayout.addWidget(self.edtInfo, 1, 2, 11, 1)
        self.label_10 = QtWidgets.QLabel(self.tabVal)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)
        self.edtDate = QtWidgets.QDateEdit(self.tabVal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtDate.sizePolicy().hasHeightForWidth())
        self.edtDate.setSizePolicy(sizePolicy)
        self.edtDate.setMinimumSize(QtCore.QSize(200, 25))
        self.edtDate.setObjectName("edtDate")
        self.gridLayout.addWidget(self.edtDate, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tabVal)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tabVal)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.edtOrder = QtWidgets.QLineEdit(self.tabVal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtOrder.sizePolicy().hasHeightForWidth())
        self.edtOrder.setSizePolicy(sizePolicy)
        self.edtOrder.setMinimumSize(QtCore.QSize(200, 25))
        self.edtOrder.setObjectName("edtOrder")
        self.gridLayout.addWidget(self.edtOrder, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tabVal, "")
        self.tabData = QtWidgets.QWidget()
        self.tabData.setObjectName("tabData")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabData)
        self.verticalLayout_2.setContentsMargins(20, 20, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.tabData)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.edtQryOrder = QtWidgets.QLineEdit(self.tabData)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtQryOrder.sizePolicy().hasHeightForWidth())
        self.edtQryOrder.setSizePolicy(sizePolicy)
        self.edtQryOrder.setMinimumSize(QtCore.QSize(150, 25))
        self.edtQryOrder.setObjectName("edtQryOrder")
        self.horizontalLayout_2.addWidget(self.edtQryOrder)
        self.label_14 = QtWidgets.QLabel(self.tabData)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_2.addWidget(self.label_14)
        self.edtQryTyp = QtWidgets.QLineEdit(self.tabData)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtQryTyp.sizePolicy().hasHeightForWidth())
        self.edtQryTyp.setSizePolicy(sizePolicy)
        self.edtQryTyp.setMinimumSize(QtCore.QSize(150, 25))
        self.edtQryTyp.setObjectName("edtQryTyp")
        self.horizontalLayout_2.addWidget(self.edtQryTyp)
        self.label_15 = QtWidgets.QLabel(self.tabData)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_2.addWidget(self.label_15)
        self.edtQrySpec = QtWidgets.QLineEdit(self.tabData)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtQrySpec.sizePolicy().hasHeightForWidth())
        self.edtQrySpec.setSizePolicy(sizePolicy)
        self.edtQrySpec.setMinimumSize(QtCore.QSize(150, 25))
        self.edtQrySpec.setObjectName("edtQrySpec")
        self.horizontalLayout_2.addWidget(self.edtQrySpec)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_11 = QtWidgets.QLabel(self.tabData)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.edtStartDate = QtWidgets.QDateEdit(self.tabData)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtStartDate.sizePolicy().hasHeightForWidth())
        self.edtStartDate.setSizePolicy(sizePolicy)
        self.edtStartDate.setMinimumSize(QtCore.QSize(170, 25))
        self.edtStartDate.setObjectName("edtStartDate")
        self.horizontalLayout.addWidget(self.edtStartDate)
        self.label_13 = QtWidgets.QLabel(self.tabData)
        self.label_13.setMinimumSize(QtCore.QSize(31, 0))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout.addWidget(self.label_13)
        self.edtEndDate = QtWidgets.QDateEdit(self.tabData)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtEndDate.sizePolicy().hasHeightForWidth())
        self.edtEndDate.setSizePolicy(sizePolicy)
        self.edtEndDate.setMinimumSize(QtCore.QSize(170, 25))
        self.edtEndDate.setObjectName("edtEndDate")
        self.horizontalLayout.addWidget(self.edtEndDate)
        spacerItem2 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btnQuery = QtWidgets.QPushButton(self.tabData)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnQuery.sizePolicy().hasHeightForWidth())
        self.btnQuery.setSizePolicy(sizePolicy)
        self.btnQuery.setObjectName("btnQuery")
        self.horizontalLayout.addWidget(self.btnQuery)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.twData = QtWidgets.QTableWidget(self.tabData)
        self.twData.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.twData.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.twData.setObjectName("twData")
        self.twData.setColumnCount(0)
        self.twData.setRowCount(0)
        self.twData.horizontalHeader().setHighlightSections(False)
        self.verticalLayout_2.addWidget(self.twData)
        self.tabWidget.addTab(self.tabData, "")
        self.tabCfg = QtWidgets.QWidget()
        self.tabCfg.setObjectName("tabCfg")
        self.tabWidget.addTab(self.tabCfg, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionManagement = QtWidgets.QAction(MainWindow)
        self.actionManagement.setObjectName("actionManagement")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btnConn, self.btnDisconn)
        MainWindow.setTabOrder(self.btnDisconn, self.tabWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "产值用料计算程序"))
        self.btnConn.setText(_translate("MainWindow", "连接"))
        self.btnDisconn.setText(_translate("MainWindow", "断开"))
        self.labConn.setText(_translate("MainWindow", "disconnect"))
        self.label_9.setText(_translate("MainWindow", "下单规格"))
        self.label_2.setText(_translate("MainWindow", "实际型号"))
        self.label_4.setText(_translate("MainWindow", "分类"))
        self.label.setText(_translate("MainWindow", "电压等级"))
        self.label_5.setText(_translate("MainWindow", "分类标准"))
        self.label_6.setText(_translate("MainWindow", "数量"))
        self.btnCount.setText(_translate("MainWindow", "确认"))
        self.btnClear.setText(_translate("MainWindow", "清空"))
        self.label_3.setText(_translate("MainWindow", "实际规格"))
        self.label_10.setText(_translate("MainWindow", "日期"))
        self.label_8.setText(_translate("MainWindow", "下单型号"))
        self.label_7.setText(_translate("MainWindow", "单号"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabVal), _translate("MainWindow", "业务处理"))
        self.label_12.setText(_translate("MainWindow", "单号"))
        self.label_14.setText(_translate("MainWindow", "型号"))
        self.label_15.setText(_translate("MainWindow", "规格"))
        self.label_11.setText(_translate("MainWindow", "日期"))
        self.label_13.setText(_translate("MainWindow", "-"))
        self.btnQuery.setText(_translate("MainWindow", "查询"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabData), _translate("MainWindow", "数据查询"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCfg), _translate("MainWindow", "系统设置"))
        self.actionManagement.setText(_translate("MainWindow", "management"))

