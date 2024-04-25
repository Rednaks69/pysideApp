# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainAppWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QDateEdit, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QMainWindow, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QTimeEdit, QVBoxLayout, QWidget)
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1531, 1123)
        icon = QIcon()
        icon.addFile(u":/assets/icons/Capture1.PNG", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"background-color:transparent;\n"
"background:none;\n"
"padding:0;\n"
"margin:0;\n"
"\n"
"}\n"
"/*menuBar*/\n"
"#menubar{\n"
"color:black;\n"
"}\n"
"#menuFile{\n"
"color:black;\n"
"}\n"
"#menuEdite{\n"
"color:black;\n"
"}\n"
"#menuAbout{\n"
"color:black;\n"
"}\n"
"\n"
"\n"
"/*centralwidget*/\n"
"#centralwidget{\n"
"	background-color: #faf8f8;\n"
"}\n"
"/*main_sideBar_container*/\n"
"#main_sideBar_container{\n"
"background-color: #5C7CFA;\n"
"}\n"
"#main_sideBar_container_2{\n"
"background-color: #5C7CFA;\n"
"}\n"
"\n"
"/*QPushButton*/\n"
"QPushButton{\n"
"text-align:left;\n"
"padding-top:2px;\n"
"padding-bottom:5px;\n"
"padding-left:10px;\n"
"padding-right:5px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #faf8f8;\n"
"color:#5C7CFA;\n"
"}\n"
"QPushButton:checked{\n"
"background-color: #faf8f8;\n"
"color:#5C7CFA;\n"
"}\n"
"#frame_main_btn_1 QPushButton{\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"}\n"
"#frame_main_btn_2 QPushButton{\n"
""
                        "border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"/*subMenu*/\n"
"\n"
"#submenu_subContainer{\n"
"color: black;\n"
"background-color: #faf8f8;\n"
"}\n"
"\n"
"#frame_7{\n"
"background-color: #faf8f8;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"}\n"
"#frame_7 label {\n"
"color:#5c7cfa;\n"
"}\n"
"\n"
"/*page Data*/\n"
"\n"
"\n"
"\n"
"\n"
"")
        MainWindow.setIconSize(QSize(55, 40))
        self.actionOuvrir = QAction(MainWindow)
        self.actionOuvrir.setObjectName(u"actionOuvrir")
        self.actionOuvrire = QAction(MainWindow)
        self.actionOuvrire.setObjectName(u"actionOuvrire")
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.actionFermer = QAction(MainWindow)
        self.actionFermer.setObjectName(u"actionFermer")
        self.actionCouper = QAction(MainWindow)
        self.actionCouper.setObjectName(u"actionCouper")
        self.actionColler = QAction(MainWindow)
        self.actionColler.setObjectName(u"actionColler")
        self.actionColler_2 = QAction(MainWindow)
        self.actionColler_2.setObjectName(u"actionColler_2")
        self.actionSupprimer = QAction(MainWindow)
        self.actionSupprimer.setObjectName(u"actionSupprimer")
        self.actionSuprimer = QAction(MainWindow)
        self.actionSuprimer.setObjectName(u"actionSuprimer")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_13 = QGridLayout(self.centralwidget)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.main_sideBar_container_2 = QWidget(self.centralwidget)
        self.main_sideBar_container_2.setObjectName(u"main_sideBar_container_2")
        self.verticalLayout_5 = QVBoxLayout(self.main_sideBar_container_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 5, 0, 0)
        self.main_sideBar_subContainer_2 = QWidget(self.main_sideBar_container_2)
        self.main_sideBar_subContainer_2.setObjectName(u"main_sideBar_subContainer_2")
        self.verticalLayout_7 = QVBoxLayout(self.main_sideBar_subContainer_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.frame_4 = QFrame(self.main_sideBar_subContainer_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menu_btn_2 = QPushButton(self.frame_4)
        self.menu_btn_2.setObjectName(u"menu_btn_2")
        font = QFont()
        font.setPointSize(9)
        self.menu_btn_2.setFont(font)
        self.menu_btn_2.setStyleSheet(u"QPushButton{\n"
"text-align:left;\n"
"padding-top:2px;\n"
"padding-bottom:5px;\n"
"padding-left:10px;\n"
"padding-right:5px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #faf8f8;\n"
"color:#5C7CFA;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/assets/icons/menu-30_active.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/assets/icons/menu-30.png", QSize(), QIcon.Normal, QIcon.On)
        self.menu_btn_2.setIcon(icon1)
        self.menu_btn_2.setIconSize(QSize(30, 30))
        self.menu_btn_2.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.menu_btn_2)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.frame_main_btn_2 = QFrame(self.main_sideBar_subContainer_2)
        self.frame_main_btn_2.setObjectName(u"frame_main_btn_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_main_btn_2.sizePolicy().hasHeightForWidth())
        self.frame_main_btn_2.setSizePolicy(sizePolicy)
        self.frame_main_btn_2.setFrameShape(QFrame.StyledPanel)
        self.frame_main_btn_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_main_btn_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.home_btn_2 = QPushButton(self.frame_main_btn_2)
        self.home_btn_2.setObjectName(u"home_btn_2")
        self.home_btn_2.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/assets/icons/dashboard-24.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/assets/icons/dashboard-24_active.png", QSize(), QIcon.Normal, QIcon.On)
        self.home_btn_2.setIcon(icon2)
        self.home_btn_2.setIconSize(QSize(24, 24))
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.home_btn_2)

        self.new_btn_2 = QPushButton(self.frame_main_btn_2)
        self.new_btn_2.setObjectName(u"new_btn_2")
        icon3 = QIcon()
        icon3.addFile(u":/assets/icons/new-file-64.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/assets/icons/new-file-64_active.png", QSize(), QIcon.Normal, QIcon.On)
        self.new_btn_2.setIcon(icon3)
        self.new_btn_2.setIconSize(QSize(24, 24))
        self.new_btn_2.setCheckable(True)
        self.new_btn_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.new_btn_2)

        self.data_btn_2 = QPushButton(self.frame_main_btn_2)
        self.data_btn_2.setObjectName(u"data_btn_2")
        icon4 = QIcon()
        icon4.addFile(u":/assets/icons/data-30.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/assets/icons/data-30_active.png", QSize(), QIcon.Normal, QIcon.On)
        self.data_btn_2.setIcon(icon4)
        self.data_btn_2.setIconSize(QSize(24, 24))
        self.data_btn_2.setCheckable(True)
        self.data_btn_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.data_btn_2)

        self.autre_btn_2 = QPushButton(self.frame_main_btn_2)
        self.autre_btn_2.setObjectName(u"autre_btn_2")
        icon5 = QIcon()
        icon5.addFile(u":/assets/icons/axie-infinity-30.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/assets/icons/axie-infinity-30_hover.png", QSize(), QIcon.Normal, QIcon.On)
        self.autre_btn_2.setIcon(icon5)
        self.autre_btn_2.setIconSize(QSize(24, 24))
        self.autre_btn_2.setCheckable(True)
        self.autre_btn_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.autre_btn_2)


        self.verticalLayout_7.addWidget(self.frame_main_btn_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.frame_6 = QFrame(self.main_sideBar_subContainer_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.settings_btn_2 = QPushButton(self.frame_6)
        self.settings_btn_2.setObjectName(u"settings_btn_2")
        icon6 = QIcon()
        icon6.addFile(u":/assets/icons/setting-30.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/assets/icons/setting-30_active.png", QSize(), QIcon.Normal, QIcon.On)
        self.settings_btn_2.setIcon(icon6)
        self.settings_btn_2.setIconSize(QSize(24, 24))
        self.settings_btn_2.setCheckable(True)

        self.verticalLayout_8.addWidget(self.settings_btn_2)

        self.quit_btn_2 = QPushButton(self.frame_6)
        self.quit_btn_2.setObjectName(u"quit_btn_2")
        icon7 = QIcon()
        icon7.addFile(u":/assets/icons/quit-30.png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/assets/icons/quit-30_active.png", QSize(), QIcon.Normal, QIcon.On)
        self.quit_btn_2.setIcon(icon7)
        self.quit_btn_2.setIconSize(QSize(24, 24))
        self.quit_btn_2.setCheckable(True)

        self.verticalLayout_8.addWidget(self.quit_btn_2)


        self.verticalLayout_7.addWidget(self.frame_6)


        self.verticalLayout_5.addWidget(self.main_sideBar_subContainer_2)


        self.gridLayout_13.addWidget(self.main_sideBar_container_2, 0, 0, 1, 1)

        self.main_sideBar_container = QWidget(self.centralwidget)
        self.main_sideBar_container.setObjectName(u"main_sideBar_container")
        self.verticalLayout = QVBoxLayout(self.main_sideBar_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 5, 0, 0)
        self.main_sideBar_subContainer = QWidget(self.main_sideBar_container)
        self.main_sideBar_subContainer.setObjectName(u"main_sideBar_subContainer")
        self.verticalLayout_3 = QVBoxLayout(self.main_sideBar_subContainer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.frame = QFrame(self.main_sideBar_subContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menu_btn = QPushButton(self.frame)
        self.menu_btn.setObjectName(u"menu_btn")
        self.menu_btn.setFont(font)
        self.menu_btn.setStyleSheet(u"QPushButton{\n"
"text-align:left;\n"
"padding-top:2px;\n"
"padding-bottom:5px;\n"
"padding-left:10px;\n"
"padding-right:5px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #faf8f8;\n"
"color:#5C7CFA;\n"
"}\n"
"")
        self.menu_btn.setIcon(icon1)
        self.menu_btn.setIconSize(QSize(30, 30))
        self.menu_btn.setCheckable(True)
        self.menu_btn.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.menu_btn, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_main_btn_1 = QFrame(self.main_sideBar_subContainer)
        self.frame_main_btn_1.setObjectName(u"frame_main_btn_1")
        sizePolicy.setHeightForWidth(self.frame_main_btn_1.sizePolicy().hasHeightForWidth())
        self.frame_main_btn_1.setSizePolicy(sizePolicy)
        self.frame_main_btn_1.setFrameShape(QFrame.StyledPanel)
        self.frame_main_btn_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_main_btn_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.home_btn = QPushButton(self.frame_main_btn_1)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setStyleSheet(u"")
        self.home_btn.setIcon(icon2)
        self.home_btn.setIconSize(QSize(24, 24))
        self.home_btn.setCheckable(True)
        self.home_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_btn)

        self.new_btn = QPushButton(self.frame_main_btn_1)
        self.new_btn.setObjectName(u"new_btn")
        self.new_btn.setIcon(icon3)
        self.new_btn.setIconSize(QSize(24, 24))
        self.new_btn.setCheckable(True)
        self.new_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.new_btn)

        self.data_btn = QPushButton(self.frame_main_btn_1)
        self.data_btn.setObjectName(u"data_btn")
        self.data_btn.setIcon(icon4)
        self.data_btn.setIconSize(QSize(24, 24))
        self.data_btn.setCheckable(True)
        self.data_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.data_btn)

        self.autre_btn = QPushButton(self.frame_main_btn_1)
        self.autre_btn.setObjectName(u"autre_btn")
        self.autre_btn.setIcon(icon5)
        self.autre_btn.setIconSize(QSize(24, 24))
        self.autre_btn.setCheckable(True)
        self.autre_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.autre_btn)


        self.verticalLayout_3.addWidget(self.frame_main_btn_1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.main_sideBar_subContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.settings_btn = QPushButton(self.frame_3)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setIcon(icon6)
        self.settings_btn.setIconSize(QSize(24, 24))
        self.settings_btn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.settings_btn)

        self.quit_btn = QPushButton(self.frame_3)
        self.quit_btn.setObjectName(u"quit_btn")
        self.quit_btn.setIcon(icon7)
        self.quit_btn.setIconSize(QSize(24, 24))
        self.quit_btn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.quit_btn)


        self.verticalLayout_3.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.main_sideBar_subContainer)


        self.gridLayout_13.addWidget(self.main_sideBar_container, 0, 1, 1, 1)

        self.subMenu_container = QWidget(self.centralwidget)
        self.subMenu_container.setObjectName(u"subMenu_container")
        self.subMenu_container.setMaximumSize(QSize(300, 16777215))
        self.subMenu_container.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.subMenu_container)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.submenu_subContainer = QWidget(self.subMenu_container)
        self.submenu_subContainer.setObjectName(u"submenu_subContainer")
        self.submenu_subContainer.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_10 = QVBoxLayout(self.submenu_subContainer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(10, 0, 0, 0)
        self.menu_stackedWidget = QStackedWidget(self.submenu_subContainer)
        self.menu_stackedWidget.setObjectName(u"menu_stackedWidget")
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.verticalLayout_12 = QVBoxLayout(self.new_page)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.new_page)
        self.frame_7.setObjectName(u"frame_7")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.frame_7.setFont(font1)
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(92, 124, 250);")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.pushButton_2 = QPushButton(self.frame_7)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon8 = QIcon()
        icon8.addFile(u":/assets/icons/quit-30_menu_active.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon8)
        self.pushButton_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.pushButton_2, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_7, 0, Qt.AlignTop)

        self.new_list_item = QWidget(self.new_page)
        self.new_list_item.setObjectName(u"new_list_item")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.new_list_item.sizePolicy().hasHeightForWidth())
        self.new_list_item.setSizePolicy(sizePolicy1)
        self.new_list_item.setStyleSheet(u"background-color: rgb(236, 234, 234);\n"
"")
        self.verticalLayout_21 = QVBoxLayout(self.new_list_item)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.Equipement_widget_2 = QWidget(self.new_list_item)
        self.Equipement_widget_2.setObjectName(u"Equipement_widget_2")
        self.Equipement_widget_2.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_8 = QHBoxLayout(self.Equipement_widget_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.Equipement_widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/assets/icons/new-company-30.png"))

        self.horizontalLayout_8.addWidget(self.label_5, 0, Qt.AlignLeft)

        self.pushButton_11 = QPushButton(self.Equipement_widget_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy2)
        self.pushButton_11.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_11.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/assets/icons/scroll-right_30.png", QSize(), QIcon.Normal, QIcon.Off)
        icon9.addFile(u":/assets/icons/scroll-down-30.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_11.setIcon(icon9)
        self.pushButton_11.setIconSize(QSize(24, 24))
        self.pushButton_11.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.pushButton_11)


        self.verticalLayout_21.addWidget(self.Equipement_widget_2)

        self.widget_3 = QWidget(self.new_list_item)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"\n"
"QPushButton{\n"
"color:rgb(92, 124, 250);\n"
"border-top-left-radius:7px;\n"
"border-bottom-left-radius:7px;\n"
"border-top-right-radius:7px;\n"
"border-bottom-right-radius:7px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(203, 203, 203);\n"
"}")
        self.verticalLayout_16 = QVBoxLayout(self.widget_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.nvDossier_EXT_btn = QPushButton(self.widget_3)
        self.nvDossier_EXT_btn.setObjectName(u"nvDossier_EXT_btn")
        icon10 = QIcon()
        icon10.addFile(u":/assets/icons/mission-30_active.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nvDossier_EXT_btn.setIcon(icon10)

        self.verticalLayout_16.addWidget(self.nvDossier_EXT_btn)

        self.allDossier_EXT_btn = QPushButton(self.widget_3)
        self.allDossier_EXT_btn.setObjectName(u"allDossier_EXT_btn")
        icon11 = QIcon()
        icon11.addFile(u":/assets/icons/consult_30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.allDossier_EXT_btn.setIcon(icon11)

        self.verticalLayout_16.addWidget(self.allDossier_EXT_btn)

        self.pushButton_14 = QPushButton(self.widget_3)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.verticalLayout_16.addWidget(self.pushButton_14)


        self.verticalLayout_21.addWidget(self.widget_3)

        self.Personnel_widget_2 = QWidget(self.new_list_item)
        self.Personnel_widget_2.setObjectName(u"Personnel_widget_2")
        self.Personnel_widget_2.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_9 = QHBoxLayout(self.Personnel_widget_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_6 = QLabel(self.Personnel_widget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setPixmap(QPixmap(u":/assets/icons/concept-30.png"))

        self.horizontalLayout_9.addWidget(self.label_6, 0, Qt.AlignLeft)

        self.pushButton_18 = QPushButton(self.Personnel_widget_2)
        self.pushButton_18.setObjectName(u"pushButton_18")
        sizePolicy2.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy2)
        self.pushButton_18.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_18.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_18.setIcon(icon9)
        self.pushButton_18.setIconSize(QSize(24, 24))
        self.pushButton_18.setCheckable(True)

        self.horizontalLayout_9.addWidget(self.pushButton_18)


        self.verticalLayout_21.addWidget(self.Personnel_widget_2)

        self.widget_5 = QWidget(self.new_list_item)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"\n"
"QPushButton{\n"
"color:rgb(92, 124, 250);\n"
"border-top-left-radius:7px;\n"
"border-bottom-left-radius:7px;\n"
"border-top-right-radius:7px;\n"
"border-bottom-right-radius:7px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(203, 203, 203);\n"
"}")
        self.verticalLayout_17 = QVBoxLayout(self.widget_5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.nvDossier_IVW_btn = QPushButton(self.widget_5)
        self.nvDossier_IVW_btn.setObjectName(u"nvDossier_IVW_btn")
        icon12 = QIcon()
        icon12.addFile(u":/assets/icons/plus-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nvDossier_IVW_btn.setIcon(icon12)

        self.verticalLayout_17.addWidget(self.nvDossier_IVW_btn)

        self.allDossier_IVW_btn = QPushButton(self.widget_5)
        self.allDossier_IVW_btn.setObjectName(u"allDossier_IVW_btn")
        self.allDossier_IVW_btn.setIcon(icon11)

        self.verticalLayout_17.addWidget(self.allDossier_IVW_btn)

        self.pushButton_17 = QPushButton(self.widget_5)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.verticalLayout_17.addWidget(self.pushButton_17)


        self.verticalLayout_21.addWidget(self.widget_5)

        self.Personnel_widget_3 = QWidget(self.new_list_item)
        self.Personnel_widget_3.setObjectName(u"Personnel_widget_3")
        self.Personnel_widget_3.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_10 = QHBoxLayout(self.Personnel_widget_3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_7 = QLabel(self.Personnel_widget_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setPixmap(QPixmap(u":/assets/icons/zoomerang-30.png"))

        self.horizontalLayout_10.addWidget(self.label_7, 0, Qt.AlignLeft)

        self.pushButton_19 = QPushButton(self.Personnel_widget_3)
        self.pushButton_19.setObjectName(u"pushButton_19")
        sizePolicy2.setHeightForWidth(self.pushButton_19.sizePolicy().hasHeightForWidth())
        self.pushButton_19.setSizePolicy(sizePolicy2)
        self.pushButton_19.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_19.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_19.setIcon(icon9)
        self.pushButton_19.setIconSize(QSize(24, 24))
        self.pushButton_19.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.pushButton_19)


        self.verticalLayout_21.addWidget(self.Personnel_widget_3)

        self.widget_6 = QWidget(self.new_list_item)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"\n"
"QPushButton{\n"
"color:rgb(92, 124, 250);\n"
"border-top-left-radius:7px;\n"
"border-bottom-left-radius:7px;\n"
"border-top-right-radius:7px;\n"
"border-bottom-right-radius:7px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(203, 203, 203);\n"
"}")
        self.verticalLayout_18 = QVBoxLayout(self.widget_6)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.nvDossier_IVD_btn = QPushButton(self.widget_6)
        self.nvDossier_IVD_btn.setObjectName(u"nvDossier_IVD_btn")
        self.nvDossier_IVD_btn.setIcon(icon12)

        self.verticalLayout_18.addWidget(self.nvDossier_IVD_btn)

        self.allDossier_IVD_btn = QPushButton(self.widget_6)
        self.allDossier_IVD_btn.setObjectName(u"allDossier_IVD_btn")
        self.allDossier_IVD_btn.setIcon(icon11)

        self.verticalLayout_18.addWidget(self.allDossier_IVD_btn)

        self.pushButton_24 = QPushButton(self.widget_6)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.verticalLayout_18.addWidget(self.pushButton_24)


        self.verticalLayout_21.addWidget(self.widget_6)

        self.Personnel_widget_5 = QWidget(self.new_list_item)
        self.Personnel_widget_5.setObjectName(u"Personnel_widget_5")
        self.Personnel_widget_5.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_12 = QHBoxLayout(self.Personnel_widget_5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_9 = QLabel(self.Personnel_widget_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setPixmap(QPixmap(u":/assets/icons/cryptocurrency-website-30.png"))

        self.horizontalLayout_12.addWidget(self.label_9, 0, Qt.AlignLeft)

        self.pushButton_21 = QPushButton(self.Personnel_widget_5)
        self.pushButton_21.setObjectName(u"pushButton_21")
        sizePolicy2.setHeightForWidth(self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy2)
        self.pushButton_21.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_21.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_21.setIcon(icon9)
        self.pushButton_21.setIconSize(QSize(24, 24))
        self.pushButton_21.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.pushButton_21)


        self.verticalLayout_21.addWidget(self.Personnel_widget_5)

        self.widget_7 = QWidget(self.new_list_item)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setStyleSheet(u"\n"
"QPushButton{\n"
"color:rgb(92, 124, 250);\n"
"border-top-left-radius:7px;\n"
"border-bottom-left-radius:7px;\n"
"border-top-right-radius:7px;\n"
"border-bottom-right-radius:7px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(203, 203, 203);\n"
"}")
        self.verticalLayout_19 = QVBoxLayout(self.widget_7)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.nvDossier_Digital_btn = QPushButton(self.widget_7)
        self.nvDossier_Digital_btn.setObjectName(u"nvDossier_Digital_btn")
        self.nvDossier_Digital_btn.setIcon(icon12)

        self.verticalLayout_19.addWidget(self.nvDossier_Digital_btn)

        self.allDossier_Digital_btn = QPushButton(self.widget_7)
        self.allDossier_Digital_btn.setObjectName(u"allDossier_Digital_btn")
        self.allDossier_Digital_btn.setIcon(icon11)

        self.verticalLayout_19.addWidget(self.allDossier_Digital_btn)

        self.pushButton_27 = QPushButton(self.widget_7)
        self.pushButton_27.setObjectName(u"pushButton_27")

        self.verticalLayout_19.addWidget(self.pushButton_27)


        self.verticalLayout_21.addWidget(self.widget_7)

        self.Personnel_widget_4 = QWidget(self.new_list_item)
        self.Personnel_widget_4.setObjectName(u"Personnel_widget_4")
        self.Personnel_widget_4.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_11 = QHBoxLayout(self.Personnel_widget_4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_8 = QLabel(self.Personnel_widget_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setPixmap(QPixmap(u":/assets/icons/axie-infinity-30.png"))

        self.horizontalLayout_11.addWidget(self.label_8, 0, Qt.AlignLeft)

        self.pushButton_20 = QPushButton(self.Personnel_widget_4)
        self.pushButton_20.setObjectName(u"pushButton_20")
        sizePolicy2.setHeightForWidth(self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy2)
        self.pushButton_20.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_20.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_20.setIcon(icon9)
        self.pushButton_20.setIconSize(QSize(24, 24))
        self.pushButton_20.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.pushButton_20)


        self.verticalLayout_21.addWidget(self.Personnel_widget_4)

        self.widget_8 = QWidget(self.new_list_item)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"\n"
"QPushButton{\n"
"color:rgb(92, 124, 250);\n"
"border-top-left-radius:7px;\n"
"border-bottom-left-radius:7px;\n"
"border-top-right-radius:7px;\n"
"border-bottom-right-radius:7px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(203, 203, 203);\n"
"}")
        self.verticalLayout_20 = QVBoxLayout(self.widget_8)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.nvDossier_Autre_btn = QPushButton(self.widget_8)
        self.nvDossier_Autre_btn.setObjectName(u"nvDossier_Autre_btn")
        self.nvDossier_Autre_btn.setIcon(icon12)

        self.verticalLayout_20.addWidget(self.nvDossier_Autre_btn)


        self.verticalLayout_21.addWidget(self.widget_8)

        self.verticalSpacer_4 = QSpacerItem(20, 249, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_4)


        self.verticalLayout_12.addWidget(self.new_list_item)

        self.menu_stackedWidget.addWidget(self.new_page)
        self.data_page = QWidget()
        self.data_page.setObjectName(u"data_page")
        self.verticalLayout_11 = QVBoxLayout(self.data_page)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.data_page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: rgb(250, 248, 248);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color:rgb(92, 124, 250);")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.pushButton_3 = QPushButton(self.frame_8)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setIcon(icon8)
        self.pushButton_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.pushButton_3, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_8, 0, Qt.AlignTop)

        self.data_list_item = QWidget(self.data_page)
        self.data_list_item.setObjectName(u"data_list_item")
        sizePolicy1.setHeightForWidth(self.data_list_item.sizePolicy().hasHeightForWidth())
        self.data_list_item.setSizePolicy(sizePolicy1)
        self.data_list_item.setStyleSheet(u"background-color: rgb(236, 234, 234);\n"
"border-top-left-radius:10px;")
        self.verticalLayout_265 = QVBoxLayout(self.data_list_item)
        self.verticalLayout_265.setObjectName(u"verticalLayout_265")
        self.Equipement_widget = QWidget(self.data_list_item)
        self.Equipement_widget.setObjectName(u"Equipement_widget")
        self.Equipement_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_4 = QHBoxLayout(self.Equipement_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.Equipement_widget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/assets/icons/equippement-30.png"))

        self.horizontalLayout_4.addWidget(self.label, 0, Qt.AlignLeft)

        self.pushButton = QPushButton(self.Equipement_widget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setLayoutDirection(Qt.RightToLeft)
        self.pushButton.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton.setIcon(icon9)
        self.pushButton.setIconSize(QSize(24, 24))
        self.pushButton.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_265.addWidget(self.Equipement_widget)

        self.widget_2 = QWidget(self.data_list_item)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"\n"
"QPushButton{\n"
"color:rgb(92, 124, 250);\n"
"border-top-left-radius:7px;\n"
"border-bottom-left-radius:7px;\n"
"border-top-right-radius:7px;\n"
"border-bottom-right-radius:7px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(203, 203, 203);\n"
"}")
        self.verticalLayout_13 = QVBoxLayout(self.widget_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.nvEquipement_btn = QPushButton(self.widget_2)
        self.nvEquipement_btn.setObjectName(u"nvEquipement_btn")
        self.nvEquipement_btn.setIcon(icon12)

        self.verticalLayout_13.addWidget(self.nvEquipement_btn)

        self.allEquipement_btn = QPushButton(self.widget_2)
        self.allEquipement_btn.setObjectName(u"allEquipement_btn")
        self.allEquipement_btn.setIcon(icon11)

        self.verticalLayout_13.addWidget(self.allEquipement_btn)

        self.pushButton_7 = QPushButton(self.widget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_13.addWidget(self.pushButton_7)


        self.verticalLayout_265.addWidget(self.widget_2)

        self.Personnel_widget = QWidget(self.data_list_item)
        self.Personnel_widget.setObjectName(u"Personnel_widget")
        self.Personnel_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_7 = QHBoxLayout(self.Personnel_widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.Personnel_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/assets/icons/employee-30.png"))

        self.horizontalLayout_7.addWidget(self.label_4, 0, Qt.AlignLeft)

        self.pushButton_4 = QPushButton(self.Personnel_widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy2.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy2)
        self.pushButton_4.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_4.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_4.setIcon(icon9)
        self.pushButton_4.setIconSize(QSize(24, 24))
        self.pushButton_4.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.pushButton_4)


        self.verticalLayout_265.addWidget(self.Personnel_widget)

        self.widget_4 = QWidget(self.data_list_item)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"\n"
"QPushButton{\n"
"color:rgb(92, 124, 250);\n"
"border-top-left-radius:7px;\n"
"border-bottom-left-radius:7px;\n"
"border-top-right-radius:7px;\n"
"border-bottom-right-radius:7px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(203, 203, 203);\n"
"}")
        self.verticalLayout_14 = QVBoxLayout(self.widget_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.nvPersonne_btn = QPushButton(self.widget_4)
        self.nvPersonne_btn.setObjectName(u"nvPersonne_btn")
        self.nvPersonne_btn.setStyleSheet(u"")
        self.nvPersonne_btn.setIcon(icon12)

        self.verticalLayout_14.addWidget(self.nvPersonne_btn)

        self.allPersonne_btn = QPushButton(self.widget_4)
        self.allPersonne_btn.setObjectName(u"allPersonne_btn")
        self.allPersonne_btn.setIcon(icon11)

        self.verticalLayout_14.addWidget(self.allPersonne_btn)

        self.pushButton_10 = QPushButton(self.widget_4)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.verticalLayout_14.addWidget(self.pushButton_10)


        self.verticalLayout_265.addWidget(self.widget_4)

        self.Personnel_widget_6 = QWidget(self.data_list_item)
        self.Personnel_widget_6.setObjectName(u"Personnel_widget_6")
        self.Personnel_widget_6.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_29 = QHBoxLayout(self.Personnel_widget_6)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_21 = QLabel(self.Personnel_widget_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setPixmap(QPixmap(u":/assets/icons/truck-weight-max-loading-30.png"))

        self.horizontalLayout_29.addWidget(self.label_21, 0, Qt.AlignLeft)

        self.pushButton_46 = QPushButton(self.Personnel_widget_6)
        self.pushButton_46.setObjectName(u"pushButton_46")
        sizePolicy2.setHeightForWidth(self.pushButton_46.sizePolicy().hasHeightForWidth())
        self.pushButton_46.setSizePolicy(sizePolicy2)
        self.pushButton_46.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_46.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_46.setIcon(icon9)
        self.pushButton_46.setIconSize(QSize(24, 24))
        self.pushButton_46.setCheckable(True)

        self.horizontalLayout_29.addWidget(self.pushButton_46)


        self.verticalLayout_265.addWidget(self.Personnel_widget_6)

        self.widget_29 = QWidget(self.data_list_item)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setStyleSheet(u"\n"
"QPushButton{\n"
"color:rgb(92, 124, 250);\n"
"border-top-left-radius:7px;\n"
"border-bottom-left-radius:7px;\n"
"border-top-right-radius:7px;\n"
"border-bottom-right-radius:7px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(203, 203, 203);\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.widget_29)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.nvFournisseur_btn = QPushButton(self.widget_29)
        self.nvFournisseur_btn.setObjectName(u"nvFournisseur_btn")
        self.nvFournisseur_btn.setIcon(icon12)

        self.verticalLayout_15.addWidget(self.nvFournisseur_btn)

        self.allFournisseur_btn = QPushButton(self.widget_29)
        self.allFournisseur_btn.setObjectName(u"allFournisseur_btn")
        self.allFournisseur_btn.setIcon(icon11)

        self.verticalLayout_15.addWidget(self.allFournisseur_btn)

        self.pushButton_45 = QPushButton(self.widget_29)
        self.pushButton_45.setObjectName(u"pushButton_45")

        self.verticalLayout_15.addWidget(self.pushButton_45)


        self.verticalLayout_265.addWidget(self.widget_29)

        self.Personnel_widget_9 = QWidget(self.data_list_item)
        self.Personnel_widget_9.setObjectName(u"Personnel_widget_9")
        self.Personnel_widget_9.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_299 = QHBoxLayout(self.Personnel_widget_9)
        self.horizontalLayout_299.setObjectName(u"horizontalLayout_299")
        self.label_162 = QLabel(self.Personnel_widget_9)
        self.label_162.setObjectName(u"label_162")
        self.label_162.setPixmap(QPixmap(u":/assets/icons/truck-weight-max-loading-30.png"))

        self.horizontalLayout_299.addWidget(self.label_162, 0, Qt.AlignLeft)

        self.pushButton_54 = QPushButton(self.Personnel_widget_9)
        self.pushButton_54.setObjectName(u"pushButton_54")
        sizePolicy2.setHeightForWidth(self.pushButton_54.sizePolicy().hasHeightForWidth())
        self.pushButton_54.setSizePolicy(sizePolicy2)
        self.pushButton_54.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_54.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_54.setIcon(icon9)
        self.pushButton_54.setIconSize(QSize(24, 24))
        self.pushButton_54.setCheckable(True)

        self.horizontalLayout_299.addWidget(self.pushButton_54)


        self.verticalLayout_265.addWidget(self.Personnel_widget_9)

        self.widget_481 = QWidget(self.data_list_item)
        self.widget_481.setObjectName(u"widget_481")
        self.widget_481.setStyleSheet(u"\n"
"QPushButton{\n"
"color:rgb(92, 124, 250);\n"
"border-top-left-radius:7px;\n"
"border-bottom-left-radius:7px;\n"
"border-top-right-radius:7px;\n"
"border-bottom-right-radius:7px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(203, 203, 203);\n"
"}")
        self.verticalLayout_30 = QVBoxLayout(self.widget_481)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.nvClient_btn = QPushButton(self.widget_481)
        self.nvClient_btn.setObjectName(u"nvClient_btn")
        self.nvClient_btn.setIcon(icon12)

        self.verticalLayout_30.addWidget(self.nvClient_btn)

        self.allFournisseur_btn_2 = QPushButton(self.widget_481)
        self.allFournisseur_btn_2.setObjectName(u"allFournisseur_btn_2")
        self.allFournisseur_btn_2.setIcon(icon11)

        self.verticalLayout_30.addWidget(self.allFournisseur_btn_2)


        self.verticalLayout_265.addWidget(self.widget_481)

        self.verticalSpacer_3 = QSpacerItem(20, 729, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_265.addItem(self.verticalSpacer_3)


        self.verticalLayout_11.addWidget(self.data_list_item)

        self.menu_stackedWidget.addWidget(self.data_page)
        self.autre_page = QWidget()
        self.autre_page.setObjectName(u"autre_page")
        self.verticalLayout_60 = QVBoxLayout(self.autre_page)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.autre_page)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFont(font1)
        self.frame_9.setStyleSheet(u"background-color: rgb(250, 248, 248);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_44.setSpacing(6)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.frame_9)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font2)
        self.label_28.setStyleSheet(u"color: rgb(92, 124, 250);")

        self.horizontalLayout_44.addWidget(self.label_28)

        self.pushButton_31 = QPushButton(self.frame_9)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setIcon(icon8)
        self.pushButton_31.setIconSize(QSize(24, 24))

        self.horizontalLayout_44.addWidget(self.pushButton_31, 0, Qt.AlignRight)


        self.verticalLayout_60.addWidget(self.frame_9)

        self.data_list_item_2 = QWidget(self.autre_page)
        self.data_list_item_2.setObjectName(u"data_list_item_2")
        sizePolicy1.setHeightForWidth(self.data_list_item_2.sizePolicy().hasHeightForWidth())
        self.data_list_item_2.setSizePolicy(sizePolicy1)
        self.data_list_item_2.setStyleSheet(u"background-color: rgb(236, 234, 234);\n"
"border-top-left-radius:10px;")
        self.verticalLayout_55 = QVBoxLayout(self.data_list_item_2)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.Equipement_widget_12 = QWidget(self.data_list_item_2)
        self.Equipement_widget_12.setObjectName(u"Equipement_widget_12")
        self.Equipement_widget_12.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_52 = QHBoxLayout(self.Equipement_widget_12)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_31 = QLabel(self.Equipement_widget_12)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setPixmap(QPixmap(u":/assets/icons/equippement-30.png"))

        self.horizontalLayout_52.addWidget(self.label_31, 0, Qt.AlignLeft)

        self.pushButton_33 = QPushButton(self.Equipement_widget_12)
        self.pushButton_33.setObjectName(u"pushButton_33")
        sizePolicy2.setHeightForWidth(self.pushButton_33.sizePolicy().hasHeightForWidth())
        self.pushButton_33.setSizePolicy(sizePolicy2)
        self.pushButton_33.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_33.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_33.setIcon(icon9)
        self.pushButton_33.setIconSize(QSize(24, 24))
        self.pushButton_33.setCheckable(True)

        self.horizontalLayout_52.addWidget(self.pushButton_33)


        self.verticalLayout_55.addWidget(self.Equipement_widget_12)

        self.widget_13 = QWidget(self.data_list_item_2)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setStyleSheet(u"\n"
"QPushButton{\n"
"color:rgb(92, 124, 250);\n"
"border-top-left-radius:7px;\n"
"border-bottom-left-radius:7px;\n"
"border-top-right-radius:7px;\n"
"border-bottom-right-radius:7px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(203, 203, 203);\n"
"}")
        self.verticalLayout_57 = QVBoxLayout(self.widget_13)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.mission_btn = QPushButton(self.widget_13)
        self.mission_btn.setObjectName(u"mission_btn")
        self.mission_btn.setIcon(icon12)

        self.verticalLayout_57.addWidget(self.mission_btn)

        self.allMissions_btn = QPushButton(self.widget_13)
        self.allMissions_btn.setObjectName(u"allMissions_btn")
        self.allMissions_btn.setIcon(icon11)

        self.verticalLayout_57.addWidget(self.allMissions_btn)

        self.searchMission_btn = QPushButton(self.widget_13)
        self.searchMission_btn.setObjectName(u"searchMission_btn")
        icon13 = QIcon()
        icon13.addFile(u":/assets/icons/search_30_active.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchMission_btn.setIcon(icon13)

        self.verticalLayout_57.addWidget(self.searchMission_btn)


        self.verticalLayout_55.addWidget(self.widget_13)

        self.Personnel_widget_7 = QWidget(self.data_list_item_2)
        self.Personnel_widget_7.setObjectName(u"Personnel_widget_7")
        self.Personnel_widget_7.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_63 = QHBoxLayout(self.Personnel_widget_7)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.label_32 = QLabel(self.Personnel_widget_7)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setPixmap(QPixmap(u":/assets/icons/employee-30.png"))

        self.horizontalLayout_63.addWidget(self.label_32, 0, Qt.AlignLeft)

        self.pushButton_60 = QPushButton(self.Personnel_widget_7)
        self.pushButton_60.setObjectName(u"pushButton_60")
        sizePolicy2.setHeightForWidth(self.pushButton_60.sizePolicy().hasHeightForWidth())
        self.pushButton_60.setSizePolicy(sizePolicy2)
        self.pushButton_60.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_60.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_60.setIcon(icon9)
        self.pushButton_60.setIconSize(QSize(24, 24))
        self.pushButton_60.setCheckable(True)

        self.horizontalLayout_63.addWidget(self.pushButton_60)


        self.verticalLayout_55.addWidget(self.Personnel_widget_7)

        self.widget_60 = QWidget(self.data_list_item_2)
        self.widget_60.setObjectName(u"widget_60")
        self.widget_60.setStyleSheet(u"\n"
"QPushButton{\n"
"color:rgb(92, 124, 250);\n"
"border-top-left-radius:7px;\n"
"border-bottom-left-radius:7px;\n"
"border-top-right-radius:7px;\n"
"border-bottom-right-radius:7px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(203, 203, 203);\n"
"}")
        self.verticalLayout_58 = QVBoxLayout(self.widget_60)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.bC_btn = QPushButton(self.widget_60)
        self.bC_btn.setObjectName(u"bC_btn")
        self.bC_btn.setStyleSheet(u"")
        self.bC_btn.setIcon(icon12)

        self.verticalLayout_58.addWidget(self.bC_btn)

        self.allBC_btn = QPushButton(self.widget_60)
        self.allBC_btn.setObjectName(u"allBC_btn")
        self.allBC_btn.setIcon(icon11)

        self.verticalLayout_58.addWidget(self.allBC_btn)


        self.verticalLayout_55.addWidget(self.widget_60)

        self.Personnel_widget_8 = QWidget(self.data_list_item_2)
        self.Personnel_widget_8.setObjectName(u"Personnel_widget_8")
        self.Personnel_widget_8.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_66 = QHBoxLayout(self.Personnel_widget_8)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.label_33 = QLabel(self.Personnel_widget_8)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setPixmap(QPixmap(u":/assets/icons/truck-weight-max-loading-30.png"))

        self.horizontalLayout_66.addWidget(self.label_33, 0, Qt.AlignLeft)

        self.pushButton_65 = QPushButton(self.Personnel_widget_8)
        self.pushButton_65.setObjectName(u"pushButton_65")
        sizePolicy2.setHeightForWidth(self.pushButton_65.sizePolicy().hasHeightForWidth())
        self.pushButton_65.setSizePolicy(sizePolicy2)
        self.pushButton_65.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_65.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_65.setIcon(icon9)
        self.pushButton_65.setIconSize(QSize(24, 24))
        self.pushButton_65.setCheckable(True)

        self.horizontalLayout_66.addWidget(self.pushButton_65)


        self.verticalLayout_55.addWidget(self.Personnel_widget_8)

        self.widget_61 = QWidget(self.data_list_item_2)
        self.widget_61.setObjectName(u"widget_61")
        self.widget_61.setStyleSheet(u"\n"
"QPushButton{\n"
"color:rgb(92, 124, 250);\n"
"border-top-left-radius:7px;\n"
"border-bottom-left-radius:7px;\n"
"border-top-right-radius:7px;\n"
"border-bottom-right-radius:7px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(203, 203, 203);\n"
"}")
        self.verticalLayout_59 = QVBoxLayout(self.widget_61)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.devis_btn = QPushButton(self.widget_61)
        self.devis_btn.setObjectName(u"devis_btn")
        self.devis_btn.setIcon(icon12)

        self.verticalLayout_59.addWidget(self.devis_btn)

        self.searchDevisbtn = QPushButton(self.widget_61)
        self.searchDevisbtn.setObjectName(u"searchDevisbtn")
        self.searchDevisbtn.setIcon(icon13)

        self.verticalLayout_59.addWidget(self.searchDevisbtn)


        self.verticalLayout_55.addWidget(self.widget_61)

        self.verticalSpacer_17 = QSpacerItem(20, 729, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_55.addItem(self.verticalSpacer_17)


        self.verticalLayout_60.addWidget(self.data_list_item_2)

        self.menu_stackedWidget.addWidget(self.autre_page)

        self.verticalLayout_10.addWidget(self.menu_stackedWidget)


        self.verticalLayout_9.addWidget(self.submenu_subContainer)


        self.gridLayout_13.addWidget(self.subMenu_container, 0, 2, 1, 1)

        self.main_body_container = QWidget(self.centralwidget)
        self.main_body_container.setObjectName(u"main_body_container")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.main_body_container.sizePolicy().hasHeightForWidth())
        self.main_body_container.setSizePolicy(sizePolicy3)
        self.main_body_container.setStyleSheet(u"background-color: #faf8f8;")
        self.verticalLayout_22 = QVBoxLayout(self.main_body_container)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.searchBar_container = QWidget(self.main_body_container)
        self.searchBar_container.setObjectName(u"searchBar_container")
        self.searchBar_container.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.horizontalLayout_15 = QHBoxLayout(self.searchBar_container)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(4, 2, 4, 8)
        self.widget_9 = QWidget(self.searchBar_container)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy3.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy3)
        self.horizontalLayout_13 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_13.setSpacing(4)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(10, 0, 0, 0)
        self.lineEdit = QLineEdit(self.widget_9)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:7px;\n"
"border-bottom-left-radius:7px;\n"
"padding-left: 10px;\n"
"padding-top:2px;\n"
"padding-bottom: 2px;")

        self.horizontalLayout_13.addWidget(self.lineEdit)

        self.comboBox_3 = QComboBox(self.widget_9)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        font3 = QFont()
        font3.setBold(True)
        self.comboBox_3.setFont(font3)
        self.comboBox_3.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding-top:2px;\n"
"\n"
"border-left-color: rgb(230, 230, 230);\n"
"color:rgb(92, 124, 250);")
        self.comboBox_3.setIconSize(QSize(16, 16))

        self.horizontalLayout_13.addWidget(self.comboBox_3)

        self.pushButton_39 = QPushButton(self.widget_9)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setStyleSheet(u"background-color: rgb(92, 124, 250);\n"
"border:none;\n"
"border-top-right-radius:7px;\n"
"border-bottom-right-radius:7px;\n"
"")
        icon14 = QIcon()
        icon14.addFile(u":/assets/icons/search_30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_39.setIcon(icon14)

        self.horizontalLayout_13.addWidget(self.pushButton_39)


        self.horizontalLayout_15.addWidget(self.widget_9)

        self.horizontalSpacer_9 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_9)

        self.widget_10 = QWidget(self.searchBar_container)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_10)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_10, 0, Qt.AlignLeft)

        self.label_11 = QLabel(self.widget_10)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(20, 20))
        self.label_11.setPixmap(QPixmap(u":/assets/icons/icons8-glyph-48.png"))
        self.label_11.setScaledContents(True)

        self.horizontalLayout_14.addWidget(self.label_11)

        self.pushButton_32 = QPushButton(self.widget_10)
        self.pushButton_32.setObjectName(u"pushButton_32")
        icon15 = QIcon()
        icon15.addFile(u":/assets/icons/menu-vertical-30_active.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_32.setIcon(icon15)
        self.pushButton_32.setIconSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.pushButton_32, 0, Qt.AlignRight)


        self.horizontalLayout_15.addWidget(self.widget_10, 0, Qt.AlignRight)


        self.verticalLayout_22.addWidget(self.searchBar_container)

        self.stackedWidget = QStackedWidget(self.main_body_container)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.gridLayout_25 = QGridLayout(self.home_page)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.widget_520 = QWidget(self.home_page)
        self.widget_520.setObjectName(u"widget_520")
        self.widget_520.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayout_304 = QHBoxLayout(self.widget_520)
        self.horizontalLayout_304.setObjectName(u"horizontalLayout_304")
        self.horizontalSpacer_332 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_304.addItem(self.horizontalSpacer_332)

        self.verticalLayout_279 = QVBoxLayout()
        self.verticalLayout_279.setObjectName(u"verticalLayout_279")
        self.verticalLayout_279.setContentsMargins(10, 10, 10, 10)
        self.verticalSpacer_101 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_279.addItem(self.verticalSpacer_101)

        self.label_164 = QLabel(self.widget_520)
        self.label_164.setObjectName(u"label_164")
        self.label_164.setPixmap(QPixmap(u":/assets/icons/output-onlinepngtools.png"))

        self.verticalLayout_279.addWidget(self.label_164)

        self.verticalSpacer_83 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_279.addItem(self.verticalSpacer_83)

        self.widget_522 = QWidget(self.widget_520)
        self.widget_522.setObjectName(u"widget_522")
        self.verticalLayout_278 = QVBoxLayout(self.widget_522)
        self.verticalLayout_278.setObjectName(u"verticalLayout_278")
        self.label_165 = QLabel(self.widget_522)
        self.label_165.setObjectName(u"label_165")
        self.label_165.setMinimumSize(QSize(0, 200))
        self.label_165.setStyleSheet(u"border-style: solid;\n"
"border-width:1px;\n"
"border-color: rgb(92, 124, 250);\n"
"border-radius:7px;")
        self.label_165.setAlignment(Qt.AlignCenter)

        self.verticalLayout_278.addWidget(self.label_165)

        self.verticalSpacer_82 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_278.addItem(self.verticalSpacer_82)

        self.widget_523 = QWidget(self.widget_522)
        self.widget_523.setObjectName(u"widget_523")
        self.horizontalLayout_303 = QHBoxLayout(self.widget_523)
        self.horizontalLayout_303.setObjectName(u"horizontalLayout_303")
        self.pushButton_173 = QPushButton(self.widget_523)
        self.pushButton_173.setObjectName(u"pushButton_173")
        self.pushButton_173.setMinimumSize(QSize(200, 40))
        self.pushButton_173.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:7px;\n"
"text-align:center;\n"
"}\n"
"")

        self.horizontalLayout_303.addWidget(self.pushButton_173)

        self.pushButton_172 = QPushButton(self.widget_523)
        self.pushButton_172.setObjectName(u"pushButton_172")
        self.pushButton_172.setMinimumSize(QSize(200, 40))
        self.pushButton_172.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:7px;\n"
"text-align:center;\n"
"}\n"
"")

        self.horizontalLayout_303.addWidget(self.pushButton_172)


        self.verticalLayout_278.addWidget(self.widget_523)


        self.verticalLayout_279.addWidget(self.widget_522)


        self.horizontalLayout_304.addLayout(self.verticalLayout_279)

        self.horizontalSpacer_330 = QSpacerItem(33, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_304.addItem(self.horizontalSpacer_330)

        self.verticalLayout_281 = QVBoxLayout()
        self.verticalLayout_281.setObjectName(u"verticalLayout_281")
        self.verticalSpacer_99 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_281.addItem(self.verticalSpacer_99)

        self.widget_524 = QWidget(self.widget_520)
        self.widget_524.setObjectName(u"widget_524")
        self.verticalLayout_280 = QVBoxLayout(self.widget_524)
        self.verticalLayout_280.setObjectName(u"verticalLayout_280")
        self.verticalSpacer_97 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_280.addItem(self.verticalSpacer_97)

        self.widget_521 = QWidget(self.widget_524)
        self.widget_521.setObjectName(u"widget_521")
        self.gridLayout_24 = QGridLayout(self.widget_521)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.pushButton_29 = QPushButton(self.widget_521)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setMinimumSize(QSize(120, 120))
        self.pushButton_29.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:7px;\n"
"text-align:center;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(194, 200, 250);\n"
"	color:rgb(92, 124, 250);\n"
"}")

        self.gridLayout_24.addWidget(self.pushButton_29, 0, 0, 1, 2)

        self.pushButton_146 = QPushButton(self.widget_521)
        self.pushButton_146.setObjectName(u"pushButton_146")
        self.pushButton_146.setMinimumSize(QSize(120, 140))
        self.pushButton_146.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:7px;\n"
"text-align:center;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(194, 200, 250);\n"
"	color:rgb(92, 124, 250);\n"
"}")

        self.gridLayout_24.addWidget(self.pushButton_146, 1, 0, 2, 4)

        self.pushButton_170 = QPushButton(self.widget_521)
        self.pushButton_170.setObjectName(u"pushButton_170")
        self.pushButton_170.setMinimumSize(QSize(120, 120))
        self.pushButton_170.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:7px;\n"
"text-align:center;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(194, 200, 250);\n"
"	color:rgb(92, 124, 250);\n"
"}")

        self.gridLayout_24.addWidget(self.pushButton_170, 3, 1, 1, 1)

        self.pushButton_171 = QPushButton(self.widget_521)
        self.pushButton_171.setObjectName(u"pushButton_171")
        self.pushButton_171.setMinimumSize(QSize(120, 120))
        self.pushButton_171.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:7px;\n"
"text-align:center;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(194, 200, 250);\n"
"	color:rgb(92, 124, 250);\n"
"}")

        self.gridLayout_24.addWidget(self.pushButton_171, 3, 3, 1, 1)

        self.pushButton_169 = QPushButton(self.widget_521)
        self.pushButton_169.setObjectName(u"pushButton_169")
        self.pushButton_169.setMinimumSize(QSize(120, 120))
        self.pushButton_169.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:7px;\n"
"text-align:center;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(194, 200, 250);\n"
"	color:rgb(92, 124, 250);\n"
"}")

        self.gridLayout_24.addWidget(self.pushButton_169, 4, 3, 1, 1)

        self.pushButton_30 = QPushButton(self.widget_521)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setMinimumSize(QSize(140, 120))
        self.pushButton_30.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:7px;\n"
"text-align:center;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(194, 200, 250);\n"
"	color:rgb(92, 124, 250);\n"
"}")

        self.gridLayout_24.addWidget(self.pushButton_30, 0, 2, 1, 2)


        self.verticalLayout_280.addWidget(self.widget_521)

        self.verticalSpacer_98 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_280.addItem(self.verticalSpacer_98)


        self.verticalLayout_281.addWidget(self.widget_524)

        self.verticalSpacer_100 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_281.addItem(self.verticalSpacer_100)


        self.horizontalLayout_304.addLayout(self.verticalLayout_281)

        self.horizontalSpacer_331 = QSpacerItem(32, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_304.addItem(self.horizontalSpacer_331)


        self.gridLayout_25.addWidget(self.widget_520, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.home_page)
        self.nv_dossier_prodEXT_page = QWidget()
        self.nv_dossier_prodEXT_page.setObjectName(u"nv_dossier_prodEXT_page")
        sizePolicy.setHeightForWidth(self.nv_dossier_prodEXT_page.sizePolicy().hasHeightForWidth())
        self.nv_dossier_prodEXT_page.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.nv_dossier_prodEXT_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(self.nv_dossier_prodEXT_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 964, 2584))
        self.verticalLayout_40 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.widget_11 = QWidget(self.scrollAreaWidgetContents)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_12 = QLabel(self.widget_11)
        self.label_12.setObjectName(u"label_12")
        font4 = QFont()
        font4.setFamilies([u"Palatino Linotype"])
        font4.setPointSize(12)
        self.label_12.setFont(font4)

        self.horizontalLayout_27.addWidget(self.label_12)

        self.horizontalSpacer_250 = QSpacerItem(355, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_250)

        self.label_13 = QLabel(self.widget_11)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_27.addWidget(self.label_13)

        self.horizontalSpacer_249 = QSpacerItem(354, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_249)

        self.label_133 = QLabel(self.widget_11)
        self.label_133.setObjectName(u"label_133")

        self.horizontalLayout_27.addWidget(self.label_133)


        self.verticalLayout_40.addWidget(self.widget_11)

        self.widget_34 = QWidget(self.scrollAreaWidgetContents)
        self.widget_34.setObjectName(u"widget_34")
        self.verticalLayout_32 = QVBoxLayout(self.widget_34)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.widget_35 = QWidget(self.widget_34)
        self.widget_35.setObjectName(u"widget_35")
        self.horizontalLayout_34 = QHBoxLayout(self.widget_35)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_5 = QWidget(self.widget_35)
        self.Equipement_widget_5.setObjectName(u"Equipement_widget_5")
        self.Equipement_widget_5.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_35 = QHBoxLayout(self.Equipement_widget_5)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_24 = QLabel(self.Equipement_widget_5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setPixmap(QPixmap(u":/assets/icons/employee-30.png"))

        self.horizontalLayout_35.addWidget(self.label_24, 0, Qt.AlignLeft)

        self.pushButton_49 = QPushButton(self.Equipement_widget_5)
        self.pushButton_49.setObjectName(u"pushButton_49")
        sizePolicy2.setHeightForWidth(self.pushButton_49.sizePolicy().hasHeightForWidth())
        self.pushButton_49.setSizePolicy(sizePolicy2)
        self.pushButton_49.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_49.setStyleSheet(u"")
        self.pushButton_49.setIconSize(QSize(24, 24))
        self.pushButton_49.setCheckable(True)

        self.horizontalLayout_35.addWidget(self.pushButton_49)


        self.horizontalLayout_34.addWidget(self.Equipement_widget_5)

        self.horizontalSpacer_18 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_18)


        self.verticalLayout_32.addWidget(self.widget_35)

        self.widget_36 = QWidget(self.widget_34)
        self.widget_36.setObjectName(u"widget_36")
        self.widget_36.setMinimumSize(QSize(0, 0))
        self.widget_36.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.verticalLayout_291 = QVBoxLayout(self.widget_36)
        self.verticalLayout_291.setObjectName(u"verticalLayout_291")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalSpacer_23 = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_23)

        self.widget_37 = QWidget(self.widget_36)
        self.widget_37.setObjectName(u"widget_37")
        sizePolicy.setHeightForWidth(self.widget_37.sizePolicy().hasHeightForWidth())
        self.widget_37.setSizePolicy(sizePolicy)
        self.widget_37.setMinimumSize(QSize(0, 0))
        self.verticalLayout_35 = QVBoxLayout(self.widget_37)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.textEdit_4 = QTextEdit(self.widget_37)
        self.textEdit_4.setObjectName(u"textEdit_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.textEdit_4.sizePolicy().hasHeightForWidth())
        self.textEdit_4.setSizePolicy(sizePolicy4)
        self.textEdit_4.setMinimumSize(QSize(0, 0))
        self.textEdit_4.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_35.addWidget(self.textEdit_4)

        self.textEdit_5 = QTextEdit(self.widget_37)
        self.textEdit_5.setObjectName(u"textEdit_5")
        sizePolicy4.setHeightForWidth(self.textEdit_5.sizePolicy().hasHeightForWidth())
        self.textEdit_5.setSizePolicy(sizePolicy4)
        self.textEdit_5.setMinimumSize(QSize(0, 0))
        self.textEdit_5.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_35.addWidget(self.textEdit_5)

        self.widget_41 = QWidget(self.widget_37)
        self.widget_41.setObjectName(u"widget_41")
        self.verticalLayout_33 = QVBoxLayout(self.widget_41)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.checkBox_ext = QCheckBox(self.widget_41)
        self.checkBox_ext.setObjectName(u"checkBox_ext")
        self.checkBox_ext.setChecked(True)

        self.verticalLayout_33.addWidget(self.checkBox_ext)

        self.checkBox_2 = QCheckBox(self.widget_41)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_33.addWidget(self.checkBox_2)


        self.verticalLayout_35.addWidget(self.widget_41)

        self.widget_38 = QWidget(self.widget_37)
        self.widget_38.setObjectName(u"widget_38")
        self.horizontalLayout_36 = QHBoxLayout(self.widget_38)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.dateEdit_3 = QDateEdit(self.widget_38)
        self.dateEdit_3.setObjectName(u"dateEdit_3")
        self.dateEdit_3.setDateTime(QDateTime(QDate(2024, 10, 31), QTime(17, 0, 0)))
        self.dateEdit_3.setCalendarPopup(True)

        self.horizontalLayout_36.addWidget(self.dateEdit_3)

        self.horizontalSpacer_19 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_19)


        self.verticalLayout_35.addWidget(self.widget_38)


        self.horizontalLayout_28.addWidget(self.widget_37)

        self.horizontalSpacer_20 = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_20)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_24)

        self.widget_39 = QWidget(self.widget_36)
        self.widget_39.setObjectName(u"widget_39")
        self.widget_39.setMinimumSize(QSize(0, 0))
        self.widget_39.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_36 = QVBoxLayout(self.widget_39)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.textEdit_6 = QTextEdit(self.widget_39)
        self.textEdit_6.setObjectName(u"textEdit_6")
        sizePolicy4.setHeightForWidth(self.textEdit_6.sizePolicy().hasHeightForWidth())
        self.textEdit_6.setSizePolicy(sizePolicy4)
        self.textEdit_6.setMinimumSize(QSize(0, 0))
        self.textEdit_6.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_36.addWidget(self.textEdit_6)

        self.widget_42 = QWidget(self.widget_39)
        self.widget_42.setObjectName(u"widget_42")
        self.verticalLayout_34 = QVBoxLayout(self.widget_42)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.checkBox_3 = QCheckBox(self.widget_42)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setChecked(True)

        self.verticalLayout_34.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.widget_42)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout_34.addWidget(self.checkBox_4)


        self.verticalLayout_36.addWidget(self.widget_42)

        self.widget_43 = QWidget(self.widget_39)
        self.widget_43.setObjectName(u"widget_43")
        self.horizontalLayout_38 = QHBoxLayout(self.widget_43)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_14 = QLabel(self.widget_43)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.label_14)

        self.timeEdit_2 = QTimeEdit(self.widget_43)
        self.timeEdit_2.setObjectName(u"timeEdit_2")

        self.horizontalLayout_38.addWidget(self.timeEdit_2)


        self.verticalLayout_36.addWidget(self.widget_43)


        self.horizontalLayout_28.addWidget(self.widget_39)

        self.horizontalSpacer_22 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_22)


        self.verticalLayout_291.addLayout(self.horizontalLayout_28)

        self.widget_40 = QWidget(self.widget_36)
        self.widget_40.setObjectName(u"widget_40")
        self.horizontalLayout_37 = QHBoxLayout(self.widget_40)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.widget_warning_14 = QWidget(self.widget_40)
        self.widget_warning_14.setObjectName(u"widget_warning_14")
        self.widget_warning_14.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_342 = QHBoxLayout(self.widget_warning_14)
        self.horizontalLayout_342.setSpacing(0)
        self.horizontalLayout_342.setObjectName(u"horizontalLayout_342")
        self.horizontalLayout_342.setContentsMargins(10, 5, 5, 5)
        self.label_219 = QLabel(self.widget_warning_14)
        self.label_219.setObjectName(u"label_219")
        self.label_219.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_342.addWidget(self.label_219)

        self.label_314 = QLabel(self.widget_warning_14)
        self.label_314.setObjectName(u"label_314")
        self.label_314.setMinimumSize(QSize(150, 0))
        self.label_314.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_314.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_342.addWidget(self.label_314)


        self.horizontalLayout_37.addWidget(self.widget_warning_14)

        self.horizontalSpacer_21 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_21)

        self.pushButton_41 = QPushButton(self.widget_40)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_41.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_37.addWidget(self.pushButton_41)


        self.verticalLayout_291.addWidget(self.widget_40)


        self.verticalLayout_32.addWidget(self.widget_36)


        self.verticalLayout_40.addWidget(self.widget_34)

        self.widget_44 = QWidget(self.scrollAreaWidgetContents)
        self.widget_44.setObjectName(u"widget_44")
        self.verticalLayout_37 = QVBoxLayout(self.widget_44)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.widget_45 = QWidget(self.widget_44)
        self.widget_45.setObjectName(u"widget_45")
        self.horizontalLayout_39 = QHBoxLayout(self.widget_45)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_6 = QWidget(self.widget_45)
        self.Equipement_widget_6.setObjectName(u"Equipement_widget_6")
        self.Equipement_widget_6.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_40 = QHBoxLayout(self.Equipement_widget_6)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_25 = QLabel(self.Equipement_widget_6)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setPixmap(QPixmap(u":/assets/icons/employee-30.png"))

        self.horizontalLayout_40.addWidget(self.label_25, 0, Qt.AlignLeft)

        self.pushButton_50 = QPushButton(self.Equipement_widget_6)
        self.pushButton_50.setObjectName(u"pushButton_50")
        sizePolicy2.setHeightForWidth(self.pushButton_50.sizePolicy().hasHeightForWidth())
        self.pushButton_50.setSizePolicy(sizePolicy2)
        self.pushButton_50.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_50.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_50.setIcon(icon9)
        self.pushButton_50.setIconSize(QSize(24, 24))
        self.pushButton_50.setCheckable(True)

        self.horizontalLayout_40.addWidget(self.pushButton_50)


        self.horizontalLayout_39.addWidget(self.Equipement_widget_6)

        self.horizontalSpacer_25 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_25)


        self.verticalLayout_37.addWidget(self.widget_45)

        self.widget_46 = QWidget(self.widget_44)
        self.widget_46.setObjectName(u"widget_46")
        self.widget_46.setMinimumSize(QSize(450, 0))
        self.widget_46.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.verticalLayout_292 = QVBoxLayout(self.widget_46)
        self.verticalLayout_292.setObjectName(u"verticalLayout_292")
        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.widget_70 = QWidget(self.widget_46)
        self.widget_70.setObjectName(u"widget_70")
        self.verticalLayout_51 = QVBoxLayout(self.widget_70)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.textEdit_12 = QTextEdit(self.widget_70)
        self.textEdit_12.setObjectName(u"textEdit_12")
        sizePolicy4.setHeightForWidth(self.textEdit_12.sizePolicy().hasHeightForWidth())
        self.textEdit_12.setSizePolicy(sizePolicy4)
        self.textEdit_12.setMinimumSize(QSize(0, 0))
        self.textEdit_12.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_51.addWidget(self.textEdit_12)

        self.verticalSpacer_5 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_51.addItem(self.verticalSpacer_5)


        self.horizontalLayout_41.addWidget(self.widget_70)

        self.widget_49 = QWidget(self.widget_46)
        self.widget_49.setObjectName(u"widget_49")
        self.widget_49.setMinimumSize(QSize(400, 0))
        self.verticalLayout_39 = QVBoxLayout(self.widget_49)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(4, 4, 4, 4)
        self.textEdit_7 = QTextEdit(self.widget_49)
        self.textEdit_7.setObjectName(u"textEdit_7")
        sizePolicy4.setHeightForWidth(self.textEdit_7.sizePolicy().hasHeightForWidth())
        self.textEdit_7.setSizePolicy(sizePolicy4)
        self.textEdit_7.setMinimumSize(QSize(0, 0))
        self.textEdit_7.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_39.addWidget(self.textEdit_7)

        self.plainTextEdit_8 = QPlainTextEdit(self.widget_49)
        self.plainTextEdit_8.setObjectName(u"plainTextEdit_8")
        self.plainTextEdit_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_39.addWidget(self.plainTextEdit_8)


        self.horizontalLayout_41.addWidget(self.widget_49)

        self.horizontalSpacer_29 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_29)


        self.verticalLayout_292.addLayout(self.horizontalLayout_41)

        self.widget_427 = QWidget(self.widget_46)
        self.widget_427.setObjectName(u"widget_427")
        self.horizontalLayout_55 = QHBoxLayout(self.widget_427)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.widget_warning_15 = QWidget(self.widget_427)
        self.widget_warning_15.setObjectName(u"widget_warning_15")
        self.widget_warning_15.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_373 = QHBoxLayout(self.widget_warning_15)
        self.horizontalLayout_373.setSpacing(0)
        self.horizontalLayout_373.setObjectName(u"horizontalLayout_373")
        self.horizontalLayout_373.setContentsMargins(10, 5, 5, 5)
        self.label_229 = QLabel(self.widget_warning_15)
        self.label_229.setObjectName(u"label_229")
        self.label_229.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_373.addWidget(self.label_229)

        self.label_315 = QLabel(self.widget_warning_15)
        self.label_315.setObjectName(u"label_315")
        self.label_315.setMinimumSize(QSize(150, 0))
        self.label_315.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_315.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_373.addWidget(self.label_315)


        self.horizontalLayout_55.addWidget(self.widget_warning_15)

        self.horizontalSpacer_261 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_261)

        self.pushButton_43 = QPushButton(self.widget_427)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_43.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_55.addWidget(self.pushButton_43)


        self.verticalLayout_292.addWidget(self.widget_427)


        self.verticalLayout_37.addWidget(self.widget_46)


        self.verticalLayout_40.addWidget(self.widget_44)

        self.widget_32 = QWidget(self.scrollAreaWidgetContents)
        self.widget_32.setObjectName(u"widget_32")
        self.verticalLayout_31 = QVBoxLayout(self.widget_32)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.widget_17 = QWidget(self.widget_32)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_32 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_4 = QWidget(self.widget_17)
        self.Equipement_widget_4.setObjectName(u"Equipement_widget_4")
        self.Equipement_widget_4.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_33 = QHBoxLayout(self.Equipement_widget_4)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_23 = QLabel(self.Equipement_widget_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setPixmap(QPixmap(u":/assets/icons/employee-30.png"))

        self.horizontalLayout_33.addWidget(self.label_23, 0, Qt.AlignLeft)

        self.pushButton_48 = QPushButton(self.Equipement_widget_4)
        self.pushButton_48.setObjectName(u"pushButton_48")
        sizePolicy2.setHeightForWidth(self.pushButton_48.sizePolicy().hasHeightForWidth())
        self.pushButton_48.setSizePolicy(sizePolicy2)
        self.pushButton_48.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_48.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_48.setIcon(icon9)
        self.pushButton_48.setIconSize(QSize(24, 24))
        self.pushButton_48.setCheckable(True)

        self.horizontalLayout_33.addWidget(self.pushButton_48)


        self.horizontalLayout_32.addWidget(self.Equipement_widget_4)

        self.horizontalSpacer_14 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_14)


        self.verticalLayout_31.addWidget(self.widget_17)

        self.widget_33 = QWidget(self.widget_32)
        self.widget_33.setObjectName(u"widget_33")
        self.widget_33.setMinimumSize(QSize(450, 0))
        self.widget_33.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.verticalLayout_293 = QVBoxLayout(self.widget_33)
        self.verticalLayout_293.setObjectName(u"verticalLayout_293")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.widget_18 = QWidget(self.widget_33)
        self.widget_18.setObjectName(u"widget_18")
        sizePolicy.setHeightForWidth(self.widget_18.sizePolicy().hasHeightForWidth())
        self.widget_18.setSizePolicy(sizePolicy)
        self.widget_18.setMinimumSize(QSize(0, 0))
        self.verticalLayout_25 = QVBoxLayout(self.widget_18)
        self.verticalLayout_25.setSpacing(10)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(4, 4, 4, 4)
        self.textEdit_3 = QTextEdit(self.widget_18)
        self.textEdit_3.setObjectName(u"textEdit_3")
        sizePolicy4.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        self.textEdit_3.setSizePolicy(sizePolicy4)
        self.textEdit_3.setMinimumSize(QSize(0, 0))
        self.textEdit_3.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_25.addWidget(self.textEdit_3)

        self.comboBox_personel = QComboBox(self.widget_18)
        self.comboBox_personel.setObjectName(u"comboBox_personel")
        self.comboBox_personel.setMinimumSize(QSize(400, 0))
        self.comboBox_personel.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_25.addWidget(self.comboBox_personel)

        self.widget_19 = QWidget(self.widget_18)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_15 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_15)

        self.pushButton_35 = QPushButton(self.widget_19)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")
        self.pushButton_35.setCheckable(True)

        self.horizontalLayout_20.addWidget(self.pushButton_35)


        self.verticalLayout_25.addWidget(self.widget_19)

        self.verticalSpacer_7 = QSpacerItem(20, 148, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_7)


        self.horizontalLayout_19.addWidget(self.widget_18)

        self.horizontalSpacer_6 = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_6)

        self.widget_20 = QWidget(self.widget_33)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMinimumSize(QSize(400, 0))
        self.verticalLayout_26 = QVBoxLayout(self.widget_20)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(4, 4, 4, 4)
        self.listWidget_2 = QListWidget(self.widget_20)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setMinimumSize(QSize(500, 0))
        self.listWidget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_26.addWidget(self.listWidget_2)

        self.widget_21 = QWidget(self.widget_20)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.pushButton_36 = QPushButton(self.widget_21)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_36.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")
        self.pushButton_36.setCheckable(True)

        self.horizontalLayout_21.addWidget(self.pushButton_36)

        self.horizontalSpacer_16 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_16)


        self.verticalLayout_26.addWidget(self.widget_21)


        self.horizontalLayout_19.addWidget(self.widget_20)

        self.horizontalSpacer_17 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_17)


        self.verticalLayout_293.addLayout(self.horizontalLayout_19)

        self.widget_484 = QWidget(self.widget_33)
        self.widget_484.setObjectName(u"widget_484")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_484)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.widget_warning_13 = QWidget(self.widget_484)
        self.widget_warning_13.setObjectName(u"widget_warning_13")
        self.widget_warning_13.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_341 = QHBoxLayout(self.widget_warning_13)
        self.horizontalLayout_341.setSpacing(0)
        self.horizontalLayout_341.setObjectName(u"horizontalLayout_341")
        self.horizontalLayout_341.setContentsMargins(10, 5, 5, 5)
        self.label_207 = QLabel(self.widget_warning_13)
        self.label_207.setObjectName(u"label_207")
        self.label_207.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_341.addWidget(self.label_207)

        self.label_313 = QLabel(self.widget_warning_13)
        self.label_313.setObjectName(u"label_313")
        self.label_313.setMinimumSize(QSize(150, 0))
        self.label_313.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_313.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_341.addWidget(self.label_313)


        self.horizontalLayout_24.addWidget(self.widget_warning_13)

        self.horizontalSpacer_263 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_263)

        self.pushButton_44 = QPushButton(self.widget_484)
        self.pushButton_44.setObjectName(u"pushButton_44")
        self.pushButton_44.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_44.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_24.addWidget(self.pushButton_44)


        self.verticalLayout_293.addWidget(self.widget_484)


        self.verticalLayout_31.addWidget(self.widget_33)


        self.verticalLayout_40.addWidget(self.widget_32)

        self.widget_53 = QWidget(self.scrollAreaWidgetContents)
        self.widget_53.setObjectName(u"widget_53")
        self.verticalLayout_46 = QVBoxLayout(self.widget_53)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.widget_62 = QWidget(self.widget_53)
        self.widget_62.setObjectName(u"widget_62")
        self.widget_62.setStyleSheet(u"")
        self.horizontalLayout_53 = QHBoxLayout(self.widget_62)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_10 = QWidget(self.widget_62)
        self.Equipement_widget_10.setObjectName(u"Equipement_widget_10")
        self.Equipement_widget_10.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_54 = QHBoxLayout(self.Equipement_widget_10)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_29 = QLabel(self.Equipement_widget_10)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setPixmap(QPixmap(u":/assets/icons/equippement-30.png"))

        self.horizontalLayout_54.addWidget(self.label_29, 0, Qt.AlignLeft)

        self.pushButton_55 = QPushButton(self.Equipement_widget_10)
        self.pushButton_55.setObjectName(u"pushButton_55")
        sizePolicy2.setHeightForWidth(self.pushButton_55.sizePolicy().hasHeightForWidth())
        self.pushButton_55.setSizePolicy(sizePolicy2)
        self.pushButton_55.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_55.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_55.setIcon(icon9)
        self.pushButton_55.setIconSize(QSize(24, 24))
        self.pushButton_55.setCheckable(True)

        self.horizontalLayout_54.addWidget(self.pushButton_55)


        self.horizontalLayout_53.addWidget(self.Equipement_widget_10)

        self.horizontalSpacer_38 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_38)


        self.verticalLayout_46.addWidget(self.widget_62)

        self.widget_63 = QWidget(self.widget_53)
        self.widget_63.setObjectName(u"widget_63")
        self.widget_63.setMinimumSize(QSize(450, 0))
        self.widget_63.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.verticalLayout_294 = QVBoxLayout(self.widget_63)
        self.verticalLayout_294.setObjectName(u"verticalLayout_294")
        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.widget_64 = QWidget(self.widget_63)
        self.widget_64.setObjectName(u"widget_64")
        sizePolicy.setHeightForWidth(self.widget_64.sizePolicy().hasHeightForWidth())
        self.widget_64.setSizePolicy(sizePolicy)
        self.widget_64.setMinimumSize(QSize(0, 0))
        self.verticalLayout_47 = QVBoxLayout(self.widget_64)
        self.verticalLayout_47.setSpacing(10)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(4, 4, 4, 4)
        self.textEdit_11 = QTextEdit(self.widget_64)
        self.textEdit_11.setObjectName(u"textEdit_11")
        sizePolicy4.setHeightForWidth(self.textEdit_11.sizePolicy().hasHeightForWidth())
        self.textEdit_11.setSizePolicy(sizePolicy4)
        self.textEdit_11.setMinimumSize(QSize(0, 0))
        self.textEdit_11.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_47.addWidget(self.textEdit_11)

        self.comboBox_6 = QComboBox(self.widget_64)
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setMinimumSize(QSize(400, 0))
        self.comboBox_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_47.addWidget(self.comboBox_6)

        self.widget_65 = QWidget(self.widget_64)
        self.widget_65.setObjectName(u"widget_65")
        self.horizontalLayout_56 = QHBoxLayout(self.widget_65)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalSpacer_39 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_56.addItem(self.horizontalSpacer_39)

        self.pushButton_56 = QPushButton(self.widget_65)
        self.pushButton_56.setObjectName(u"pushButton_56")
        self.pushButton_56.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")
        self.pushButton_56.setCheckable(True)

        self.horizontalLayout_56.addWidget(self.pushButton_56)


        self.verticalLayout_47.addWidget(self.widget_65)

        self.verticalSpacer_10 = QSpacerItem(20, 148, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_47.addItem(self.verticalSpacer_10)


        self.horizontalLayout_43.addWidget(self.widget_64)

        self.horizontalSpacer_40 = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_40)

        self.widget_66 = QWidget(self.widget_63)
        self.widget_66.setObjectName(u"widget_66")
        self.widget_66.setMinimumSize(QSize(400, 0))
        self.verticalLayout_48 = QVBoxLayout(self.widget_66)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(4, 4, 4, 4)
        self.listWidget_5 = QListWidget(self.widget_66)
        self.listWidget_5.setObjectName(u"listWidget_5")
        self.listWidget_5.setMinimumSize(QSize(500, 0))
        self.listWidget_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_48.addWidget(self.listWidget_5)

        self.widget_67 = QWidget(self.widget_66)
        self.widget_67.setObjectName(u"widget_67")
        self.horizontalLayout_57 = QHBoxLayout(self.widget_67)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.pushButton_57 = QPushButton(self.widget_67)
        self.pushButton_57.setObjectName(u"pushButton_57")
        self.pushButton_57.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_57.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_57.addWidget(self.pushButton_57)

        self.horizontalSpacer_41 = QSpacerItem(361, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_41)


        self.verticalLayout_48.addWidget(self.widget_67)


        self.horizontalLayout_43.addWidget(self.widget_66)

        self.horizontalSpacer_42 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_42)


        self.verticalLayout_294.addLayout(self.horizontalLayout_43)

        self.widget_485 = QWidget(self.widget_63)
        self.widget_485.setObjectName(u"widget_485")
        self.horizontalLayout_315 = QHBoxLayout(self.widget_485)
        self.horizontalLayout_315.setObjectName(u"horizontalLayout_315")
        self.widget_warning_18 = QWidget(self.widget_485)
        self.widget_warning_18.setObjectName(u"widget_warning_18")
        self.widget_warning_18.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_379 = QHBoxLayout(self.widget_warning_18)
        self.horizontalLayout_379.setSpacing(0)
        self.horizontalLayout_379.setObjectName(u"horizontalLayout_379")
        self.horizontalLayout_379.setContentsMargins(10, 5, 5, 5)
        self.label_232 = QLabel(self.widget_warning_18)
        self.label_232.setObjectName(u"label_232")
        self.label_232.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_379.addWidget(self.label_232)

        self.label_318 = QLabel(self.widget_warning_18)
        self.label_318.setObjectName(u"label_318")
        self.label_318.setMinimumSize(QSize(150, 0))
        self.label_318.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_318.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_379.addWidget(self.label_318)


        self.horizontalLayout_315.addWidget(self.widget_warning_18)

        self.horizontalSpacer_319 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_315.addItem(self.horizontalSpacer_319)

        self.pushButton_62 = QPushButton(self.widget_485)
        self.pushButton_62.setObjectName(u"pushButton_62")
        self.pushButton_62.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_62.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_315.addWidget(self.pushButton_62)


        self.verticalLayout_294.addWidget(self.widget_485)


        self.verticalLayout_46.addWidget(self.widget_63)

        self.widget_68 = QWidget(self.widget_53)
        self.widget_68.setObjectName(u"widget_68")
        self.widget_68.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_49 = QVBoxLayout(self.widget_68)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.widget_69 = QWidget(self.widget_68)
        self.widget_69.setObjectName(u"widget_69")
        self.horizontalLayout_58 = QHBoxLayout(self.widget_69)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_49.addWidget(self.widget_69)


        self.verticalLayout_46.addWidget(self.widget_68)


        self.verticalLayout_40.addWidget(self.widget_53)

        self.widget_71 = QWidget(self.scrollAreaWidgetContents)
        self.widget_71.setObjectName(u"widget_71")
        self.verticalLayout_50 = QVBoxLayout(self.widget_71)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.widget_72 = QWidget(self.widget_71)
        self.widget_72.setObjectName(u"widget_72")
        self.widget_72.setStyleSheet(u"")
        self.horizontalLayout_59 = QHBoxLayout(self.widget_72)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_11 = QWidget(self.widget_72)
        self.Equipement_widget_11.setObjectName(u"Equipement_widget_11")
        self.Equipement_widget_11.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_60 = QHBoxLayout(self.Equipement_widget_11)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_30 = QLabel(self.Equipement_widget_11)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setPixmap(QPixmap(u":/assets/icons/equippement-30.png"))

        self.horizontalLayout_60.addWidget(self.label_30, 0, Qt.AlignLeft)

        self.pushButton_58 = QPushButton(self.Equipement_widget_11)
        self.pushButton_58.setObjectName(u"pushButton_58")
        sizePolicy2.setHeightForWidth(self.pushButton_58.sizePolicy().hasHeightForWidth())
        self.pushButton_58.setSizePolicy(sizePolicy2)
        self.pushButton_58.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_58.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_58.setIcon(icon9)
        self.pushButton_58.setIconSize(QSize(24, 24))
        self.pushButton_58.setCheckable(True)

        self.horizontalLayout_60.addWidget(self.pushButton_58)


        self.horizontalLayout_59.addWidget(self.Equipement_widget_11)

        self.horizontalSpacer_43 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_43)


        self.verticalLayout_50.addWidget(self.widget_72)

        self.widget_73 = QWidget(self.widget_71)
        self.widget_73.setObjectName(u"widget_73")
        self.widget_73.setMinimumSize(QSize(450, 0))
        self.widget_73.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.horizontalLayout_61 = QHBoxLayout(self.widget_73)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(10, 10, 10, 10)
        self.widget_74 = QWidget(self.widget_73)
        self.widget_74.setObjectName(u"widget_74")
        sizePolicy.setHeightForWidth(self.widget_74.sizePolicy().hasHeightForWidth())
        self.widget_74.setSizePolicy(sizePolicy)
        self.widget_74.setMinimumSize(QSize(400, 0))
        self.verticalLayout_319 = QVBoxLayout(self.widget_74)
        self.verticalLayout_319.setObjectName(u"verticalLayout_319")
        self.horizontalLayout_431 = QHBoxLayout()
        self.horizontalLayout_431.setObjectName(u"horizontalLayout_431")
        self.textEdit_13 = QTextEdit(self.widget_74)
        self.textEdit_13.setObjectName(u"textEdit_13")
        sizePolicy4.setHeightForWidth(self.textEdit_13.sizePolicy().hasHeightForWidth())
        self.textEdit_13.setSizePolicy(sizePolicy4)
        self.textEdit_13.setMinimumSize(QSize(0, 0))
        self.textEdit_13.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_431.addWidget(self.textEdit_13)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_431.addItem(self.horizontalSpacer_13)

        self.label_44 = QLabel(self.widget_74)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_431.addWidget(self.label_44)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_431.addItem(self.horizontalSpacer_31)

        self.widget_14 = QWidget(self.widget_74)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_42 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalSpacer = QSpacerItem(119, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer)

        self.label_15 = QLabel(self.widget_14)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_42.addWidget(self.label_15)


        self.horizontalLayout_431.addWidget(self.widget_14)


        self.verticalLayout_319.addLayout(self.horizontalLayout_431)

        self.widget_54 = QWidget(self.widget_74)
        self.widget_54.setObjectName(u"widget_54")
        sizePolicy3.setHeightForWidth(self.widget_54.sizePolicy().hasHeightForWidth())
        self.widget_54.setSizePolicy(sizePolicy3)
        self.widget_54.setMinimumSize(QSize(300, 0))
        self.verticalLayout_42 = QVBoxLayout(self.widget_54)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_16 = QLabel(self.widget_54)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_42.addWidget(self.label_16)

        self.verticalSpacer_9 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_42.addItem(self.verticalSpacer_9)

        self.comboBox_5 = QComboBox(self.widget_54)
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_42.addWidget(self.comboBox_5)


        self.verticalLayout_319.addWidget(self.widget_54)

        self.widget_76 = QWidget(self.widget_74)
        self.widget_76.setObjectName(u"widget_76")
        self.verticalLayout_52 = QVBoxLayout(self.widget_76)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_3 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_3)

        self.widget_55 = QWidget(self.widget_76)
        self.widget_55.setObjectName(u"widget_55")
        self.verticalLayout_43 = QVBoxLayout(self.widget_55)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_17 = QLabel(self.widget_55)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_43.addWidget(self.label_17)

        self.verticalSpacer_12 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_43.addItem(self.verticalSpacer_12)

        self.lineEdit_4 = QLineEdit(self.widget_55)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_43.addWidget(self.lineEdit_4)


        self.horizontalLayout_17.addWidget(self.widget_55)

        self.horizontalSpacer_4 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_4)

        self.widget_56 = QWidget(self.widget_76)
        self.widget_56.setObjectName(u"widget_56")
        self.verticalLayout_44 = QVBoxLayout(self.widget_56)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.label_18 = QLabel(self.widget_56)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_44.addWidget(self.label_18)

        self.verticalSpacer_13 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_44.addItem(self.verticalSpacer_13)

        self.lineEdit_5 = QLineEdit(self.widget_56)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_44.addWidget(self.lineEdit_5)


        self.horizontalLayout_17.addWidget(self.widget_56)

        self.horizontalSpacer_8 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_8)

        self.widget_57 = QWidget(self.widget_76)
        self.widget_57.setObjectName(u"widget_57")
        self.verticalLayout_45 = QVBoxLayout(self.widget_57)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_19 = QLabel(self.widget_57)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_45.addWidget(self.label_19)

        self.verticalSpacer_14 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_45.addItem(self.verticalSpacer_14)

        self.lineEdit_6 = QLineEdit(self.widget_57)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_45.addWidget(self.lineEdit_6)


        self.horizontalLayout_17.addWidget(self.widget_57)

        self.horizontalSpacer_26 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_26)

        self.widget_58 = QWidget(self.widget_76)
        self.widget_58.setObjectName(u"widget_58")
        self.verticalLayout_53 = QVBoxLayout(self.widget_58)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.label_20 = QLabel(self.widget_58)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_53.addWidget(self.label_20)

        self.verticalSpacer_15 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_53.addItem(self.verticalSpacer_15)

        self.lineEdit_7 = QLineEdit(self.widget_58)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_53.addWidget(self.lineEdit_7)


        self.horizontalLayout_17.addWidget(self.widget_58)

        self.horizontalSpacer_27 = QSpacerItem(11, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_27)

        self.widget_59 = QWidget(self.widget_76)
        self.widget_59.setObjectName(u"widget_59")
        self.verticalLayout_56 = QVBoxLayout(self.widget_59)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.label_26 = QLabel(self.widget_59)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setLayoutDirection(Qt.LeftToRight)
        self.label_26.setAlignment(Qt.AlignCenter)

        self.verticalLayout_56.addWidget(self.label_26)

        self.verticalSpacer_16 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_56.addItem(self.verticalSpacer_16)

        self.lineEdit_8 = QLineEdit(self.widget_59)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_56.addWidget(self.lineEdit_8)


        self.horizontalLayout_17.addWidget(self.widget_59)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_2)


        self.verticalLayout_52.addLayout(self.horizontalLayout_17)

        self.widget_157 = QWidget(self.widget_76)
        self.widget_157.setObjectName(u"widget_157")
        self.horizontalLayout_430 = QHBoxLayout(self.widget_157)
        self.horizontalLayout_430.setObjectName(u"horizontalLayout_430")
        self.horizontalSpacer_98 = QSpacerItem(594, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_430.addItem(self.horizontalSpacer_98)

        self.pushButton_63 = QPushButton(self.widget_157)
        self.pushButton_63.setObjectName(u"pushButton_63")
        self.pushButton_63.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_430.addWidget(self.pushButton_63)

        self.horizontalSpacer_97 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_430.addItem(self.horizontalSpacer_97)


        self.verticalLayout_52.addWidget(self.widget_157)


        self.verticalLayout_319.addWidget(self.widget_76)

        self.widget_75 = QWidget(self.widget_74)
        self.widget_75.setObjectName(u"widget_75")
        self.horizontalLayout_62 = QHBoxLayout(self.widget_75)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.widget_warning_16 = QWidget(self.widget_75)
        self.widget_warning_16.setObjectName(u"widget_warning_16")
        self.widget_warning_16.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_377 = QHBoxLayout(self.widget_warning_16)
        self.horizontalLayout_377.setSpacing(0)
        self.horizontalLayout_377.setObjectName(u"horizontalLayout_377")
        self.horizontalLayout_377.setContentsMargins(10, 5, 5, 5)
        self.label_230 = QLabel(self.widget_warning_16)
        self.label_230.setObjectName(u"label_230")
        self.label_230.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_377.addWidget(self.label_230)

        self.label_316 = QLabel(self.widget_warning_16)
        self.label_316.setObjectName(u"label_316")
        self.label_316.setMinimumSize(QSize(150, 0))
        self.label_316.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_316.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_377.addWidget(self.label_316)


        self.horizontalLayout_62.addWidget(self.widget_warning_16)

        self.horizontalSpacer_44 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_44)

        self.pushButton_59 = QPushButton(self.widget_75)
        self.pushButton_59.setObjectName(u"pushButton_59")
        self.pushButton_59.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_62.addWidget(self.pushButton_59)


        self.verticalLayout_319.addWidget(self.widget_75)

        self.verticalSpacer_11 = QSpacerItem(20, 148, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_319.addItem(self.verticalSpacer_11)


        self.horizontalLayout_61.addWidget(self.widget_74)


        self.verticalLayout_50.addWidget(self.widget_73)

        self.widget_78 = QWidget(self.widget_71)
        self.widget_78.setObjectName(u"widget_78")
        self.widget_78.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_54 = QVBoxLayout(self.widget_78)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.widget_79 = QWidget(self.widget_78)
        self.widget_79.setObjectName(u"widget_79")
        self.horizontalLayout_64 = QHBoxLayout(self.widget_79)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_54.addWidget(self.widget_79)


        self.verticalLayout_50.addWidget(self.widget_78)


        self.verticalLayout_40.addWidget(self.widget_71)

        self.widget_31 = QWidget(self.scrollAreaWidgetContents)
        self.widget_31.setObjectName(u"widget_31")
        self.verticalLayout_29 = QVBoxLayout(self.widget_31)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.widget_16 = QWidget(self.widget_31)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setStyleSheet(u"")
        self.horizontalLayout_31 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_3 = QWidget(self.widget_16)
        self.Equipement_widget_3.setObjectName(u"Equipement_widget_3")
        self.Equipement_widget_3.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_30 = QHBoxLayout(self.Equipement_widget_3)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_22 = QLabel(self.Equipement_widget_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setPixmap(QPixmap(u":/assets/icons/equippement-30.png"))

        self.horizontalLayout_30.addWidget(self.label_22, 0, Qt.AlignLeft)

        self.pushButton_47 = QPushButton(self.Equipement_widget_3)
        self.pushButton_47.setObjectName(u"pushButton_47")
        sizePolicy2.setHeightForWidth(self.pushButton_47.sizePolicy().hasHeightForWidth())
        self.pushButton_47.setSizePolicy(sizePolicy2)
        self.pushButton_47.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_47.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_47.setIcon(icon9)
        self.pushButton_47.setIconSize(QSize(24, 24))
        self.pushButton_47.setCheckable(True)

        self.horizontalLayout_30.addWidget(self.pushButton_47)


        self.horizontalLayout_31.addWidget(self.Equipement_widget_3)

        self.horizontalSpacer_11 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_11)


        self.verticalLayout_29.addWidget(self.widget_16)

        self.widget_30 = QWidget(self.widget_31)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setMinimumSize(QSize(450, 0))
        self.widget_30.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.verticalLayout_24 = QVBoxLayout(self.widget_30)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_5 = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_5)

        self.widget_12 = QWidget(self.widget_30)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_23 = QVBoxLayout(self.widget_12)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.textEdit_15 = QTextEdit(self.widget_12)
        self.textEdit_15.setObjectName(u"textEdit_15")
        sizePolicy4.setHeightForWidth(self.textEdit_15.sizePolicy().hasHeightForWidth())
        self.textEdit_15.setSizePolicy(sizePolicy4)
        self.textEdit_15.setMinimumSize(QSize(0, 0))
        self.textEdit_15.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_23.addWidget(self.textEdit_15)

        self.verticalSpacer_6 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_6)

        self.widget_87 = QWidget(self.widget_12)
        self.widget_87.setObjectName(u"widget_87")
        sizePolicy3.setHeightForWidth(self.widget_87.sizePolicy().hasHeightForWidth())
        self.widget_87.setSizePolicy(sizePolicy3)
        self.widget_87.setMinimumSize(QSize(300, 0))
        self.verticalLayout_65 = QVBoxLayout(self.widget_87)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.label_36 = QLabel(self.widget_87)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_65.addWidget(self.label_36)

        self.verticalSpacer_24 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_65.addItem(self.verticalSpacer_24)

        self.comboBox_8 = QComboBox(self.widget_87)
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_65.addWidget(self.comboBox_8)


        self.verticalLayout_23.addWidget(self.widget_87)

        self.widget_94 = QWidget(self.widget_12)
        self.widget_94.setObjectName(u"widget_94")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_94)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_51 = QSpacerItem(361, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_51)

        self.pushButton_40 = QPushButton(self.widget_94)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_40.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_18.addWidget(self.pushButton_40)


        self.verticalLayout_23.addWidget(self.widget_94)


        self.horizontalLayout_16.addWidget(self.widget_12)

        self.horizontalSpacer_10 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_10)


        self.verticalLayout_24.addLayout(self.horizontalLayout_16)

        self.widget_77 = QWidget(self.widget_30)
        self.widget_77.setObjectName(u"widget_77")
        sizePolicy.setHeightForWidth(self.widget_77.sizePolicy().hasHeightForWidth())
        self.widget_77.setSizePolicy(sizePolicy)
        self.widget_77.setMinimumSize(QSize(400, 0))
        self.verticalLayout_64 = QVBoxLayout(self.widget_77)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.widget_86 = QWidget(self.widget_77)
        self.widget_86.setObjectName(u"widget_86")
        self.verticalLayout_320 = QVBoxLayout(self.widget_86)
        self.verticalLayout_320.setObjectName(u"verticalLayout_320")
        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalSpacer_46 = QSpacerItem(13, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_46)

        self.widget_88 = QWidget(self.widget_86)
        self.widget_88.setObjectName(u"widget_88")
        self.verticalLayout_66 = QVBoxLayout(self.widget_88)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.label_37 = QLabel(self.widget_88)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignCenter)

        self.verticalLayout_66.addWidget(self.label_37)

        self.lineEdit_14 = QLineEdit(self.widget_88)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_66.addWidget(self.lineEdit_14)


        self.horizontalLayout_47.addWidget(self.widget_88)

        self.horizontalSpacer_47 = QSpacerItem(13, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_47)

        self.widget_89 = QWidget(self.widget_86)
        self.widget_89.setObjectName(u"widget_89")
        self.verticalLayout_67 = QVBoxLayout(self.widget_89)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.label_38 = QLabel(self.widget_89)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignCenter)

        self.verticalLayout_67.addWidget(self.label_38)

        self.lineEdit_15 = QLineEdit(self.widget_89)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_67.addWidget(self.lineEdit_15)


        self.horizontalLayout_47.addWidget(self.widget_89)

        self.horizontalSpacer_48 = QSpacerItem(13, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_48)

        self.widget_90 = QWidget(self.widget_86)
        self.widget_90.setObjectName(u"widget_90")
        self.verticalLayout_68 = QVBoxLayout(self.widget_90)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.label_39 = QLabel(self.widget_90)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setAlignment(Qt.AlignCenter)

        self.verticalLayout_68.addWidget(self.label_39)

        self.lineEdit_16 = QLineEdit(self.widget_90)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_68.addWidget(self.lineEdit_16)


        self.horizontalLayout_47.addWidget(self.widget_90)

        self.horizontalSpacer_49 = QSpacerItem(13, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_49)

        self.widget_91 = QWidget(self.widget_86)
        self.widget_91.setObjectName(u"widget_91")
        self.verticalLayout_69 = QVBoxLayout(self.widget_91)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.label_40 = QLabel(self.widget_91)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.verticalLayout_69.addWidget(self.label_40)

        self.lineEdit_17 = QLineEdit(self.widget_91)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_69.addWidget(self.lineEdit_17)


        self.horizontalLayout_47.addWidget(self.widget_91)

        self.horizontalSpacer_50 = QSpacerItem(13, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_50)

        self.widget_92 = QWidget(self.widget_86)
        self.widget_92.setObjectName(u"widget_92")
        self.verticalLayout_70 = QVBoxLayout(self.widget_92)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.label_41 = QLabel(self.widget_92)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setLayoutDirection(Qt.LeftToRight)
        self.label_41.setAlignment(Qt.AlignCenter)

        self.verticalLayout_70.addWidget(self.label_41)

        self.lineEdit_18 = QLineEdit(self.widget_92)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_70.addWidget(self.lineEdit_18)


        self.horizontalLayout_47.addWidget(self.widget_92)


        self.verticalLayout_320.addLayout(self.horizontalLayout_47)

        self.widget_158 = QWidget(self.widget_86)
        self.widget_158.setObjectName(u"widget_158")
        self.horizontalLayout_432 = QHBoxLayout(self.widget_158)
        self.horizontalLayout_432.setObjectName(u"horizontalLayout_432")
        self.horizontalSpacer_352 = QSpacerItem(594, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_432.addItem(self.horizontalSpacer_352)

        self.pushButton_66 = QPushButton(self.widget_158)
        self.pushButton_66.setObjectName(u"pushButton_66")
        self.pushButton_66.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_432.addWidget(self.pushButton_66)

        self.horizontalSpacer_353 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_432.addItem(self.horizontalSpacer_353)


        self.verticalLayout_320.addWidget(self.widget_158)


        self.verticalLayout_64.addWidget(self.widget_86)

        self.verticalSpacer_25 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_64.addItem(self.verticalSpacer_25)

        self.widget_93 = QWidget(self.widget_77)
        self.widget_93.setObjectName(u"widget_93")
        self.horizontalLayout_65 = QHBoxLayout(self.widget_93)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.widget_warning_17 = QWidget(self.widget_93)
        self.widget_warning_17.setObjectName(u"widget_warning_17")
        self.widget_warning_17.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_378 = QHBoxLayout(self.widget_warning_17)
        self.horizontalLayout_378.setSpacing(0)
        self.horizontalLayout_378.setObjectName(u"horizontalLayout_378")
        self.horizontalLayout_378.setContentsMargins(10, 5, 5, 5)
        self.label_231 = QLabel(self.widget_warning_17)
        self.label_231.setObjectName(u"label_231")
        self.label_231.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_378.addWidget(self.label_231)

        self.label_317 = QLabel(self.widget_warning_17)
        self.label_317.setObjectName(u"label_317")
        self.label_317.setMinimumSize(QSize(150, 0))
        self.label_317.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_317.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_378.addWidget(self.label_317)


        self.horizontalLayout_65.addWidget(self.widget_warning_17)

        self.horizontalSpacer_52 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_65.addItem(self.horizontalSpacer_52)

        self.pushButton_61 = QPushButton(self.widget_93)
        self.pushButton_61.setObjectName(u"pushButton_61")
        self.pushButton_61.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_65.addWidget(self.pushButton_61)


        self.verticalLayout_64.addWidget(self.widget_93)


        self.verticalLayout_24.addWidget(self.widget_77)


        self.verticalLayout_29.addWidget(self.widget_30)

        self.widget_25 = QWidget(self.widget_31)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_28 = QVBoxLayout(self.widget_25)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.widget_26 = QWidget(self.widget_25)
        self.widget_26.setObjectName(u"widget_26")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_28.addWidget(self.widget_26)


        self.verticalLayout_29.addWidget(self.widget_25)


        self.verticalLayout_40.addWidget(self.widget_31)

        self.widget_47 = QWidget(self.scrollAreaWidgetContents)
        self.widget_47.setObjectName(u"widget_47")
        self.verticalLayout_38 = QVBoxLayout(self.widget_47)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.widget_22 = QWidget(self.widget_47)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setStyleSheet(u"")
        self.horizontalLayout_45 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_8 = QWidget(self.widget_22)
        self.Equipement_widget_8.setObjectName(u"Equipement_widget_8")
        self.Equipement_widget_8.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_46 = QHBoxLayout(self.Equipement_widget_8)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_27 = QLabel(self.Equipement_widget_8)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setPixmap(QPixmap(u":/assets/icons/equippement-30.png"))

        self.horizontalLayout_46.addWidget(self.label_27, 0, Qt.AlignLeft)

        self.pushButton_52 = QPushButton(self.Equipement_widget_8)
        self.pushButton_52.setObjectName(u"pushButton_52")
        sizePolicy2.setHeightForWidth(self.pushButton_52.sizePolicy().hasHeightForWidth())
        self.pushButton_52.setSizePolicy(sizePolicy2)
        self.pushButton_52.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_52.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_52.setIcon(icon9)
        self.pushButton_52.setIconSize(QSize(24, 24))
        self.pushButton_52.setCheckable(True)

        self.horizontalLayout_46.addWidget(self.pushButton_52)


        self.horizontalLayout_45.addWidget(self.Equipement_widget_8)

        self.horizontalSpacer_30 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_30)


        self.verticalLayout_38.addWidget(self.widget_22)

        self.widget_48 = QWidget(self.widget_47)
        self.widget_48.setObjectName(u"widget_48")
        self.widget_48.setMinimumSize(QSize(450, 0))
        self.widget_48.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.verticalLayout_321 = QVBoxLayout(self.widget_48)
        self.verticalLayout_321.setObjectName(u"verticalLayout_321")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_7 = QSpacerItem(255, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_7)

        self.widget_23 = QWidget(self.widget_48)
        self.widget_23.setObjectName(u"widget_23")
        sizePolicy.setHeightForWidth(self.widget_23.sizePolicy().hasHeightForWidth())
        self.widget_23.setSizePolicy(sizePolicy)
        self.widget_23.setMinimumSize(QSize(400, 0))
        self.verticalLayout_27 = QVBoxLayout(self.widget_23)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalSpacer_55 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_55)

        self.label_189 = QLabel(self.widget_23)
        self.label_189.setObjectName(u"label_189")

        self.horizontalLayout_51.addWidget(self.label_189)

        self.horizontalSpacer_54 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_54)


        self.verticalLayout_27.addLayout(self.horizontalLayout_51)

        self.widget_27 = QWidget(self.widget_23)
        self.widget_27.setObjectName(u"widget_27")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_32 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_32)


        self.verticalLayout_27.addWidget(self.widget_27)

        self.lineEdit_3 = QLineEdit(self.widget_23)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_27.addWidget(self.lineEdit_3)


        self.horizontalLayout_23.addWidget(self.widget_23)

        self.horizontalSpacer_33 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_33)


        self.verticalLayout_321.addLayout(self.horizontalLayout_23)

        self.widget_159 = QWidget(self.widget_48)
        self.widget_159.setObjectName(u"widget_159")
        self.horizontalLayout_433 = QHBoxLayout(self.widget_159)
        self.horizontalLayout_433.setObjectName(u"horizontalLayout_433")
        self.horizontalSpacer_354 = QSpacerItem(594, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_433.addItem(self.horizontalSpacer_354)

        self.pushButton_67 = QPushButton(self.widget_159)
        self.pushButton_67.setObjectName(u"pushButton_67")
        self.pushButton_67.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_433.addWidget(self.pushButton_67)

        self.horizontalSpacer_355 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_433.addItem(self.horizontalSpacer_355)


        self.verticalLayout_321.addWidget(self.widget_159)


        self.verticalLayout_38.addWidget(self.widget_48)

        self.widget_51 = QWidget(self.widget_47)
        self.widget_51.setObjectName(u"widget_51")
        self.widget_51.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_41 = QVBoxLayout(self.widget_51)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.widget_52 = QWidget(self.widget_51)
        self.widget_52.setObjectName(u"widget_52")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_52)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_41.addWidget(self.widget_52)


        self.verticalLayout_38.addWidget(self.widget_51)


        self.verticalLayout_40.addWidget(self.widget_47)

        self.widget_28 = QWidget(self.scrollAreaWidgetContents)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setStyleSheet(u"")
        self.horizontalLayout_48 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.Equipement_widget_7 = QWidget(self.widget_28)
        self.Equipement_widget_7.setObjectName(u"Equipement_widget_7")
        self.Equipement_widget_7.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 191, 191);\n"
"border-radius:10px;\n"
"color: white;\n"
"}\n"
"")
        self.horizontalLayout_49 = QHBoxLayout(self.Equipement_widget_7)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.pushButton_51 = QPushButton(self.Equipement_widget_7)
        self.pushButton_51.setObjectName(u"pushButton_51")
        sizePolicy2.setHeightForWidth(self.pushButton_51.sizePolicy().hasHeightForWidth())
        self.pushButton_51.setSizePolicy(sizePolicy2)
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        self.pushButton_51.setFont(font5)
        self.pushButton_51.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_51.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(255, 191, 191);\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 191, 191);\n"
"}\n"
"")
        self.pushButton_51.setIcon(icon9)
        self.pushButton_51.setIconSize(QSize(24, 24))
        self.pushButton_51.setCheckable(True)

        self.horizontalLayout_49.addWidget(self.pushButton_51)


        self.horizontalLayout_48.addWidget(self.Equipement_widget_7)

        self.horizontalSpacer_53 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_53)

        self.Equipement_widget_9 = QWidget(self.widget_28)
        self.Equipement_widget_9.setObjectName(u"Equipement_widget_9")
        self.Equipement_widget_9.setStyleSheet(u"QWidget{\n"
"background-color: rgb(104, 246, 73);\n"
"border-radius:10px;\n"
"color: white;\n"
"}\n"
"")
        self.horizontalLayout_50 = QHBoxLayout(self.Equipement_widget_9)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.pushButton_53 = QPushButton(self.Equipement_widget_9)
        self.pushButton_53.setObjectName(u"pushButton_53")
        sizePolicy2.setHeightForWidth(self.pushButton_53.sizePolicy().hasHeightForWidth())
        self.pushButton_53.setSizePolicy(sizePolicy2)
        self.pushButton_53.setFont(font5)
        self.pushButton_53.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_53.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(104, 246, 73);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(104, 246, 73);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(104, 246, 73);\n"
"}\n"
"")
        self.pushButton_53.setIcon(icon9)
        self.pushButton_53.setIconSize(QSize(24, 24))
        self.pushButton_53.setCheckable(True)

        self.horizontalLayout_50.addWidget(self.pushButton_53)


        self.horizontalLayout_48.addWidget(self.Equipement_widget_9)


        self.verticalLayout_40.addWidget(self.widget_28)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.nv_dossier_prodEXT_page)
        self.nv_dossier_prodINW_page = QWidget()
        self.nv_dossier_prodINW_page.setObjectName(u"nv_dossier_prodINW_page")
        self.gridLayout_2 = QGridLayout(self.nv_dossier_prodINW_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea_2 = QScrollArea(self.nv_dossier_prodINW_page)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -1158, 964, 2204))
        self.verticalLayout_61 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.widget_80 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_80.setObjectName(u"widget_80")
        self.horizontalLayout_159 = QHBoxLayout(self.widget_80)
        self.horizontalLayout_159.setObjectName(u"horizontalLayout_159")
        self.label_34 = QLabel(self.widget_80)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font4)

        self.horizontalLayout_159.addWidget(self.label_34)

        self.horizontalSpacer_254 = QSpacerItem(353, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_159.addItem(self.horizontalSpacer_254)

        self.label_35 = QLabel(self.widget_80)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_159.addWidget(self.label_35)

        self.horizontalSpacer_253 = QSpacerItem(353, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_159.addItem(self.horizontalSpacer_253)

        self.label_134 = QLabel(self.widget_80)
        self.label_134.setObjectName(u"label_134")

        self.horizontalLayout_159.addWidget(self.label_134)


        self.verticalLayout_61.addWidget(self.widget_80)

        self.widget_81 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_81.setObjectName(u"widget_81")
        self.verticalLayout_62 = QVBoxLayout(self.widget_81)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.widget_82 = QWidget(self.widget_81)
        self.widget_82.setObjectName(u"widget_82")
        self.horizontalLayout_68 = QHBoxLayout(self.widget_82)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_13 = QWidget(self.widget_82)
        self.Equipement_widget_13.setObjectName(u"Equipement_widget_13")
        self.Equipement_widget_13.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_69 = QHBoxLayout(self.Equipement_widget_13)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.label_42 = QLabel(self.Equipement_widget_13)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setPixmap(QPixmap(u":/assets/icons/employee-30.png"))

        self.horizontalLayout_69.addWidget(self.label_42, 0, Qt.AlignLeft)

        self.pushButton_64 = QPushButton(self.Equipement_widget_13)
        self.pushButton_64.setObjectName(u"pushButton_64")
        sizePolicy2.setHeightForWidth(self.pushButton_64.sizePolicy().hasHeightForWidth())
        self.pushButton_64.setSizePolicy(sizePolicy2)
        self.pushButton_64.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_64.setStyleSheet(u"")
        self.pushButton_64.setIconSize(QSize(24, 24))
        self.pushButton_64.setCheckable(True)

        self.horizontalLayout_69.addWidget(self.pushButton_64)


        self.horizontalLayout_68.addWidget(self.Equipement_widget_13)

        self.horizontalSpacer_34 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_68.addItem(self.horizontalSpacer_34)


        self.verticalLayout_62.addWidget(self.widget_82)

        self.widget_83 = QWidget(self.widget_81)
        self.widget_83.setObjectName(u"widget_83")
        self.widget_83.setMinimumSize(QSize(0, 0))
        self.widget_83.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.verticalLayout_295 = QVBoxLayout(self.widget_83)
        self.verticalLayout_295.setObjectName(u"verticalLayout_295")
        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalSpacer_35 = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_70.addItem(self.horizontalSpacer_35)

        self.widget_84 = QWidget(self.widget_83)
        self.widget_84.setObjectName(u"widget_84")
        sizePolicy.setHeightForWidth(self.widget_84.sizePolicy().hasHeightForWidth())
        self.widget_84.setSizePolicy(sizePolicy)
        self.widget_84.setMinimumSize(QSize(0, 0))
        self.verticalLayout_63 = QVBoxLayout(self.widget_84)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.textEdit_10 = QTextEdit(self.widget_84)
        self.textEdit_10.setObjectName(u"textEdit_10")
        sizePolicy4.setHeightForWidth(self.textEdit_10.sizePolicy().hasHeightForWidth())
        self.textEdit_10.setSizePolicy(sizePolicy4)
        self.textEdit_10.setMinimumSize(QSize(0, 0))
        self.textEdit_10.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_63.addWidget(self.textEdit_10)

        self.textEdit_14 = QTextEdit(self.widget_84)
        self.textEdit_14.setObjectName(u"textEdit_14")
        sizePolicy4.setHeightForWidth(self.textEdit_14.sizePolicy().hasHeightForWidth())
        self.textEdit_14.setSizePolicy(sizePolicy4)
        self.textEdit_14.setMinimumSize(QSize(0, 0))
        self.textEdit_14.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_63.addWidget(self.textEdit_14)

        self.widget_85 = QWidget(self.widget_84)
        self.widget_85.setObjectName(u"widget_85")
        self.verticalLayout_71 = QVBoxLayout(self.widget_85)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.checkBox_5 = QCheckBox(self.widget_85)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setChecked(True)

        self.verticalLayout_71.addWidget(self.checkBox_5)

        self.checkBox_6 = QCheckBox(self.widget_85)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.verticalLayout_71.addWidget(self.checkBox_6)


        self.verticalLayout_63.addWidget(self.widget_85)

        self.widget_95 = QWidget(self.widget_84)
        self.widget_95.setObjectName(u"widget_95")
        self.horizontalLayout_71 = QHBoxLayout(self.widget_95)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.dateEdit_4 = QDateEdit(self.widget_95)
        self.dateEdit_4.setObjectName(u"dateEdit_4")
        self.dateEdit_4.setDateTime(QDateTime(QDate(2024, 10, 31), QTime(17, 0, 0)))
        self.dateEdit_4.setCalendarPopup(True)

        self.horizontalLayout_71.addWidget(self.dateEdit_4)

        self.horizontalSpacer_36 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_71.addItem(self.horizontalSpacer_36)


        self.verticalLayout_63.addWidget(self.widget_95)


        self.horizontalLayout_70.addWidget(self.widget_84)

        self.horizontalSpacer_45 = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_70.addItem(self.horizontalSpacer_45)

        self.horizontalSpacer_56 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_70.addItem(self.horizontalSpacer_56)

        self.widget_96 = QWidget(self.widget_83)
        self.widget_96.setObjectName(u"widget_96")
        self.widget_96.setMinimumSize(QSize(0, 0))
        self.widget_96.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_72 = QVBoxLayout(self.widget_96)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.textEdit_16 = QTextEdit(self.widget_96)
        self.textEdit_16.setObjectName(u"textEdit_16")
        sizePolicy4.setHeightForWidth(self.textEdit_16.sizePolicy().hasHeightForWidth())
        self.textEdit_16.setSizePolicy(sizePolicy4)
        self.textEdit_16.setMinimumSize(QSize(0, 0))
        self.textEdit_16.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_72.addWidget(self.textEdit_16)

        self.widget_97 = QWidget(self.widget_96)
        self.widget_97.setObjectName(u"widget_97")
        self.verticalLayout_73 = QVBoxLayout(self.widget_97)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.checkBox_7 = QCheckBox(self.widget_97)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setChecked(True)

        self.verticalLayout_73.addWidget(self.checkBox_7)

        self.checkBox_8 = QCheckBox(self.widget_97)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.verticalLayout_73.addWidget(self.checkBox_8)


        self.verticalLayout_72.addWidget(self.widget_97)

        self.widget_98 = QWidget(self.widget_96)
        self.widget_98.setObjectName(u"widget_98")
        self.horizontalLayout_72 = QHBoxLayout(self.widget_98)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.label_43 = QLabel(self.widget_98)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_72.addWidget(self.label_43)

        self.lineEdit_9 = QLineEdit(self.widget_98)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_72.addWidget(self.lineEdit_9)


        self.verticalLayout_72.addWidget(self.widget_98)


        self.horizontalLayout_70.addWidget(self.widget_96)

        self.horizontalSpacer_58 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_70.addItem(self.horizontalSpacer_58)


        self.verticalLayout_295.addLayout(self.horizontalLayout_70)

        self.widget_99 = QWidget(self.widget_83)
        self.widget_99.setObjectName(u"widget_99")
        self.horizontalLayout_73 = QHBoxLayout(self.widget_99)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.widget_warning_19 = QWidget(self.widget_99)
        self.widget_warning_19.setObjectName(u"widget_warning_19")
        self.widget_warning_19.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_384 = QHBoxLayout(self.widget_warning_19)
        self.horizontalLayout_384.setSpacing(0)
        self.horizontalLayout_384.setObjectName(u"horizontalLayout_384")
        self.horizontalLayout_384.setContentsMargins(10, 5, 5, 5)
        self.label_280 = QLabel(self.widget_warning_19)
        self.label_280.setObjectName(u"label_280")
        self.label_280.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_384.addWidget(self.label_280)

        self.label_319 = QLabel(self.widget_warning_19)
        self.label_319.setObjectName(u"label_319")
        self.label_319.setMinimumSize(QSize(150, 0))
        self.label_319.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_319.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_384.addWidget(self.label_319)


        self.horizontalLayout_73.addWidget(self.widget_warning_19)

        self.horizontalSpacer_57 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_73.addItem(self.horizontalSpacer_57)

        self.pushButton_68 = QPushButton(self.widget_99)
        self.pushButton_68.setObjectName(u"pushButton_68")
        self.pushButton_68.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_68.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")
        self.pushButton_68.setCheckable(True)

        self.horizontalLayout_73.addWidget(self.pushButton_68)


        self.verticalLayout_295.addWidget(self.widget_99)


        self.verticalLayout_62.addWidget(self.widget_83)


        self.verticalLayout_61.addWidget(self.widget_81)

        self.widget_100 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_100.setObjectName(u"widget_100")
        self.verticalLayout_74 = QVBoxLayout(self.widget_100)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.widget_101 = QWidget(self.widget_100)
        self.widget_101.setObjectName(u"widget_101")
        self.horizontalLayout_74 = QHBoxLayout(self.widget_101)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_14 = QWidget(self.widget_101)
        self.Equipement_widget_14.setObjectName(u"Equipement_widget_14")
        self.Equipement_widget_14.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_75 = QHBoxLayout(self.Equipement_widget_14)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.label_45 = QLabel(self.Equipement_widget_14)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setPixmap(QPixmap(u":/assets/icons/employee-30.png"))

        self.horizontalLayout_75.addWidget(self.label_45, 0, Qt.AlignLeft)

        self.pushButton_69 = QPushButton(self.Equipement_widget_14)
        self.pushButton_69.setObjectName(u"pushButton_69")
        sizePolicy2.setHeightForWidth(self.pushButton_69.sizePolicy().hasHeightForWidth())
        self.pushButton_69.setSizePolicy(sizePolicy2)
        self.pushButton_69.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_69.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_69.setIcon(icon9)
        self.pushButton_69.setIconSize(QSize(24, 24))
        self.pushButton_69.setCheckable(True)

        self.horizontalLayout_75.addWidget(self.pushButton_69)


        self.horizontalLayout_74.addWidget(self.Equipement_widget_14)

        self.horizontalSpacer_59 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_74.addItem(self.horizontalSpacer_59)


        self.verticalLayout_74.addWidget(self.widget_101)

        self.widget_102 = QWidget(self.widget_100)
        self.widget_102.setObjectName(u"widget_102")
        self.widget_102.setMinimumSize(QSize(450, 0))
        self.widget_102.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.verticalLayout_296 = QVBoxLayout(self.widget_102)
        self.verticalLayout_296.setObjectName(u"verticalLayout_296")
        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.widget_103 = QWidget(self.widget_102)
        self.widget_103.setObjectName(u"widget_103")
        self.verticalLayout_75 = QVBoxLayout(self.widget_103)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.textEdit_17 = QTextEdit(self.widget_103)
        self.textEdit_17.setObjectName(u"textEdit_17")
        sizePolicy4.setHeightForWidth(self.textEdit_17.sizePolicy().hasHeightForWidth())
        self.textEdit_17.setSizePolicy(sizePolicy4)
        self.textEdit_17.setMinimumSize(QSize(0, 0))
        self.textEdit_17.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_75.addWidget(self.textEdit_17)

        self.verticalSpacer_18 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_75.addItem(self.verticalSpacer_18)


        self.horizontalLayout_76.addWidget(self.widget_103)

        self.widget_104 = QWidget(self.widget_102)
        self.widget_104.setObjectName(u"widget_104")
        self.widget_104.setMinimumSize(QSize(400, 0))
        self.verticalLayout_76 = QVBoxLayout(self.widget_104)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(4, 4, 4, 4)
        self.textEdit_18 = QTextEdit(self.widget_104)
        self.textEdit_18.setObjectName(u"textEdit_18")
        sizePolicy4.setHeightForWidth(self.textEdit_18.sizePolicy().hasHeightForWidth())
        self.textEdit_18.setSizePolicy(sizePolicy4)
        self.textEdit_18.setMinimumSize(QSize(0, 0))
        self.textEdit_18.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_76.addWidget(self.textEdit_18)

        self.plainTextEdit_19 = QPlainTextEdit(self.widget_104)
        self.plainTextEdit_19.setObjectName(u"plainTextEdit_19")
        self.plainTextEdit_19.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_76.addWidget(self.plainTextEdit_19)


        self.horizontalLayout_76.addWidget(self.widget_104)

        self.horizontalSpacer_61 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_76.addItem(self.horizontalSpacer_61)


        self.verticalLayout_296.addLayout(self.horizontalLayout_76)

        self.widget_486 = QWidget(self.widget_102)
        self.widget_486.setObjectName(u"widget_486")
        self.horizontalLayout_316 = QHBoxLayout(self.widget_486)
        self.horizontalLayout_316.setObjectName(u"horizontalLayout_316")
        self.widget_warning_20 = QWidget(self.widget_486)
        self.widget_warning_20.setObjectName(u"widget_warning_20")
        self.widget_warning_20.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_385 = QHBoxLayout(self.widget_warning_20)
        self.horizontalLayout_385.setSpacing(0)
        self.horizontalLayout_385.setObjectName(u"horizontalLayout_385")
        self.horizontalLayout_385.setContentsMargins(10, 5, 5, 5)
        self.label_281 = QLabel(self.widget_warning_20)
        self.label_281.setObjectName(u"label_281")
        self.label_281.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_385.addWidget(self.label_281)

        self.label_320 = QLabel(self.widget_warning_20)
        self.label_320.setObjectName(u"label_320")
        self.label_320.setMinimumSize(QSize(150, 0))
        self.label_320.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_320.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_385.addWidget(self.label_320)


        self.horizontalLayout_316.addWidget(self.widget_warning_20)

        self.horizontalSpacer_333 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_316.addItem(self.horizontalSpacer_333)

        self.pushButton_162 = QPushButton(self.widget_486)
        self.pushButton_162.setObjectName(u"pushButton_162")
        self.pushButton_162.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_162.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")
        self.pushButton_162.setCheckable(True)

        self.horizontalLayout_316.addWidget(self.pushButton_162)


        self.verticalLayout_296.addWidget(self.widget_486)


        self.verticalLayout_74.addWidget(self.widget_102)


        self.verticalLayout_61.addWidget(self.widget_100)

        self.widget_106 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_106.setObjectName(u"widget_106")
        self.verticalLayout_77 = QVBoxLayout(self.widget_106)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.widget_107 = QWidget(self.widget_106)
        self.widget_107.setObjectName(u"widget_107")
        self.horizontalLayout_78 = QHBoxLayout(self.widget_107)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_15 = QWidget(self.widget_107)
        self.Equipement_widget_15.setObjectName(u"Equipement_widget_15")
        self.Equipement_widget_15.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_79 = QHBoxLayout(self.Equipement_widget_15)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.label_46 = QLabel(self.Equipement_widget_15)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setPixmap(QPixmap(u":/assets/icons/employee-30.png"))

        self.horizontalLayout_79.addWidget(self.label_46, 0, Qt.AlignLeft)

        self.pushButton_71 = QPushButton(self.Equipement_widget_15)
        self.pushButton_71.setObjectName(u"pushButton_71")
        sizePolicy2.setHeightForWidth(self.pushButton_71.sizePolicy().hasHeightForWidth())
        self.pushButton_71.setSizePolicy(sizePolicy2)
        self.pushButton_71.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_71.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_71.setIcon(icon9)
        self.pushButton_71.setIconSize(QSize(24, 24))
        self.pushButton_71.setCheckable(True)

        self.horizontalLayout_79.addWidget(self.pushButton_71)


        self.horizontalLayout_78.addWidget(self.Equipement_widget_15)

        self.horizontalSpacer_62 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_78.addItem(self.horizontalSpacer_62)


        self.verticalLayout_77.addWidget(self.widget_107)

        self.widget_108 = QWidget(self.widget_106)
        self.widget_108.setObjectName(u"widget_108")
        self.widget_108.setMinimumSize(QSize(450, 0))
        self.widget_108.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.verticalLayout_297 = QVBoxLayout(self.widget_108)
        self.verticalLayout_297.setObjectName(u"verticalLayout_297")
        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.widget_109 = QWidget(self.widget_108)
        self.widget_109.setObjectName(u"widget_109")
        sizePolicy.setHeightForWidth(self.widget_109.sizePolicy().hasHeightForWidth())
        self.widget_109.setSizePolicy(sizePolicy)
        self.widget_109.setMinimumSize(QSize(0, 0))
        self.verticalLayout_78 = QVBoxLayout(self.widget_109)
        self.verticalLayout_78.setSpacing(10)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(4, 4, 4, 4)
        self.textEdit_20 = QTextEdit(self.widget_109)
        self.textEdit_20.setObjectName(u"textEdit_20")
        sizePolicy4.setHeightForWidth(self.textEdit_20.sizePolicy().hasHeightForWidth())
        self.textEdit_20.setSizePolicy(sizePolicy4)
        self.textEdit_20.setMinimumSize(QSize(0, 0))
        self.textEdit_20.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_78.addWidget(self.textEdit_20)

        self.comboBox_4 = QComboBox(self.widget_109)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(400, 0))
        self.comboBox_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_78.addWidget(self.comboBox_4)

        self.widget_110 = QWidget(self.widget_109)
        self.widget_110.setObjectName(u"widget_110")
        self.horizontalLayout_81 = QHBoxLayout(self.widget_110)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalSpacer_63 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_81.addItem(self.horizontalSpacer_63)

        self.pushButton_72 = QPushButton(self.widget_110)
        self.pushButton_72.setObjectName(u"pushButton_72")
        self.pushButton_72.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")
        self.pushButton_72.setCheckable(True)

        self.horizontalLayout_81.addWidget(self.pushButton_72)


        self.verticalLayout_78.addWidget(self.widget_110)

        self.verticalSpacer_19 = QSpacerItem(20, 148, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_78.addItem(self.verticalSpacer_19)


        self.horizontalLayout_77.addWidget(self.widget_109)

        self.horizontalSpacer_12 = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_77.addItem(self.horizontalSpacer_12)

        self.widget_111 = QWidget(self.widget_108)
        self.widget_111.setObjectName(u"widget_111")
        self.widget_111.setMinimumSize(QSize(400, 0))
        self.verticalLayout_79 = QVBoxLayout(self.widget_111)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(4, 4, 4, 4)
        self.listWidget_3 = QListWidget(self.widget_111)
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setMinimumSize(QSize(500, 0))
        self.listWidget_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_79.addWidget(self.listWidget_3)

        self.widget_112 = QWidget(self.widget_111)
        self.widget_112.setObjectName(u"widget_112")
        self.horizontalLayout_82 = QHBoxLayout(self.widget_112)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.pushButton_73 = QPushButton(self.widget_112)
        self.pushButton_73.setObjectName(u"pushButton_73")
        self.pushButton_73.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_73.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")
        self.pushButton_73.setCheckable(True)

        self.horizontalLayout_82.addWidget(self.pushButton_73)

        self.horizontalSpacer_64 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_82.addItem(self.horizontalSpacer_64)


        self.verticalLayout_79.addWidget(self.widget_112)


        self.horizontalLayout_77.addWidget(self.widget_111)

        self.horizontalSpacer_65 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_77.addItem(self.horizontalSpacer_65)


        self.verticalLayout_297.addLayout(self.horizontalLayout_77)

        self.widget_105 = QWidget(self.widget_108)
        self.widget_105.setObjectName(u"widget_105")
        self.horizontalLayout_80 = QHBoxLayout(self.widget_105)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.widget_warning_21 = QWidget(self.widget_105)
        self.widget_warning_21.setObjectName(u"widget_warning_21")
        self.widget_warning_21.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_387 = QHBoxLayout(self.widget_warning_21)
        self.horizontalLayout_387.setSpacing(0)
        self.horizontalLayout_387.setObjectName(u"horizontalLayout_387")
        self.horizontalLayout_387.setContentsMargins(10, 5, 5, 5)
        self.label_282 = QLabel(self.widget_warning_21)
        self.label_282.setObjectName(u"label_282")
        self.label_282.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_387.addWidget(self.label_282)

        self.label_321 = QLabel(self.widget_warning_21)
        self.label_321.setObjectName(u"label_321")
        self.label_321.setMinimumSize(QSize(150, 0))
        self.label_321.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_321.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_387.addWidget(self.label_321)


        self.horizontalLayout_80.addWidget(self.widget_warning_21)

        self.horizontalSpacer_60 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_80.addItem(self.horizontalSpacer_60)

        self.pushButton_70 = QPushButton(self.widget_105)
        self.pushButton_70.setObjectName(u"pushButton_70")
        self.pushButton_70.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_70.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")
        self.pushButton_70.setCheckable(True)

        self.horizontalLayout_80.addWidget(self.pushButton_70)


        self.verticalLayout_297.addWidget(self.widget_105)


        self.verticalLayout_77.addWidget(self.widget_108)


        self.verticalLayout_61.addWidget(self.widget_106)

        self.widget_113 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_113.setObjectName(u"widget_113")
        self.verticalLayout_80 = QVBoxLayout(self.widget_113)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.widget_114 = QWidget(self.widget_113)
        self.widget_114.setObjectName(u"widget_114")
        self.widget_114.setStyleSheet(u"")
        self.horizontalLayout_83 = QHBoxLayout(self.widget_114)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_16 = QWidget(self.widget_114)
        self.Equipement_widget_16.setObjectName(u"Equipement_widget_16")
        self.Equipement_widget_16.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_84 = QHBoxLayout(self.Equipement_widget_16)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.label_47 = QLabel(self.Equipement_widget_16)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setPixmap(QPixmap(u":/assets/icons/equippement-30.png"))

        self.horizontalLayout_84.addWidget(self.label_47, 0, Qt.AlignLeft)

        self.pushButton_74 = QPushButton(self.Equipement_widget_16)
        self.pushButton_74.setObjectName(u"pushButton_74")
        sizePolicy2.setHeightForWidth(self.pushButton_74.sizePolicy().hasHeightForWidth())
        self.pushButton_74.setSizePolicy(sizePolicy2)
        self.pushButton_74.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_74.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_74.setIcon(icon9)
        self.pushButton_74.setIconSize(QSize(24, 24))
        self.pushButton_74.setCheckable(True)

        self.horizontalLayout_84.addWidget(self.pushButton_74)


        self.horizontalLayout_83.addWidget(self.Equipement_widget_16)

        self.horizontalSpacer_66 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_83.addItem(self.horizontalSpacer_66)


        self.verticalLayout_80.addWidget(self.widget_114)

        self.widget_115 = QWidget(self.widget_113)
        self.widget_115.setObjectName(u"widget_115")
        self.widget_115.setMinimumSize(QSize(450, 0))
        self.widget_115.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.verticalLayout_298 = QVBoxLayout(self.widget_115)
        self.verticalLayout_298.setObjectName(u"verticalLayout_298")
        self.horizontalLayout_85 = QHBoxLayout()
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.widget_116 = QWidget(self.widget_115)
        self.widget_116.setObjectName(u"widget_116")
        sizePolicy.setHeightForWidth(self.widget_116.sizePolicy().hasHeightForWidth())
        self.widget_116.setSizePolicy(sizePolicy)
        self.widget_116.setMinimumSize(QSize(0, 0))
        self.verticalLayout_81 = QVBoxLayout(self.widget_116)
        self.verticalLayout_81.setSpacing(10)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(4, 4, 4, 4)
        self.textEdit_21 = QTextEdit(self.widget_116)
        self.textEdit_21.setObjectName(u"textEdit_21")
        sizePolicy4.setHeightForWidth(self.textEdit_21.sizePolicy().hasHeightForWidth())
        self.textEdit_21.setSizePolicy(sizePolicy4)
        self.textEdit_21.setMinimumSize(QSize(0, 0))
        self.textEdit_21.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_81.addWidget(self.textEdit_21)

        self.comboBox_7 = QComboBox(self.widget_116)
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setMinimumSize(QSize(400, 0))
        self.comboBox_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_81.addWidget(self.comboBox_7)

        self.widget_117 = QWidget(self.widget_116)
        self.widget_117.setObjectName(u"widget_117")
        self.horizontalLayout_86 = QHBoxLayout(self.widget_117)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalSpacer_67 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_86.addItem(self.horizontalSpacer_67)

        self.pushButton_75 = QPushButton(self.widget_117)
        self.pushButton_75.setObjectName(u"pushButton_75")
        self.pushButton_75.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")
        self.pushButton_75.setCheckable(True)

        self.horizontalLayout_86.addWidget(self.pushButton_75)


        self.verticalLayout_81.addWidget(self.widget_117)

        self.verticalSpacer_20 = QSpacerItem(20, 148, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_81.addItem(self.verticalSpacer_20)


        self.horizontalLayout_85.addWidget(self.widget_116)

        self.horizontalSpacer_68 = QSpacerItem(43, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_85.addItem(self.horizontalSpacer_68)

        self.widget_118 = QWidget(self.widget_115)
        self.widget_118.setObjectName(u"widget_118")
        self.widget_118.setMinimumSize(QSize(400, 0))
        self.verticalLayout_82 = QVBoxLayout(self.widget_118)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(4, 4, 4, 4)
        self.listWidget_6 = QListWidget(self.widget_118)
        self.listWidget_6.setObjectName(u"listWidget_6")
        self.listWidget_6.setMinimumSize(QSize(500, 0))
        self.listWidget_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_82.addWidget(self.listWidget_6)

        self.widget_119 = QWidget(self.widget_118)
        self.widget_119.setObjectName(u"widget_119")
        self.horizontalLayout_87 = QHBoxLayout(self.widget_119)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.pushButton_76 = QPushButton(self.widget_119)
        self.pushButton_76.setObjectName(u"pushButton_76")
        self.pushButton_76.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_76.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")
        self.pushButton_76.setCheckable(True)

        self.horizontalLayout_87.addWidget(self.pushButton_76)

        self.horizontalSpacer_69 = QSpacerItem(361, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_87.addItem(self.horizontalSpacer_69)


        self.verticalLayout_82.addWidget(self.widget_119)


        self.horizontalLayout_85.addWidget(self.widget_118)

        self.horizontalSpacer_70 = QSpacerItem(34, 131, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_85.addItem(self.horizontalSpacer_70)


        self.verticalLayout_298.addLayout(self.horizontalLayout_85)

        self.widget_492 = QWidget(self.widget_115)
        self.widget_492.setObjectName(u"widget_492")
        self.horizontalLayout_317 = QHBoxLayout(self.widget_492)
        self.horizontalLayout_317.setObjectName(u"horizontalLayout_317")
        self.widget_warning_22 = QWidget(self.widget_492)
        self.widget_warning_22.setObjectName(u"widget_warning_22")
        self.widget_warning_22.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_388 = QHBoxLayout(self.widget_warning_22)
        self.horizontalLayout_388.setSpacing(0)
        self.horizontalLayout_388.setObjectName(u"horizontalLayout_388")
        self.horizontalLayout_388.setContentsMargins(10, 5, 5, 5)
        self.label_283 = QLabel(self.widget_warning_22)
        self.label_283.setObjectName(u"label_283")
        self.label_283.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_388.addWidget(self.label_283)

        self.label_322 = QLabel(self.widget_warning_22)
        self.label_322.setObjectName(u"label_322")
        self.label_322.setMinimumSize(QSize(150, 0))
        self.label_322.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_322.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_388.addWidget(self.label_322)


        self.horizontalLayout_317.addWidget(self.widget_warning_22)

        self.horizontalSpacer_334 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_317.addItem(self.horizontalSpacer_334)

        self.pushButton_163 = QPushButton(self.widget_492)
        self.pushButton_163.setObjectName(u"pushButton_163")
        self.pushButton_163.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_163.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")
        self.pushButton_163.setCheckable(True)

        self.horizontalLayout_317.addWidget(self.pushButton_163)


        self.verticalLayout_298.addWidget(self.widget_492)


        self.verticalLayout_80.addWidget(self.widget_115)

        self.widget_120 = QWidget(self.widget_113)
        self.widget_120.setObjectName(u"widget_120")
        self.widget_120.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_83 = QVBoxLayout(self.widget_120)
        self.verticalLayout_83.setSpacing(0)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.widget_121 = QWidget(self.widget_120)
        self.widget_121.setObjectName(u"widget_121")
        self.horizontalLayout_88 = QHBoxLayout(self.widget_121)
        self.horizontalLayout_88.setSpacing(0)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_83.addWidget(self.widget_121)


        self.verticalLayout_80.addWidget(self.widget_120)


        self.verticalLayout_61.addWidget(self.widget_113)

        self.widget_122 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_122.setObjectName(u"widget_122")
        self.verticalLayout_84 = QVBoxLayout(self.widget_122)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.widget_123 = QWidget(self.widget_122)
        self.widget_123.setObjectName(u"widget_123")
        self.widget_123.setStyleSheet(u"")
        self.horizontalLayout_89 = QHBoxLayout(self.widget_123)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_17 = QWidget(self.widget_123)
        self.Equipement_widget_17.setObjectName(u"Equipement_widget_17")
        self.Equipement_widget_17.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_90 = QHBoxLayout(self.Equipement_widget_17)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.label_48 = QLabel(self.Equipement_widget_17)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setPixmap(QPixmap(u":/assets/icons/equippement-30.png"))

        self.horizontalLayout_90.addWidget(self.label_48, 0, Qt.AlignLeft)

        self.pushButton_77 = QPushButton(self.Equipement_widget_17)
        self.pushButton_77.setObjectName(u"pushButton_77")
        sizePolicy2.setHeightForWidth(self.pushButton_77.sizePolicy().hasHeightForWidth())
        self.pushButton_77.setSizePolicy(sizePolicy2)
        self.pushButton_77.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_77.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_77.setIcon(icon9)
        self.pushButton_77.setIconSize(QSize(24, 24))
        self.pushButton_77.setCheckable(True)

        self.horizontalLayout_90.addWidget(self.pushButton_77)


        self.horizontalLayout_89.addWidget(self.Equipement_widget_17)

        self.horizontalSpacer_71 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_89.addItem(self.horizontalSpacer_71)


        self.verticalLayout_84.addWidget(self.widget_123)

        self.widget_124 = QWidget(self.widget_122)
        self.widget_124.setObjectName(u"widget_124")
        self.widget_124.setMinimumSize(QSize(450, 0))
        self.widget_124.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.horizontalLayout_91 = QHBoxLayout(self.widget_124)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(10, 10, 10, 10)
        self.widget_125 = QWidget(self.widget_124)
        self.widget_125.setObjectName(u"widget_125")
        sizePolicy.setHeightForWidth(self.widget_125.sizePolicy().hasHeightForWidth())
        self.widget_125.setSizePolicy(sizePolicy)
        self.widget_125.setMinimumSize(QSize(400, 0))
        self.verticalLayout_85 = QVBoxLayout(self.widget_125)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.textEdit_22 = QTextEdit(self.widget_125)
        self.textEdit_22.setObjectName(u"textEdit_22")
        sizePolicy4.setHeightForWidth(self.textEdit_22.sizePolicy().hasHeightForWidth())
        self.textEdit_22.setSizePolicy(sizePolicy4)
        self.textEdit_22.setMinimumSize(QSize(0, 0))
        self.textEdit_22.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_85.addWidget(self.textEdit_22)

        self.widget_126 = QWidget(self.widget_125)
        self.widget_126.setObjectName(u"widget_126")
        self.horizontalLayout_92 = QHBoxLayout(self.widget_126)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(10, 10, 10, 10)
        self.horizontalSpacer_72 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_92.addItem(self.horizontalSpacer_72)

        self.widget_127 = QWidget(self.widget_126)
        self.widget_127.setObjectName(u"widget_127")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_127.sizePolicy().hasHeightForWidth())
        self.widget_127.setSizePolicy(sizePolicy5)
        self.widget_127.setMinimumSize(QSize(300, 0))
        self.verticalLayout_86 = QVBoxLayout(self.widget_127)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.label_49 = QLabel(self.widget_127)
        self.label_49.setObjectName(u"label_49")

        self.verticalLayout_86.addWidget(self.label_49)

        self.verticalSpacer_21 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_86.addItem(self.verticalSpacer_21)

        self.comboBox_9 = QComboBox(self.widget_127)
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_86.addWidget(self.comboBox_9)


        self.horizontalLayout_92.addWidget(self.widget_127)

        self.horizontalSpacer_73 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_92.addItem(self.horizontalSpacer_73)

        self.widget_128 = QWidget(self.widget_126)
        self.widget_128.setObjectName(u"widget_128")
        self.verticalLayout_87 = QVBoxLayout(self.widget_128)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.label_50 = QLabel(self.widget_128)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setAlignment(Qt.AlignCenter)

        self.verticalLayout_87.addWidget(self.label_50)

        self.verticalSpacer_22 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_87.addItem(self.verticalSpacer_22)

        self.lineEdit_10 = QLineEdit(self.widget_128)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_87.addWidget(self.lineEdit_10)


        self.horizontalLayout_92.addWidget(self.widget_128)

        self.horizontalSpacer_74 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_92.addItem(self.horizontalSpacer_74)

        self.widget_129 = QWidget(self.widget_126)
        self.widget_129.setObjectName(u"widget_129")
        self.verticalLayout_88 = QVBoxLayout(self.widget_129)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.label_51 = QLabel(self.widget_129)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setAlignment(Qt.AlignCenter)

        self.verticalLayout_88.addWidget(self.label_51)

        self.verticalSpacer_23 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_88.addItem(self.verticalSpacer_23)

        self.lineEdit_11 = QLineEdit(self.widget_129)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_88.addWidget(self.lineEdit_11)


        self.horizontalLayout_92.addWidget(self.widget_129)

        self.horizontalSpacer_75 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_92.addItem(self.horizontalSpacer_75)

        self.widget_130 = QWidget(self.widget_126)
        self.widget_130.setObjectName(u"widget_130")
        self.verticalLayout_89 = QVBoxLayout(self.widget_130)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.label_52 = QLabel(self.widget_130)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setAlignment(Qt.AlignCenter)

        self.verticalLayout_89.addWidget(self.label_52)

        self.verticalSpacer_26 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_89.addItem(self.verticalSpacer_26)

        self.lineEdit_12 = QLineEdit(self.widget_130)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_89.addWidget(self.lineEdit_12)


        self.horizontalLayout_92.addWidget(self.widget_130)

        self.horizontalSpacer_76 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_92.addItem(self.horizontalSpacer_76)

        self.widget_131 = QWidget(self.widget_126)
        self.widget_131.setObjectName(u"widget_131")
        self.verticalLayout_90 = QVBoxLayout(self.widget_131)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.label_53 = QLabel(self.widget_131)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setAlignment(Qt.AlignCenter)

        self.verticalLayout_90.addWidget(self.label_53)

        self.verticalSpacer_27 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_90.addItem(self.verticalSpacer_27)

        self.lineEdit_13 = QLineEdit(self.widget_131)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_90.addWidget(self.lineEdit_13)


        self.horizontalLayout_92.addWidget(self.widget_131)

        self.horizontalSpacer_77 = QSpacerItem(11, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_92.addItem(self.horizontalSpacer_77)

        self.widget_132 = QWidget(self.widget_126)
        self.widget_132.setObjectName(u"widget_132")
        self.verticalLayout_91 = QVBoxLayout(self.widget_132)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.label_54 = QLabel(self.widget_132)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setLayoutDirection(Qt.LeftToRight)
        self.label_54.setAlignment(Qt.AlignCenter)

        self.verticalLayout_91.addWidget(self.label_54)

        self.verticalSpacer_28 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_91.addItem(self.verticalSpacer_28)

        self.lineEdit_19 = QLineEdit(self.widget_132)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_91.addWidget(self.lineEdit_19)


        self.horizontalLayout_92.addWidget(self.widget_132)

        self.horizontalSpacer_78 = QSpacerItem(171, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_92.addItem(self.horizontalSpacer_78)


        self.verticalLayout_85.addWidget(self.widget_126)

        self.widget_133 = QWidget(self.widget_125)
        self.widget_133.setObjectName(u"widget_133")
        self.horizontalLayout_93 = QHBoxLayout(self.widget_133)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.widget_warning_23 = QWidget(self.widget_133)
        self.widget_warning_23.setObjectName(u"widget_warning_23")
        self.widget_warning_23.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_389 = QHBoxLayout(self.widget_warning_23)
        self.horizontalLayout_389.setSpacing(0)
        self.horizontalLayout_389.setObjectName(u"horizontalLayout_389")
        self.horizontalLayout_389.setContentsMargins(10, 5, 5, 5)
        self.label_287 = QLabel(self.widget_warning_23)
        self.label_287.setObjectName(u"label_287")
        self.label_287.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_389.addWidget(self.label_287)

        self.label_323 = QLabel(self.widget_warning_23)
        self.label_323.setObjectName(u"label_323")
        self.label_323.setMinimumSize(QSize(150, 0))
        self.label_323.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_323.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_389.addWidget(self.label_323)


        self.horizontalLayout_93.addWidget(self.widget_warning_23)

        self.horizontalSpacer_79 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_93.addItem(self.horizontalSpacer_79)

        self.pushButton_78 = QPushButton(self.widget_133)
        self.pushButton_78.setObjectName(u"pushButton_78")
        self.pushButton_78.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")
        self.pushButton_78.setCheckable(True)

        self.horizontalLayout_93.addWidget(self.pushButton_78)


        self.verticalLayout_85.addWidget(self.widget_133)

        self.verticalSpacer_29 = QSpacerItem(20, 148, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_85.addItem(self.verticalSpacer_29)


        self.horizontalLayout_91.addWidget(self.widget_125)


        self.verticalLayout_84.addWidget(self.widget_124)

        self.widget_134 = QWidget(self.widget_122)
        self.widget_134.setObjectName(u"widget_134")
        self.widget_134.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_92 = QVBoxLayout(self.widget_134)
        self.verticalLayout_92.setSpacing(0)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.widget_135 = QWidget(self.widget_134)
        self.widget_135.setObjectName(u"widget_135")
        self.horizontalLayout_94 = QHBoxLayout(self.widget_135)
        self.horizontalLayout_94.setSpacing(0)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_92.addWidget(self.widget_135)


        self.verticalLayout_84.addWidget(self.widget_134)


        self.verticalLayout_61.addWidget(self.widget_122)

        self.widget_136 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_136.setObjectName(u"widget_136")
        self.verticalLayout_93 = QVBoxLayout(self.widget_136)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.widget_137 = QWidget(self.widget_136)
        self.widget_137.setObjectName(u"widget_137")
        self.widget_137.setStyleSheet(u"")
        self.horizontalLayout_95 = QHBoxLayout(self.widget_137)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_18 = QWidget(self.widget_137)
        self.Equipement_widget_18.setObjectName(u"Equipement_widget_18")
        self.Equipement_widget_18.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_96 = QHBoxLayout(self.Equipement_widget_18)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.label_55 = QLabel(self.Equipement_widget_18)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setPixmap(QPixmap(u":/assets/icons/equippement-30.png"))

        self.horizontalLayout_96.addWidget(self.label_55, 0, Qt.AlignLeft)

        self.pushButton_79 = QPushButton(self.Equipement_widget_18)
        self.pushButton_79.setObjectName(u"pushButton_79")
        sizePolicy2.setHeightForWidth(self.pushButton_79.sizePolicy().hasHeightForWidth())
        self.pushButton_79.setSizePolicy(sizePolicy2)
        self.pushButton_79.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_79.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_79.setIcon(icon9)
        self.pushButton_79.setIconSize(QSize(24, 24))
        self.pushButton_79.setCheckable(True)

        self.horizontalLayout_96.addWidget(self.pushButton_79)


        self.horizontalLayout_95.addWidget(self.Equipement_widget_18)

        self.horizontalSpacer_80 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_95.addItem(self.horizontalSpacer_80)


        self.verticalLayout_93.addWidget(self.widget_137)

        self.widget_138 = QWidget(self.widget_136)
        self.widget_138.setObjectName(u"widget_138")
        self.widget_138.setMinimumSize(QSize(450, 0))
        self.widget_138.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.horizontalLayout_97 = QHBoxLayout(self.widget_138)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalSpacer_81 = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_97.addItem(self.horizontalSpacer_81)

        self.widget_139 = QWidget(self.widget_138)
        self.widget_139.setObjectName(u"widget_139")
        self.verticalLayout_94 = QVBoxLayout(self.widget_139)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.textEdit_23 = QTextEdit(self.widget_139)
        self.textEdit_23.setObjectName(u"textEdit_23")
        sizePolicy4.setHeightForWidth(self.textEdit_23.sizePolicy().hasHeightForWidth())
        self.textEdit_23.setSizePolicy(sizePolicy4)
        self.textEdit_23.setMinimumSize(QSize(0, 0))
        self.textEdit_23.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_94.addWidget(self.textEdit_23)

        self.verticalSpacer_30 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_94.addItem(self.verticalSpacer_30)

        self.widget_140 = QWidget(self.widget_139)
        self.widget_140.setObjectName(u"widget_140")
        sizePolicy5.setHeightForWidth(self.widget_140.sizePolicy().hasHeightForWidth())
        self.widget_140.setSizePolicy(sizePolicy5)
        self.widget_140.setMinimumSize(QSize(300, 0))
        self.verticalLayout_95 = QVBoxLayout(self.widget_140)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.label_56 = QLabel(self.widget_140)
        self.label_56.setObjectName(u"label_56")

        self.verticalLayout_95.addWidget(self.label_56)

        self.verticalSpacer_31 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_95.addItem(self.verticalSpacer_31)

        self.comboBox_10 = QComboBox(self.widget_140)
        self.comboBox_10.setObjectName(u"comboBox_10")
        self.comboBox_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_95.addWidget(self.comboBox_10)


        self.verticalLayout_94.addWidget(self.widget_140)

        self.widget_141 = QWidget(self.widget_139)
        self.widget_141.setObjectName(u"widget_141")
        self.horizontalLayout_98 = QHBoxLayout(self.widget_141)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalSpacer_82 = QSpacerItem(361, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_98.addItem(self.horizontalSpacer_82)

        self.pushButton_80 = QPushButton(self.widget_141)
        self.pushButton_80.setObjectName(u"pushButton_80")
        self.pushButton_80.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_80.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")
        self.pushButton_80.setCheckable(True)

        self.horizontalLayout_98.addWidget(self.pushButton_80)


        self.verticalLayout_94.addWidget(self.widget_141)


        self.horizontalLayout_97.addWidget(self.widget_139)

        self.widget_142 = QWidget(self.widget_138)
        self.widget_142.setObjectName(u"widget_142")
        self.widget_142.setMinimumSize(QSize(0, 0))
        self.verticalLayout_96 = QVBoxLayout(self.widget_142)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.verticalLayout_96.setContentsMargins(4, 4, 4, 4)

        self.horizontalLayout_97.addWidget(self.widget_142)

        self.horizontalSpacer_84 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_97.addItem(self.horizontalSpacer_84)

        self.widget_144 = QWidget(self.widget_138)
        self.widget_144.setObjectName(u"widget_144")
        sizePolicy.setHeightForWidth(self.widget_144.sizePolicy().hasHeightForWidth())
        self.widget_144.setSizePolicy(sizePolicy)
        self.widget_144.setMinimumSize(QSize(400, 0))
        self.verticalLayout_97 = QVBoxLayout(self.widget_144)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.widget_145 = QWidget(self.widget_144)
        self.widget_145.setObjectName(u"widget_145")
        self.horizontalLayout_100 = QHBoxLayout(self.widget_145)
        self.horizontalLayout_100.setSpacing(0)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalLayout_100.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_85 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_100.addItem(self.horizontalSpacer_85)

        self.horizontalSpacer_86 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_100.addItem(self.horizontalSpacer_86)

        self.widget_146 = QWidget(self.widget_145)
        self.widget_146.setObjectName(u"widget_146")
        self.verticalLayout_98 = QVBoxLayout(self.widget_146)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.label_57 = QLabel(self.widget_146)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setAlignment(Qt.AlignCenter)

        self.verticalLayout_98.addWidget(self.label_57)

        self.lineEdit_20 = QLineEdit(self.widget_146)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_98.addWidget(self.lineEdit_20)


        self.horizontalLayout_100.addWidget(self.widget_146)

        self.horizontalSpacer_87 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_100.addItem(self.horizontalSpacer_87)

        self.widget_147 = QWidget(self.widget_145)
        self.widget_147.setObjectName(u"widget_147")
        self.verticalLayout_99 = QVBoxLayout(self.widget_147)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.label_58 = QLabel(self.widget_147)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setAlignment(Qt.AlignCenter)

        self.verticalLayout_99.addWidget(self.label_58)

        self.lineEdit_21 = QLineEdit(self.widget_147)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_99.addWidget(self.lineEdit_21)


        self.horizontalLayout_100.addWidget(self.widget_147)

        self.horizontalSpacer_88 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_100.addItem(self.horizontalSpacer_88)

        self.widget_148 = QWidget(self.widget_145)
        self.widget_148.setObjectName(u"widget_148")
        self.verticalLayout_100 = QVBoxLayout(self.widget_148)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.label_59 = QLabel(self.widget_148)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setAlignment(Qt.AlignCenter)

        self.verticalLayout_100.addWidget(self.label_59)

        self.lineEdit_22 = QLineEdit(self.widget_148)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_100.addWidget(self.lineEdit_22)


        self.horizontalLayout_100.addWidget(self.widget_148)

        self.horizontalSpacer_89 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_100.addItem(self.horizontalSpacer_89)

        self.widget_149 = QWidget(self.widget_145)
        self.widget_149.setObjectName(u"widget_149")
        self.verticalLayout_101 = QVBoxLayout(self.widget_149)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.label_60 = QLabel(self.widget_149)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setAlignment(Qt.AlignCenter)

        self.verticalLayout_101.addWidget(self.label_60)

        self.lineEdit_23 = QLineEdit(self.widget_149)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_101.addWidget(self.lineEdit_23)


        self.horizontalLayout_100.addWidget(self.widget_149)

        self.horizontalSpacer_90 = QSpacerItem(11, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_100.addItem(self.horizontalSpacer_90)

        self.widget_150 = QWidget(self.widget_145)
        self.widget_150.setObjectName(u"widget_150")
        self.verticalLayout_102 = QVBoxLayout(self.widget_150)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.label_61 = QLabel(self.widget_150)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setLayoutDirection(Qt.LeftToRight)
        self.label_61.setAlignment(Qt.AlignCenter)

        self.verticalLayout_102.addWidget(self.label_61)

        self.lineEdit_24 = QLineEdit(self.widget_150)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_102.addWidget(self.lineEdit_24)


        self.horizontalLayout_100.addWidget(self.widget_150)


        self.verticalLayout_97.addWidget(self.widget_145)

        self.verticalSpacer_32 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_97.addItem(self.verticalSpacer_32)

        self.widget_151 = QWidget(self.widget_144)
        self.widget_151.setObjectName(u"widget_151")
        self.horizontalLayout_101 = QHBoxLayout(self.widget_151)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.widget_warning_24 = QWidget(self.widget_151)
        self.widget_warning_24.setObjectName(u"widget_warning_24")
        self.widget_warning_24.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_390 = QHBoxLayout(self.widget_warning_24)
        self.horizontalLayout_390.setSpacing(0)
        self.horizontalLayout_390.setObjectName(u"horizontalLayout_390")
        self.horizontalLayout_390.setContentsMargins(10, 5, 5, 5)
        self.label_288 = QLabel(self.widget_warning_24)
        self.label_288.setObjectName(u"label_288")
        self.label_288.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_390.addWidget(self.label_288)

        self.label_324 = QLabel(self.widget_warning_24)
        self.label_324.setObjectName(u"label_324")
        self.label_324.setMinimumSize(QSize(150, 0))
        self.label_324.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_324.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_390.addWidget(self.label_324)


        self.horizontalLayout_101.addWidget(self.widget_warning_24)

        self.horizontalSpacer_91 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_101.addItem(self.horizontalSpacer_91)

        self.pushButton_82 = QPushButton(self.widget_151)
        self.pushButton_82.setObjectName(u"pushButton_82")
        self.pushButton_82.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")
        self.pushButton_82.setCheckable(True)

        self.horizontalLayout_101.addWidget(self.pushButton_82)


        self.verticalLayout_97.addWidget(self.widget_151)


        self.horizontalLayout_97.addWidget(self.widget_144)


        self.verticalLayout_93.addWidget(self.widget_138)

        self.widget_152 = QWidget(self.widget_136)
        self.widget_152.setObjectName(u"widget_152")
        self.widget_152.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_103 = QVBoxLayout(self.widget_152)
        self.verticalLayout_103.setSpacing(0)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.verticalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.widget_153 = QWidget(self.widget_152)
        self.widget_153.setObjectName(u"widget_153")
        self.horizontalLayout_102 = QHBoxLayout(self.widget_153)
        self.horizontalLayout_102.setSpacing(0)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.horizontalLayout_102.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_103.addWidget(self.widget_153)


        self.verticalLayout_93.addWidget(self.widget_152)


        self.verticalLayout_61.addWidget(self.widget_136)

        self.widget_154 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_154.setObjectName(u"widget_154")
        self.verticalLayout_104 = QVBoxLayout(self.widget_154)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.widget_155 = QWidget(self.widget_154)
        self.widget_155.setObjectName(u"widget_155")
        self.widget_155.setStyleSheet(u"")
        self.horizontalLayout_103 = QHBoxLayout(self.widget_155)
        self.horizontalLayout_103.setSpacing(0)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.horizontalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_19 = QWidget(self.widget_155)
        self.Equipement_widget_19.setObjectName(u"Equipement_widget_19")
        self.Equipement_widget_19.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_104 = QHBoxLayout(self.Equipement_widget_19)
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.label_62 = QLabel(self.Equipement_widget_19)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setPixmap(QPixmap(u":/assets/icons/equippement-30.png"))

        self.horizontalLayout_104.addWidget(self.label_62, 0, Qt.AlignLeft)

        self.pushButton_83 = QPushButton(self.Equipement_widget_19)
        self.pushButton_83.setObjectName(u"pushButton_83")
        sizePolicy2.setHeightForWidth(self.pushButton_83.sizePolicy().hasHeightForWidth())
        self.pushButton_83.setSizePolicy(sizePolicy2)
        self.pushButton_83.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_83.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_83.setIcon(icon9)
        self.pushButton_83.setIconSize(QSize(24, 24))
        self.pushButton_83.setCheckable(True)

        self.horizontalLayout_104.addWidget(self.pushButton_83)


        self.horizontalLayout_103.addWidget(self.Equipement_widget_19)

        self.horizontalSpacer_92 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_103.addItem(self.horizontalSpacer_92)


        self.verticalLayout_104.addWidget(self.widget_155)

        self.widget_156 = QWidget(self.widget_154)
        self.widget_156.setObjectName(u"widget_156")
        self.widget_156.setMinimumSize(QSize(450, 0))
        self.widget_156.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.horizontalLayout_107 = QHBoxLayout(self.widget_156)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalSpacer_28 = QSpacerItem(255, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_107.addItem(self.horizontalSpacer_28)

        self.widget_24 = QWidget(self.widget_156)
        self.widget_24.setObjectName(u"widget_24")
        sizePolicy.setHeightForWidth(self.widget_24.sizePolicy().hasHeightForWidth())
        self.widget_24.setSizePolicy(sizePolicy)
        self.widget_24.setMinimumSize(QSize(400, 0))
        self.verticalLayout_105 = QVBoxLayout(self.widget_24)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.horizontalLayout_105 = QHBoxLayout()
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.horizontalSpacer_93 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_105.addItem(self.horizontalSpacer_93)

        self.label_197 = QLabel(self.widget_24)
        self.label_197.setObjectName(u"label_197")

        self.horizontalLayout_105.addWidget(self.label_197)

        self.horizontalSpacer_94 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_105.addItem(self.horizontalSpacer_94)


        self.verticalLayout_105.addLayout(self.horizontalLayout_105)

        self.widget_50 = QWidget(self.widget_24)
        self.widget_50.setObjectName(u"widget_50")
        self.horizontalLayout_106 = QHBoxLayout(self.widget_50)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.horizontalSpacer_95 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_106.addItem(self.horizontalSpacer_95)


        self.verticalLayout_105.addWidget(self.widget_50)

        self.lineEdit_25 = QLineEdit(self.widget_24)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_105.addWidget(self.lineEdit_25)


        self.horizontalLayout_107.addWidget(self.widget_24)

        self.horizontalSpacer_96 = QSpacerItem(237, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_107.addItem(self.horizontalSpacer_96)


        self.verticalLayout_104.addWidget(self.widget_156)

        self.widget_160 = QWidget(self.widget_154)
        self.widget_160.setObjectName(u"widget_160")
        self.widget_160.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_106 = QVBoxLayout(self.widget_160)
        self.verticalLayout_106.setSpacing(0)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.verticalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.widget_161 = QWidget(self.widget_160)
        self.widget_161.setObjectName(u"widget_161")
        self.horizontalLayout_109 = QHBoxLayout(self.widget_161)
        self.horizontalLayout_109.setSpacing(0)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.horizontalLayout_109.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_106.addWidget(self.widget_161)


        self.verticalLayout_104.addWidget(self.widget_160)


        self.verticalLayout_61.addWidget(self.widget_154)

        self.widget_162 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_162.setObjectName(u"widget_162")
        self.widget_162.setStyleSheet(u"")
        self.horizontalLayout_110 = QHBoxLayout(self.widget_162)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.Equipement_widget_20 = QWidget(self.widget_162)
        self.Equipement_widget_20.setObjectName(u"Equipement_widget_20")
        self.Equipement_widget_20.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 191, 191);\n"
"border-radius:10px;\n"
"color: white;\n"
"}\n"
"")
        self.horizontalLayout_111 = QHBoxLayout(self.Equipement_widget_20)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.pushButton_84 = QPushButton(self.Equipement_widget_20)
        self.pushButton_84.setObjectName(u"pushButton_84")
        sizePolicy2.setHeightForWidth(self.pushButton_84.sizePolicy().hasHeightForWidth())
        self.pushButton_84.setSizePolicy(sizePolicy2)
        self.pushButton_84.setFont(font5)
        self.pushButton_84.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_84.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(255, 191, 191);\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 191, 191);\n"
"}\n"
"")
        self.pushButton_84.setIcon(icon9)
        self.pushButton_84.setIconSize(QSize(24, 24))
        self.pushButton_84.setCheckable(True)

        self.horizontalLayout_111.addWidget(self.pushButton_84)


        self.horizontalLayout_110.addWidget(self.Equipement_widget_20)

        self.horizontalSpacer_99 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_110.addItem(self.horizontalSpacer_99)

        self.Equipement_widget_21 = QWidget(self.widget_162)
        self.Equipement_widget_21.setObjectName(u"Equipement_widget_21")
        self.Equipement_widget_21.setStyleSheet(u"QWidget{\n"
"background-color: rgb(104, 246, 73);\n"
"border-radius:10px;\n"
"color: white;\n"
"}\n"
"")
        self.horizontalLayout_112 = QHBoxLayout(self.Equipement_widget_21)
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.pushButton_85 = QPushButton(self.Equipement_widget_21)
        self.pushButton_85.setObjectName(u"pushButton_85")
        sizePolicy2.setHeightForWidth(self.pushButton_85.sizePolicy().hasHeightForWidth())
        self.pushButton_85.setSizePolicy(sizePolicy2)
        self.pushButton_85.setFont(font5)
        self.pushButton_85.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_85.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(104, 246, 73);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(104, 246, 73);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(104, 246, 73);\n"
"}\n"
"")
        self.pushButton_85.setIcon(icon9)
        self.pushButton_85.setIconSize(QSize(24, 24))
        self.pushButton_85.setCheckable(True)

        self.horizontalLayout_112.addWidget(self.pushButton_85)


        self.horizontalLayout_110.addWidget(self.Equipement_widget_21)


        self.verticalLayout_61.addWidget(self.widget_162)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_2.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.nv_dossier_prodINW_page)
        self.nv_dossier_prodIVD_page = QWidget()
        self.nv_dossier_prodIVD_page.setObjectName(u"nv_dossier_prodIVD_page")
        self.gridLayout_3 = QGridLayout(self.nv_dossier_prodIVD_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea_3 = QScrollArea(self.nv_dossier_prodIVD_page)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 634, 2274))
        self.verticalLayout_107 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.widget_163 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_163.setObjectName(u"widget_163")
        self.horizontalLayout_113 = QHBoxLayout(self.widget_163)
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.label_63 = QLabel(self.widget_163)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font4)

        self.horizontalLayout_113.addWidget(self.label_63)

        self.horizontalSpacer_255 = QSpacerItem(347, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_113.addItem(self.horizontalSpacer_255)

        self.label_64 = QLabel(self.widget_163)
        self.label_64.setObjectName(u"label_64")

        self.horizontalLayout_113.addWidget(self.label_64)

        self.horizontalSpacer_256 = QSpacerItem(346, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_113.addItem(self.horizontalSpacer_256)

        self.label_136 = QLabel(self.widget_163)
        self.label_136.setObjectName(u"label_136")

        self.horizontalLayout_113.addWidget(self.label_136)


        self.verticalLayout_107.addWidget(self.widget_163)

        self.widget_164 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_164.setObjectName(u"widget_164")
        self.verticalLayout_108 = QVBoxLayout(self.widget_164)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.widget_165 = QWidget(self.widget_164)
        self.widget_165.setObjectName(u"widget_165")
        self.horizontalLayout_114 = QHBoxLayout(self.widget_165)
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.horizontalLayout_114.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_22 = QWidget(self.widget_165)
        self.Equipement_widget_22.setObjectName(u"Equipement_widget_22")
        self.Equipement_widget_22.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_115 = QHBoxLayout(self.Equipement_widget_22)
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.label_65 = QLabel(self.Equipement_widget_22)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setPixmap(QPixmap(u":/assets/icons/employee-30.png"))

        self.horizontalLayout_115.addWidget(self.label_65, 0, Qt.AlignLeft)

        self.pushButton_86 = QPushButton(self.Equipement_widget_22)
        self.pushButton_86.setObjectName(u"pushButton_86")
        sizePolicy2.setHeightForWidth(self.pushButton_86.sizePolicy().hasHeightForWidth())
        self.pushButton_86.setSizePolicy(sizePolicy2)
        self.pushButton_86.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_86.setStyleSheet(u"")
        self.pushButton_86.setIconSize(QSize(24, 24))
        self.pushButton_86.setCheckable(True)

        self.horizontalLayout_115.addWidget(self.pushButton_86)


        self.horizontalLayout_114.addWidget(self.Equipement_widget_22)

        self.horizontalSpacer_100 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_114.addItem(self.horizontalSpacer_100)


        self.verticalLayout_108.addWidget(self.widget_165)

        self.widget_166 = QWidget(self.widget_164)
        self.widget_166.setObjectName(u"widget_166")
        self.widget_166.setMinimumSize(QSize(0, 0))
        self.widget_166.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.verticalLayout_299 = QVBoxLayout(self.widget_166)
        self.verticalLayout_299.setObjectName(u"verticalLayout_299")
        self.horizontalLayout_108 = QHBoxLayout()
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.horizontalSpacer_101 = QSpacerItem(34, 207, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_108.addItem(self.horizontalSpacer_101)

        self.widget_167 = QWidget(self.widget_166)
        self.widget_167.setObjectName(u"widget_167")
        sizePolicy.setHeightForWidth(self.widget_167.sizePolicy().hasHeightForWidth())
        self.widget_167.setSizePolicy(sizePolicy)
        self.widget_167.setMinimumSize(QSize(0, 0))
        self.verticalLayout_109 = QVBoxLayout(self.widget_167)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.textEdit_25 = QTextEdit(self.widget_167)
        self.textEdit_25.setObjectName(u"textEdit_25")
        sizePolicy4.setHeightForWidth(self.textEdit_25.sizePolicy().hasHeightForWidth())
        self.textEdit_25.setSizePolicy(sizePolicy4)
        self.textEdit_25.setMinimumSize(QSize(0, 0))
        self.textEdit_25.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_109.addWidget(self.textEdit_25)

        self.textEdit_26 = QTextEdit(self.widget_167)
        self.textEdit_26.setObjectName(u"textEdit_26")
        sizePolicy4.setHeightForWidth(self.textEdit_26.sizePolicy().hasHeightForWidth())
        self.textEdit_26.setSizePolicy(sizePolicy4)
        self.textEdit_26.setMinimumSize(QSize(0, 0))
        self.textEdit_26.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_109.addWidget(self.textEdit_26)

        self.widget_168 = QWidget(self.widget_167)
        self.widget_168.setObjectName(u"widget_168")
        self.verticalLayout_110 = QVBoxLayout(self.widget_168)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.checkBox_9 = QCheckBox(self.widget_168)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setChecked(True)

        self.verticalLayout_110.addWidget(self.checkBox_9)

        self.checkBox_10 = QCheckBox(self.widget_168)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.verticalLayout_110.addWidget(self.checkBox_10)


        self.verticalLayout_109.addWidget(self.widget_168)

        self.widget_169 = QWidget(self.widget_167)
        self.widget_169.setObjectName(u"widget_169")
        self.horizontalLayout_117 = QHBoxLayout(self.widget_169)
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.dateEdit_5 = QDateEdit(self.widget_169)
        self.dateEdit_5.setObjectName(u"dateEdit_5")
        self.dateEdit_5.setDateTime(QDateTime(QDate(2024, 10, 31), QTime(17, 0, 0)))
        self.dateEdit_5.setCalendarPopup(True)

        self.horizontalLayout_117.addWidget(self.dateEdit_5)

        self.horizontalSpacer_102 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_117.addItem(self.horizontalSpacer_102)


        self.verticalLayout_109.addWidget(self.widget_169)


        self.horizontalLayout_108.addWidget(self.widget_167)

        self.horizontalSpacer_103 = QSpacerItem(34, 207, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_108.addItem(self.horizontalSpacer_103)

        self.horizontalSpacer_104 = QSpacerItem(29, 207, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_108.addItem(self.horizontalSpacer_104)

        self.widget_170 = QWidget(self.widget_166)
        self.widget_170.setObjectName(u"widget_170")
        self.widget_170.setMinimumSize(QSize(0, 0))
        self.widget_170.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_111 = QVBoxLayout(self.widget_170)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.textEdit_27 = QTextEdit(self.widget_170)
        self.textEdit_27.setObjectName(u"textEdit_27")
        sizePolicy4.setHeightForWidth(self.textEdit_27.sizePolicy().hasHeightForWidth())
        self.textEdit_27.setSizePolicy(sizePolicy4)
        self.textEdit_27.setMinimumSize(QSize(0, 0))
        self.textEdit_27.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_111.addWidget(self.textEdit_27)

        self.widget_171 = QWidget(self.widget_170)
        self.widget_171.setObjectName(u"widget_171")
        self.verticalLayout_112 = QVBoxLayout(self.widget_171)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.checkBox_11 = QCheckBox(self.widget_171)
        self.checkBox_11.setObjectName(u"checkBox_11")
        self.checkBox_11.setChecked(True)

        self.verticalLayout_112.addWidget(self.checkBox_11)

        self.checkBox_12 = QCheckBox(self.widget_171)
        self.checkBox_12.setObjectName(u"checkBox_12")

        self.verticalLayout_112.addWidget(self.checkBox_12)


        self.verticalLayout_111.addWidget(self.widget_171)

        self.widget_172 = QWidget(self.widget_170)
        self.widget_172.setObjectName(u"widget_172")
        self.horizontalLayout_118 = QHBoxLayout(self.widget_172)
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.label_66 = QLabel(self.widget_172)
        self.label_66.setObjectName(u"label_66")

        self.horizontalLayout_118.addWidget(self.label_66)

        self.lineEdit_26 = QLineEdit(self.widget_172)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_118.addWidget(self.lineEdit_26)


        self.verticalLayout_111.addWidget(self.widget_172)


        self.horizontalLayout_108.addWidget(self.widget_170)

        self.horizontalSpacer_106 = QSpacerItem(89, 207, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_108.addItem(self.horizontalSpacer_106)


        self.verticalLayout_299.addLayout(self.horizontalLayout_108)

        self.widget_173 = QWidget(self.widget_166)
        self.widget_173.setObjectName(u"widget_173")
        self.horizontalLayout_119 = QHBoxLayout(self.widget_173)
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.widget_warning_25 = QWidget(self.widget_173)
        self.widget_warning_25.setObjectName(u"widget_warning_25")
        self.widget_warning_25.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_391 = QHBoxLayout(self.widget_warning_25)
        self.horizontalLayout_391.setSpacing(0)
        self.horizontalLayout_391.setObjectName(u"horizontalLayout_391")
        self.horizontalLayout_391.setContentsMargins(10, 5, 5, 5)
        self.label_289 = QLabel(self.widget_warning_25)
        self.label_289.setObjectName(u"label_289")
        self.label_289.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_391.addWidget(self.label_289)

        self.label_325 = QLabel(self.widget_warning_25)
        self.label_325.setObjectName(u"label_325")
        self.label_325.setMinimumSize(QSize(150, 0))
        self.label_325.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_325.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_391.addWidget(self.label_325)


        self.horizontalLayout_119.addWidget(self.widget_warning_25)

        self.horizontalSpacer_105 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_119.addItem(self.horizontalSpacer_105)

        self.pushButton_87 = QPushButton(self.widget_173)
        self.pushButton_87.setObjectName(u"pushButton_87")
        self.pushButton_87.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_87.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_119.addWidget(self.pushButton_87)


        self.verticalLayout_299.addWidget(self.widget_173)


        self.verticalLayout_108.addWidget(self.widget_166)


        self.verticalLayout_107.addWidget(self.widget_164)

        self.widget_174 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_174.setObjectName(u"widget_174")
        self.verticalLayout_113 = QVBoxLayout(self.widget_174)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.widget_175 = QWidget(self.widget_174)
        self.widget_175.setObjectName(u"widget_175")
        self.horizontalLayout_120 = QHBoxLayout(self.widget_175)
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.horizontalLayout_120.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_23 = QWidget(self.widget_175)
        self.Equipement_widget_23.setObjectName(u"Equipement_widget_23")
        self.Equipement_widget_23.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_121 = QHBoxLayout(self.Equipement_widget_23)
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.label_68 = QLabel(self.Equipement_widget_23)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setPixmap(QPixmap(u":/assets/icons/employee-30.png"))

        self.horizontalLayout_121.addWidget(self.label_68, 0, Qt.AlignLeft)

        self.pushButton_88 = QPushButton(self.Equipement_widget_23)
        self.pushButton_88.setObjectName(u"pushButton_88")
        sizePolicy2.setHeightForWidth(self.pushButton_88.sizePolicy().hasHeightForWidth())
        self.pushButton_88.setSizePolicy(sizePolicy2)
        self.pushButton_88.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_88.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_88.setIcon(icon9)
        self.pushButton_88.setIconSize(QSize(24, 24))
        self.pushButton_88.setCheckable(True)

        self.horizontalLayout_121.addWidget(self.pushButton_88)


        self.horizontalLayout_120.addWidget(self.Equipement_widget_23)

        self.horizontalSpacer_107 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_120.addItem(self.horizontalSpacer_107)


        self.verticalLayout_113.addWidget(self.widget_175)

        self.widget_176 = QWidget(self.widget_174)
        self.widget_176.setObjectName(u"widget_176")
        self.widget_176.setMinimumSize(QSize(450, 0))
        self.widget_176.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.verticalLayout_300 = QVBoxLayout(self.widget_176)
        self.verticalLayout_300.setObjectName(u"verticalLayout_300")
        self.horizontalLayout_116 = QHBoxLayout()
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.widget_177 = QWidget(self.widget_176)
        self.widget_177.setObjectName(u"widget_177")
        self.verticalLayout_114 = QVBoxLayout(self.widget_177)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.textEdit_28 = QTextEdit(self.widget_177)
        self.textEdit_28.setObjectName(u"textEdit_28")
        sizePolicy4.setHeightForWidth(self.textEdit_28.sizePolicy().hasHeightForWidth())
        self.textEdit_28.setSizePolicy(sizePolicy4)
        self.textEdit_28.setMinimumSize(QSize(0, 0))
        self.textEdit_28.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_114.addWidget(self.textEdit_28)

        self.verticalSpacer_34 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_114.addItem(self.verticalSpacer_34)


        self.horizontalLayout_116.addWidget(self.widget_177)

        self.widget_178 = QWidget(self.widget_176)
        self.widget_178.setObjectName(u"widget_178")
        self.widget_178.setMinimumSize(QSize(400, 0))
        self.verticalLayout_115 = QVBoxLayout(self.widget_178)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.verticalLayout_115.setContentsMargins(4, 4, 4, 4)
        self.textEdit_29 = QTextEdit(self.widget_178)
        self.textEdit_29.setObjectName(u"textEdit_29")
        sizePolicy4.setHeightForWidth(self.textEdit_29.sizePolicy().hasHeightForWidth())
        self.textEdit_29.setSizePolicy(sizePolicy4)
        self.textEdit_29.setMinimumSize(QSize(0, 0))
        self.textEdit_29.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_115.addWidget(self.textEdit_29)

        self.textEdit_30 = QTextEdit(self.widget_178)
        self.textEdit_30.setObjectName(u"textEdit_30")
        self.textEdit_30.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_115.addWidget(self.textEdit_30)


        self.horizontalLayout_116.addWidget(self.widget_178)

        self.horizontalSpacer_109 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_116.addItem(self.horizontalSpacer_109)


        self.verticalLayout_300.addLayout(self.horizontalLayout_116)

        self.widget_493 = QWidget(self.widget_176)
        self.widget_493.setObjectName(u"widget_493")
        self.horizontalLayout_122 = QHBoxLayout(self.widget_493)
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.widget_warning_26 = QWidget(self.widget_493)
        self.widget_warning_26.setObjectName(u"widget_warning_26")
        self.widget_warning_26.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_392 = QHBoxLayout(self.widget_warning_26)
        self.horizontalLayout_392.setSpacing(0)
        self.horizontalLayout_392.setObjectName(u"horizontalLayout_392")
        self.horizontalLayout_392.setContentsMargins(10, 5, 5, 5)
        self.label_258 = QLabel(self.widget_warning_26)
        self.label_258.setObjectName(u"label_258")
        self.label_258.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_392.addWidget(self.label_258)

        self.label_326 = QLabel(self.widget_warning_26)
        self.label_326.setObjectName(u"label_326")
        self.label_326.setMinimumSize(QSize(150, 0))
        self.label_326.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_326.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_392.addWidget(self.label_326)


        self.horizontalLayout_122.addWidget(self.widget_warning_26)

        self.horizontalSpacer_335 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_122.addItem(self.horizontalSpacer_335)

        self.pushButton_164 = QPushButton(self.widget_493)
        self.pushButton_164.setObjectName(u"pushButton_164")
        self.pushButton_164.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_164.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_122.addWidget(self.pushButton_164)


        self.verticalLayout_300.addWidget(self.widget_493)


        self.verticalLayout_113.addWidget(self.widget_176)


        self.verticalLayout_107.addWidget(self.widget_174)

        self.widget_180 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_180.setObjectName(u"widget_180")
        self.verticalLayout_116 = QVBoxLayout(self.widget_180)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.widget_181 = QWidget(self.widget_180)
        self.widget_181.setObjectName(u"widget_181")
        self.horizontalLayout_124 = QHBoxLayout(self.widget_181)
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.horizontalLayout_124.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_24 = QWidget(self.widget_181)
        self.Equipement_widget_24.setObjectName(u"Equipement_widget_24")
        self.Equipement_widget_24.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_125 = QHBoxLayout(self.Equipement_widget_24)
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.label_69 = QLabel(self.Equipement_widget_24)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setPixmap(QPixmap(u":/assets/icons/employee-30.png"))

        self.horizontalLayout_125.addWidget(self.label_69, 0, Qt.AlignLeft)

        self.pushButton_90 = QPushButton(self.Equipement_widget_24)
        self.pushButton_90.setObjectName(u"pushButton_90")
        sizePolicy2.setHeightForWidth(self.pushButton_90.sizePolicy().hasHeightForWidth())
        self.pushButton_90.setSizePolicy(sizePolicy2)
        self.pushButton_90.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_90.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_90.setIcon(icon9)
        self.pushButton_90.setIconSize(QSize(24, 24))
        self.pushButton_90.setCheckable(True)

        self.horizontalLayout_125.addWidget(self.pushButton_90)


        self.horizontalLayout_124.addWidget(self.Equipement_widget_24)

        self.horizontalSpacer_110 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_124.addItem(self.horizontalSpacer_110)


        self.verticalLayout_116.addWidget(self.widget_181)

        self.widget_182 = QWidget(self.widget_180)
        self.widget_182.setObjectName(u"widget_182")
        self.widget_182.setMinimumSize(QSize(450, 0))
        self.widget_182.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.verticalLayout_301 = QVBoxLayout(self.widget_182)
        self.verticalLayout_301.setObjectName(u"verticalLayout_301")
        self.horizontalLayout_123 = QHBoxLayout()
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.widget_183 = QWidget(self.widget_182)
        self.widget_183.setObjectName(u"widget_183")
        sizePolicy.setHeightForWidth(self.widget_183.sizePolicy().hasHeightForWidth())
        self.widget_183.setSizePolicy(sizePolicy)
        self.widget_183.setMinimumSize(QSize(0, 0))
        self.verticalLayout_117 = QVBoxLayout(self.widget_183)
        self.verticalLayout_117.setSpacing(10)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.verticalLayout_117.setContentsMargins(4, 4, 4, 4)
        self.textEdit_31 = QTextEdit(self.widget_183)
        self.textEdit_31.setObjectName(u"textEdit_31")
        sizePolicy4.setHeightForWidth(self.textEdit_31.sizePolicy().hasHeightForWidth())
        self.textEdit_31.setSizePolicy(sizePolicy4)
        self.textEdit_31.setMinimumSize(QSize(0, 0))
        self.textEdit_31.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_117.addWidget(self.textEdit_31)

        self.comboBox_11 = QComboBox(self.widget_183)
        self.comboBox_11.setObjectName(u"comboBox_11")
        self.comboBox_11.setMinimumSize(QSize(400, 0))
        self.comboBox_11.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_117.addWidget(self.comboBox_11)

        self.widget_184 = QWidget(self.widget_183)
        self.widget_184.setObjectName(u"widget_184")
        self.horizontalLayout_127 = QHBoxLayout(self.widget_184)
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.horizontalSpacer_111 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_127.addItem(self.horizontalSpacer_111)

        self.pushButton_91 = QPushButton(self.widget_184)
        self.pushButton_91.setObjectName(u"pushButton_91")
        self.pushButton_91.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_127.addWidget(self.pushButton_91)


        self.verticalLayout_117.addWidget(self.widget_184)

        self.verticalSpacer_35 = QSpacerItem(20, 148, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_117.addItem(self.verticalSpacer_35)


        self.horizontalLayout_123.addWidget(self.widget_183)

        self.horizontalSpacer_112 = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_123.addItem(self.horizontalSpacer_112)

        self.widget_185 = QWidget(self.widget_182)
        self.widget_185.setObjectName(u"widget_185")
        self.widget_185.setMinimumSize(QSize(400, 0))
        self.verticalLayout_118 = QVBoxLayout(self.widget_185)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.verticalLayout_118.setContentsMargins(4, 4, 4, 4)
        self.listView_7 = QListView(self.widget_185)
        self.listView_7.setObjectName(u"listView_7")
        self.listView_7.setMinimumSize(QSize(500, 0))
        self.listView_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_118.addWidget(self.listView_7)

        self.widget_186 = QWidget(self.widget_185)
        self.widget_186.setObjectName(u"widget_186")
        self.horizontalLayout_128 = QHBoxLayout(self.widget_186)
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.pushButton_92 = QPushButton(self.widget_186)
        self.pushButton_92.setObjectName(u"pushButton_92")
        self.pushButton_92.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_92.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_128.addWidget(self.pushButton_92)

        self.horizontalSpacer_113 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_128.addItem(self.horizontalSpacer_113)


        self.verticalLayout_118.addWidget(self.widget_186)


        self.horizontalLayout_123.addWidget(self.widget_185)

        self.horizontalSpacer_114 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_123.addItem(self.horizontalSpacer_114)


        self.verticalLayout_301.addLayout(self.horizontalLayout_123)

        self.widget_179 = QWidget(self.widget_182)
        self.widget_179.setObjectName(u"widget_179")
        self.horizontalLayout_126 = QHBoxLayout(self.widget_179)
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.widget_warning_27 = QWidget(self.widget_179)
        self.widget_warning_27.setObjectName(u"widget_warning_27")
        self.widget_warning_27.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_393 = QHBoxLayout(self.widget_warning_27)
        self.horizontalLayout_393.setSpacing(0)
        self.horizontalLayout_393.setObjectName(u"horizontalLayout_393")
        self.horizontalLayout_393.setContentsMargins(10, 5, 5, 5)
        self.label_262 = QLabel(self.widget_warning_27)
        self.label_262.setObjectName(u"label_262")
        self.label_262.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_393.addWidget(self.label_262)

        self.label_327 = QLabel(self.widget_warning_27)
        self.label_327.setObjectName(u"label_327")
        self.label_327.setMinimumSize(QSize(150, 0))
        self.label_327.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_327.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_393.addWidget(self.label_327)


        self.horizontalLayout_126.addWidget(self.widget_warning_27)

        self.horizontalSpacer_108 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_126.addItem(self.horizontalSpacer_108)

        self.pushButton_89 = QPushButton(self.widget_179)
        self.pushButton_89.setObjectName(u"pushButton_89")
        self.pushButton_89.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_89.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_126.addWidget(self.pushButton_89)


        self.verticalLayout_301.addWidget(self.widget_179)


        self.verticalLayout_116.addWidget(self.widget_182)


        self.verticalLayout_107.addWidget(self.widget_180)

        self.widget_187 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_187.setObjectName(u"widget_187")
        self.verticalLayout_119 = QVBoxLayout(self.widget_187)
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")
        self.widget_188 = QWidget(self.widget_187)
        self.widget_188.setObjectName(u"widget_188")
        self.widget_188.setStyleSheet(u"")
        self.horizontalLayout_129 = QHBoxLayout(self.widget_188)
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.horizontalLayout_129.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_25 = QWidget(self.widget_188)
        self.Equipement_widget_25.setObjectName(u"Equipement_widget_25")
        self.Equipement_widget_25.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_130 = QHBoxLayout(self.Equipement_widget_25)
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.label_70 = QLabel(self.Equipement_widget_25)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setPixmap(QPixmap(u":/assets/icons/equippement-30.png"))

        self.horizontalLayout_130.addWidget(self.label_70, 0, Qt.AlignLeft)

        self.pushButton_93 = QPushButton(self.Equipement_widget_25)
        self.pushButton_93.setObjectName(u"pushButton_93")
        sizePolicy2.setHeightForWidth(self.pushButton_93.sizePolicy().hasHeightForWidth())
        self.pushButton_93.setSizePolicy(sizePolicy2)
        self.pushButton_93.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_93.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_93.setIcon(icon9)
        self.pushButton_93.setIconSize(QSize(24, 24))
        self.pushButton_93.setCheckable(True)

        self.horizontalLayout_130.addWidget(self.pushButton_93)


        self.horizontalLayout_129.addWidget(self.Equipement_widget_25)

        self.horizontalSpacer_115 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_129.addItem(self.horizontalSpacer_115)


        self.verticalLayout_119.addWidget(self.widget_188)

        self.widget_189 = QWidget(self.widget_187)
        self.widget_189.setObjectName(u"widget_189")
        self.widget_189.setMinimumSize(QSize(450, 0))
        self.widget_189.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.verticalLayout_306 = QVBoxLayout(self.widget_189)
        self.verticalLayout_306.setObjectName(u"verticalLayout_306")
        self.horizontalLayout_131 = QHBoxLayout()
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.widget_190 = QWidget(self.widget_189)
        self.widget_190.setObjectName(u"widget_190")
        sizePolicy.setHeightForWidth(self.widget_190.sizePolicy().hasHeightForWidth())
        self.widget_190.setSizePolicy(sizePolicy)
        self.widget_190.setMinimumSize(QSize(0, 0))
        self.verticalLayout_120 = QVBoxLayout(self.widget_190)
        self.verticalLayout_120.setSpacing(10)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")
        self.verticalLayout_120.setContentsMargins(4, 4, 4, 4)
        self.textEdit_32 = QTextEdit(self.widget_190)
        self.textEdit_32.setObjectName(u"textEdit_32")
        sizePolicy4.setHeightForWidth(self.textEdit_32.sizePolicy().hasHeightForWidth())
        self.textEdit_32.setSizePolicy(sizePolicy4)
        self.textEdit_32.setMinimumSize(QSize(0, 0))
        self.textEdit_32.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_120.addWidget(self.textEdit_32)

        self.comboBox_12 = QComboBox(self.widget_190)
        self.comboBox_12.setObjectName(u"comboBox_12")
        self.comboBox_12.setMinimumSize(QSize(400, 0))
        self.comboBox_12.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_120.addWidget(self.comboBox_12)

        self.widget_191 = QWidget(self.widget_190)
        self.widget_191.setObjectName(u"widget_191")
        self.horizontalLayout_132 = QHBoxLayout(self.widget_191)
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.horizontalSpacer_116 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_132.addItem(self.horizontalSpacer_116)

        self.pushButton_94 = QPushButton(self.widget_191)
        self.pushButton_94.setObjectName(u"pushButton_94")
        self.pushButton_94.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_132.addWidget(self.pushButton_94)


        self.verticalLayout_120.addWidget(self.widget_191)

        self.verticalSpacer_36 = QSpacerItem(20, 148, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_120.addItem(self.verticalSpacer_36)


        self.horizontalLayout_131.addWidget(self.widget_190)

        self.horizontalSpacer_117 = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_131.addItem(self.horizontalSpacer_117)

        self.widget_192 = QWidget(self.widget_189)
        self.widget_192.setObjectName(u"widget_192")
        self.widget_192.setMinimumSize(QSize(400, 0))
        self.verticalLayout_121 = QVBoxLayout(self.widget_192)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.verticalLayout_121.setContentsMargins(4, 4, 4, 4)
        self.listView_8 = QListView(self.widget_192)
        self.listView_8.setObjectName(u"listView_8")
        self.listView_8.setMinimumSize(QSize(500, 0))
        self.listView_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_121.addWidget(self.listView_8)

        self.widget_193 = QWidget(self.widget_192)
        self.widget_193.setObjectName(u"widget_193")
        self.horizontalLayout_133 = QHBoxLayout(self.widget_193)
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.pushButton_95 = QPushButton(self.widget_193)
        self.pushButton_95.setObjectName(u"pushButton_95")
        self.pushButton_95.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_95.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_133.addWidget(self.pushButton_95)

        self.horizontalSpacer_118 = QSpacerItem(361, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_133.addItem(self.horizontalSpacer_118)


        self.verticalLayout_121.addWidget(self.widget_193)


        self.horizontalLayout_131.addWidget(self.widget_192)

        self.horizontalSpacer_119 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_131.addItem(self.horizontalSpacer_119)


        self.verticalLayout_306.addLayout(self.horizontalLayout_131)

        self.widget_494 = QWidget(self.widget_189)
        self.widget_494.setObjectName(u"widget_494")
        self.horizontalLayout_318 = QHBoxLayout(self.widget_494)
        self.horizontalLayout_318.setObjectName(u"horizontalLayout_318")
        self.widget_warning_28 = QWidget(self.widget_494)
        self.widget_warning_28.setObjectName(u"widget_warning_28")
        self.widget_warning_28.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_394 = QHBoxLayout(self.widget_warning_28)
        self.horizontalLayout_394.setSpacing(0)
        self.horizontalLayout_394.setObjectName(u"horizontalLayout_394")
        self.horizontalLayout_394.setContentsMargins(10, 5, 5, 5)
        self.label_263 = QLabel(self.widget_warning_28)
        self.label_263.setObjectName(u"label_263")
        self.label_263.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_394.addWidget(self.label_263)

        self.label_328 = QLabel(self.widget_warning_28)
        self.label_328.setObjectName(u"label_328")
        self.label_328.setMinimumSize(QSize(150, 0))
        self.label_328.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_328.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_394.addWidget(self.label_328)


        self.horizontalLayout_318.addWidget(self.widget_warning_28)

        self.horizontalSpacer_336 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_318.addItem(self.horizontalSpacer_336)

        self.pushButton_174 = QPushButton(self.widget_494)
        self.pushButton_174.setObjectName(u"pushButton_174")
        self.pushButton_174.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_174.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_318.addWidget(self.pushButton_174)


        self.verticalLayout_306.addWidget(self.widget_494)


        self.verticalLayout_119.addWidget(self.widget_189)

        self.widget_194 = QWidget(self.widget_187)
        self.widget_194.setObjectName(u"widget_194")
        self.widget_194.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_122 = QVBoxLayout(self.widget_194)
        self.verticalLayout_122.setSpacing(0)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")
        self.verticalLayout_122.setContentsMargins(0, 0, 0, 0)
        self.widget_195 = QWidget(self.widget_194)
        self.widget_195.setObjectName(u"widget_195")
        self.horizontalLayout_134 = QHBoxLayout(self.widget_195)
        self.horizontalLayout_134.setSpacing(0)
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.horizontalLayout_134.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_122.addWidget(self.widget_195)


        self.verticalLayout_119.addWidget(self.widget_194)


        self.verticalLayout_107.addWidget(self.widget_187)

        self.widget_196 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_196.setObjectName(u"widget_196")
        self.verticalLayout_123 = QVBoxLayout(self.widget_196)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.widget_197 = QWidget(self.widget_196)
        self.widget_197.setObjectName(u"widget_197")
        self.widget_197.setStyleSheet(u"")
        self.horizontalLayout_135 = QHBoxLayout(self.widget_197)
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.horizontalLayout_135.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_26 = QWidget(self.widget_197)
        self.Equipement_widget_26.setObjectName(u"Equipement_widget_26")
        self.Equipement_widget_26.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_136 = QHBoxLayout(self.Equipement_widget_26)
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.label_71 = QLabel(self.Equipement_widget_26)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setPixmap(QPixmap(u":/assets/icons/equippement-30.png"))

        self.horizontalLayout_136.addWidget(self.label_71, 0, Qt.AlignLeft)

        self.pushButton_96 = QPushButton(self.Equipement_widget_26)
        self.pushButton_96.setObjectName(u"pushButton_96")
        sizePolicy2.setHeightForWidth(self.pushButton_96.sizePolicy().hasHeightForWidth())
        self.pushButton_96.setSizePolicy(sizePolicy2)
        self.pushButton_96.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_96.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_96.setIcon(icon9)
        self.pushButton_96.setIconSize(QSize(24, 24))
        self.pushButton_96.setCheckable(True)

        self.horizontalLayout_136.addWidget(self.pushButton_96)


        self.horizontalLayout_135.addWidget(self.Equipement_widget_26)

        self.horizontalSpacer_120 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_135.addItem(self.horizontalSpacer_120)


        self.verticalLayout_123.addWidget(self.widget_197)

        self.widget_198 = QWidget(self.widget_196)
        self.widget_198.setObjectName(u"widget_198")
        self.widget_198.setMinimumSize(QSize(450, 0))
        self.widget_198.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.horizontalLayout_137 = QHBoxLayout(self.widget_198)
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.horizontalLayout_137.setContentsMargins(10, 10, 10, 10)
        self.widget_199 = QWidget(self.widget_198)
        self.widget_199.setObjectName(u"widget_199")
        sizePolicy.setHeightForWidth(self.widget_199.sizePolicy().hasHeightForWidth())
        self.widget_199.setSizePolicy(sizePolicy)
        self.widget_199.setMinimumSize(QSize(400, 0))
        self.verticalLayout_124 = QVBoxLayout(self.widget_199)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.textEdit_33 = QTextEdit(self.widget_199)
        self.textEdit_33.setObjectName(u"textEdit_33")
        sizePolicy4.setHeightForWidth(self.textEdit_33.sizePolicy().hasHeightForWidth())
        self.textEdit_33.setSizePolicy(sizePolicy4)
        self.textEdit_33.setMinimumSize(QSize(0, 0))
        self.textEdit_33.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_124.addWidget(self.textEdit_33)

        self.widget_200 = QWidget(self.widget_199)
        self.widget_200.setObjectName(u"widget_200")
        self.horizontalLayout_138 = QHBoxLayout(self.widget_200)
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.horizontalLayout_138.setContentsMargins(10, 10, 10, 10)
        self.horizontalSpacer_121 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_138.addItem(self.horizontalSpacer_121)

        self.widget_201 = QWidget(self.widget_200)
        self.widget_201.setObjectName(u"widget_201")
        sizePolicy5.setHeightForWidth(self.widget_201.sizePolicy().hasHeightForWidth())
        self.widget_201.setSizePolicy(sizePolicy5)
        self.widget_201.setMinimumSize(QSize(300, 0))
        self.verticalLayout_125 = QVBoxLayout(self.widget_201)
        self.verticalLayout_125.setObjectName(u"verticalLayout_125")
        self.label_72 = QLabel(self.widget_201)
        self.label_72.setObjectName(u"label_72")

        self.verticalLayout_125.addWidget(self.label_72)

        self.verticalSpacer_37 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_125.addItem(self.verticalSpacer_37)

        self.comboBox_13 = QComboBox(self.widget_201)
        self.comboBox_13.setObjectName(u"comboBox_13")
        self.comboBox_13.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_125.addWidget(self.comboBox_13)


        self.horizontalLayout_138.addWidget(self.widget_201)

        self.horizontalSpacer_122 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_138.addItem(self.horizontalSpacer_122)

        self.widget_202 = QWidget(self.widget_200)
        self.widget_202.setObjectName(u"widget_202")
        self.verticalLayout_126 = QVBoxLayout(self.widget_202)
        self.verticalLayout_126.setObjectName(u"verticalLayout_126")
        self.label_73 = QLabel(self.widget_202)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setAlignment(Qt.AlignCenter)

        self.verticalLayout_126.addWidget(self.label_73)

        self.verticalSpacer_38 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_126.addItem(self.verticalSpacer_38)

        self.lineEdit_27 = QLineEdit(self.widget_202)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_126.addWidget(self.lineEdit_27)


        self.horizontalLayout_138.addWidget(self.widget_202)

        self.horizontalSpacer_123 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_138.addItem(self.horizontalSpacer_123)

        self.widget_203 = QWidget(self.widget_200)
        self.widget_203.setObjectName(u"widget_203")
        self.verticalLayout_127 = QVBoxLayout(self.widget_203)
        self.verticalLayout_127.setObjectName(u"verticalLayout_127")
        self.label_74 = QLabel(self.widget_203)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setAlignment(Qt.AlignCenter)

        self.verticalLayout_127.addWidget(self.label_74)

        self.verticalSpacer_39 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_127.addItem(self.verticalSpacer_39)

        self.lineEdit_28 = QLineEdit(self.widget_203)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_127.addWidget(self.lineEdit_28)


        self.horizontalLayout_138.addWidget(self.widget_203)

        self.horizontalSpacer_124 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_138.addItem(self.horizontalSpacer_124)

        self.widget_204 = QWidget(self.widget_200)
        self.widget_204.setObjectName(u"widget_204")
        self.verticalLayout_128 = QVBoxLayout(self.widget_204)
        self.verticalLayout_128.setObjectName(u"verticalLayout_128")
        self.label_75 = QLabel(self.widget_204)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setAlignment(Qt.AlignCenter)

        self.verticalLayout_128.addWidget(self.label_75)

        self.verticalSpacer_40 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_128.addItem(self.verticalSpacer_40)

        self.lineEdit_29 = QLineEdit(self.widget_204)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_128.addWidget(self.lineEdit_29)


        self.horizontalLayout_138.addWidget(self.widget_204)

        self.horizontalSpacer_125 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_138.addItem(self.horizontalSpacer_125)

        self.widget_205 = QWidget(self.widget_200)
        self.widget_205.setObjectName(u"widget_205")
        self.verticalLayout_129 = QVBoxLayout(self.widget_205)
        self.verticalLayout_129.setObjectName(u"verticalLayout_129")
        self.label_76 = QLabel(self.widget_205)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setAlignment(Qt.AlignCenter)

        self.verticalLayout_129.addWidget(self.label_76)

        self.verticalSpacer_41 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_129.addItem(self.verticalSpacer_41)

        self.lineEdit_30 = QLineEdit(self.widget_205)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        self.lineEdit_30.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_129.addWidget(self.lineEdit_30)


        self.horizontalLayout_138.addWidget(self.widget_205)

        self.horizontalSpacer_126 = QSpacerItem(11, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_138.addItem(self.horizontalSpacer_126)

        self.widget_206 = QWidget(self.widget_200)
        self.widget_206.setObjectName(u"widget_206")
        self.verticalLayout_130 = QVBoxLayout(self.widget_206)
        self.verticalLayout_130.setObjectName(u"verticalLayout_130")
        self.label_77 = QLabel(self.widget_206)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setLayoutDirection(Qt.LeftToRight)
        self.label_77.setAlignment(Qt.AlignCenter)

        self.verticalLayout_130.addWidget(self.label_77)

        self.verticalSpacer_42 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_130.addItem(self.verticalSpacer_42)

        self.lineEdit_31 = QLineEdit(self.widget_206)
        self.lineEdit_31.setObjectName(u"lineEdit_31")
        self.lineEdit_31.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_130.addWidget(self.lineEdit_31)


        self.horizontalLayout_138.addWidget(self.widget_206)

        self.horizontalSpacer_127 = QSpacerItem(171, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_138.addItem(self.horizontalSpacer_127)


        self.verticalLayout_124.addWidget(self.widget_200)

        self.widget_207 = QWidget(self.widget_199)
        self.widget_207.setObjectName(u"widget_207")
        self.horizontalLayout_139 = QHBoxLayout(self.widget_207)
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.widget_warning_29 = QWidget(self.widget_207)
        self.widget_warning_29.setObjectName(u"widget_warning_29")
        self.widget_warning_29.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_395 = QHBoxLayout(self.widget_warning_29)
        self.horizontalLayout_395.setSpacing(0)
        self.horizontalLayout_395.setObjectName(u"horizontalLayout_395")
        self.horizontalLayout_395.setContentsMargins(10, 5, 5, 5)
        self.label_292 = QLabel(self.widget_warning_29)
        self.label_292.setObjectName(u"label_292")
        self.label_292.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_395.addWidget(self.label_292)

        self.label_329 = QLabel(self.widget_warning_29)
        self.label_329.setObjectName(u"label_329")
        self.label_329.setMinimumSize(QSize(150, 0))
        self.label_329.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_329.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_395.addWidget(self.label_329)


        self.horizontalLayout_139.addWidget(self.widget_warning_29)

        self.horizontalSpacer_128 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_139.addItem(self.horizontalSpacer_128)

        self.pushButton_97 = QPushButton(self.widget_207)
        self.pushButton_97.setObjectName(u"pushButton_97")
        self.pushButton_97.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_139.addWidget(self.pushButton_97)


        self.verticalLayout_124.addWidget(self.widget_207)

        self.verticalSpacer_43 = QSpacerItem(20, 148, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_124.addItem(self.verticalSpacer_43)


        self.horizontalLayout_137.addWidget(self.widget_199)


        self.verticalLayout_123.addWidget(self.widget_198)

        self.widget_208 = QWidget(self.widget_196)
        self.widget_208.setObjectName(u"widget_208")
        self.widget_208.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_131 = QVBoxLayout(self.widget_208)
        self.verticalLayout_131.setSpacing(0)
        self.verticalLayout_131.setObjectName(u"verticalLayout_131")
        self.verticalLayout_131.setContentsMargins(0, 0, 0, 0)
        self.widget_209 = QWidget(self.widget_208)
        self.widget_209.setObjectName(u"widget_209")
        self.horizontalLayout_140 = QHBoxLayout(self.widget_209)
        self.horizontalLayout_140.setSpacing(0)
        self.horizontalLayout_140.setObjectName(u"horizontalLayout_140")
        self.horizontalLayout_140.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_131.addWidget(self.widget_209)


        self.verticalLayout_123.addWidget(self.widget_208)


        self.verticalLayout_107.addWidget(self.widget_196)

        self.widget_210 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_210.setObjectName(u"widget_210")
        self.verticalLayout_132 = QVBoxLayout(self.widget_210)
        self.verticalLayout_132.setObjectName(u"verticalLayout_132")
        self.widget_211 = QWidget(self.widget_210)
        self.widget_211.setObjectName(u"widget_211")
        self.widget_211.setStyleSheet(u"")
        self.horizontalLayout_141 = QHBoxLayout(self.widget_211)
        self.horizontalLayout_141.setObjectName(u"horizontalLayout_141")
        self.horizontalLayout_141.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_27 = QWidget(self.widget_211)
        self.Equipement_widget_27.setObjectName(u"Equipement_widget_27")
        self.Equipement_widget_27.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_142 = QHBoxLayout(self.Equipement_widget_27)
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.label_78 = QLabel(self.Equipement_widget_27)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setPixmap(QPixmap(u":/assets/icons/equippement-30.png"))

        self.horizontalLayout_142.addWidget(self.label_78, 0, Qt.AlignLeft)

        self.pushButton_98 = QPushButton(self.Equipement_widget_27)
        self.pushButton_98.setObjectName(u"pushButton_98")
        sizePolicy2.setHeightForWidth(self.pushButton_98.sizePolicy().hasHeightForWidth())
        self.pushButton_98.setSizePolicy(sizePolicy2)
        self.pushButton_98.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_98.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_98.setIcon(icon9)
        self.pushButton_98.setIconSize(QSize(24, 24))
        self.pushButton_98.setCheckable(True)

        self.horizontalLayout_142.addWidget(self.pushButton_98)


        self.horizontalLayout_141.addWidget(self.Equipement_widget_27)

        self.horizontalSpacer_129 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_141.addItem(self.horizontalSpacer_129)


        self.verticalLayout_132.addWidget(self.widget_211)

        self.widget_212 = QWidget(self.widget_210)
        self.widget_212.setObjectName(u"widget_212")
        self.widget_212.setMinimumSize(QSize(450, 0))
        self.widget_212.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.horizontalLayout_143 = QHBoxLayout(self.widget_212)
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.horizontalSpacer_130 = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_143.addItem(self.horizontalSpacer_130)

        self.widget_213 = QWidget(self.widget_212)
        self.widget_213.setObjectName(u"widget_213")
        self.verticalLayout_133 = QVBoxLayout(self.widget_213)
        self.verticalLayout_133.setObjectName(u"verticalLayout_133")
        self.textEdit_34 = QTextEdit(self.widget_213)
        self.textEdit_34.setObjectName(u"textEdit_34")
        sizePolicy4.setHeightForWidth(self.textEdit_34.sizePolicy().hasHeightForWidth())
        self.textEdit_34.setSizePolicy(sizePolicy4)
        self.textEdit_34.setMinimumSize(QSize(0, 0))
        self.textEdit_34.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_133.addWidget(self.textEdit_34)

        self.verticalSpacer_44 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_133.addItem(self.verticalSpacer_44)

        self.widget_214 = QWidget(self.widget_213)
        self.widget_214.setObjectName(u"widget_214")
        sizePolicy5.setHeightForWidth(self.widget_214.sizePolicy().hasHeightForWidth())
        self.widget_214.setSizePolicy(sizePolicy5)
        self.widget_214.setMinimumSize(QSize(300, 0))
        self.verticalLayout_134 = QVBoxLayout(self.widget_214)
        self.verticalLayout_134.setObjectName(u"verticalLayout_134")
        self.label_79 = QLabel(self.widget_214)
        self.label_79.setObjectName(u"label_79")

        self.verticalLayout_134.addWidget(self.label_79)

        self.verticalSpacer_45 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_134.addItem(self.verticalSpacer_45)

        self.comboBox_14 = QComboBox(self.widget_214)
        self.comboBox_14.setObjectName(u"comboBox_14")
        self.comboBox_14.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_134.addWidget(self.comboBox_14)


        self.verticalLayout_133.addWidget(self.widget_214)

        self.widget_215 = QWidget(self.widget_213)
        self.widget_215.setObjectName(u"widget_215")
        self.horizontalLayout_144 = QHBoxLayout(self.widget_215)
        self.horizontalLayout_144.setObjectName(u"horizontalLayout_144")
        self.horizontalSpacer_131 = QSpacerItem(361, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_144.addItem(self.horizontalSpacer_131)

        self.pushButton_99 = QPushButton(self.widget_215)
        self.pushButton_99.setObjectName(u"pushButton_99")
        self.pushButton_99.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_99.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_144.addWidget(self.pushButton_99)


        self.verticalLayout_133.addWidget(self.widget_215)


        self.horizontalLayout_143.addWidget(self.widget_213)

        self.widget_216 = QWidget(self.widget_212)
        self.widget_216.setObjectName(u"widget_216")
        self.widget_216.setMinimumSize(QSize(0, 0))
        self.verticalLayout_135 = QVBoxLayout(self.widget_216)
        self.verticalLayout_135.setObjectName(u"verticalLayout_135")
        self.verticalLayout_135.setContentsMargins(4, 4, 4, 4)
        self.listView_9 = QListView(self.widget_216)
        self.listView_9.setObjectName(u"listView_9")
        self.listView_9.setMinimumSize(QSize(0, 0))
        self.listView_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_135.addWidget(self.listView_9)

        self.widget_217 = QWidget(self.widget_216)
        self.widget_217.setObjectName(u"widget_217")
        self.horizontalLayout_145 = QHBoxLayout(self.widget_217)
        self.horizontalLayout_145.setObjectName(u"horizontalLayout_145")
        self.pushButton_100 = QPushButton(self.widget_217)
        self.pushButton_100.setObjectName(u"pushButton_100")
        self.pushButton_100.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_100.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_145.addWidget(self.pushButton_100)

        self.horizontalSpacer_132 = QSpacerItem(361, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_145.addItem(self.horizontalSpacer_132)


        self.verticalLayout_135.addWidget(self.widget_217)


        self.horizontalLayout_143.addWidget(self.widget_216)

        self.horizontalSpacer_133 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_143.addItem(self.horizontalSpacer_133)

        self.widget_218 = QWidget(self.widget_212)
        self.widget_218.setObjectName(u"widget_218")
        sizePolicy.setHeightForWidth(self.widget_218.sizePolicy().hasHeightForWidth())
        self.widget_218.setSizePolicy(sizePolicy)
        self.widget_218.setMinimumSize(QSize(400, 0))
        self.verticalLayout_136 = QVBoxLayout(self.widget_218)
        self.verticalLayout_136.setObjectName(u"verticalLayout_136")
        self.widget_219 = QWidget(self.widget_218)
        self.widget_219.setObjectName(u"widget_219")
        self.horizontalLayout_146 = QHBoxLayout(self.widget_219)
        self.horizontalLayout_146.setSpacing(0)
        self.horizontalLayout_146.setObjectName(u"horizontalLayout_146")
        self.horizontalLayout_146.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_134 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_146.addItem(self.horizontalSpacer_134)

        self.horizontalSpacer_135 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_146.addItem(self.horizontalSpacer_135)

        self.widget_220 = QWidget(self.widget_219)
        self.widget_220.setObjectName(u"widget_220")
        self.verticalLayout_137 = QVBoxLayout(self.widget_220)
        self.verticalLayout_137.setObjectName(u"verticalLayout_137")
        self.label_80 = QLabel(self.widget_220)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setAlignment(Qt.AlignCenter)

        self.verticalLayout_137.addWidget(self.label_80)

        self.lineEdit_32 = QLineEdit(self.widget_220)
        self.lineEdit_32.setObjectName(u"lineEdit_32")
        self.lineEdit_32.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_137.addWidget(self.lineEdit_32)


        self.horizontalLayout_146.addWidget(self.widget_220)

        self.horizontalSpacer_136 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_146.addItem(self.horizontalSpacer_136)

        self.widget_221 = QWidget(self.widget_219)
        self.widget_221.setObjectName(u"widget_221")
        self.verticalLayout_138 = QVBoxLayout(self.widget_221)
        self.verticalLayout_138.setObjectName(u"verticalLayout_138")
        self.label_81 = QLabel(self.widget_221)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setAlignment(Qt.AlignCenter)

        self.verticalLayout_138.addWidget(self.label_81)

        self.lineEdit_33 = QLineEdit(self.widget_221)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        self.lineEdit_33.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_138.addWidget(self.lineEdit_33)


        self.horizontalLayout_146.addWidget(self.widget_221)

        self.horizontalSpacer_137 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_146.addItem(self.horizontalSpacer_137)

        self.widget_222 = QWidget(self.widget_219)
        self.widget_222.setObjectName(u"widget_222")
        self.verticalLayout_139 = QVBoxLayout(self.widget_222)
        self.verticalLayout_139.setObjectName(u"verticalLayout_139")
        self.label_82 = QLabel(self.widget_222)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setAlignment(Qt.AlignCenter)

        self.verticalLayout_139.addWidget(self.label_82)

        self.lineEdit_34 = QLineEdit(self.widget_222)
        self.lineEdit_34.setObjectName(u"lineEdit_34")
        self.lineEdit_34.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_139.addWidget(self.lineEdit_34)


        self.horizontalLayout_146.addWidget(self.widget_222)

        self.horizontalSpacer_138 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_146.addItem(self.horizontalSpacer_138)

        self.widget_223 = QWidget(self.widget_219)
        self.widget_223.setObjectName(u"widget_223")
        self.verticalLayout_140 = QVBoxLayout(self.widget_223)
        self.verticalLayout_140.setObjectName(u"verticalLayout_140")
        self.label_83 = QLabel(self.widget_223)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setAlignment(Qt.AlignCenter)

        self.verticalLayout_140.addWidget(self.label_83)

        self.lineEdit_35 = QLineEdit(self.widget_223)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        self.lineEdit_35.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_140.addWidget(self.lineEdit_35)


        self.horizontalLayout_146.addWidget(self.widget_223)

        self.horizontalSpacer_139 = QSpacerItem(11, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_146.addItem(self.horizontalSpacer_139)

        self.widget_224 = QWidget(self.widget_219)
        self.widget_224.setObjectName(u"widget_224")
        self.verticalLayout_141 = QVBoxLayout(self.widget_224)
        self.verticalLayout_141.setObjectName(u"verticalLayout_141")
        self.label_84 = QLabel(self.widget_224)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setLayoutDirection(Qt.LeftToRight)
        self.label_84.setAlignment(Qt.AlignCenter)

        self.verticalLayout_141.addWidget(self.label_84)

        self.lineEdit_36 = QLineEdit(self.widget_224)
        self.lineEdit_36.setObjectName(u"lineEdit_36")
        self.lineEdit_36.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_141.addWidget(self.lineEdit_36)


        self.horizontalLayout_146.addWidget(self.widget_224)


        self.verticalLayout_136.addWidget(self.widget_219)

        self.verticalSpacer_46 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_136.addItem(self.verticalSpacer_46)

        self.widget_225 = QWidget(self.widget_218)
        self.widget_225.setObjectName(u"widget_225")
        self.horizontalLayout_147 = QHBoxLayout(self.widget_225)
        self.horizontalLayout_147.setObjectName(u"horizontalLayout_147")
        self.widget_warning_30 = QWidget(self.widget_225)
        self.widget_warning_30.setObjectName(u"widget_warning_30")
        self.widget_warning_30.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_396 = QHBoxLayout(self.widget_warning_30)
        self.horizontalLayout_396.setSpacing(0)
        self.horizontalLayout_396.setObjectName(u"horizontalLayout_396")
        self.horizontalLayout_396.setContentsMargins(10, 5, 5, 5)
        self.label_330 = QLabel(self.widget_warning_30)
        self.label_330.setObjectName(u"label_330")
        self.label_330.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_396.addWidget(self.label_330)

        self.label_331 = QLabel(self.widget_warning_30)
        self.label_331.setObjectName(u"label_331")
        self.label_331.setMinimumSize(QSize(150, 0))
        self.label_331.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_331.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_396.addWidget(self.label_331)


        self.horizontalLayout_147.addWidget(self.widget_warning_30)

        self.horizontalSpacer_140 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_147.addItem(self.horizontalSpacer_140)

        self.pushButton_101 = QPushButton(self.widget_225)
        self.pushButton_101.setObjectName(u"pushButton_101")
        self.pushButton_101.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_147.addWidget(self.pushButton_101)


        self.verticalLayout_136.addWidget(self.widget_225)


        self.horizontalLayout_143.addWidget(self.widget_218)


        self.verticalLayout_132.addWidget(self.widget_212)

        self.widget_226 = QWidget(self.widget_210)
        self.widget_226.setObjectName(u"widget_226")
        self.widget_226.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_142 = QVBoxLayout(self.widget_226)
        self.verticalLayout_142.setSpacing(0)
        self.verticalLayout_142.setObjectName(u"verticalLayout_142")
        self.verticalLayout_142.setContentsMargins(0, 0, 0, 0)
        self.widget_227 = QWidget(self.widget_226)
        self.widget_227.setObjectName(u"widget_227")
        self.horizontalLayout_148 = QHBoxLayout(self.widget_227)
        self.horizontalLayout_148.setSpacing(0)
        self.horizontalLayout_148.setObjectName(u"horizontalLayout_148")
        self.horizontalLayout_148.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_142.addWidget(self.widget_227)


        self.verticalLayout_132.addWidget(self.widget_226)


        self.verticalLayout_107.addWidget(self.widget_210)

        self.widget_228 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_228.setObjectName(u"widget_228")
        self.verticalLayout_143 = QVBoxLayout(self.widget_228)
        self.verticalLayout_143.setObjectName(u"verticalLayout_143")
        self.widget_229 = QWidget(self.widget_228)
        self.widget_229.setObjectName(u"widget_229")
        self.widget_229.setStyleSheet(u"")
        self.horizontalLayout_149 = QHBoxLayout(self.widget_229)
        self.horizontalLayout_149.setSpacing(0)
        self.horizontalLayout_149.setObjectName(u"horizontalLayout_149")
        self.horizontalLayout_149.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_28 = QWidget(self.widget_229)
        self.Equipement_widget_28.setObjectName(u"Equipement_widget_28")
        self.Equipement_widget_28.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_150 = QHBoxLayout(self.Equipement_widget_28)
        self.horizontalLayout_150.setObjectName(u"horizontalLayout_150")
        self.label_85 = QLabel(self.Equipement_widget_28)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setPixmap(QPixmap(u":/assets/icons/equippement-30.png"))

        self.horizontalLayout_150.addWidget(self.label_85, 0, Qt.AlignLeft)

        self.pushButton_102 = QPushButton(self.Equipement_widget_28)
        self.pushButton_102.setObjectName(u"pushButton_102")
        sizePolicy2.setHeightForWidth(self.pushButton_102.sizePolicy().hasHeightForWidth())
        self.pushButton_102.setSizePolicy(sizePolicy2)
        self.pushButton_102.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_102.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_102.setIcon(icon9)
        self.pushButton_102.setIconSize(QSize(24, 24))
        self.pushButton_102.setCheckable(True)

        self.horizontalLayout_150.addWidget(self.pushButton_102)


        self.horizontalLayout_149.addWidget(self.Equipement_widget_28)

        self.horizontalSpacer_141 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_149.addItem(self.horizontalSpacer_141)


        self.verticalLayout_143.addWidget(self.widget_229)

        self.widget_230 = QWidget(self.widget_228)
        self.widget_230.setObjectName(u"widget_230")
        self.widget_230.setMinimumSize(QSize(450, 0))
        self.widget_230.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.horizontalLayout_151 = QHBoxLayout(self.widget_230)
        self.horizontalLayout_151.setObjectName(u"horizontalLayout_151")
        self.horizontalSpacer_142 = QSpacerItem(255, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_151.addItem(self.horizontalSpacer_142)

        self.widget_231 = QWidget(self.widget_230)
        self.widget_231.setObjectName(u"widget_231")
        sizePolicy.setHeightForWidth(self.widget_231.sizePolicy().hasHeightForWidth())
        self.widget_231.setSizePolicy(sizePolicy)
        self.widget_231.setMinimumSize(QSize(400, 0))
        self.verticalLayout_144 = QVBoxLayout(self.widget_231)
        self.verticalLayout_144.setObjectName(u"verticalLayout_144")
        self.widget_232 = QWidget(self.widget_231)
        self.widget_232.setObjectName(u"widget_232")
        self.horizontalLayout_152 = QHBoxLayout(self.widget_232)
        self.horizontalLayout_152.setObjectName(u"horizontalLayout_152")
        self.horizontalSpacer_143 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_152.addItem(self.horizontalSpacer_143)


        self.verticalLayout_144.addWidget(self.widget_232)

        self.horizontalLayout_153 = QHBoxLayout()
        self.horizontalLayout_153.setObjectName(u"horizontalLayout_153")
        self.horizontalSpacer_144 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_153.addItem(self.horizontalSpacer_144)

        self.textEdit_35 = QTextEdit(self.widget_231)
        self.textEdit_35.setObjectName(u"textEdit_35")
        sizePolicy4.setHeightForWidth(self.textEdit_35.sizePolicy().hasHeightForWidth())
        self.textEdit_35.setSizePolicy(sizePolicy4)
        self.textEdit_35.setMinimumSize(QSize(0, 0))
        self.textEdit_35.setMaximumSize(QSize(16777215, 40))
        self.textEdit_35.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.horizontalLayout_153.addWidget(self.textEdit_35)

        self.horizontalSpacer_145 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_153.addItem(self.horizontalSpacer_145)


        self.verticalLayout_144.addLayout(self.horizontalLayout_153)

        self.lineEdit_37 = QLineEdit(self.widget_231)
        self.lineEdit_37.setObjectName(u"lineEdit_37")
        self.lineEdit_37.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_144.addWidget(self.lineEdit_37)

        self.widget_233 = QWidget(self.widget_231)
        self.widget_233.setObjectName(u"widget_233")
        self.horizontalLayout_154 = QHBoxLayout(self.widget_233)
        self.horizontalLayout_154.setObjectName(u"horizontalLayout_154")
        self.horizontalSpacer_146 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_154.addItem(self.horizontalSpacer_146)


        self.verticalLayout_144.addWidget(self.widget_233)

        self.verticalSpacer_47 = QSpacerItem(20, 148, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_144.addItem(self.verticalSpacer_47)


        self.horizontalLayout_151.addWidget(self.widget_231)

        self.horizontalSpacer_147 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_151.addItem(self.horizontalSpacer_147)


        self.verticalLayout_143.addWidget(self.widget_230)

        self.widget_234 = QWidget(self.widget_228)
        self.widget_234.setObjectName(u"widget_234")
        self.widget_234.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_145 = QVBoxLayout(self.widget_234)
        self.verticalLayout_145.setSpacing(0)
        self.verticalLayout_145.setObjectName(u"verticalLayout_145")
        self.verticalLayout_145.setContentsMargins(0, 0, 0, 0)
        self.widget_235 = QWidget(self.widget_234)
        self.widget_235.setObjectName(u"widget_235")
        self.horizontalLayout_155 = QHBoxLayout(self.widget_235)
        self.horizontalLayout_155.setSpacing(0)
        self.horizontalLayout_155.setObjectName(u"horizontalLayout_155")
        self.horizontalLayout_155.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_145.addWidget(self.widget_235)


        self.verticalLayout_143.addWidget(self.widget_234)


        self.verticalLayout_107.addWidget(self.widget_228)

        self.widget_236 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_236.setObjectName(u"widget_236")
        self.widget_236.setStyleSheet(u"")
        self.horizontalLayout_156 = QHBoxLayout(self.widget_236)
        self.horizontalLayout_156.setObjectName(u"horizontalLayout_156")
        self.Equipement_widget_29 = QWidget(self.widget_236)
        self.Equipement_widget_29.setObjectName(u"Equipement_widget_29")
        self.Equipement_widget_29.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 191, 191);\n"
"border-radius:10px;\n"
"color: white;\n"
"}\n"
"")
        self.horizontalLayout_157 = QHBoxLayout(self.Equipement_widget_29)
        self.horizontalLayout_157.setObjectName(u"horizontalLayout_157")
        self.pushButton_103 = QPushButton(self.Equipement_widget_29)
        self.pushButton_103.setObjectName(u"pushButton_103")
        sizePolicy2.setHeightForWidth(self.pushButton_103.sizePolicy().hasHeightForWidth())
        self.pushButton_103.setSizePolicy(sizePolicy2)
        self.pushButton_103.setFont(font5)
        self.pushButton_103.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_103.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(255, 191, 191);\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 191, 191);\n"
"}\n"
"")
        self.pushButton_103.setIcon(icon9)
        self.pushButton_103.setIconSize(QSize(24, 24))
        self.pushButton_103.setCheckable(True)

        self.horizontalLayout_157.addWidget(self.pushButton_103)


        self.horizontalLayout_156.addWidget(self.Equipement_widget_29)

        self.horizontalSpacer_148 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_156.addItem(self.horizontalSpacer_148)

        self.Equipement_widget_30 = QWidget(self.widget_236)
        self.Equipement_widget_30.setObjectName(u"Equipement_widget_30")
        self.Equipement_widget_30.setStyleSheet(u"QWidget{\n"
"background-color: rgb(104, 246, 73);\n"
"border-radius:10px;\n"
"color: white;\n"
"}\n"
"")
        self.horizontalLayout_158 = QHBoxLayout(self.Equipement_widget_30)
        self.horizontalLayout_158.setObjectName(u"horizontalLayout_158")
        self.pushButton_104 = QPushButton(self.Equipement_widget_30)
        self.pushButton_104.setObjectName(u"pushButton_104")
        sizePolicy2.setHeightForWidth(self.pushButton_104.sizePolicy().hasHeightForWidth())
        self.pushButton_104.setSizePolicy(sizePolicy2)
        self.pushButton_104.setFont(font5)
        self.pushButton_104.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_104.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(104, 246, 73);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(104, 246, 73);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(104, 246, 73);\n"
"}\n"
"")
        self.pushButton_104.setIcon(icon9)
        self.pushButton_104.setIconSize(QSize(24, 24))
        self.pushButton_104.setCheckable(True)

        self.horizontalLayout_158.addWidget(self.pushButton_104)


        self.horizontalLayout_156.addWidget(self.Equipement_widget_30)


        self.verticalLayout_107.addWidget(self.widget_236)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_3.addWidget(self.scrollArea_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.nv_dossier_prodIVD_page)
        self.nv_dossier_prodDigital_page = QWidget()
        self.nv_dossier_prodDigital_page.setObjectName(u"nv_dossier_prodDigital_page")
        self.gridLayout_5 = QGridLayout(self.nv_dossier_prodDigital_page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.scrollArea_5 = QScrollArea(self.nv_dossier_prodDigital_page)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 634, 2311))
        self.verticalLayout_185 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_185.setObjectName(u"verticalLayout_185")
        self.widget_311 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_311.setObjectName(u"widget_311")
        self.horizontalLayout_205 = QHBoxLayout(self.widget_311)
        self.horizontalLayout_205.setObjectName(u"horizontalLayout_205")
        self.label_109 = QLabel(self.widget_311)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setFont(font4)

        self.horizontalLayout_205.addWidget(self.label_109)

        self.horizontalSpacer_247 = QSpacerItem(348, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_205.addItem(self.horizontalSpacer_247)

        self.label_110 = QLabel(self.widget_311)
        self.label_110.setObjectName(u"label_110")

        self.horizontalLayout_205.addWidget(self.label_110)

        self.horizontalSpacer_248 = QSpacerItem(347, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_205.addItem(self.horizontalSpacer_248)

        self.label_132 = QLabel(self.widget_311)
        self.label_132.setObjectName(u"label_132")

        self.horizontalLayout_205.addWidget(self.label_132)


        self.verticalLayout_185.addWidget(self.widget_311)

        self.widget_312 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_312.setObjectName(u"widget_312")
        self.verticalLayout_186 = QVBoxLayout(self.widget_312)
        self.verticalLayout_186.setObjectName(u"verticalLayout_186")
        self.widget_313 = QWidget(self.widget_312)
        self.widget_313.setObjectName(u"widget_313")
        self.horizontalLayout_206 = QHBoxLayout(self.widget_313)
        self.horizontalLayout_206.setObjectName(u"horizontalLayout_206")
        self.horizontalLayout_206.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_40 = QWidget(self.widget_313)
        self.Equipement_widget_40.setObjectName(u"Equipement_widget_40")
        self.Equipement_widget_40.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_207 = QHBoxLayout(self.Equipement_widget_40)
        self.horizontalLayout_207.setObjectName(u"horizontalLayout_207")
        self.label_111 = QLabel(self.Equipement_widget_40)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setPixmap(QPixmap(u":/assets/icons/employee-30.png"))

        self.horizontalLayout_207.addWidget(self.label_111, 0, Qt.AlignLeft)

        self.pushButton_124 = QPushButton(self.Equipement_widget_40)
        self.pushButton_124.setObjectName(u"pushButton_124")
        sizePolicy2.setHeightForWidth(self.pushButton_124.sizePolicy().hasHeightForWidth())
        self.pushButton_124.setSizePolicy(sizePolicy2)
        self.pushButton_124.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_124.setStyleSheet(u"")
        self.pushButton_124.setIconSize(QSize(24, 24))
        self.pushButton_124.setCheckable(True)

        self.horizontalLayout_207.addWidget(self.pushButton_124)


        self.horizontalLayout_206.addWidget(self.Equipement_widget_40)

        self.horizontalSpacer_198 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_206.addItem(self.horizontalSpacer_198)


        self.verticalLayout_186.addWidget(self.widget_313)

        self.widget_314 = QWidget(self.widget_312)
        self.widget_314.setObjectName(u"widget_314")
        self.widget_314.setMinimumSize(QSize(0, 0))
        self.widget_314.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.verticalLayout_307 = QVBoxLayout(self.widget_314)
        self.verticalLayout_307.setObjectName(u"verticalLayout_307")
        self.horizontalLayout_208 = QHBoxLayout()
        self.horizontalLayout_208.setObjectName(u"horizontalLayout_208")
        self.horizontalSpacer_199 = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_208.addItem(self.horizontalSpacer_199)

        self.widget_315 = QWidget(self.widget_314)
        self.widget_315.setObjectName(u"widget_315")
        sizePolicy.setHeightForWidth(self.widget_315.sizePolicy().hasHeightForWidth())
        self.widget_315.setSizePolicy(sizePolicy)
        self.widget_315.setMinimumSize(QSize(0, 0))
        self.verticalLayout_187 = QVBoxLayout(self.widget_315)
        self.verticalLayout_187.setObjectName(u"verticalLayout_187")
        self.textEdit_47 = QTextEdit(self.widget_315)
        self.textEdit_47.setObjectName(u"textEdit_47")
        sizePolicy4.setHeightForWidth(self.textEdit_47.sizePolicy().hasHeightForWidth())
        self.textEdit_47.setSizePolicy(sizePolicy4)
        self.textEdit_47.setMinimumSize(QSize(0, 0))
        self.textEdit_47.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_187.addWidget(self.textEdit_47)

        self.textEdit_48 = QTextEdit(self.widget_315)
        self.textEdit_48.setObjectName(u"textEdit_48")
        sizePolicy4.setHeightForWidth(self.textEdit_48.sizePolicy().hasHeightForWidth())
        self.textEdit_48.setSizePolicy(sizePolicy4)
        self.textEdit_48.setMinimumSize(QSize(0, 0))
        self.textEdit_48.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_187.addWidget(self.textEdit_48)

        self.widget_316 = QWidget(self.widget_315)
        self.widget_316.setObjectName(u"widget_316")
        self.verticalLayout_188 = QVBoxLayout(self.widget_316)
        self.verticalLayout_188.setObjectName(u"verticalLayout_188")
        self.checkBox_17 = QCheckBox(self.widget_316)
        self.checkBox_17.setObjectName(u"checkBox_17")
        self.checkBox_17.setChecked(True)

        self.verticalLayout_188.addWidget(self.checkBox_17)

        self.checkBox_18 = QCheckBox(self.widget_316)
        self.checkBox_18.setObjectName(u"checkBox_18")

        self.verticalLayout_188.addWidget(self.checkBox_18)


        self.verticalLayout_187.addWidget(self.widget_316)

        self.widget_317 = QWidget(self.widget_315)
        self.widget_317.setObjectName(u"widget_317")
        self.horizontalLayout_209 = QHBoxLayout(self.widget_317)
        self.horizontalLayout_209.setObjectName(u"horizontalLayout_209")
        self.dateEdit_7 = QDateEdit(self.widget_317)
        self.dateEdit_7.setObjectName(u"dateEdit_7")
        self.dateEdit_7.setDateTime(QDateTime(QDate(2024, 10, 31), QTime(17, 0, 0)))
        self.dateEdit_7.setCalendarPopup(True)

        self.horizontalLayout_209.addWidget(self.dateEdit_7)

        self.horizontalSpacer_200 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_209.addItem(self.horizontalSpacer_200)


        self.verticalLayout_187.addWidget(self.widget_317)


        self.horizontalLayout_208.addWidget(self.widget_315)

        self.horizontalSpacer_201 = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_208.addItem(self.horizontalSpacer_201)

        self.horizontalSpacer_202 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_208.addItem(self.horizontalSpacer_202)

        self.widget_318 = QWidget(self.widget_314)
        self.widget_318.setObjectName(u"widget_318")
        self.widget_318.setMinimumSize(QSize(0, 0))
        self.widget_318.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_189 = QVBoxLayout(self.widget_318)
        self.verticalLayout_189.setObjectName(u"verticalLayout_189")
        self.textEdit_49 = QTextEdit(self.widget_318)
        self.textEdit_49.setObjectName(u"textEdit_49")
        sizePolicy4.setHeightForWidth(self.textEdit_49.sizePolicy().hasHeightForWidth())
        self.textEdit_49.setSizePolicy(sizePolicy4)
        self.textEdit_49.setMinimumSize(QSize(0, 0))
        self.textEdit_49.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_189.addWidget(self.textEdit_49)

        self.widget_319 = QWidget(self.widget_318)
        self.widget_319.setObjectName(u"widget_319")
        self.verticalLayout_190 = QVBoxLayout(self.widget_319)
        self.verticalLayout_190.setObjectName(u"verticalLayout_190")
        self.checkBox_19 = QCheckBox(self.widget_319)
        self.checkBox_19.setObjectName(u"checkBox_19")
        self.checkBox_19.setChecked(True)

        self.verticalLayout_190.addWidget(self.checkBox_19)

        self.checkBox_20 = QCheckBox(self.widget_319)
        self.checkBox_20.setObjectName(u"checkBox_20")

        self.verticalLayout_190.addWidget(self.checkBox_20)


        self.verticalLayout_189.addWidget(self.widget_319)

        self.widget_320 = QWidget(self.widget_318)
        self.widget_320.setObjectName(u"widget_320")
        self.horizontalLayout_210 = QHBoxLayout(self.widget_320)
        self.horizontalLayout_210.setObjectName(u"horizontalLayout_210")
        self.label_112 = QLabel(self.widget_320)
        self.label_112.setObjectName(u"label_112")

        self.horizontalLayout_210.addWidget(self.label_112)

        self.lineEdit_50 = QLineEdit(self.widget_320)
        self.lineEdit_50.setObjectName(u"lineEdit_50")
        self.lineEdit_50.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_210.addWidget(self.lineEdit_50)


        self.verticalLayout_189.addWidget(self.widget_320)


        self.horizontalLayout_208.addWidget(self.widget_318)

        self.horizontalSpacer_204 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_208.addItem(self.horizontalSpacer_204)


        self.verticalLayout_307.addLayout(self.horizontalLayout_208)

        self.widget_321 = QWidget(self.widget_314)
        self.widget_321.setObjectName(u"widget_321")
        self.horizontalLayout_211 = QHBoxLayout(self.widget_321)
        self.horizontalLayout_211.setObjectName(u"horizontalLayout_211")
        self.widget_warning_31 = QWidget(self.widget_321)
        self.widget_warning_31.setObjectName(u"widget_warning_31")
        self.widget_warning_31.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_399 = QHBoxLayout(self.widget_warning_31)
        self.horizontalLayout_399.setSpacing(0)
        self.horizontalLayout_399.setObjectName(u"horizontalLayout_399")
        self.horizontalLayout_399.setContentsMargins(10, 5, 5, 5)
        self.label_332 = QLabel(self.widget_warning_31)
        self.label_332.setObjectName(u"label_332")
        self.label_332.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_399.addWidget(self.label_332)

        self.label_333 = QLabel(self.widget_warning_31)
        self.label_333.setObjectName(u"label_333")
        self.label_333.setMinimumSize(QSize(150, 0))
        self.label_333.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_333.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_399.addWidget(self.label_333)


        self.horizontalLayout_211.addWidget(self.widget_warning_31)

        self.horizontalSpacer_203 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_211.addItem(self.horizontalSpacer_203)

        self.pushButton_125 = QPushButton(self.widget_321)
        self.pushButton_125.setObjectName(u"pushButton_125")
        self.pushButton_125.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_125.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_211.addWidget(self.pushButton_125)


        self.verticalLayout_307.addWidget(self.widget_321)


        self.verticalLayout_186.addWidget(self.widget_314)


        self.verticalLayout_185.addWidget(self.widget_312)

        self.widget_322 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_322.setObjectName(u"widget_322")
        self.verticalLayout_191 = QVBoxLayout(self.widget_322)
        self.verticalLayout_191.setObjectName(u"verticalLayout_191")
        self.widget_323 = QWidget(self.widget_322)
        self.widget_323.setObjectName(u"widget_323")
        self.horizontalLayout_212 = QHBoxLayout(self.widget_323)
        self.horizontalLayout_212.setObjectName(u"horizontalLayout_212")
        self.horizontalLayout_212.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_41 = QWidget(self.widget_323)
        self.Equipement_widget_41.setObjectName(u"Equipement_widget_41")
        self.Equipement_widget_41.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_213 = QHBoxLayout(self.Equipement_widget_41)
        self.horizontalLayout_213.setObjectName(u"horizontalLayout_213")
        self.label_114 = QLabel(self.Equipement_widget_41)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setPixmap(QPixmap(u":/assets/icons/employee-30.png"))

        self.horizontalLayout_213.addWidget(self.label_114, 0, Qt.AlignLeft)

        self.pushButton_126 = QPushButton(self.Equipement_widget_41)
        self.pushButton_126.setObjectName(u"pushButton_126")
        sizePolicy2.setHeightForWidth(self.pushButton_126.sizePolicy().hasHeightForWidth())
        self.pushButton_126.setSizePolicy(sizePolicy2)
        self.pushButton_126.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_126.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_126.setIcon(icon9)
        self.pushButton_126.setIconSize(QSize(24, 24))
        self.pushButton_126.setCheckable(True)

        self.horizontalLayout_213.addWidget(self.pushButton_126)


        self.horizontalLayout_212.addWidget(self.Equipement_widget_41)

        self.horizontalSpacer_205 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_212.addItem(self.horizontalSpacer_205)


        self.verticalLayout_191.addWidget(self.widget_323)

        self.widget_324 = QWidget(self.widget_322)
        self.widget_324.setObjectName(u"widget_324")
        self.widget_324.setMinimumSize(QSize(450, 0))
        self.widget_324.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.verticalLayout_310 = QVBoxLayout(self.widget_324)
        self.verticalLayout_310.setObjectName(u"verticalLayout_310")
        self.horizontalLayout_214 = QHBoxLayout()
        self.horizontalLayout_214.setObjectName(u"horizontalLayout_214")
        self.widget_325 = QWidget(self.widget_324)
        self.widget_325.setObjectName(u"widget_325")
        self.verticalLayout_192 = QVBoxLayout(self.widget_325)
        self.verticalLayout_192.setObjectName(u"verticalLayout_192")
        self.textEdit_50 = QTextEdit(self.widget_325)
        self.textEdit_50.setObjectName(u"textEdit_50")
        sizePolicy4.setHeightForWidth(self.textEdit_50.sizePolicy().hasHeightForWidth())
        self.textEdit_50.setSizePolicy(sizePolicy4)
        self.textEdit_50.setMinimumSize(QSize(0, 0))
        self.textEdit_50.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_192.addWidget(self.textEdit_50)

        self.verticalSpacer_62 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_192.addItem(self.verticalSpacer_62)


        self.horizontalLayout_214.addWidget(self.widget_325)

        self.widget_326 = QWidget(self.widget_324)
        self.widget_326.setObjectName(u"widget_326")
        self.widget_326.setMinimumSize(QSize(400, 0))
        self.verticalLayout_193 = QVBoxLayout(self.widget_326)
        self.verticalLayout_193.setObjectName(u"verticalLayout_193")
        self.verticalLayout_193.setContentsMargins(4, 4, 4, 4)
        self.textEdit_51 = QTextEdit(self.widget_326)
        self.textEdit_51.setObjectName(u"textEdit_51")
        sizePolicy4.setHeightForWidth(self.textEdit_51.sizePolicy().hasHeightForWidth())
        self.textEdit_51.setSizePolicy(sizePolicy4)
        self.textEdit_51.setMinimumSize(QSize(0, 0))
        self.textEdit_51.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_193.addWidget(self.textEdit_51)

        self.textEdit_52 = QTextEdit(self.widget_326)
        self.textEdit_52.setObjectName(u"textEdit_52")
        self.textEdit_52.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_193.addWidget(self.textEdit_52)

        self.widget_327 = QWidget(self.widget_326)
        self.widget_327.setObjectName(u"widget_327")
        self.horizontalLayout_215 = QHBoxLayout(self.widget_327)
        self.horizontalLayout_215.setObjectName(u"horizontalLayout_215")
        self.horizontalSpacer_206 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_215.addItem(self.horizontalSpacer_206)

        self.pushButton_127 = QPushButton(self.widget_327)
        self.pushButton_127.setObjectName(u"pushButton_127")
        self.pushButton_127.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_127.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_215.addWidget(self.pushButton_127)


        self.verticalLayout_193.addWidget(self.widget_327)


        self.horizontalLayout_214.addWidget(self.widget_326)

        self.horizontalSpacer_207 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_214.addItem(self.horizontalSpacer_207)


        self.verticalLayout_310.addLayout(self.horizontalLayout_214)

        self.widget_495 = QWidget(self.widget_324)
        self.widget_495.setObjectName(u"widget_495")
        self.horizontalLayout_319 = QHBoxLayout(self.widget_495)
        self.horizontalLayout_319.setObjectName(u"horizontalLayout_319")
        self.widget_warning_32 = QWidget(self.widget_495)
        self.widget_warning_32.setObjectName(u"widget_warning_32")
        self.widget_warning_32.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_400 = QHBoxLayout(self.widget_warning_32)
        self.horizontalLayout_400.setSpacing(0)
        self.horizontalLayout_400.setObjectName(u"horizontalLayout_400")
        self.horizontalLayout_400.setContentsMargins(10, 5, 5, 5)
        self.label_264 = QLabel(self.widget_warning_32)
        self.label_264.setObjectName(u"label_264")
        self.label_264.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_400.addWidget(self.label_264)

        self.label_334 = QLabel(self.widget_warning_32)
        self.label_334.setObjectName(u"label_334")
        self.label_334.setMinimumSize(QSize(150, 0))
        self.label_334.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_334.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_400.addWidget(self.label_334)


        self.horizontalLayout_319.addWidget(self.widget_warning_32)

        self.horizontalSpacer_337 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_319.addItem(self.horizontalSpacer_337)

        self.pushButton_175 = QPushButton(self.widget_495)
        self.pushButton_175.setObjectName(u"pushButton_175")
        self.pushButton_175.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_175.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_319.addWidget(self.pushButton_175)


        self.verticalLayout_310.addWidget(self.widget_495)


        self.verticalLayout_191.addWidget(self.widget_324)


        self.verticalLayout_185.addWidget(self.widget_322)

        self.widget_328 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_328.setObjectName(u"widget_328")
        self.verticalLayout_194 = QVBoxLayout(self.widget_328)
        self.verticalLayout_194.setObjectName(u"verticalLayout_194")
        self.widget_329 = QWidget(self.widget_328)
        self.widget_329.setObjectName(u"widget_329")
        self.horizontalLayout_216 = QHBoxLayout(self.widget_329)
        self.horizontalLayout_216.setObjectName(u"horizontalLayout_216")
        self.horizontalLayout_216.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_42 = QWidget(self.widget_329)
        self.Equipement_widget_42.setObjectName(u"Equipement_widget_42")
        self.Equipement_widget_42.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_217 = QHBoxLayout(self.Equipement_widget_42)
        self.horizontalLayout_217.setObjectName(u"horizontalLayout_217")
        self.label_115 = QLabel(self.Equipement_widget_42)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setPixmap(QPixmap(u":/assets/icons/employee-30.png"))

        self.horizontalLayout_217.addWidget(self.label_115, 0, Qt.AlignLeft)

        self.pushButton_128 = QPushButton(self.Equipement_widget_42)
        self.pushButton_128.setObjectName(u"pushButton_128")
        sizePolicy2.setHeightForWidth(self.pushButton_128.sizePolicy().hasHeightForWidth())
        self.pushButton_128.setSizePolicy(sizePolicy2)
        self.pushButton_128.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_128.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_128.setIcon(icon9)
        self.pushButton_128.setIconSize(QSize(24, 24))
        self.pushButton_128.setCheckable(True)

        self.horizontalLayout_217.addWidget(self.pushButton_128)


        self.horizontalLayout_216.addWidget(self.Equipement_widget_42)

        self.horizontalSpacer_208 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_216.addItem(self.horizontalSpacer_208)


        self.verticalLayout_194.addWidget(self.widget_329)

        self.widget_330 = QWidget(self.widget_328)
        self.widget_330.setObjectName(u"widget_330")
        self.widget_330.setMinimumSize(QSize(450, 0))
        self.widget_330.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.verticalLayout_311 = QVBoxLayout(self.widget_330)
        self.verticalLayout_311.setObjectName(u"verticalLayout_311")
        self.horizontalLayout_218 = QHBoxLayout()
        self.horizontalLayout_218.setObjectName(u"horizontalLayout_218")
        self.widget_331 = QWidget(self.widget_330)
        self.widget_331.setObjectName(u"widget_331")
        sizePolicy.setHeightForWidth(self.widget_331.sizePolicy().hasHeightForWidth())
        self.widget_331.setSizePolicy(sizePolicy)
        self.widget_331.setMinimumSize(QSize(0, 0))
        self.verticalLayout_195 = QVBoxLayout(self.widget_331)
        self.verticalLayout_195.setSpacing(10)
        self.verticalLayout_195.setObjectName(u"verticalLayout_195")
        self.verticalLayout_195.setContentsMargins(4, 4, 4, 4)
        self.textEdit_53 = QTextEdit(self.widget_331)
        self.textEdit_53.setObjectName(u"textEdit_53")
        sizePolicy4.setHeightForWidth(self.textEdit_53.sizePolicy().hasHeightForWidth())
        self.textEdit_53.setSizePolicy(sizePolicy4)
        self.textEdit_53.setMinimumSize(QSize(0, 0))
        self.textEdit_53.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_195.addWidget(self.textEdit_53)

        self.comboBox_19 = QComboBox(self.widget_331)
        self.comboBox_19.setObjectName(u"comboBox_19")
        self.comboBox_19.setMinimumSize(QSize(400, 0))
        self.comboBox_19.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_195.addWidget(self.comboBox_19)

        self.widget_332 = QWidget(self.widget_331)
        self.widget_332.setObjectName(u"widget_332")
        self.horizontalLayout_219 = QHBoxLayout(self.widget_332)
        self.horizontalLayout_219.setObjectName(u"horizontalLayout_219")
        self.horizontalSpacer_209 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_219.addItem(self.horizontalSpacer_209)

        self.pushButton_129 = QPushButton(self.widget_332)
        self.pushButton_129.setObjectName(u"pushButton_129")
        self.pushButton_129.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_219.addWidget(self.pushButton_129)


        self.verticalLayout_195.addWidget(self.widget_332)

        self.verticalSpacer_63 = QSpacerItem(20, 148, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_195.addItem(self.verticalSpacer_63)


        self.horizontalLayout_218.addWidget(self.widget_331)

        self.horizontalSpacer_210 = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_218.addItem(self.horizontalSpacer_210)

        self.widget_333 = QWidget(self.widget_330)
        self.widget_333.setObjectName(u"widget_333")
        self.widget_333.setMinimumSize(QSize(400, 0))
        self.verticalLayout_196 = QVBoxLayout(self.widget_333)
        self.verticalLayout_196.setObjectName(u"verticalLayout_196")
        self.verticalLayout_196.setContentsMargins(4, 4, 4, 4)
        self.listView_13 = QListView(self.widget_333)
        self.listView_13.setObjectName(u"listView_13")
        self.listView_13.setMinimumSize(QSize(500, 0))
        self.listView_13.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_196.addWidget(self.listView_13)

        self.widget_334 = QWidget(self.widget_333)
        self.widget_334.setObjectName(u"widget_334")
        self.horizontalLayout_220 = QHBoxLayout(self.widget_334)
        self.horizontalLayout_220.setObjectName(u"horizontalLayout_220")
        self.pushButton_130 = QPushButton(self.widget_334)
        self.pushButton_130.setObjectName(u"pushButton_130")
        self.pushButton_130.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_130.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_220.addWidget(self.pushButton_130)

        self.horizontalSpacer_211 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_220.addItem(self.horizontalSpacer_211)


        self.verticalLayout_196.addWidget(self.widget_334)


        self.horizontalLayout_218.addWidget(self.widget_333)

        self.horizontalSpacer_212 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_218.addItem(self.horizontalSpacer_212)


        self.verticalLayout_311.addLayout(self.horizontalLayout_218)

        self.widget_496 = QWidget(self.widget_330)
        self.widget_496.setObjectName(u"widget_496")
        self.horizontalLayout_320 = QHBoxLayout(self.widget_496)
        self.horizontalLayout_320.setObjectName(u"horizontalLayout_320")
        self.widget_warning_33 = QWidget(self.widget_496)
        self.widget_warning_33.setObjectName(u"widget_warning_33")
        self.widget_warning_33.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_407 = QHBoxLayout(self.widget_warning_33)
        self.horizontalLayout_407.setSpacing(0)
        self.horizontalLayout_407.setObjectName(u"horizontalLayout_407")
        self.horizontalLayout_407.setContentsMargins(10, 5, 5, 5)
        self.label_268 = QLabel(self.widget_warning_33)
        self.label_268.setObjectName(u"label_268")
        self.label_268.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_407.addWidget(self.label_268)

        self.label_335 = QLabel(self.widget_warning_33)
        self.label_335.setObjectName(u"label_335")
        self.label_335.setMinimumSize(QSize(150, 0))
        self.label_335.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_335.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_407.addWidget(self.label_335)


        self.horizontalLayout_320.addWidget(self.widget_warning_33)

        self.horizontalSpacer_338 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_320.addItem(self.horizontalSpacer_338)

        self.pushButton_176 = QPushButton(self.widget_496)
        self.pushButton_176.setObjectName(u"pushButton_176")
        self.pushButton_176.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_176.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_320.addWidget(self.pushButton_176)


        self.verticalLayout_311.addWidget(self.widget_496)


        self.verticalLayout_194.addWidget(self.widget_330)


        self.verticalLayout_185.addWidget(self.widget_328)

        self.widget_335 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_335.setObjectName(u"widget_335")
        self.verticalLayout_197 = QVBoxLayout(self.widget_335)
        self.verticalLayout_197.setObjectName(u"verticalLayout_197")
        self.widget_336 = QWidget(self.widget_335)
        self.widget_336.setObjectName(u"widget_336")
        self.widget_336.setStyleSheet(u"")
        self.horizontalLayout_221 = QHBoxLayout(self.widget_336)
        self.horizontalLayout_221.setObjectName(u"horizontalLayout_221")
        self.horizontalLayout_221.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_43 = QWidget(self.widget_336)
        self.Equipement_widget_43.setObjectName(u"Equipement_widget_43")
        self.Equipement_widget_43.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_222 = QHBoxLayout(self.Equipement_widget_43)
        self.horizontalLayout_222.setObjectName(u"horizontalLayout_222")
        self.label_116 = QLabel(self.Equipement_widget_43)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setPixmap(QPixmap(u":/assets/icons/equippement-30.png"))

        self.horizontalLayout_222.addWidget(self.label_116, 0, Qt.AlignLeft)

        self.pushButton_131 = QPushButton(self.Equipement_widget_43)
        self.pushButton_131.setObjectName(u"pushButton_131")
        sizePolicy2.setHeightForWidth(self.pushButton_131.sizePolicy().hasHeightForWidth())
        self.pushButton_131.setSizePolicy(sizePolicy2)
        self.pushButton_131.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_131.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_131.setIcon(icon9)
        self.pushButton_131.setIconSize(QSize(24, 24))
        self.pushButton_131.setCheckable(True)

        self.horizontalLayout_222.addWidget(self.pushButton_131)


        self.horizontalLayout_221.addWidget(self.Equipement_widget_43)

        self.horizontalSpacer_213 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_221.addItem(self.horizontalSpacer_213)


        self.verticalLayout_197.addWidget(self.widget_336)

        self.widget_337 = QWidget(self.widget_335)
        self.widget_337.setObjectName(u"widget_337")
        self.widget_337.setMinimumSize(QSize(450, 0))
        self.widget_337.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.verticalLayout_312 = QVBoxLayout(self.widget_337)
        self.verticalLayout_312.setObjectName(u"verticalLayout_312")
        self.horizontalLayout_223 = QHBoxLayout()
        self.horizontalLayout_223.setObjectName(u"horizontalLayout_223")
        self.widget_338 = QWidget(self.widget_337)
        self.widget_338.setObjectName(u"widget_338")
        sizePolicy.setHeightForWidth(self.widget_338.sizePolicy().hasHeightForWidth())
        self.widget_338.setSizePolicy(sizePolicy)
        self.widget_338.setMinimumSize(QSize(0, 0))
        self.verticalLayout_198 = QVBoxLayout(self.widget_338)
        self.verticalLayout_198.setSpacing(10)
        self.verticalLayout_198.setObjectName(u"verticalLayout_198")
        self.verticalLayout_198.setContentsMargins(4, 4, 4, 4)
        self.textEdit_54 = QTextEdit(self.widget_338)
        self.textEdit_54.setObjectName(u"textEdit_54")
        sizePolicy4.setHeightForWidth(self.textEdit_54.sizePolicy().hasHeightForWidth())
        self.textEdit_54.setSizePolicy(sizePolicy4)
        self.textEdit_54.setMinimumSize(QSize(0, 0))
        self.textEdit_54.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_198.addWidget(self.textEdit_54)

        self.comboBox_20 = QComboBox(self.widget_338)
        self.comboBox_20.setObjectName(u"comboBox_20")
        self.comboBox_20.setMinimumSize(QSize(400, 0))
        self.comboBox_20.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_198.addWidget(self.comboBox_20)

        self.widget_339 = QWidget(self.widget_338)
        self.widget_339.setObjectName(u"widget_339")
        self.horizontalLayout_224 = QHBoxLayout(self.widget_339)
        self.horizontalLayout_224.setObjectName(u"horizontalLayout_224")
        self.horizontalSpacer_214 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_224.addItem(self.horizontalSpacer_214)

        self.pushButton_132 = QPushButton(self.widget_339)
        self.pushButton_132.setObjectName(u"pushButton_132")
        self.pushButton_132.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_224.addWidget(self.pushButton_132)


        self.verticalLayout_198.addWidget(self.widget_339)

        self.verticalSpacer_64 = QSpacerItem(20, 148, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_198.addItem(self.verticalSpacer_64)


        self.horizontalLayout_223.addWidget(self.widget_338)

        self.horizontalSpacer_215 = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_223.addItem(self.horizontalSpacer_215)

        self.widget_340 = QWidget(self.widget_337)
        self.widget_340.setObjectName(u"widget_340")
        self.widget_340.setMinimumSize(QSize(400, 0))
        self.verticalLayout_199 = QVBoxLayout(self.widget_340)
        self.verticalLayout_199.setObjectName(u"verticalLayout_199")
        self.verticalLayout_199.setContentsMargins(4, 4, 4, 4)
        self.listView_14 = QListView(self.widget_340)
        self.listView_14.setObjectName(u"listView_14")
        self.listView_14.setMinimumSize(QSize(500, 0))
        self.listView_14.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_199.addWidget(self.listView_14)

        self.widget_341 = QWidget(self.widget_340)
        self.widget_341.setObjectName(u"widget_341")
        self.horizontalLayout_225 = QHBoxLayout(self.widget_341)
        self.horizontalLayout_225.setObjectName(u"horizontalLayout_225")
        self.pushButton_133 = QPushButton(self.widget_341)
        self.pushButton_133.setObjectName(u"pushButton_133")
        self.pushButton_133.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_133.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_225.addWidget(self.pushButton_133)

        self.horizontalSpacer_216 = QSpacerItem(361, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_225.addItem(self.horizontalSpacer_216)


        self.verticalLayout_199.addWidget(self.widget_341)


        self.horizontalLayout_223.addWidget(self.widget_340)

        self.horizontalSpacer_217 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_223.addItem(self.horizontalSpacer_217)


        self.verticalLayout_312.addLayout(self.horizontalLayout_223)

        self.widget_497 = QWidget(self.widget_337)
        self.widget_497.setObjectName(u"widget_497")
        self.horizontalLayout_321 = QHBoxLayout(self.widget_497)
        self.horizontalLayout_321.setObjectName(u"horizontalLayout_321")
        self.widget_warning_34 = QWidget(self.widget_497)
        self.widget_warning_34.setObjectName(u"widget_warning_34")
        self.widget_warning_34.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_413 = QHBoxLayout(self.widget_warning_34)
        self.horizontalLayout_413.setSpacing(0)
        self.horizontalLayout_413.setObjectName(u"horizontalLayout_413")
        self.horizontalLayout_413.setContentsMargins(10, 5, 5, 5)
        self.label_272 = QLabel(self.widget_warning_34)
        self.label_272.setObjectName(u"label_272")
        self.label_272.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_413.addWidget(self.label_272)

        self.label_336 = QLabel(self.widget_warning_34)
        self.label_336.setObjectName(u"label_336")
        self.label_336.setMinimumSize(QSize(150, 0))
        self.label_336.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_336.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_413.addWidget(self.label_336)


        self.horizontalLayout_321.addWidget(self.widget_warning_34)

        self.horizontalSpacer_349 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_321.addItem(self.horizontalSpacer_349)

        self.pushButton_177 = QPushButton(self.widget_497)
        self.pushButton_177.setObjectName(u"pushButton_177")
        self.pushButton_177.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_177.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_321.addWidget(self.pushButton_177)


        self.verticalLayout_312.addWidget(self.widget_497)


        self.verticalLayout_197.addWidget(self.widget_337)

        self.widget_342 = QWidget(self.widget_335)
        self.widget_342.setObjectName(u"widget_342")
        self.widget_342.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_200 = QVBoxLayout(self.widget_342)
        self.verticalLayout_200.setSpacing(0)
        self.verticalLayout_200.setObjectName(u"verticalLayout_200")
        self.verticalLayout_200.setContentsMargins(0, 0, 0, 0)
        self.widget_343 = QWidget(self.widget_342)
        self.widget_343.setObjectName(u"widget_343")
        self.horizontalLayout_226 = QHBoxLayout(self.widget_343)
        self.horizontalLayout_226.setSpacing(0)
        self.horizontalLayout_226.setObjectName(u"horizontalLayout_226")
        self.horizontalLayout_226.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_200.addWidget(self.widget_343)


        self.verticalLayout_197.addWidget(self.widget_342)


        self.verticalLayout_185.addWidget(self.widget_335)

        self.widget_344 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_344.setObjectName(u"widget_344")
        self.verticalLayout_201 = QVBoxLayout(self.widget_344)
        self.verticalLayout_201.setObjectName(u"verticalLayout_201")
        self.widget_345 = QWidget(self.widget_344)
        self.widget_345.setObjectName(u"widget_345")
        self.widget_345.setStyleSheet(u"")
        self.horizontalLayout_227 = QHBoxLayout(self.widget_345)
        self.horizontalLayout_227.setObjectName(u"horizontalLayout_227")
        self.horizontalLayout_227.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_44 = QWidget(self.widget_345)
        self.Equipement_widget_44.setObjectName(u"Equipement_widget_44")
        self.Equipement_widget_44.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_228 = QHBoxLayout(self.Equipement_widget_44)
        self.horizontalLayout_228.setObjectName(u"horizontalLayout_228")
        self.label_117 = QLabel(self.Equipement_widget_44)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setPixmap(QPixmap(u":/assets/icons/equippement-30.png"))

        self.horizontalLayout_228.addWidget(self.label_117, 0, Qt.AlignLeft)

        self.pushButton_134 = QPushButton(self.Equipement_widget_44)
        self.pushButton_134.setObjectName(u"pushButton_134")
        sizePolicy2.setHeightForWidth(self.pushButton_134.sizePolicy().hasHeightForWidth())
        self.pushButton_134.setSizePolicy(sizePolicy2)
        self.pushButton_134.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_134.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_134.setIcon(icon9)
        self.pushButton_134.setIconSize(QSize(24, 24))
        self.pushButton_134.setCheckable(True)

        self.horizontalLayout_228.addWidget(self.pushButton_134)


        self.horizontalLayout_227.addWidget(self.Equipement_widget_44)

        self.horizontalSpacer_218 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_227.addItem(self.horizontalSpacer_218)


        self.verticalLayout_201.addWidget(self.widget_345)

        self.widget_346 = QWidget(self.widget_344)
        self.widget_346.setObjectName(u"widget_346")
        self.widget_346.setMinimumSize(QSize(450, 0))
        self.widget_346.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.horizontalLayout_229 = QHBoxLayout(self.widget_346)
        self.horizontalLayout_229.setObjectName(u"horizontalLayout_229")
        self.horizontalLayout_229.setContentsMargins(10, 10, 10, 10)
        self.widget_347 = QWidget(self.widget_346)
        self.widget_347.setObjectName(u"widget_347")
        sizePolicy.setHeightForWidth(self.widget_347.sizePolicy().hasHeightForWidth())
        self.widget_347.setSizePolicy(sizePolicy)
        self.widget_347.setMinimumSize(QSize(400, 0))
        self.verticalLayout_202 = QVBoxLayout(self.widget_347)
        self.verticalLayout_202.setObjectName(u"verticalLayout_202")
        self.textEdit_55 = QTextEdit(self.widget_347)
        self.textEdit_55.setObjectName(u"textEdit_55")
        sizePolicy4.setHeightForWidth(self.textEdit_55.sizePolicy().hasHeightForWidth())
        self.textEdit_55.setSizePolicy(sizePolicy4)
        self.textEdit_55.setMinimumSize(QSize(0, 0))
        self.textEdit_55.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_202.addWidget(self.textEdit_55)

        self.widget_348 = QWidget(self.widget_347)
        self.widget_348.setObjectName(u"widget_348")
        self.horizontalLayout_230 = QHBoxLayout(self.widget_348)
        self.horizontalLayout_230.setObjectName(u"horizontalLayout_230")
        self.horizontalLayout_230.setContentsMargins(10, 10, 10, 10)
        self.horizontalSpacer_219 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_230.addItem(self.horizontalSpacer_219)

        self.widget_349 = QWidget(self.widget_348)
        self.widget_349.setObjectName(u"widget_349")
        sizePolicy5.setHeightForWidth(self.widget_349.sizePolicy().hasHeightForWidth())
        self.widget_349.setSizePolicy(sizePolicy5)
        self.widget_349.setMinimumSize(QSize(300, 0))
        self.verticalLayout_203 = QVBoxLayout(self.widget_349)
        self.verticalLayout_203.setObjectName(u"verticalLayout_203")
        self.label_118 = QLabel(self.widget_349)
        self.label_118.setObjectName(u"label_118")

        self.verticalLayout_203.addWidget(self.label_118)

        self.verticalSpacer_65 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_203.addItem(self.verticalSpacer_65)

        self.comboBox_21 = QComboBox(self.widget_349)
        self.comboBox_21.setObjectName(u"comboBox_21")
        self.comboBox_21.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_203.addWidget(self.comboBox_21)


        self.horizontalLayout_230.addWidget(self.widget_349)

        self.horizontalSpacer_220 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_230.addItem(self.horizontalSpacer_220)

        self.widget_350 = QWidget(self.widget_348)
        self.widget_350.setObjectName(u"widget_350")
        self.verticalLayout_204 = QVBoxLayout(self.widget_350)
        self.verticalLayout_204.setObjectName(u"verticalLayout_204")
        self.label_119 = QLabel(self.widget_350)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setAlignment(Qt.AlignCenter)

        self.verticalLayout_204.addWidget(self.label_119)

        self.verticalSpacer_66 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_204.addItem(self.verticalSpacer_66)

        self.lineEdit_51 = QLineEdit(self.widget_350)
        self.lineEdit_51.setObjectName(u"lineEdit_51")
        self.lineEdit_51.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_204.addWidget(self.lineEdit_51)


        self.horizontalLayout_230.addWidget(self.widget_350)

        self.horizontalSpacer_221 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_230.addItem(self.horizontalSpacer_221)

        self.widget_351 = QWidget(self.widget_348)
        self.widget_351.setObjectName(u"widget_351")
        self.verticalLayout_205 = QVBoxLayout(self.widget_351)
        self.verticalLayout_205.setObjectName(u"verticalLayout_205")
        self.label_120 = QLabel(self.widget_351)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setAlignment(Qt.AlignCenter)

        self.verticalLayout_205.addWidget(self.label_120)

        self.verticalSpacer_67 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_205.addItem(self.verticalSpacer_67)

        self.lineEdit_52 = QLineEdit(self.widget_351)
        self.lineEdit_52.setObjectName(u"lineEdit_52")
        self.lineEdit_52.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_205.addWidget(self.lineEdit_52)


        self.horizontalLayout_230.addWidget(self.widget_351)

        self.horizontalSpacer_222 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_230.addItem(self.horizontalSpacer_222)

        self.widget_352 = QWidget(self.widget_348)
        self.widget_352.setObjectName(u"widget_352")
        self.verticalLayout_206 = QVBoxLayout(self.widget_352)
        self.verticalLayout_206.setObjectName(u"verticalLayout_206")
        self.label_121 = QLabel(self.widget_352)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setAlignment(Qt.AlignCenter)

        self.verticalLayout_206.addWidget(self.label_121)

        self.verticalSpacer_68 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_206.addItem(self.verticalSpacer_68)

        self.lineEdit_53 = QLineEdit(self.widget_352)
        self.lineEdit_53.setObjectName(u"lineEdit_53")
        self.lineEdit_53.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_206.addWidget(self.lineEdit_53)


        self.horizontalLayout_230.addWidget(self.widget_352)

        self.horizontalSpacer_223 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_230.addItem(self.horizontalSpacer_223)

        self.widget_353 = QWidget(self.widget_348)
        self.widget_353.setObjectName(u"widget_353")
        self.verticalLayout_207 = QVBoxLayout(self.widget_353)
        self.verticalLayout_207.setObjectName(u"verticalLayout_207")
        self.label_122 = QLabel(self.widget_353)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setAlignment(Qt.AlignCenter)

        self.verticalLayout_207.addWidget(self.label_122)

        self.verticalSpacer_69 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_207.addItem(self.verticalSpacer_69)

        self.lineEdit_54 = QLineEdit(self.widget_353)
        self.lineEdit_54.setObjectName(u"lineEdit_54")
        self.lineEdit_54.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_207.addWidget(self.lineEdit_54)


        self.horizontalLayout_230.addWidget(self.widget_353)

        self.horizontalSpacer_224 = QSpacerItem(11, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_230.addItem(self.horizontalSpacer_224)

        self.widget_354 = QWidget(self.widget_348)
        self.widget_354.setObjectName(u"widget_354")
        self.verticalLayout_208 = QVBoxLayout(self.widget_354)
        self.verticalLayout_208.setObjectName(u"verticalLayout_208")
        self.label_123 = QLabel(self.widget_354)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setLayoutDirection(Qt.LeftToRight)
        self.label_123.setAlignment(Qt.AlignCenter)

        self.verticalLayout_208.addWidget(self.label_123)

        self.verticalSpacer_70 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_208.addItem(self.verticalSpacer_70)

        self.lineEdit_55 = QLineEdit(self.widget_354)
        self.lineEdit_55.setObjectName(u"lineEdit_55")
        self.lineEdit_55.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_208.addWidget(self.lineEdit_55)


        self.horizontalLayout_230.addWidget(self.widget_354)

        self.horizontalSpacer_225 = QSpacerItem(171, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_230.addItem(self.horizontalSpacer_225)


        self.verticalLayout_202.addWidget(self.widget_348)

        self.widget_355 = QWidget(self.widget_347)
        self.widget_355.setObjectName(u"widget_355")
        self.horizontalLayout_231 = QHBoxLayout(self.widget_355)
        self.horizontalLayout_231.setObjectName(u"horizontalLayout_231")
        self.widget_warning_35 = QWidget(self.widget_355)
        self.widget_warning_35.setObjectName(u"widget_warning_35")
        self.widget_warning_35.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_414 = QHBoxLayout(self.widget_warning_35)
        self.horizontalLayout_414.setSpacing(0)
        self.horizontalLayout_414.setObjectName(u"horizontalLayout_414")
        self.horizontalLayout_414.setContentsMargins(10, 5, 5, 5)
        self.label_337 = QLabel(self.widget_warning_35)
        self.label_337.setObjectName(u"label_337")
        self.label_337.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_414.addWidget(self.label_337)

        self.label_338 = QLabel(self.widget_warning_35)
        self.label_338.setObjectName(u"label_338")
        self.label_338.setMinimumSize(QSize(150, 0))
        self.label_338.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_338.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_414.addWidget(self.label_338)


        self.horizontalLayout_231.addWidget(self.widget_warning_35)

        self.horizontalSpacer_226 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_231.addItem(self.horizontalSpacer_226)

        self.pushButton_135 = QPushButton(self.widget_355)
        self.pushButton_135.setObjectName(u"pushButton_135")
        self.pushButton_135.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_231.addWidget(self.pushButton_135)


        self.verticalLayout_202.addWidget(self.widget_355)

        self.verticalSpacer_71 = QSpacerItem(20, 148, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_202.addItem(self.verticalSpacer_71)


        self.horizontalLayout_229.addWidget(self.widget_347)


        self.verticalLayout_201.addWidget(self.widget_346)

        self.widget_356 = QWidget(self.widget_344)
        self.widget_356.setObjectName(u"widget_356")
        self.widget_356.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_209 = QVBoxLayout(self.widget_356)
        self.verticalLayout_209.setSpacing(0)
        self.verticalLayout_209.setObjectName(u"verticalLayout_209")
        self.verticalLayout_209.setContentsMargins(0, 0, 0, 0)
        self.widget_357 = QWidget(self.widget_356)
        self.widget_357.setObjectName(u"widget_357")
        self.horizontalLayout_232 = QHBoxLayout(self.widget_357)
        self.horizontalLayout_232.setSpacing(0)
        self.horizontalLayout_232.setObjectName(u"horizontalLayout_232")
        self.horizontalLayout_232.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_209.addWidget(self.widget_357)


        self.verticalLayout_201.addWidget(self.widget_356)


        self.verticalLayout_185.addWidget(self.widget_344)

        self.widget_358 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_358.setObjectName(u"widget_358")
        self.verticalLayout_210 = QVBoxLayout(self.widget_358)
        self.verticalLayout_210.setObjectName(u"verticalLayout_210")
        self.widget_359 = QWidget(self.widget_358)
        self.widget_359.setObjectName(u"widget_359")
        self.widget_359.setStyleSheet(u"")
        self.horizontalLayout_233 = QHBoxLayout(self.widget_359)
        self.horizontalLayout_233.setObjectName(u"horizontalLayout_233")
        self.horizontalLayout_233.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_45 = QWidget(self.widget_359)
        self.Equipement_widget_45.setObjectName(u"Equipement_widget_45")
        self.Equipement_widget_45.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_234 = QHBoxLayout(self.Equipement_widget_45)
        self.horizontalLayout_234.setObjectName(u"horizontalLayout_234")
        self.label_124 = QLabel(self.Equipement_widget_45)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setPixmap(QPixmap(u":/assets/icons/equippement-30.png"))

        self.horizontalLayout_234.addWidget(self.label_124, 0, Qt.AlignLeft)

        self.pushButton_136 = QPushButton(self.Equipement_widget_45)
        self.pushButton_136.setObjectName(u"pushButton_136")
        sizePolicy2.setHeightForWidth(self.pushButton_136.sizePolicy().hasHeightForWidth())
        self.pushButton_136.setSizePolicy(sizePolicy2)
        self.pushButton_136.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_136.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_136.setIcon(icon9)
        self.pushButton_136.setIconSize(QSize(24, 24))
        self.pushButton_136.setCheckable(True)

        self.horizontalLayout_234.addWidget(self.pushButton_136)


        self.horizontalLayout_233.addWidget(self.Equipement_widget_45)

        self.horizontalSpacer_227 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_233.addItem(self.horizontalSpacer_227)


        self.verticalLayout_210.addWidget(self.widget_359)

        self.widget_360 = QWidget(self.widget_358)
        self.widget_360.setObjectName(u"widget_360")
        self.widget_360.setMinimumSize(QSize(450, 0))
        self.widget_360.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.horizontalLayout_235 = QHBoxLayout(self.widget_360)
        self.horizontalLayout_235.setObjectName(u"horizontalLayout_235")
        self.horizontalSpacer_228 = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_235.addItem(self.horizontalSpacer_228)

        self.widget_361 = QWidget(self.widget_360)
        self.widget_361.setObjectName(u"widget_361")
        self.verticalLayout_211 = QVBoxLayout(self.widget_361)
        self.verticalLayout_211.setObjectName(u"verticalLayout_211")
        self.textEdit_56 = QTextEdit(self.widget_361)
        self.textEdit_56.setObjectName(u"textEdit_56")
        sizePolicy4.setHeightForWidth(self.textEdit_56.sizePolicy().hasHeightForWidth())
        self.textEdit_56.setSizePolicy(sizePolicy4)
        self.textEdit_56.setMinimumSize(QSize(0, 0))
        self.textEdit_56.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_211.addWidget(self.textEdit_56)

        self.verticalSpacer_72 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_211.addItem(self.verticalSpacer_72)

        self.widget_362 = QWidget(self.widget_361)
        self.widget_362.setObjectName(u"widget_362")
        sizePolicy5.setHeightForWidth(self.widget_362.sizePolicy().hasHeightForWidth())
        self.widget_362.setSizePolicy(sizePolicy5)
        self.widget_362.setMinimumSize(QSize(300, 0))
        self.verticalLayout_212 = QVBoxLayout(self.widget_362)
        self.verticalLayout_212.setObjectName(u"verticalLayout_212")
        self.label_125 = QLabel(self.widget_362)
        self.label_125.setObjectName(u"label_125")

        self.verticalLayout_212.addWidget(self.label_125)

        self.verticalSpacer_73 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_212.addItem(self.verticalSpacer_73)

        self.comboBox_22 = QComboBox(self.widget_362)
        self.comboBox_22.setObjectName(u"comboBox_22")
        self.comboBox_22.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_212.addWidget(self.comboBox_22)


        self.verticalLayout_211.addWidget(self.widget_362)

        self.widget_363 = QWidget(self.widget_361)
        self.widget_363.setObjectName(u"widget_363")
        self.horizontalLayout_236 = QHBoxLayout(self.widget_363)
        self.horizontalLayout_236.setObjectName(u"horizontalLayout_236")
        self.horizontalSpacer_229 = QSpacerItem(361, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_236.addItem(self.horizontalSpacer_229)

        self.pushButton_137 = QPushButton(self.widget_363)
        self.pushButton_137.setObjectName(u"pushButton_137")
        self.pushButton_137.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_137.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_236.addWidget(self.pushButton_137)


        self.verticalLayout_211.addWidget(self.widget_363)


        self.horizontalLayout_235.addWidget(self.widget_361)

        self.widget_364 = QWidget(self.widget_360)
        self.widget_364.setObjectName(u"widget_364")
        self.widget_364.setMinimumSize(QSize(0, 0))
        self.verticalLayout_213 = QVBoxLayout(self.widget_364)
        self.verticalLayout_213.setObjectName(u"verticalLayout_213")
        self.verticalLayout_213.setContentsMargins(4, 4, 4, 4)
        self.listView_15 = QListView(self.widget_364)
        self.listView_15.setObjectName(u"listView_15")
        self.listView_15.setMinimumSize(QSize(0, 0))
        self.listView_15.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_213.addWidget(self.listView_15)

        self.widget_365 = QWidget(self.widget_364)
        self.widget_365.setObjectName(u"widget_365")
        self.horizontalLayout_237 = QHBoxLayout(self.widget_365)
        self.horizontalLayout_237.setObjectName(u"horizontalLayout_237")
        self.pushButton_138 = QPushButton(self.widget_365)
        self.pushButton_138.setObjectName(u"pushButton_138")
        self.pushButton_138.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_138.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_237.addWidget(self.pushButton_138)

        self.horizontalSpacer_230 = QSpacerItem(361, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_237.addItem(self.horizontalSpacer_230)


        self.verticalLayout_213.addWidget(self.widget_365)


        self.horizontalLayout_235.addWidget(self.widget_364)

        self.horizontalSpacer_231 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_235.addItem(self.horizontalSpacer_231)

        self.widget_366 = QWidget(self.widget_360)
        self.widget_366.setObjectName(u"widget_366")
        sizePolicy.setHeightForWidth(self.widget_366.sizePolicy().hasHeightForWidth())
        self.widget_366.setSizePolicy(sizePolicy)
        self.widget_366.setMinimumSize(QSize(400, 0))
        self.verticalLayout_214 = QVBoxLayout(self.widget_366)
        self.verticalLayout_214.setObjectName(u"verticalLayout_214")
        self.widget_367 = QWidget(self.widget_366)
        self.widget_367.setObjectName(u"widget_367")
        self.horizontalLayout_238 = QHBoxLayout(self.widget_367)
        self.horizontalLayout_238.setSpacing(0)
        self.horizontalLayout_238.setObjectName(u"horizontalLayout_238")
        self.horizontalLayout_238.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_232 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_238.addItem(self.horizontalSpacer_232)

        self.horizontalSpacer_233 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_238.addItem(self.horizontalSpacer_233)

        self.widget_368 = QWidget(self.widget_367)
        self.widget_368.setObjectName(u"widget_368")
        self.verticalLayout_215 = QVBoxLayout(self.widget_368)
        self.verticalLayout_215.setObjectName(u"verticalLayout_215")
        self.label_126 = QLabel(self.widget_368)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setAlignment(Qt.AlignCenter)

        self.verticalLayout_215.addWidget(self.label_126)

        self.lineEdit_56 = QLineEdit(self.widget_368)
        self.lineEdit_56.setObjectName(u"lineEdit_56")
        self.lineEdit_56.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_215.addWidget(self.lineEdit_56)


        self.horizontalLayout_238.addWidget(self.widget_368)

        self.horizontalSpacer_234 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_238.addItem(self.horizontalSpacer_234)

        self.widget_369 = QWidget(self.widget_367)
        self.widget_369.setObjectName(u"widget_369")
        self.verticalLayout_216 = QVBoxLayout(self.widget_369)
        self.verticalLayout_216.setObjectName(u"verticalLayout_216")
        self.label_127 = QLabel(self.widget_369)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setAlignment(Qt.AlignCenter)

        self.verticalLayout_216.addWidget(self.label_127)

        self.lineEdit_57 = QLineEdit(self.widget_369)
        self.lineEdit_57.setObjectName(u"lineEdit_57")
        self.lineEdit_57.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_216.addWidget(self.lineEdit_57)


        self.horizontalLayout_238.addWidget(self.widget_369)

        self.horizontalSpacer_235 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_238.addItem(self.horizontalSpacer_235)

        self.widget_370 = QWidget(self.widget_367)
        self.widget_370.setObjectName(u"widget_370")
        self.verticalLayout_217 = QVBoxLayout(self.widget_370)
        self.verticalLayout_217.setObjectName(u"verticalLayout_217")
        self.label_128 = QLabel(self.widget_370)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setAlignment(Qt.AlignCenter)

        self.verticalLayout_217.addWidget(self.label_128)

        self.lineEdit_58 = QLineEdit(self.widget_370)
        self.lineEdit_58.setObjectName(u"lineEdit_58")
        self.lineEdit_58.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_217.addWidget(self.lineEdit_58)


        self.horizontalLayout_238.addWidget(self.widget_370)

        self.horizontalSpacer_236 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_238.addItem(self.horizontalSpacer_236)

        self.widget_371 = QWidget(self.widget_367)
        self.widget_371.setObjectName(u"widget_371")
        self.verticalLayout_218 = QVBoxLayout(self.widget_371)
        self.verticalLayout_218.setObjectName(u"verticalLayout_218")
        self.label_129 = QLabel(self.widget_371)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setAlignment(Qt.AlignCenter)

        self.verticalLayout_218.addWidget(self.label_129)

        self.lineEdit_59 = QLineEdit(self.widget_371)
        self.lineEdit_59.setObjectName(u"lineEdit_59")
        self.lineEdit_59.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_218.addWidget(self.lineEdit_59)


        self.horizontalLayout_238.addWidget(self.widget_371)

        self.horizontalSpacer_237 = QSpacerItem(11, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_238.addItem(self.horizontalSpacer_237)

        self.widget_372 = QWidget(self.widget_367)
        self.widget_372.setObjectName(u"widget_372")
        self.verticalLayout_219 = QVBoxLayout(self.widget_372)
        self.verticalLayout_219.setObjectName(u"verticalLayout_219")
        self.label_130 = QLabel(self.widget_372)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setLayoutDirection(Qt.LeftToRight)
        self.label_130.setAlignment(Qt.AlignCenter)

        self.verticalLayout_219.addWidget(self.label_130)

        self.lineEdit_60 = QLineEdit(self.widget_372)
        self.lineEdit_60.setObjectName(u"lineEdit_60")
        self.lineEdit_60.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_219.addWidget(self.lineEdit_60)


        self.horizontalLayout_238.addWidget(self.widget_372)


        self.verticalLayout_214.addWidget(self.widget_367)

        self.verticalSpacer_74 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_214.addItem(self.verticalSpacer_74)

        self.widget_373 = QWidget(self.widget_366)
        self.widget_373.setObjectName(u"widget_373")
        self.horizontalLayout_239 = QHBoxLayout(self.widget_373)
        self.horizontalLayout_239.setObjectName(u"horizontalLayout_239")
        self.widget_warning_36 = QWidget(self.widget_373)
        self.widget_warning_36.setObjectName(u"widget_warning_36")
        self.widget_warning_36.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_415 = QHBoxLayout(self.widget_warning_36)
        self.horizontalLayout_415.setSpacing(0)
        self.horizontalLayout_415.setObjectName(u"horizontalLayout_415")
        self.horizontalLayout_415.setContentsMargins(10, 5, 5, 5)
        self.label_339 = QLabel(self.widget_warning_36)
        self.label_339.setObjectName(u"label_339")
        self.label_339.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_415.addWidget(self.label_339)

        self.label_340 = QLabel(self.widget_warning_36)
        self.label_340.setObjectName(u"label_340")
        self.label_340.setMinimumSize(QSize(150, 0))
        self.label_340.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_340.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_415.addWidget(self.label_340)


        self.horizontalLayout_239.addWidget(self.widget_warning_36)

        self.horizontalSpacer_238 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_239.addItem(self.horizontalSpacer_238)

        self.pushButton_139 = QPushButton(self.widget_373)
        self.pushButton_139.setObjectName(u"pushButton_139")
        self.pushButton_139.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_239.addWidget(self.pushButton_139)


        self.verticalLayout_214.addWidget(self.widget_373)


        self.horizontalLayout_235.addWidget(self.widget_366)


        self.verticalLayout_210.addWidget(self.widget_360)

        self.widget_374 = QWidget(self.widget_358)
        self.widget_374.setObjectName(u"widget_374")
        self.widget_374.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_220 = QVBoxLayout(self.widget_374)
        self.verticalLayout_220.setSpacing(0)
        self.verticalLayout_220.setObjectName(u"verticalLayout_220")
        self.verticalLayout_220.setContentsMargins(0, 0, 0, 0)
        self.widget_375 = QWidget(self.widget_374)
        self.widget_375.setObjectName(u"widget_375")
        self.horizontalLayout_240 = QHBoxLayout(self.widget_375)
        self.horizontalLayout_240.setSpacing(0)
        self.horizontalLayout_240.setObjectName(u"horizontalLayout_240")
        self.horizontalLayout_240.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_220.addWidget(self.widget_375)


        self.verticalLayout_210.addWidget(self.widget_374)


        self.verticalLayout_185.addWidget(self.widget_358)

        self.widget_376 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_376.setObjectName(u"widget_376")
        self.verticalLayout_221 = QVBoxLayout(self.widget_376)
        self.verticalLayout_221.setObjectName(u"verticalLayout_221")
        self.widget_377 = QWidget(self.widget_376)
        self.widget_377.setObjectName(u"widget_377")
        self.widget_377.setStyleSheet(u"")
        self.horizontalLayout_241 = QHBoxLayout(self.widget_377)
        self.horizontalLayout_241.setSpacing(0)
        self.horizontalLayout_241.setObjectName(u"horizontalLayout_241")
        self.horizontalLayout_241.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_46 = QWidget(self.widget_377)
        self.Equipement_widget_46.setObjectName(u"Equipement_widget_46")
        self.Equipement_widget_46.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_242 = QHBoxLayout(self.Equipement_widget_46)
        self.horizontalLayout_242.setObjectName(u"horizontalLayout_242")
        self.label_131 = QLabel(self.Equipement_widget_46)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setPixmap(QPixmap(u":/assets/icons/equippement-30.png"))

        self.horizontalLayout_242.addWidget(self.label_131, 0, Qt.AlignLeft)

        self.pushButton_140 = QPushButton(self.Equipement_widget_46)
        self.pushButton_140.setObjectName(u"pushButton_140")
        sizePolicy2.setHeightForWidth(self.pushButton_140.sizePolicy().hasHeightForWidth())
        self.pushButton_140.setSizePolicy(sizePolicy2)
        self.pushButton_140.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_140.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_140.setIcon(icon9)
        self.pushButton_140.setIconSize(QSize(24, 24))
        self.pushButton_140.setCheckable(True)

        self.horizontalLayout_242.addWidget(self.pushButton_140)


        self.horizontalLayout_241.addWidget(self.Equipement_widget_46)

        self.horizontalSpacer_239 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_241.addItem(self.horizontalSpacer_239)


        self.verticalLayout_221.addWidget(self.widget_377)

        self.widget_378 = QWidget(self.widget_376)
        self.widget_378.setObjectName(u"widget_378")
        self.widget_378.setMinimumSize(QSize(450, 0))
        self.widget_378.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.horizontalLayout_243 = QHBoxLayout(self.widget_378)
        self.horizontalLayout_243.setObjectName(u"horizontalLayout_243")
        self.horizontalSpacer_240 = QSpacerItem(255, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_243.addItem(self.horizontalSpacer_240)

        self.widget_379 = QWidget(self.widget_378)
        self.widget_379.setObjectName(u"widget_379")
        sizePolicy.setHeightForWidth(self.widget_379.sizePolicy().hasHeightForWidth())
        self.widget_379.setSizePolicy(sizePolicy)
        self.widget_379.setMinimumSize(QSize(400, 0))
        self.verticalLayout_222 = QVBoxLayout(self.widget_379)
        self.verticalLayout_222.setObjectName(u"verticalLayout_222")
        self.widget_380 = QWidget(self.widget_379)
        self.widget_380.setObjectName(u"widget_380")
        self.horizontalLayout_244 = QHBoxLayout(self.widget_380)
        self.horizontalLayout_244.setObjectName(u"horizontalLayout_244")
        self.horizontalSpacer_241 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_244.addItem(self.horizontalSpacer_241)


        self.verticalLayout_222.addWidget(self.widget_380)

        self.horizontalLayout_245 = QHBoxLayout()
        self.horizontalLayout_245.setObjectName(u"horizontalLayout_245")
        self.horizontalSpacer_242 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_245.addItem(self.horizontalSpacer_242)

        self.textEdit_57 = QTextEdit(self.widget_379)
        self.textEdit_57.setObjectName(u"textEdit_57")
        sizePolicy4.setHeightForWidth(self.textEdit_57.sizePolicy().hasHeightForWidth())
        self.textEdit_57.setSizePolicy(sizePolicy4)
        self.textEdit_57.setMinimumSize(QSize(0, 0))
        self.textEdit_57.setMaximumSize(QSize(16777215, 40))
        self.textEdit_57.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.horizontalLayout_245.addWidget(self.textEdit_57)

        self.horizontalSpacer_243 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_245.addItem(self.horizontalSpacer_243)


        self.verticalLayout_222.addLayout(self.horizontalLayout_245)

        self.lineEdit_61 = QLineEdit(self.widget_379)
        self.lineEdit_61.setObjectName(u"lineEdit_61")
        self.lineEdit_61.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_222.addWidget(self.lineEdit_61)

        self.widget_381 = QWidget(self.widget_379)
        self.widget_381.setObjectName(u"widget_381")
        self.horizontalLayout_246 = QHBoxLayout(self.widget_381)
        self.horizontalLayout_246.setObjectName(u"horizontalLayout_246")
        self.horizontalSpacer_244 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_246.addItem(self.horizontalSpacer_244)


        self.verticalLayout_222.addWidget(self.widget_381)

        self.verticalSpacer_75 = QSpacerItem(20, 148, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_222.addItem(self.verticalSpacer_75)


        self.horizontalLayout_243.addWidget(self.widget_379)

        self.horizontalSpacer_245 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_243.addItem(self.horizontalSpacer_245)


        self.verticalLayout_221.addWidget(self.widget_378)

        self.widget_382 = QWidget(self.widget_376)
        self.widget_382.setObjectName(u"widget_382")
        self.widget_382.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_223 = QVBoxLayout(self.widget_382)
        self.verticalLayout_223.setSpacing(0)
        self.verticalLayout_223.setObjectName(u"verticalLayout_223")
        self.verticalLayout_223.setContentsMargins(0, 0, 0, 0)
        self.widget_383 = QWidget(self.widget_382)
        self.widget_383.setObjectName(u"widget_383")
        self.horizontalLayout_247 = QHBoxLayout(self.widget_383)
        self.horizontalLayout_247.setSpacing(0)
        self.horizontalLayout_247.setObjectName(u"horizontalLayout_247")
        self.horizontalLayout_247.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_223.addWidget(self.widget_383)


        self.verticalLayout_221.addWidget(self.widget_382)


        self.verticalLayout_185.addWidget(self.widget_376)

        self.widget_384 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_384.setObjectName(u"widget_384")
        self.widget_384.setStyleSheet(u"")
        self.horizontalLayout_248 = QHBoxLayout(self.widget_384)
        self.horizontalLayout_248.setObjectName(u"horizontalLayout_248")
        self.Equipement_widget_47 = QWidget(self.widget_384)
        self.Equipement_widget_47.setObjectName(u"Equipement_widget_47")
        self.Equipement_widget_47.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 191, 191);\n"
"border-radius:10px;\n"
"color: white;\n"
"}\n"
"")
        self.horizontalLayout_249 = QHBoxLayout(self.Equipement_widget_47)
        self.horizontalLayout_249.setObjectName(u"horizontalLayout_249")
        self.pushButton_141 = QPushButton(self.Equipement_widget_47)
        self.pushButton_141.setObjectName(u"pushButton_141")
        sizePolicy2.setHeightForWidth(self.pushButton_141.sizePolicy().hasHeightForWidth())
        self.pushButton_141.setSizePolicy(sizePolicy2)
        self.pushButton_141.setFont(font5)
        self.pushButton_141.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_141.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(255, 191, 191);\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 191, 191);\n"
"}\n"
"")
        self.pushButton_141.setIcon(icon9)
        self.pushButton_141.setIconSize(QSize(24, 24))
        self.pushButton_141.setCheckable(True)

        self.horizontalLayout_249.addWidget(self.pushButton_141)


        self.horizontalLayout_248.addWidget(self.Equipement_widget_47)

        self.horizontalSpacer_246 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_248.addItem(self.horizontalSpacer_246)

        self.Equipement_widget_48 = QWidget(self.widget_384)
        self.Equipement_widget_48.setObjectName(u"Equipement_widget_48")
        self.Equipement_widget_48.setStyleSheet(u"QWidget{\n"
"background-color: rgb(104, 246, 73);\n"
"border-radius:10px;\n"
"color: white;\n"
"}\n"
"")
        self.horizontalLayout_250 = QHBoxLayout(self.Equipement_widget_48)
        self.horizontalLayout_250.setObjectName(u"horizontalLayout_250")
        self.pushButton_142 = QPushButton(self.Equipement_widget_48)
        self.pushButton_142.setObjectName(u"pushButton_142")
        sizePolicy2.setHeightForWidth(self.pushButton_142.sizePolicy().hasHeightForWidth())
        self.pushButton_142.setSizePolicy(sizePolicy2)
        self.pushButton_142.setFont(font5)
        self.pushButton_142.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_142.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(104, 246, 73);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(104, 246, 73);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(104, 246, 73);\n"
"}\n"
"")
        self.pushButton_142.setIcon(icon9)
        self.pushButton_142.setIconSize(QSize(24, 24))
        self.pushButton_142.setCheckable(True)

        self.horizontalLayout_250.addWidget(self.pushButton_142)


        self.horizontalLayout_248.addWidget(self.Equipement_widget_48)


        self.verticalLayout_185.addWidget(self.widget_384)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.gridLayout_5.addWidget(self.scrollArea_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.nv_dossier_prodDigital_page)
        self.autre_newMission_page = QWidget()
        self.autre_newMission_page.setObjectName(u"autre_newMission_page")
        self.gridLayout_10 = QGridLayout(self.autre_newMission_page)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.scrollArea_10 = QScrollArea(self.autre_newMission_page)
        self.scrollArea_10.setObjectName(u"scrollArea_10")
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollAreaWidgetContents_10 = QWidget()
        self.scrollAreaWidgetContents_10.setObjectName(u"scrollAreaWidgetContents_10")
        self.scrollAreaWidgetContents_10.setGeometry(QRect(0, 0, 634, 1903))
        self.gridLayout_16 = QGridLayout(self.scrollAreaWidgetContents_10)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.widget_428 = QWidget(self.scrollAreaWidgetContents_10)
        self.widget_428.setObjectName(u"widget_428")
        self.horizontalLayout_290 = QHBoxLayout(self.widget_428)
        self.horizontalLayout_290.setObjectName(u"horizontalLayout_290")
        self.label_160 = QLabel(self.widget_428)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setFont(font4)
        self.label_160.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(236, 234, 234);\n"
"	color: rgb(175, 148, 223);\n"
"padding-left:10px;\n"
"padding-right:40px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"}")

        self.horizontalLayout_290.addWidget(self.label_160)

        self.horizontalSpacer_287 = QSpacerItem(364, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_290.addItem(self.horizontalSpacer_287)

        self.label_233 = QLabel(self.widget_428)
        self.label_233.setObjectName(u"label_233")
        self.label_233.setFont(font5)

        self.horizontalLayout_290.addWidget(self.label_233)

        self.horizontalSpacer_288 = QSpacerItem(364, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_290.addItem(self.horizontalSpacer_288)

        self.label_234 = QLabel(self.widget_428)
        self.label_234.setObjectName(u"label_234")
        self.label_234.setFont(font5)

        self.horizontalLayout_290.addWidget(self.label_234)


        self.gridLayout_16.addWidget(self.widget_428, 0, 0, 1, 1)

        self.widget_682 = QWidget(self.scrollAreaWidgetContents_10)
        self.widget_682.setObjectName(u"widget_682")
        self.verticalLayout_381 = QVBoxLayout(self.widget_682)
        self.verticalLayout_381.setObjectName(u"verticalLayout_381")
        self.widget_683 = QWidget(self.widget_682)
        self.widget_683.setObjectName(u"widget_683")
        self.horizontalLayout_436 = QHBoxLayout(self.widget_683)
        self.horizontalLayout_436.setObjectName(u"horizontalLayout_436")
        self.horizontalLayout_436.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_85 = QWidget(self.widget_683)
        self.Equipement_widget_85.setObjectName(u"Equipement_widget_85")
        self.Equipement_widget_85.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_437 = QHBoxLayout(self.Equipement_widget_85)
        self.horizontalLayout_437.setObjectName(u"horizontalLayout_437")
        self.label_236 = QLabel(self.Equipement_widget_85)
        self.label_236.setObjectName(u"label_236")
        self.label_236.setPixmap(QPixmap(u":/assets/icons/employee-30.png"))

        self.horizontalLayout_437.addWidget(self.label_236, 0, Qt.AlignLeft)

        self.pushButton_219 = QPushButton(self.Equipement_widget_85)
        self.pushButton_219.setObjectName(u"pushButton_219")
        sizePolicy2.setHeightForWidth(self.pushButton_219.sizePolicy().hasHeightForWidth())
        self.pushButton_219.setSizePolicy(sizePolicy2)
        self.pushButton_219.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_219.setStyleSheet(u"")
        self.pushButton_219.setIconSize(QSize(24, 24))
        self.pushButton_219.setCheckable(True)

        self.horizontalLayout_437.addWidget(self.pushButton_219)


        self.horizontalLayout_436.addWidget(self.Equipement_widget_85)

        self.horizontalSpacer_463 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_436.addItem(self.horizontalSpacer_463)


        self.verticalLayout_381.addWidget(self.widget_683)

        self.widget_684 = QWidget(self.widget_682)
        self.widget_684.setObjectName(u"widget_684")
        self.widget_684.setMinimumSize(QSize(0, 0))
        self.widget_684.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.verticalLayout_313 = QVBoxLayout(self.widget_684)
        self.verticalLayout_313.setObjectName(u"verticalLayout_313")
        self.horizontalLayout_322 = QHBoxLayout()
        self.horizontalLayout_322.setObjectName(u"horizontalLayout_322")
        self.horizontalSpacer_464 = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_322.addItem(self.horizontalSpacer_464)

        self.widget_685 = QWidget(self.widget_684)
        self.widget_685.setObjectName(u"widget_685")
        sizePolicy.setHeightForWidth(self.widget_685.sizePolicy().hasHeightForWidth())
        self.widget_685.setSizePolicy(sizePolicy)
        self.widget_685.setMinimumSize(QSize(0, 0))
        self.verticalLayout_382 = QVBoxLayout(self.widget_685)
        self.verticalLayout_382.setObjectName(u"verticalLayout_382")
        self.textEdit_102 = QTextEdit(self.widget_685)
        self.textEdit_102.setObjectName(u"textEdit_102")
        sizePolicy4.setHeightForWidth(self.textEdit_102.sizePolicy().hasHeightForWidth())
        self.textEdit_102.setSizePolicy(sizePolicy4)
        self.textEdit_102.setMinimumSize(QSize(0, 0))
        self.textEdit_102.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_382.addWidget(self.textEdit_102)

        self.textEdit_103 = QTextEdit(self.widget_685)
        self.textEdit_103.setObjectName(u"textEdit_103")
        sizePolicy4.setHeightForWidth(self.textEdit_103.sizePolicy().hasHeightForWidth())
        self.textEdit_103.setSizePolicy(sizePolicy4)
        self.textEdit_103.setMinimumSize(QSize(0, 0))
        self.textEdit_103.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_382.addWidget(self.textEdit_103)

        self.widget_686 = QWidget(self.widget_685)
        self.widget_686.setObjectName(u"widget_686")
        self.verticalLayout_383 = QVBoxLayout(self.widget_686)
        self.verticalLayout_383.setObjectName(u"verticalLayout_383")
        self.checkBox_37 = QCheckBox(self.widget_686)
        self.checkBox_37.setObjectName(u"checkBox_37")
        self.checkBox_37.setChecked(True)

        self.verticalLayout_383.addWidget(self.checkBox_37)

        self.checkBox_38 = QCheckBox(self.widget_686)
        self.checkBox_38.setObjectName(u"checkBox_38")

        self.verticalLayout_383.addWidget(self.checkBox_38)


        self.verticalLayout_382.addWidget(self.widget_686)

        self.widget_687 = QWidget(self.widget_685)
        self.widget_687.setObjectName(u"widget_687")
        self.horizontalLayout_439 = QHBoxLayout(self.widget_687)
        self.horizontalLayout_439.setObjectName(u"horizontalLayout_439")
        self.dateEdit_12 = QDateEdit(self.widget_687)
        self.dateEdit_12.setObjectName(u"dateEdit_12")
        self.dateEdit_12.setDateTime(QDateTime(QDate(2024, 10, 31), QTime(17, 0, 0)))
        self.dateEdit_12.setCalendarPopup(True)

        self.horizontalLayout_439.addWidget(self.dateEdit_12)

        self.horizontalSpacer_465 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_439.addItem(self.horizontalSpacer_465)


        self.verticalLayout_382.addWidget(self.widget_687)


        self.horizontalLayout_322.addWidget(self.widget_685)

        self.horizontalSpacer_466 = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_322.addItem(self.horizontalSpacer_466)

        self.horizontalSpacer_467 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_322.addItem(self.horizontalSpacer_467)

        self.widget_688 = QWidget(self.widget_684)
        self.widget_688.setObjectName(u"widget_688")
        self.widget_688.setMinimumSize(QSize(0, 0))
        self.widget_688.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_384 = QVBoxLayout(self.widget_688)
        self.verticalLayout_384.setObjectName(u"verticalLayout_384")
        self.textEdit_104 = QTextEdit(self.widget_688)
        self.textEdit_104.setObjectName(u"textEdit_104")
        sizePolicy4.setHeightForWidth(self.textEdit_104.sizePolicy().hasHeightForWidth())
        self.textEdit_104.setSizePolicy(sizePolicy4)
        self.textEdit_104.setMinimumSize(QSize(0, 0))
        self.textEdit_104.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_384.addWidget(self.textEdit_104)

        self.widget_689 = QWidget(self.widget_688)
        self.widget_689.setObjectName(u"widget_689")
        self.verticalLayout_385 = QVBoxLayout(self.widget_689)
        self.verticalLayout_385.setObjectName(u"verticalLayout_385")
        self.checkBox_39 = QCheckBox(self.widget_689)
        self.checkBox_39.setObjectName(u"checkBox_39")
        self.checkBox_39.setChecked(True)

        self.verticalLayout_385.addWidget(self.checkBox_39)

        self.checkBox_40 = QCheckBox(self.widget_689)
        self.checkBox_40.setObjectName(u"checkBox_40")

        self.verticalLayout_385.addWidget(self.checkBox_40)


        self.verticalLayout_384.addWidget(self.widget_689)

        self.widget_690 = QWidget(self.widget_688)
        self.widget_690.setObjectName(u"widget_690")
        self.horizontalLayout_440 = QHBoxLayout(self.widget_690)
        self.horizontalLayout_440.setObjectName(u"horizontalLayout_440")
        self.label_237 = QLabel(self.widget_690)
        self.label_237.setObjectName(u"label_237")

        self.horizontalLayout_440.addWidget(self.label_237)

        self.lineEdit_110 = QLineEdit(self.widget_690)
        self.lineEdit_110.setObjectName(u"lineEdit_110")
        self.lineEdit_110.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_440.addWidget(self.lineEdit_110)


        self.verticalLayout_384.addWidget(self.widget_690)


        self.horizontalLayout_322.addWidget(self.widget_688)

        self.horizontalSpacer_469 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_322.addItem(self.horizontalSpacer_469)


        self.verticalLayout_313.addLayout(self.horizontalLayout_322)

        self.widget_691 = QWidget(self.widget_684)
        self.widget_691.setObjectName(u"widget_691")
        self.horizontalLayout_417 = QHBoxLayout(self.widget_691)
        self.horizontalLayout_417.setObjectName(u"horizontalLayout_417")
        self.widget_warning_37 = QWidget(self.widget_691)
        self.widget_warning_37.setObjectName(u"widget_warning_37")
        self.widget_warning_37.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_416 = QHBoxLayout(self.widget_warning_37)
        self.horizontalLayout_416.setSpacing(0)
        self.horizontalLayout_416.setObjectName(u"horizontalLayout_416")
        self.horizontalLayout_416.setContentsMargins(10, 5, 5, 5)
        self.label_238 = QLabel(self.widget_warning_37)
        self.label_238.setObjectName(u"label_238")
        self.label_238.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_416.addWidget(self.label_238)

        self.label_341 = QLabel(self.widget_warning_37)
        self.label_341.setObjectName(u"label_341")
        self.label_341.setMinimumSize(QSize(150, 0))
        self.label_341.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_341.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_416.addWidget(self.label_341)


        self.horizontalLayout_417.addWidget(self.widget_warning_37)

        self.horizontalSpacer_468 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_417.addItem(self.horizontalSpacer_468)

        self.pushButton_220 = QPushButton(self.widget_691)
        self.pushButton_220.setObjectName(u"pushButton_220")
        self.pushButton_220.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_220.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_417.addWidget(self.pushButton_220)


        self.verticalLayout_313.addWidget(self.widget_691)


        self.verticalLayout_381.addWidget(self.widget_684)


        self.gridLayout_16.addWidget(self.widget_682, 1, 0, 1, 1)

        self.widget_698 = QWidget(self.scrollAreaWidgetContents_10)
        self.widget_698.setObjectName(u"widget_698")
        self.verticalLayout_389 = QVBoxLayout(self.widget_698)
        self.verticalLayout_389.setObjectName(u"verticalLayout_389")
        self.widget_699 = QWidget(self.widget_698)
        self.widget_699.setObjectName(u"widget_699")
        self.horizontalLayout_446 = QHBoxLayout(self.widget_699)
        self.horizontalLayout_446.setObjectName(u"horizontalLayout_446")
        self.horizontalLayout_446.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_87 = QWidget(self.widget_699)
        self.Equipement_widget_87.setObjectName(u"Equipement_widget_87")
        self.Equipement_widget_87.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_447 = QHBoxLayout(self.Equipement_widget_87)
        self.horizontalLayout_447.setObjectName(u"horizontalLayout_447")
        self.label_240 = QLabel(self.Equipement_widget_87)
        self.label_240.setObjectName(u"label_240")
        self.label_240.setPixmap(QPixmap(u":/assets/icons/employee-30.png"))

        self.horizontalLayout_447.addWidget(self.label_240, 0, Qt.AlignLeft)

        self.pushButton_223 = QPushButton(self.Equipement_widget_87)
        self.pushButton_223.setObjectName(u"pushButton_223")
        sizePolicy2.setHeightForWidth(self.pushButton_223.sizePolicy().hasHeightForWidth())
        self.pushButton_223.setSizePolicy(sizePolicy2)
        self.pushButton_223.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_223.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_223.setIcon(icon9)
        self.pushButton_223.setIconSize(QSize(24, 24))
        self.pushButton_223.setCheckable(True)

        self.horizontalLayout_447.addWidget(self.pushButton_223)


        self.horizontalLayout_446.addWidget(self.Equipement_widget_87)

        self.horizontalSpacer_473 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_446.addItem(self.horizontalSpacer_473)


        self.verticalLayout_389.addWidget(self.widget_699)

        self.widget_700 = QWidget(self.widget_698)
        self.widget_700.setObjectName(u"widget_700")
        self.widget_700.setMinimumSize(QSize(450, 0))
        self.widget_700.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.verticalLayout_314 = QVBoxLayout(self.widget_700)
        self.verticalLayout_314.setObjectName(u"verticalLayout_314")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_701 = QWidget(self.widget_700)
        self.widget_701.setObjectName(u"widget_701")
        sizePolicy.setHeightForWidth(self.widget_701.sizePolicy().hasHeightForWidth())
        self.widget_701.setSizePolicy(sizePolicy)
        self.widget_701.setMinimumSize(QSize(0, 0))
        self.verticalLayout_251 = QVBoxLayout(self.widget_701)
        self.verticalLayout_251.setObjectName(u"verticalLayout_251")
        self.verticalSpacer_133 = QSpacerItem(20, 148, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_251.addItem(self.verticalSpacer_133)

        self.textEdit_109 = QTextEdit(self.widget_701)
        self.textEdit_109.setObjectName(u"textEdit_109")
        sizePolicy4.setHeightForWidth(self.textEdit_109.sizePolicy().hasHeightForWidth())
        self.textEdit_109.setSizePolicy(sizePolicy4)
        self.textEdit_109.setMinimumSize(QSize(0, 0))
        self.textEdit_109.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_251.addWidget(self.textEdit_109)

        self.comboBox_40 = QComboBox(self.widget_701)
        self.comboBox_40.setObjectName(u"comboBox_40")
        self.comboBox_40.setMinimumSize(QSize(0, 0))
        self.comboBox_40.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_251.addWidget(self.comboBox_40)

        self.textEdit_108 = QTextEdit(self.widget_701)
        self.textEdit_108.setObjectName(u"textEdit_108")
        sizePolicy4.setHeightForWidth(self.textEdit_108.sizePolicy().hasHeightForWidth())
        self.textEdit_108.setSizePolicy(sizePolicy4)
        self.textEdit_108.setMinimumSize(QSize(0, 0))
        self.textEdit_108.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_251.addWidget(self.textEdit_108)

        self.comboBox_39 = QComboBox(self.widget_701)
        self.comboBox_39.setObjectName(u"comboBox_39")
        self.comboBox_39.setMinimumSize(QSize(0, 0))
        self.comboBox_39.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_251.addWidget(self.comboBox_39)

        self.widget_702 = QWidget(self.widget_701)
        self.widget_702.setObjectName(u"widget_702")
        self.horizontalLayout_449 = QHBoxLayout(self.widget_702)
        self.horizontalLayout_449.setObjectName(u"horizontalLayout_449")
        self.horizontalSpacer_474 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_449.addItem(self.horizontalSpacer_474)

        self.pushButton_224 = QPushButton(self.widget_702)
        self.pushButton_224.setObjectName(u"pushButton_224")
        self.pushButton_224.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_449.addWidget(self.pushButton_224)


        self.verticalLayout_251.addWidget(self.widget_702)


        self.horizontalLayout.addWidget(self.widget_701)

        self.horizontalSpacer_475 = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_475)

        self.widget_703 = QWidget(self.widget_700)
        self.widget_703.setObjectName(u"widget_703")
        self.widget_703.setMinimumSize(QSize(0, 0))
        self.verticalLayout_391 = QVBoxLayout(self.widget_703)
        self.verticalLayout_391.setObjectName(u"verticalLayout_391")
        self.verticalLayout_391.setContentsMargins(4, 4, 4, 4)
        self.listView_28 = QListView(self.widget_703)
        self.listView_28.setObjectName(u"listView_28")
        self.listView_28.setMinimumSize(QSize(0, 0))
        self.listView_28.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_391.addWidget(self.listView_28)

        self.widget_704 = QWidget(self.widget_703)
        self.widget_704.setObjectName(u"widget_704")
        self.horizontalLayout_450 = QHBoxLayout(self.widget_704)
        self.horizontalLayout_450.setObjectName(u"horizontalLayout_450")
        self.pushButton_225 = QPushButton(self.widget_704)
        self.pushButton_225.setObjectName(u"pushButton_225")
        self.pushButton_225.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_225.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_450.addWidget(self.pushButton_225)

        self.horizontalSpacer_476 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_450.addItem(self.horizontalSpacer_476)


        self.verticalLayout_391.addWidget(self.widget_704)


        self.horizontalLayout.addWidget(self.widget_703)

        self.horizontalSpacer_477 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_477)


        self.verticalLayout_314.addLayout(self.horizontalLayout)

        self.widget_692 = QWidget(self.widget_700)
        self.widget_692.setObjectName(u"widget_692")
        self.horizontalLayout_419 = QHBoxLayout(self.widget_692)
        self.horizontalLayout_419.setObjectName(u"horizontalLayout_419")
        self.widget_warning_38 = QWidget(self.widget_692)
        self.widget_warning_38.setObjectName(u"widget_warning_38")
        self.widget_warning_38.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_418 = QHBoxLayout(self.widget_warning_38)
        self.horizontalLayout_418.setSpacing(0)
        self.horizontalLayout_418.setObjectName(u"horizontalLayout_418")
        self.horizontalLayout_418.setContentsMargins(10, 5, 5, 5)
        self.label_273 = QLabel(self.widget_warning_38)
        self.label_273.setObjectName(u"label_273")
        self.label_273.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_418.addWidget(self.label_273)

        self.label_342 = QLabel(self.widget_warning_38)
        self.label_342.setObjectName(u"label_342")
        self.label_342.setMinimumSize(QSize(150, 0))
        self.label_342.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_342.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_418.addWidget(self.label_342)


        self.horizontalLayout_419.addWidget(self.widget_warning_38)

        self.horizontalSpacer_470 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_419.addItem(self.horizontalSpacer_470)

        self.pushButton_221 = QPushButton(self.widget_692)
        self.pushButton_221.setObjectName(u"pushButton_221")
        self.pushButton_221.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_221.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_419.addWidget(self.pushButton_221)


        self.verticalLayout_314.addWidget(self.widget_692)


        self.verticalLayout_389.addWidget(self.widget_700)


        self.gridLayout_16.addWidget(self.widget_698, 2, 0, 1, 1)

        self.widget_714 = QWidget(self.scrollAreaWidgetContents_10)
        self.widget_714.setObjectName(u"widget_714")
        self.verticalLayout_396 = QVBoxLayout(self.widget_714)
        self.verticalLayout_396.setObjectName(u"verticalLayout_396")
        self.widget_715 = QWidget(self.widget_714)
        self.widget_715.setObjectName(u"widget_715")
        self.widget_715.setStyleSheet(u"")
        self.horizontalLayout_457 = QHBoxLayout(self.widget_715)
        self.horizontalLayout_457.setObjectName(u"horizontalLayout_457")
        self.horizontalLayout_457.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_89 = QWidget(self.widget_715)
        self.Equipement_widget_89.setObjectName(u"Equipement_widget_89")
        self.Equipement_widget_89.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_458 = QHBoxLayout(self.Equipement_widget_89)
        self.horizontalLayout_458.setObjectName(u"horizontalLayout_458")
        self.label_242 = QLabel(self.Equipement_widget_89)
        self.label_242.setObjectName(u"label_242")
        self.label_242.setPixmap(QPixmap(u":/assets/icons/equippement-30.png"))

        self.horizontalLayout_458.addWidget(self.label_242, 0, Qt.AlignLeft)

        self.pushButton_229 = QPushButton(self.Equipement_widget_89)
        self.pushButton_229.setObjectName(u"pushButton_229")
        sizePolicy2.setHeightForWidth(self.pushButton_229.sizePolicy().hasHeightForWidth())
        self.pushButton_229.setSizePolicy(sizePolicy2)
        self.pushButton_229.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_229.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_229.setIcon(icon9)
        self.pushButton_229.setIconSize(QSize(24, 24))
        self.pushButton_229.setCheckable(True)

        self.horizontalLayout_458.addWidget(self.pushButton_229)


        self.horizontalLayout_457.addWidget(self.Equipement_widget_89)

        self.horizontalSpacer_483 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_457.addItem(self.horizontalSpacer_483)


        self.verticalLayout_396.addWidget(self.widget_715)

        self.widget_716 = QWidget(self.widget_714)
        self.widget_716.setObjectName(u"widget_716")
        self.widget_716.setMinimumSize(QSize(450, 0))
        self.widget_716.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.horizontalLayout_459 = QHBoxLayout(self.widget_716)
        self.horizontalLayout_459.setObjectName(u"horizontalLayout_459")
        self.horizontalLayout_459.setContentsMargins(10, 10, 10, 10)
        self.widget_717 = QWidget(self.widget_716)
        self.widget_717.setObjectName(u"widget_717")
        sizePolicy.setHeightForWidth(self.widget_717.sizePolicy().hasHeightForWidth())
        self.widget_717.setSizePolicy(sizePolicy)
        self.widget_717.setMinimumSize(QSize(400, 0))
        self.verticalLayout_397 = QVBoxLayout(self.widget_717)
        self.verticalLayout_397.setObjectName(u"verticalLayout_397")
        self.textEdit_110 = QTextEdit(self.widget_717)
        self.textEdit_110.setObjectName(u"textEdit_110")
        sizePolicy4.setHeightForWidth(self.textEdit_110.sizePolicy().hasHeightForWidth())
        self.textEdit_110.setSizePolicy(sizePolicy4)
        self.textEdit_110.setMinimumSize(QSize(0, 0))
        self.textEdit_110.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_397.addWidget(self.textEdit_110)

        self.widget_718 = QWidget(self.widget_717)
        self.widget_718.setObjectName(u"widget_718")
        self.horizontalLayout_460 = QHBoxLayout(self.widget_718)
        self.horizontalLayout_460.setObjectName(u"horizontalLayout_460")
        self.horizontalLayout_460.setContentsMargins(10, 10, 10, 10)
        self.horizontalSpacer_484 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_460.addItem(self.horizontalSpacer_484)

        self.widget_719 = QWidget(self.widget_718)
        self.widget_719.setObjectName(u"widget_719")
        sizePolicy5.setHeightForWidth(self.widget_719.sizePolicy().hasHeightForWidth())
        self.widget_719.setSizePolicy(sizePolicy5)
        self.widget_719.setMinimumSize(QSize(300, 0))
        self.verticalLayout_398 = QVBoxLayout(self.widget_719)
        self.verticalLayout_398.setObjectName(u"verticalLayout_398")
        self.label_243 = QLabel(self.widget_719)
        self.label_243.setObjectName(u"label_243")

        self.verticalLayout_398.addWidget(self.label_243)

        self.verticalSpacer_135 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_398.addItem(self.verticalSpacer_135)

        self.comboBox_41 = QComboBox(self.widget_719)
        self.comboBox_41.setObjectName(u"comboBox_41")
        self.comboBox_41.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_398.addWidget(self.comboBox_41)


        self.horizontalLayout_460.addWidget(self.widget_719)

        self.horizontalSpacer_485 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_460.addItem(self.horizontalSpacer_485)

        self.widget_720 = QWidget(self.widget_718)
        self.widget_720.setObjectName(u"widget_720")
        self.verticalLayout_399 = QVBoxLayout(self.widget_720)
        self.verticalLayout_399.setObjectName(u"verticalLayout_399")
        self.label_244 = QLabel(self.widget_720)
        self.label_244.setObjectName(u"label_244")
        self.label_244.setAlignment(Qt.AlignCenter)

        self.verticalLayout_399.addWidget(self.label_244)

        self.verticalSpacer_136 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_399.addItem(self.verticalSpacer_136)

        self.lineEdit_111 = QLineEdit(self.widget_720)
        self.lineEdit_111.setObjectName(u"lineEdit_111")
        self.lineEdit_111.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_399.addWidget(self.lineEdit_111)


        self.horizontalLayout_460.addWidget(self.widget_720)

        self.horizontalSpacer_486 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_460.addItem(self.horizontalSpacer_486)

        self.widget_721 = QWidget(self.widget_718)
        self.widget_721.setObjectName(u"widget_721")
        self.verticalLayout_400 = QVBoxLayout(self.widget_721)
        self.verticalLayout_400.setObjectName(u"verticalLayout_400")
        self.label_245 = QLabel(self.widget_721)
        self.label_245.setObjectName(u"label_245")
        self.label_245.setAlignment(Qt.AlignCenter)

        self.verticalLayout_400.addWidget(self.label_245)

        self.verticalSpacer_137 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_400.addItem(self.verticalSpacer_137)

        self.lineEdit_112 = QLineEdit(self.widget_721)
        self.lineEdit_112.setObjectName(u"lineEdit_112")
        self.lineEdit_112.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_400.addWidget(self.lineEdit_112)


        self.horizontalLayout_460.addWidget(self.widget_721)

        self.horizontalSpacer_487 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_460.addItem(self.horizontalSpacer_487)

        self.widget_722 = QWidget(self.widget_718)
        self.widget_722.setObjectName(u"widget_722")
        self.verticalLayout_401 = QVBoxLayout(self.widget_722)
        self.verticalLayout_401.setObjectName(u"verticalLayout_401")
        self.label_246 = QLabel(self.widget_722)
        self.label_246.setObjectName(u"label_246")
        self.label_246.setAlignment(Qt.AlignCenter)

        self.verticalLayout_401.addWidget(self.label_246)

        self.verticalSpacer_138 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_401.addItem(self.verticalSpacer_138)

        self.lineEdit_113 = QLineEdit(self.widget_722)
        self.lineEdit_113.setObjectName(u"lineEdit_113")
        self.lineEdit_113.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_401.addWidget(self.lineEdit_113)


        self.horizontalLayout_460.addWidget(self.widget_722)

        self.horizontalSpacer_488 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_460.addItem(self.horizontalSpacer_488)

        self.widget_723 = QWidget(self.widget_718)
        self.widget_723.setObjectName(u"widget_723")
        self.verticalLayout_402 = QVBoxLayout(self.widget_723)
        self.verticalLayout_402.setObjectName(u"verticalLayout_402")
        self.label_247 = QLabel(self.widget_723)
        self.label_247.setObjectName(u"label_247")
        self.label_247.setAlignment(Qt.AlignCenter)

        self.verticalLayout_402.addWidget(self.label_247)

        self.verticalSpacer_139 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_402.addItem(self.verticalSpacer_139)

        self.lineEdit_114 = QLineEdit(self.widget_723)
        self.lineEdit_114.setObjectName(u"lineEdit_114")
        self.lineEdit_114.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_402.addWidget(self.lineEdit_114)


        self.horizontalLayout_460.addWidget(self.widget_723)

        self.horizontalSpacer_489 = QSpacerItem(11, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_460.addItem(self.horizontalSpacer_489)

        self.widget_724 = QWidget(self.widget_718)
        self.widget_724.setObjectName(u"widget_724")
        self.verticalLayout_403 = QVBoxLayout(self.widget_724)
        self.verticalLayout_403.setObjectName(u"verticalLayout_403")
        self.label_248 = QLabel(self.widget_724)
        self.label_248.setObjectName(u"label_248")
        self.label_248.setLayoutDirection(Qt.LeftToRight)
        self.label_248.setAlignment(Qt.AlignCenter)

        self.verticalLayout_403.addWidget(self.label_248)

        self.verticalSpacer_140 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_403.addItem(self.verticalSpacer_140)

        self.lineEdit_115 = QLineEdit(self.widget_724)
        self.lineEdit_115.setObjectName(u"lineEdit_115")
        self.lineEdit_115.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_403.addWidget(self.lineEdit_115)


        self.horizontalLayout_460.addWidget(self.widget_724)

        self.horizontalSpacer_490 = QSpacerItem(171, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_460.addItem(self.horizontalSpacer_490)


        self.verticalLayout_397.addWidget(self.widget_718)

        self.widget_725 = QWidget(self.widget_717)
        self.widget_725.setObjectName(u"widget_725")
        self.horizontalLayout_421 = QHBoxLayout(self.widget_725)
        self.horizontalLayout_421.setObjectName(u"horizontalLayout_421")
        self.widget_warning_39 = QWidget(self.widget_725)
        self.widget_warning_39.setObjectName(u"widget_warning_39")
        self.widget_warning_39.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_420 = QHBoxLayout(self.widget_warning_39)
        self.horizontalLayout_420.setSpacing(0)
        self.horizontalLayout_420.setObjectName(u"horizontalLayout_420")
        self.horizontalLayout_420.setContentsMargins(10, 5, 5, 5)
        self.label_343 = QLabel(self.widget_warning_39)
        self.label_343.setObjectName(u"label_343")
        self.label_343.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_420.addWidget(self.label_343)

        self.label_344 = QLabel(self.widget_warning_39)
        self.label_344.setObjectName(u"label_344")
        self.label_344.setMinimumSize(QSize(150, 0))
        self.label_344.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_344.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_420.addWidget(self.label_344)


        self.horizontalLayout_421.addWidget(self.widget_warning_39)

        self.horizontalSpacer_491 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_421.addItem(self.horizontalSpacer_491)

        self.pushButton_230 = QPushButton(self.widget_725)
        self.pushButton_230.setObjectName(u"pushButton_230")
        self.pushButton_230.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_421.addWidget(self.pushButton_230)


        self.verticalLayout_397.addWidget(self.widget_725)

        self.verticalSpacer_141 = QSpacerItem(20, 148, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_397.addItem(self.verticalSpacer_141)


        self.horizontalLayout_459.addWidget(self.widget_717)


        self.verticalLayout_396.addWidget(self.widget_716)

        self.widget_726 = QWidget(self.widget_714)
        self.widget_726.setObjectName(u"widget_726")
        self.widget_726.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_404 = QVBoxLayout(self.widget_726)
        self.verticalLayout_404.setSpacing(0)
        self.verticalLayout_404.setObjectName(u"verticalLayout_404")
        self.verticalLayout_404.setContentsMargins(0, 0, 0, 0)
        self.widget_727 = QWidget(self.widget_726)
        self.widget_727.setObjectName(u"widget_727")
        self.horizontalLayout_462 = QHBoxLayout(self.widget_727)
        self.horizontalLayout_462.setSpacing(0)
        self.horizontalLayout_462.setObjectName(u"horizontalLayout_462")
        self.horizontalLayout_462.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_404.addWidget(self.widget_727)


        self.verticalLayout_396.addWidget(self.widget_726)


        self.gridLayout_16.addWidget(self.widget_714, 3, 0, 1, 1)

        self.widget_728 = QWidget(self.scrollAreaWidgetContents_10)
        self.widget_728.setObjectName(u"widget_728")
        self.verticalLayout_405 = QVBoxLayout(self.widget_728)
        self.verticalLayout_405.setObjectName(u"verticalLayout_405")
        self.widget_729 = QWidget(self.widget_728)
        self.widget_729.setObjectName(u"widget_729")
        self.widget_729.setStyleSheet(u"")
        self.horizontalLayout_463 = QHBoxLayout(self.widget_729)
        self.horizontalLayout_463.setObjectName(u"horizontalLayout_463")
        self.horizontalLayout_463.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_90 = QWidget(self.widget_729)
        self.Equipement_widget_90.setObjectName(u"Equipement_widget_90")
        self.Equipement_widget_90.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_464 = QHBoxLayout(self.Equipement_widget_90)
        self.horizontalLayout_464.setObjectName(u"horizontalLayout_464")
        self.label_249 = QLabel(self.Equipement_widget_90)
        self.label_249.setObjectName(u"label_249")
        self.label_249.setPixmap(QPixmap(u":/assets/icons/equippement-30.png"))

        self.horizontalLayout_464.addWidget(self.label_249, 0, Qt.AlignLeft)

        self.pushButton_231 = QPushButton(self.Equipement_widget_90)
        self.pushButton_231.setObjectName(u"pushButton_231")
        sizePolicy2.setHeightForWidth(self.pushButton_231.sizePolicy().hasHeightForWidth())
        self.pushButton_231.setSizePolicy(sizePolicy2)
        self.pushButton_231.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_231.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_231.setIcon(icon9)
        self.pushButton_231.setIconSize(QSize(24, 24))
        self.pushButton_231.setCheckable(True)

        self.horizontalLayout_464.addWidget(self.pushButton_231)


        self.horizontalLayout_463.addWidget(self.Equipement_widget_90)

        self.horizontalSpacer_492 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_463.addItem(self.horizontalSpacer_492)


        self.verticalLayout_405.addWidget(self.widget_729)

        self.widget_730 = QWidget(self.widget_728)
        self.widget_730.setObjectName(u"widget_730")
        self.widget_730.setMinimumSize(QSize(450, 0))
        self.widget_730.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.horizontalLayout_292 = QHBoxLayout(self.widget_730)
        self.horizontalLayout_292.setObjectName(u"horizontalLayout_292")
        self.horizontalSpacer_493 = QSpacerItem(13, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_292.addItem(self.horizontalSpacer_493)

        self.verticalLayout_252 = QVBoxLayout()
        self.verticalLayout_252.setObjectName(u"verticalLayout_252")
        self.horizontalLayout_291 = QHBoxLayout()
        self.horizontalLayout_291.setObjectName(u"horizontalLayout_291")
        self.widget_731 = QWidget(self.widget_730)
        self.widget_731.setObjectName(u"widget_731")
        self.verticalLayout_406 = QVBoxLayout(self.widget_731)
        self.verticalLayout_406.setObjectName(u"verticalLayout_406")
        self.textEdit_111 = QTextEdit(self.widget_731)
        self.textEdit_111.setObjectName(u"textEdit_111")
        sizePolicy4.setHeightForWidth(self.textEdit_111.sizePolicy().hasHeightForWidth())
        self.textEdit_111.setSizePolicy(sizePolicy4)
        self.textEdit_111.setMinimumSize(QSize(0, 0))
        self.textEdit_111.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_406.addWidget(self.textEdit_111)

        self.verticalSpacer_142 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_406.addItem(self.verticalSpacer_142)

        self.widget_732 = QWidget(self.widget_731)
        self.widget_732.setObjectName(u"widget_732")
        sizePolicy5.setHeightForWidth(self.widget_732.sizePolicy().hasHeightForWidth())
        self.widget_732.setSizePolicy(sizePolicy5)
        self.widget_732.setMinimumSize(QSize(300, 0))
        self.verticalLayout_407 = QVBoxLayout(self.widget_732)
        self.verticalLayout_407.setObjectName(u"verticalLayout_407")
        self.label_250 = QLabel(self.widget_732)
        self.label_250.setObjectName(u"label_250")

        self.verticalLayout_407.addWidget(self.label_250)

        self.verticalSpacer_143 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_407.addItem(self.verticalSpacer_143)

        self.comboBox_42 = QComboBox(self.widget_732)
        self.comboBox_42.setObjectName(u"comboBox_42")
        self.comboBox_42.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_407.addWidget(self.comboBox_42)


        self.verticalLayout_406.addWidget(self.widget_732)

        self.widget_733 = QWidget(self.widget_731)
        self.widget_733.setObjectName(u"widget_733")
        self.horizontalLayout_466 = QHBoxLayout(self.widget_733)
        self.horizontalLayout_466.setObjectName(u"horizontalLayout_466")
        self.horizontalSpacer_494 = QSpacerItem(361, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_466.addItem(self.horizontalSpacer_494)

        self.pushButton_232 = QPushButton(self.widget_733)
        self.pushButton_232.setObjectName(u"pushButton_232")
        self.pushButton_232.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_232.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_466.addWidget(self.pushButton_232)


        self.verticalLayout_406.addWidget(self.widget_733)


        self.horizontalLayout_291.addWidget(self.widget_731)

        self.widget_734 = QWidget(self.widget_730)
        self.widget_734.setObjectName(u"widget_734")
        self.widget_734.setMinimumSize(QSize(0, 0))
        self.verticalLayout_408 = QVBoxLayout(self.widget_734)
        self.verticalLayout_408.setObjectName(u"verticalLayout_408")
        self.verticalLayout_408.setContentsMargins(4, 4, 4, 4)
        self.listView_30 = QListView(self.widget_734)
        self.listView_30.setObjectName(u"listView_30")
        self.listView_30.setMinimumSize(QSize(0, 0))
        self.listView_30.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_408.addWidget(self.listView_30)

        self.widget_735 = QWidget(self.widget_734)
        self.widget_735.setObjectName(u"widget_735")
        self.horizontalLayout_467 = QHBoxLayout(self.widget_735)
        self.horizontalLayout_467.setObjectName(u"horizontalLayout_467")
        self.pushButton_233 = QPushButton(self.widget_735)
        self.pushButton_233.setObjectName(u"pushButton_233")
        self.pushButton_233.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_233.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_467.addWidget(self.pushButton_233)

        self.horizontalSpacer_495 = QSpacerItem(361, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_467.addItem(self.horizontalSpacer_495)


        self.verticalLayout_408.addWidget(self.widget_735)


        self.horizontalLayout_291.addWidget(self.widget_734)


        self.verticalLayout_252.addLayout(self.horizontalLayout_291)

        self.widget_736 = QWidget(self.widget_730)
        self.widget_736.setObjectName(u"widget_736")
        sizePolicy.setHeightForWidth(self.widget_736.sizePolicy().hasHeightForWidth())
        self.widget_736.setSizePolicy(sizePolicy)
        self.widget_736.setMinimumSize(QSize(400, 0))
        self.verticalLayout_409 = QVBoxLayout(self.widget_736)
        self.verticalLayout_409.setObjectName(u"verticalLayout_409")
        self.widget_737 = QWidget(self.widget_736)
        self.widget_737.setObjectName(u"widget_737")
        self.horizontalLayout_468 = QHBoxLayout(self.widget_737)
        self.horizontalLayout_468.setSpacing(0)
        self.horizontalLayout_468.setObjectName(u"horizontalLayout_468")
        self.horizontalLayout_468.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_498 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_468.addItem(self.horizontalSpacer_498)

        self.widget_738 = QWidget(self.widget_737)
        self.widget_738.setObjectName(u"widget_738")
        self.verticalLayout_410 = QVBoxLayout(self.widget_738)
        self.verticalLayout_410.setObjectName(u"verticalLayout_410")
        self.label_251 = QLabel(self.widget_738)
        self.label_251.setObjectName(u"label_251")
        self.label_251.setAlignment(Qt.AlignCenter)

        self.verticalLayout_410.addWidget(self.label_251)

        self.lineEdit_116 = QLineEdit(self.widget_738)
        self.lineEdit_116.setObjectName(u"lineEdit_116")
        self.lineEdit_116.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_410.addWidget(self.lineEdit_116)


        self.horizontalLayout_468.addWidget(self.widget_738)

        self.horizontalSpacer_499 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_468.addItem(self.horizontalSpacer_499)

        self.widget_739 = QWidget(self.widget_737)
        self.widget_739.setObjectName(u"widget_739")
        self.verticalLayout_411 = QVBoxLayout(self.widget_739)
        self.verticalLayout_411.setObjectName(u"verticalLayout_411")
        self.label_252 = QLabel(self.widget_739)
        self.label_252.setObjectName(u"label_252")
        self.label_252.setAlignment(Qt.AlignCenter)

        self.verticalLayout_411.addWidget(self.label_252)

        self.lineEdit_117 = QLineEdit(self.widget_739)
        self.lineEdit_117.setObjectName(u"lineEdit_117")
        self.lineEdit_117.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_411.addWidget(self.lineEdit_117)


        self.horizontalLayout_468.addWidget(self.widget_739)

        self.horizontalSpacer_500 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_468.addItem(self.horizontalSpacer_500)

        self.widget_740 = QWidget(self.widget_737)
        self.widget_740.setObjectName(u"widget_740")
        self.verticalLayout_412 = QVBoxLayout(self.widget_740)
        self.verticalLayout_412.setObjectName(u"verticalLayout_412")
        self.label_253 = QLabel(self.widget_740)
        self.label_253.setObjectName(u"label_253")
        self.label_253.setAlignment(Qt.AlignCenter)

        self.verticalLayout_412.addWidget(self.label_253)

        self.lineEdit_118 = QLineEdit(self.widget_740)
        self.lineEdit_118.setObjectName(u"lineEdit_118")
        self.lineEdit_118.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_412.addWidget(self.lineEdit_118)


        self.horizontalLayout_468.addWidget(self.widget_740)

        self.horizontalSpacer_501 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_468.addItem(self.horizontalSpacer_501)

        self.widget_741 = QWidget(self.widget_737)
        self.widget_741.setObjectName(u"widget_741")
        self.verticalLayout_413 = QVBoxLayout(self.widget_741)
        self.verticalLayout_413.setObjectName(u"verticalLayout_413")
        self.label_254 = QLabel(self.widget_741)
        self.label_254.setObjectName(u"label_254")
        self.label_254.setAlignment(Qt.AlignCenter)

        self.verticalLayout_413.addWidget(self.label_254)

        self.lineEdit_119 = QLineEdit(self.widget_741)
        self.lineEdit_119.setObjectName(u"lineEdit_119")
        self.lineEdit_119.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_413.addWidget(self.lineEdit_119)


        self.horizontalLayout_468.addWidget(self.widget_741)

        self.horizontalSpacer_502 = QSpacerItem(11, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_468.addItem(self.horizontalSpacer_502)

        self.widget_742 = QWidget(self.widget_737)
        self.widget_742.setObjectName(u"widget_742")
        self.verticalLayout_414 = QVBoxLayout(self.widget_742)
        self.verticalLayout_414.setObjectName(u"verticalLayout_414")
        self.label_255 = QLabel(self.widget_742)
        self.label_255.setObjectName(u"label_255")
        self.label_255.setLayoutDirection(Qt.LeftToRight)
        self.label_255.setAlignment(Qt.AlignCenter)

        self.verticalLayout_414.addWidget(self.label_255)

        self.lineEdit_120 = QLineEdit(self.widget_742)
        self.lineEdit_120.setObjectName(u"lineEdit_120")
        self.lineEdit_120.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_414.addWidget(self.lineEdit_120)


        self.horizontalLayout_468.addWidget(self.widget_742)


        self.verticalLayout_409.addWidget(self.widget_737)

        self.widget_743 = QWidget(self.widget_736)
        self.widget_743.setObjectName(u"widget_743")
        self.horizontalLayout_423 = QHBoxLayout(self.widget_743)
        self.horizontalLayout_423.setObjectName(u"horizontalLayout_423")
        self.widget_warning_40 = QWidget(self.widget_743)
        self.widget_warning_40.setObjectName(u"widget_warning_40")
        self.widget_warning_40.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_422 = QHBoxLayout(self.widget_warning_40)
        self.horizontalLayout_422.setSpacing(0)
        self.horizontalLayout_422.setObjectName(u"horizontalLayout_422")
        self.horizontalLayout_422.setContentsMargins(10, 5, 5, 5)
        self.label_345 = QLabel(self.widget_warning_40)
        self.label_345.setObjectName(u"label_345")
        self.label_345.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_422.addWidget(self.label_345)

        self.label_346 = QLabel(self.widget_warning_40)
        self.label_346.setObjectName(u"label_346")
        self.label_346.setMinimumSize(QSize(150, 0))
        self.label_346.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_346.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_422.addWidget(self.label_346)


        self.horizontalLayout_423.addWidget(self.widget_warning_40)

        self.horizontalSpacer_503 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_423.addItem(self.horizontalSpacer_503)

        self.pushButton_234 = QPushButton(self.widget_743)
        self.pushButton_234.setObjectName(u"pushButton_234")
        self.pushButton_234.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_423.addWidget(self.pushButton_234)


        self.verticalLayout_409.addWidget(self.widget_743)

        self.verticalSpacer_144 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_409.addItem(self.verticalSpacer_144)


        self.verticalLayout_252.addWidget(self.widget_736)


        self.horizontalLayout_292.addLayout(self.verticalLayout_252)

        self.horizontalSpacer_496 = QSpacerItem(30, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_292.addItem(self.horizontalSpacer_496)


        self.verticalLayout_405.addWidget(self.widget_730)

        self.widget_744 = QWidget(self.widget_728)
        self.widget_744.setObjectName(u"widget_744")
        self.widget_744.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_415 = QVBoxLayout(self.widget_744)
        self.verticalLayout_415.setSpacing(0)
        self.verticalLayout_415.setObjectName(u"verticalLayout_415")
        self.verticalLayout_415.setContentsMargins(0, 0, 0, 0)
        self.widget_745 = QWidget(self.widget_744)
        self.widget_745.setObjectName(u"widget_745")
        self.horizontalLayout_470 = QHBoxLayout(self.widget_745)
        self.horizontalLayout_470.setSpacing(0)
        self.horizontalLayout_470.setObjectName(u"horizontalLayout_470")
        self.horizontalLayout_470.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_415.addWidget(self.widget_745)


        self.verticalLayout_405.addWidget(self.widget_744)


        self.gridLayout_16.addWidget(self.widget_728, 4, 0, 1, 1)

        self.widget_746 = QWidget(self.scrollAreaWidgetContents_10)
        self.widget_746.setObjectName(u"widget_746")
        self.verticalLayout_416 = QVBoxLayout(self.widget_746)
        self.verticalLayout_416.setObjectName(u"verticalLayout_416")
        self.widget_747 = QWidget(self.widget_746)
        self.widget_747.setObjectName(u"widget_747")
        self.widget_747.setStyleSheet(u"")
        self.horizontalLayout_471 = QHBoxLayout(self.widget_747)
        self.horizontalLayout_471.setSpacing(0)
        self.horizontalLayout_471.setObjectName(u"horizontalLayout_471")
        self.horizontalLayout_471.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_91 = QWidget(self.widget_747)
        self.Equipement_widget_91.setObjectName(u"Equipement_widget_91")
        self.Equipement_widget_91.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_472 = QHBoxLayout(self.Equipement_widget_91)
        self.horizontalLayout_472.setObjectName(u"horizontalLayout_472")
        self.label_256 = QLabel(self.Equipement_widget_91)
        self.label_256.setObjectName(u"label_256")
        self.label_256.setPixmap(QPixmap(u":/assets/icons/equippement-30.png"))

        self.horizontalLayout_472.addWidget(self.label_256, 0, Qt.AlignLeft)

        self.pushButton_235 = QPushButton(self.Equipement_widget_91)
        self.pushButton_235.setObjectName(u"pushButton_235")
        sizePolicy2.setHeightForWidth(self.pushButton_235.sizePolicy().hasHeightForWidth())
        self.pushButton_235.setSizePolicy(sizePolicy2)
        self.pushButton_235.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_235.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_235.setIcon(icon9)
        self.pushButton_235.setIconSize(QSize(24, 24))
        self.pushButton_235.setCheckable(True)

        self.horizontalLayout_472.addWidget(self.pushButton_235)


        self.horizontalLayout_471.addWidget(self.Equipement_widget_91)

        self.horizontalSpacer_504 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_471.addItem(self.horizontalSpacer_504)


        self.verticalLayout_416.addWidget(self.widget_747)

        self.widget_748 = QWidget(self.widget_746)
        self.widget_748.setObjectName(u"widget_748")
        self.widget_748.setMinimumSize(QSize(450, 0))
        self.widget_748.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.horizontalLayout_473 = QHBoxLayout(self.widget_748)
        self.horizontalLayout_473.setObjectName(u"horizontalLayout_473")
        self.horizontalSpacer_505 = QSpacerItem(255, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_473.addItem(self.horizontalSpacer_505)

        self.widget_749 = QWidget(self.widget_748)
        self.widget_749.setObjectName(u"widget_749")
        sizePolicy.setHeightForWidth(self.widget_749.sizePolicy().hasHeightForWidth())
        self.widget_749.setSizePolicy(sizePolicy)
        self.widget_749.setMinimumSize(QSize(400, 0))
        self.verticalLayout_417 = QVBoxLayout(self.widget_749)
        self.verticalLayout_417.setObjectName(u"verticalLayout_417")
        self.widget_750 = QWidget(self.widget_749)
        self.widget_750.setObjectName(u"widget_750")
        self.horizontalLayout_474 = QHBoxLayout(self.widget_750)
        self.horizontalLayout_474.setObjectName(u"horizontalLayout_474")
        self.horizontalSpacer_506 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_474.addItem(self.horizontalSpacer_506)


        self.verticalLayout_417.addWidget(self.widget_750)

        self.horizontalLayout_475 = QHBoxLayout()
        self.horizontalLayout_475.setObjectName(u"horizontalLayout_475")
        self.horizontalSpacer_507 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_475.addItem(self.horizontalSpacer_507)

        self.textEdit_112 = QTextEdit(self.widget_749)
        self.textEdit_112.setObjectName(u"textEdit_112")
        sizePolicy4.setHeightForWidth(self.textEdit_112.sizePolicy().hasHeightForWidth())
        self.textEdit_112.setSizePolicy(sizePolicy4)
        self.textEdit_112.setMinimumSize(QSize(0, 0))
        self.textEdit_112.setMaximumSize(QSize(16777215, 40))
        self.textEdit_112.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.horizontalLayout_475.addWidget(self.textEdit_112)

        self.horizontalSpacer_508 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_475.addItem(self.horizontalSpacer_508)


        self.verticalLayout_417.addLayout(self.horizontalLayout_475)

        self.lineEdit_121 = QLineEdit(self.widget_749)
        self.lineEdit_121.setObjectName(u"lineEdit_121")
        self.lineEdit_121.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_417.addWidget(self.lineEdit_121)

        self.widget_751 = QWidget(self.widget_749)
        self.widget_751.setObjectName(u"widget_751")
        self.horizontalLayout_476 = QHBoxLayout(self.widget_751)
        self.horizontalLayout_476.setObjectName(u"horizontalLayout_476")
        self.horizontalSpacer_509 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_476.addItem(self.horizontalSpacer_509)


        self.verticalLayout_417.addWidget(self.widget_751)

        self.verticalSpacer_145 = QSpacerItem(20, 148, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_417.addItem(self.verticalSpacer_145)


        self.horizontalLayout_473.addWidget(self.widget_749)

        self.horizontalSpacer_510 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_473.addItem(self.horizontalSpacer_510)


        self.verticalLayout_416.addWidget(self.widget_748)

        self.widget_752 = QWidget(self.widget_746)
        self.widget_752.setObjectName(u"widget_752")
        self.widget_752.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_418 = QVBoxLayout(self.widget_752)
        self.verticalLayout_418.setSpacing(0)
        self.verticalLayout_418.setObjectName(u"verticalLayout_418")
        self.verticalLayout_418.setContentsMargins(0, 0, 0, 0)
        self.widget_753 = QWidget(self.widget_752)
        self.widget_753.setObjectName(u"widget_753")
        self.horizontalLayout_477 = QHBoxLayout(self.widget_753)
        self.horizontalLayout_477.setSpacing(0)
        self.horizontalLayout_477.setObjectName(u"horizontalLayout_477")
        self.horizontalLayout_477.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_418.addWidget(self.widget_753)


        self.verticalLayout_416.addWidget(self.widget_752)


        self.gridLayout_16.addWidget(self.widget_746, 5, 0, 1, 1)

        self.widget_754 = QWidget(self.scrollAreaWidgetContents_10)
        self.widget_754.setObjectName(u"widget_754")
        self.widget_754.setStyleSheet(u"")
        self.horizontalLayout_478 = QHBoxLayout(self.widget_754)
        self.horizontalLayout_478.setObjectName(u"horizontalLayout_478")
        self.Equipement_widget_92 = QWidget(self.widget_754)
        self.Equipement_widget_92.setObjectName(u"Equipement_widget_92")
        self.Equipement_widget_92.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 191, 191);\n"
"border-radius:10px;\n"
"color: white;\n"
"}\n"
"")
        self.horizontalLayout_479 = QHBoxLayout(self.Equipement_widget_92)
        self.horizontalLayout_479.setObjectName(u"horizontalLayout_479")
        self.pushButton_236 = QPushButton(self.Equipement_widget_92)
        self.pushButton_236.setObjectName(u"pushButton_236")
        sizePolicy2.setHeightForWidth(self.pushButton_236.sizePolicy().hasHeightForWidth())
        self.pushButton_236.setSizePolicy(sizePolicy2)
        self.pushButton_236.setFont(font5)
        self.pushButton_236.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_236.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(255, 191, 191);\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 191, 191);\n"
"}\n"
"")
        self.pushButton_236.setIcon(icon9)
        self.pushButton_236.setIconSize(QSize(24, 24))
        self.pushButton_236.setCheckable(True)

        self.horizontalLayout_479.addWidget(self.pushButton_236)


        self.horizontalLayout_478.addWidget(self.Equipement_widget_92)

        self.horizontalSpacer_511 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_478.addItem(self.horizontalSpacer_511)

        self.Equipement_widget_93 = QWidget(self.widget_754)
        self.Equipement_widget_93.setObjectName(u"Equipement_widget_93")
        self.Equipement_widget_93.setStyleSheet(u"QWidget{\n"
"background-color: rgb(104, 246, 73);\n"
"border-radius:10px;\n"
"color: white;\n"
"}\n"
"")
        self.horizontalLayout_480 = QHBoxLayout(self.Equipement_widget_93)
        self.horizontalLayout_480.setObjectName(u"horizontalLayout_480")
        self.pushButton_237 = QPushButton(self.Equipement_widget_93)
        self.pushButton_237.setObjectName(u"pushButton_237")
        sizePolicy2.setHeightForWidth(self.pushButton_237.sizePolicy().hasHeightForWidth())
        self.pushButton_237.setSizePolicy(sizePolicy2)
        self.pushButton_237.setFont(font5)
        self.pushButton_237.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_237.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(104, 246, 73);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(104, 246, 73);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(104, 246, 73);\n"
"}\n"
"")
        self.pushButton_237.setIcon(icon9)
        self.pushButton_237.setIconSize(QSize(24, 24))
        self.pushButton_237.setCheckable(True)

        self.horizontalLayout_480.addWidget(self.pushButton_237)


        self.horizontalLayout_478.addWidget(self.Equipement_widget_93)


        self.gridLayout_16.addWidget(self.widget_754, 6, 0, 1, 1)

        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_10)

        self.gridLayout_10.addWidget(self.scrollArea_10, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.autre_newMission_page)
        self.data_newEquipement_page = QWidget()
        self.data_newEquipement_page.setObjectName(u"data_newEquipement_page")
        self.gridLayout_8 = QGridLayout(self.data_newEquipement_page)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.scrollArea_8 = QScrollArea(self.data_newEquipement_page)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 486, 1205))
        self.gridLayout_18 = QGridLayout(self.scrollAreaWidgetContents_8)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.widget_534 = QWidget(self.scrollAreaWidgetContents_8)
        self.widget_534.setObjectName(u"widget_534")
        self.horizontalLayout_362 = QHBoxLayout(self.widget_534)
        self.horizontalLayout_362.setObjectName(u"horizontalLayout_362")
        self.label_201 = QLabel(self.widget_534)
        self.label_201.setObjectName(u"label_201")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_201.sizePolicy().hasHeightForWidth())
        self.label_201.setSizePolicy(sizePolicy6)
        self.label_201.setFont(font4)
        self.label_201.setStyleSheet(u"QLabel{\n"
"background-color: rgb(36, 38, 140);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:10px;\n"
"padding-right:40px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"}")

        self.horizontalLayout_362.addWidget(self.label_201)

        self.horizontalSpacer_297 = QSpacerItem(364, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_362.addItem(self.horizontalSpacer_297)

        self.label_241 = QLabel(self.widget_534)
        self.label_241.setObjectName(u"label_241")
        self.label_241.setFont(font5)

        self.horizontalLayout_362.addWidget(self.label_241)

        self.horizontalSpacer_298 = QSpacerItem(364, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_362.addItem(self.horizontalSpacer_298)

        self.label_257 = QLabel(self.widget_534)
        self.label_257.setObjectName(u"label_257")
        self.label_257.setFont(font5)

        self.horizontalLayout_362.addWidget(self.label_257)


        self.gridLayout_18.addWidget(self.widget_534, 0, 0, 1, 1)

        self.widget_429 = QWidget(self.scrollAreaWidgetContents_8)
        self.widget_429.setObjectName(u"widget_429")
        self.gridLayout_17 = QGridLayout(self.widget_429)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.widget_430 = QWidget(self.widget_429)
        self.widget_430.setObjectName(u"widget_430")
        self.horizontalLayout_274 = QHBoxLayout(self.widget_430)
        self.horizontalLayout_274.setObjectName(u"horizontalLayout_274")
        self.horizontalLayout_274.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_53 = QWidget(self.widget_430)
        self.Equipement_widget_53.setObjectName(u"Equipement_widget_53")
        sizePolicy6.setHeightForWidth(self.Equipement_widget_53.sizePolicy().hasHeightForWidth())
        self.Equipement_widget_53.setSizePolicy(sizePolicy6)
        self.Equipement_widget_53.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_293 = QHBoxLayout(self.Equipement_widget_53)
        self.horizontalLayout_293.setObjectName(u"horizontalLayout_293")
        self.label_148 = QLabel(self.Equipement_widget_53)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setPixmap(QPixmap(u":/assets/icons/tools-30.png"))

        self.horizontalLayout_293.addWidget(self.label_148, 0, Qt.AlignLeft)

        self.pushButton_148 = QPushButton(self.Equipement_widget_53)
        self.pushButton_148.setObjectName(u"pushButton_148")
        sizePolicy2.setHeightForWidth(self.pushButton_148.sizePolicy().hasHeightForWidth())
        self.pushButton_148.setSizePolicy(sizePolicy2)
        self.pushButton_148.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_148.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(245, 245, 245);\n"
"}\n"
"")
        self.pushButton_148.setIconSize(QSize(24, 24))
        self.pushButton_148.setCheckable(False)

        self.horizontalLayout_293.addWidget(self.pushButton_148)


        self.horizontalLayout_274.addWidget(self.Equipement_widget_53)

        self.horizontalSpacer_270 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_274.addItem(self.horizontalSpacer_270)


        self.gridLayout_17.addWidget(self.widget_430, 0, 0, 1, 1)

        self.widget_431 = QWidget(self.widget_429)
        self.widget_431.setObjectName(u"widget_431")
        self.widget_431.setMinimumSize(QSize(450, 0))
        self.widget_431.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(245, 245, 245);")
        self.verticalLayout_255 = QVBoxLayout(self.widget_431)
        self.verticalLayout_255.setSpacing(0)
        self.verticalLayout_255.setObjectName(u"verticalLayout_255")
        self.verticalLayout_255.setContentsMargins(-1, -1, -1, 0)
        self.widget_432 = QWidget(self.widget_431)
        self.widget_432.setObjectName(u"widget_432")
        self.horizontalLayout_346 = QHBoxLayout(self.widget_432)
        self.horizontalLayout_346.setObjectName(u"horizontalLayout_346")
        self.horizontalSpacer_290 = QSpacerItem(251, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_346.addItem(self.horizontalSpacer_290)

        self.widget_433 = QWidget(self.widget_432)
        self.widget_433.setObjectName(u"widget_433")
        self.widget_433.setMinimumSize(QSize(600, 0))
        self.widget_433.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_247 = QVBoxLayout(self.widget_433)
        self.verticalLayout_247.setSpacing(10)
        self.verticalLayout_247.setObjectName(u"verticalLayout_247")
        self.verticalLayout_247.setContentsMargins(14, 14, 14, 14)
        self.widget_434 = QWidget(self.widget_433)
        self.widget_434.setObjectName(u"widget_434")
        self.widget_434.setMinimumSize(QSize(500, 0))
        self.widget_434.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-radius:5px;\n"
"")
        self.horizontalLayout_344 = QHBoxLayout(self.widget_434)
        self.horizontalLayout_344.setSpacing(30)
        self.horizontalLayout_344.setObjectName(u"horizontalLayout_344")
        self.label_185 = QLabel(self.widget_434)
        self.label_185.setObjectName(u"label_185")
        sizePolicy3.setHeightForWidth(self.label_185.sizePolicy().hasHeightForWidth())
        self.label_185.setSizePolicy(sizePolicy3)
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setItalic(False)
        self.label_185.setFont(font6)
        self.label_185.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_185.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_344.addWidget(self.label_185)

        self.lineEdit_67 = QLineEdit(self.widget_434)
        self.lineEdit_67.setObjectName(u"lineEdit_67")
        sizePolicy4.setHeightForWidth(self.lineEdit_67.sizePolicy().hasHeightForWidth())
        self.lineEdit_67.setSizePolicy(sizePolicy4)
        self.lineEdit_67.setMinimumSize(QSize(350, 0))
        self.lineEdit_67.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_67.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"padding-left:10px;")

        self.horizontalLayout_344.addWidget(self.lineEdit_67)


        self.verticalLayout_247.addWidget(self.widget_434)

        self.widget_435 = QWidget(self.widget_433)
        self.widget_435.setObjectName(u"widget_435")
        self.widget_435.setMinimumSize(QSize(350, 0))
        self.widget_435.setMaximumSize(QSize(16777215, 16777215))
        self.widget_435.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-radius:5px;\n"
"")
        self.horizontalLayout_345 = QHBoxLayout(self.widget_435)
        self.horizontalLayout_345.setSpacing(30)
        self.horizontalLayout_345.setObjectName(u"horizontalLayout_345")
        self.label_186 = QLabel(self.widget_435)
        self.label_186.setObjectName(u"label_186")
        sizePolicy3.setHeightForWidth(self.label_186.sizePolicy().hasHeightForWidth())
        self.label_186.setSizePolicy(sizePolicy3)
        self.label_186.setFont(font6)
        self.label_186.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_186.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_345.addWidget(self.label_186)

        self.lineEdit_68 = QLineEdit(self.widget_435)
        self.lineEdit_68.setObjectName(u"lineEdit_68")
        sizePolicy4.setHeightForWidth(self.lineEdit_68.sizePolicy().hasHeightForWidth())
        self.lineEdit_68.setSizePolicy(sizePolicy4)
        self.lineEdit_68.setMinimumSize(QSize(350, 0))
        self.lineEdit_68.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_68.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"padding-left:10px;")

        self.horizontalLayout_345.addWidget(self.lineEdit_68)


        self.verticalLayout_247.addWidget(self.widget_435)

        self.widget_437 = QWidget(self.widget_433)
        self.widget_437.setObjectName(u"widget_437")
        sizePolicy3.setHeightForWidth(self.widget_437.sizePolicy().hasHeightForWidth())
        self.widget_437.setSizePolicy(sizePolicy3)
        self.widget_437.setMinimumSize(QSize(350, 0))
        self.widget_437.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-radius:5px;\n"
"")
        self.horizontalLayout_347 = QHBoxLayout(self.widget_437)
        self.horizontalLayout_347.setSpacing(30)
        self.horizontalLayout_347.setObjectName(u"horizontalLayout_347")
        self.label_188 = QLabel(self.widget_437)
        self.label_188.setObjectName(u"label_188")
        sizePolicy3.setHeightForWidth(self.label_188.sizePolicy().hasHeightForWidth())
        self.label_188.setSizePolicy(sizePolicy3)
        self.label_188.setFont(font6)
        self.label_188.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_188.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_347.addWidget(self.label_188)

        self.lineEdit_69 = QLineEdit(self.widget_437)
        self.lineEdit_69.setObjectName(u"lineEdit_69")
        sizePolicy4.setHeightForWidth(self.lineEdit_69.sizePolicy().hasHeightForWidth())
        self.lineEdit_69.setSizePolicy(sizePolicy4)
        self.lineEdit_69.setMinimumSize(QSize(350, 0))
        self.lineEdit_69.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_69.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"padding-left:10px;")

        self.horizontalLayout_347.addWidget(self.lineEdit_69)


        self.verticalLayout_247.addWidget(self.widget_437)

        self.widget_439 = QWidget(self.widget_433)
        self.widget_439.setObjectName(u"widget_439")
        self.widget_439.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-radius:5px;\n"
"")
        self.horizontalLayout_343 = QHBoxLayout(self.widget_439)
        self.horizontalLayout_343.setSpacing(15)
        self.horizontalLayout_343.setObjectName(u"horizontalLayout_343")
        self.label_190 = QLabel(self.widget_439)
        self.label_190.setObjectName(u"label_190")
        self.label_190.setFont(font6)
        self.label_190.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_190.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_343.addWidget(self.label_190)

        self.widget = QWidget(self.widget_439)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";\n"
"border-radius:5px;")
        self.verticalLayout_253 = QVBoxLayout(self.widget)
        self.verticalLayout_253.setSpacing(8)
        self.verticalLayout_253.setObjectName(u"verticalLayout_253")
        self.verticalLayout_253.setContentsMargins(10, 6, 6, 6)
        self.checkBox_24 = QCheckBox(self.widget)
        self.checkBox_24.setObjectName(u"checkBox_24")
        self.checkBox_24.setStyleSheet(u"")
        self.checkBox_24.setAutoExclusive(True)

        self.verticalLayout_253.addWidget(self.checkBox_24)

        self.checkBox_29 = QCheckBox(self.widget)
        self.checkBox_29.setObjectName(u"checkBox_29")
        self.checkBox_29.setAutoExclusive(True)

        self.verticalLayout_253.addWidget(self.checkBox_29)


        self.horizontalLayout_343.addWidget(self.widget)


        self.verticalLayout_247.addWidget(self.widget_439)

        self.widget_440 = QWidget(self.widget_433)
        self.widget_440.setObjectName(u"widget_440")
        self.widget_440.setMinimumSize(QSize(500, 0))
        self.widget_440.setMaximumSize(QSize(16777215, 16777215))
        self.widget_440.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-radius:5px;\n"
"")
        self.horizontalLayout_350 = QHBoxLayout(self.widget_440)
        self.horizontalLayout_350.setSpacing(30)
        self.horizontalLayout_350.setObjectName(u"horizontalLayout_350")
        self.label_191 = QLabel(self.widget_440)
        self.label_191.setObjectName(u"label_191")
        sizePolicy3.setHeightForWidth(self.label_191.sizePolicy().hasHeightForWidth())
        self.label_191.setSizePolicy(sizePolicy3)
        self.label_191.setFont(font6)
        self.label_191.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_191.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_350.addWidget(self.label_191)

        self.lineEdit_71 = QLineEdit(self.widget_440)
        self.lineEdit_71.setObjectName(u"lineEdit_71")
        sizePolicy4.setHeightForWidth(self.lineEdit_71.sizePolicy().hasHeightForWidth())
        self.lineEdit_71.setSizePolicy(sizePolicy4)
        self.lineEdit_71.setMinimumSize(QSize(350, 0))
        self.lineEdit_71.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_71.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"padding-left:10px;")

        self.horizontalLayout_350.addWidget(self.lineEdit_71)


        self.verticalLayout_247.addWidget(self.widget_440)


        self.horizontalLayout_346.addWidget(self.widget_433)

        self.horizontalSpacer_291 = QSpacerItem(250, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_346.addItem(self.horizontalSpacer_291)


        self.verticalLayout_255.addWidget(self.widget_432)

        self.widget_438 = QWidget(self.widget_431)
        self.widget_438.setObjectName(u"widget_438")
        self.widget_438.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius:5px;")
        self.horizontalLayout_286 = QHBoxLayout(self.widget_438)
        self.horizontalLayout_286.setObjectName(u"horizontalLayout_286")
        self.widget_warning_4 = QWidget(self.widget_438)
        self.widget_warning_4.setObjectName(u"widget_warning_4")
        self.widget_warning_4.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_336 = QHBoxLayout(self.widget_warning_4)
        self.horizontalLayout_336.setSpacing(0)
        self.horizontalLayout_336.setObjectName(u"horizontalLayout_336")
        self.horizontalLayout_336.setContentsMargins(10, 5, 5, 5)
        self.label_220 = QLabel(self.widget_warning_4)
        self.label_220.setObjectName(u"label_220")
        self.label_220.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_336.addWidget(self.label_220)

        self.label_296 = QLabel(self.widget_warning_4)
        self.label_296.setObjectName(u"label_296")
        self.label_296.setMinimumSize(QSize(150, 0))
        self.label_296.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_296.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_336.addWidget(self.label_296)


        self.horizontalLayout_286.addWidget(self.widget_warning_4)

        self.horizontalSpacer_292 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_286.addItem(self.horizontalSpacer_292)

        self.pushButton_152 = QPushButton(self.widget_438)
        self.pushButton_152.setObjectName(u"pushButton_152")
        self.pushButton_152.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_152.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(36, 38, 140);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:10px;\n"
"padding-right:40px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/assets/icons/quit-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_152.setIcon(icon16)
        self.pushButton_152.setCheckable(True)

        self.horizontalLayout_286.addWidget(self.pushButton_152)


        self.verticalLayout_255.addWidget(self.widget_438)


        self.gridLayout_17.addWidget(self.widget_431, 1, 0, 1, 1)


        self.gridLayout_18.addWidget(self.widget_429, 1, 0, 1, 1)

        self.widget_436 = QWidget(self.scrollAreaWidgetContents_8)
        self.widget_436.setObjectName(u"widget_436")
        font7 = QFont()
        font7.setPointSize(7)
        self.widget_436.setFont(font7)
        self.verticalLayout_303 = QVBoxLayout(self.widget_436)
        self.verticalLayout_303.setObjectName(u"verticalLayout_303")
        self.widget_441 = QWidget(self.widget_436)
        self.widget_441.setObjectName(u"widget_441")
        self.horizontalLayout_349 = QHBoxLayout(self.widget_441)
        self.horizontalLayout_349.setObjectName(u"horizontalLayout_349")
        self.horizontalLayout_349.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_54 = QWidget(self.widget_441)
        self.Equipement_widget_54.setObjectName(u"Equipement_widget_54")
        sizePolicy6.setHeightForWidth(self.Equipement_widget_54.sizePolicy().hasHeightForWidth())
        self.Equipement_widget_54.setSizePolicy(sizePolicy6)
        self.Equipement_widget_54.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_351 = QHBoxLayout(self.Equipement_widget_54)
        self.horizontalLayout_351.setObjectName(u"horizontalLayout_351")
        self.label_187 = QLabel(self.Equipement_widget_54)
        self.label_187.setObjectName(u"label_187")
        self.label_187.setPixmap(QPixmap(u":/assets/icons/property-30.png"))

        self.horizontalLayout_351.addWidget(self.label_187, 0, Qt.AlignLeft)

        self.pushButton_153 = QPushButton(self.Equipement_widget_54)
        self.pushButton_153.setObjectName(u"pushButton_153")
        sizePolicy2.setHeightForWidth(self.pushButton_153.sizePolicy().hasHeightForWidth())
        self.pushButton_153.setSizePolicy(sizePolicy2)
        self.pushButton_153.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_153.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_153.setIcon(icon9)
        self.pushButton_153.setIconSize(QSize(24, 24))
        self.pushButton_153.setCheckable(True)

        self.horizontalLayout_351.addWidget(self.pushButton_153)


        self.horizontalLayout_349.addWidget(self.Equipement_widget_54)

        self.horizontalSpacer_293 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_349.addItem(self.horizontalSpacer_293)


        self.verticalLayout_303.addWidget(self.widget_441)

        self.widget_442 = QWidget(self.widget_436)
        self.widget_442.setObjectName(u"widget_442")
        self.widget_442.setMinimumSize(QSize(450, 0))
        self.widget_442.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(245, 245, 245);")
        self.verticalLayout_302 = QVBoxLayout(self.widget_442)
        self.verticalLayout_302.setSpacing(0)
        self.verticalLayout_302.setObjectName(u"verticalLayout_302")
        self.widget_443 = QWidget(self.widget_442)
        self.widget_443.setObjectName(u"widget_443")
        self.widget_443.setMinimumSize(QSize(250, 0))
        self.horizontalLayout_360 = QHBoxLayout(self.widget_443)
        self.horizontalLayout_360.setObjectName(u"horizontalLayout_360")
        self.horizontalSpacer_294 = QSpacerItem(251, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_360.addItem(self.horizontalSpacer_294)

        self.widget_444 = QWidget(self.widget_443)
        self.widget_444.setObjectName(u"widget_444")
        self.widget_444.setMinimumSize(QSize(650, 0))
        self.widget_444.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_261 = QVBoxLayout(self.widget_444)
        self.verticalLayout_261.setSpacing(10)
        self.verticalLayout_261.setObjectName(u"verticalLayout_261")
        self.verticalLayout_261.setContentsMargins(14, 14, 14, 14)
        self.widget_448 = QWidget(self.widget_444)
        self.widget_448.setObjectName(u"widget_448")
        self.widget_448.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-radius:5px;\n"
"")
        self.horizontalLayout_356 = QHBoxLayout(self.widget_448)
        self.horizontalLayout_356.setObjectName(u"horizontalLayout_356")
        self.label_195 = QLabel(self.widget_448)
        self.label_195.setObjectName(u"label_195")
        self.label_195.setFont(font6)
        self.label_195.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_195.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_356.addWidget(self.label_195)

        self.widget1 = QWidget(self.widget_448)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";\n"
"border-radius:5px;")
        self.verticalLayout_258 = QVBoxLayout(self.widget1)
        self.verticalLayout_258.setSpacing(8)
        self.verticalLayout_258.setObjectName(u"verticalLayout_258")
        self.verticalLayout_258.setContentsMargins(10, 6, 6, 6)
        self.checkBox_30 = QCheckBox(self.widget1)
        self.checkBox_30.setObjectName(u"checkBox_30")
        self.checkBox_30.setChecked(True)
        self.checkBox_30.setAutoExclusive(True)

        self.verticalLayout_258.addWidget(self.checkBox_30)

        self.checkBox_31 = QCheckBox(self.widget1)
        self.checkBox_31.setObjectName(u"checkBox_31")
        self.checkBox_31.setAutoExclusive(True)

        self.verticalLayout_258.addWidget(self.checkBox_31)


        self.horizontalLayout_356.addWidget(self.widget1)


        self.verticalLayout_261.addWidget(self.widget_448)

        self.widget_454 = QWidget(self.widget_444)
        self.widget_454.setObjectName(u"widget_454")
        sizePolicy3.setHeightForWidth(self.widget_454.sizePolicy().hasHeightForWidth())
        self.widget_454.setSizePolicy(sizePolicy3)
        self.widget_454.setMinimumSize(QSize(300, 0))
        self.widget_454.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-radius:5px;\n"
"")
        self.horizontalLayout_355 = QHBoxLayout(self.widget_454)
        self.horizontalLayout_355.setObjectName(u"horizontalLayout_355")
        self.widget_455 = QWidget(self.widget_454)
        self.widget_455.setObjectName(u"widget_455")
        self.verticalLayout_259 = QVBoxLayout(self.widget_455)
        self.verticalLayout_259.setObjectName(u"verticalLayout_259")
        self.label_199 = QLabel(self.widget_455)
        self.label_199.setObjectName(u"label_199")
        self.label_199.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 12pt \"Segoe UI\";")
        self.label_199.setAlignment(Qt.AlignCenter)

        self.verticalLayout_259.addWidget(self.label_199)

        self.verticalSpacer_85 = QSpacerItem(20, 111, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_259.addItem(self.verticalSpacer_85)


        self.horizontalLayout_355.addWidget(self.widget_455)

        self.widget_456 = QWidget(self.widget_454)
        self.widget_456.setObjectName(u"widget_456")
        sizePolicy5.setHeightForWidth(self.widget_456.sizePolicy().hasHeightForWidth())
        self.widget_456.setSizePolicy(sizePolicy5)
        self.widget_456.setMinimumSize(QSize(460, 0))
        self.verticalLayout_260 = QVBoxLayout(self.widget_456)
        self.verticalLayout_260.setObjectName(u"verticalLayout_260")
        self.verticalLayout_260.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_86 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_260.addItem(self.verticalSpacer_86)

        self.widget_447 = QWidget(self.widget_456)
        self.widget_447.setObjectName(u"widget_447")
        sizePolicy.setHeightForWidth(self.widget_447.sizePolicy().hasHeightForWidth())
        self.widget_447.setSizePolicy(sizePolicy)
        self.widget_447.setMinimumSize(QSize(220, 0))
        self.horizontalLayout_357 = QHBoxLayout(self.widget_447)
        self.horizontalLayout_357.setSpacing(13)
        self.horizontalLayout_357.setObjectName(u"horizontalLayout_357")
        self.label_194 = QLabel(self.widget_447)
        self.label_194.setObjectName(u"label_194")
        sizePolicy3.setHeightForWidth(self.label_194.sizePolicy().hasHeightForWidth())
        self.label_194.setSizePolicy(sizePolicy3)
        self.label_194.setFont(font6)
        self.label_194.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_194.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_357.addWidget(self.label_194)

        self.lineEdit_73 = QLineEdit(self.widget_447)
        self.lineEdit_73.setObjectName(u"lineEdit_73")
        sizePolicy4.setHeightForWidth(self.lineEdit_73.sizePolicy().hasHeightForWidth())
        self.lineEdit_73.setSizePolicy(sizePolicy4)
        self.lineEdit_73.setMinimumSize(QSize(300, 0))
        self.lineEdit_73.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_73.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"padding-left:10px;")

        self.horizontalLayout_357.addWidget(self.lineEdit_73)


        self.verticalLayout_260.addWidget(self.widget_447)

        self.widget_449 = QWidget(self.widget_456)
        self.widget_449.setObjectName(u"widget_449")
        sizePolicy.setHeightForWidth(self.widget_449.sizePolicy().hasHeightForWidth())
        self.widget_449.setSizePolicy(sizePolicy)
        self.widget_449.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_359 = QHBoxLayout(self.widget_449)
        self.horizontalLayout_359.setSpacing(100)
        self.horizontalLayout_359.setObjectName(u"horizontalLayout_359")
        self.label_196 = QLabel(self.widget_449)
        self.label_196.setObjectName(u"label_196")
        self.label_196.setFont(font6)
        self.label_196.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_196.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_359.addWidget(self.label_196)

        self.lineEdit_86 = QLineEdit(self.widget_449)
        self.lineEdit_86.setObjectName(u"lineEdit_86")
        sizePolicy4.setHeightForWidth(self.lineEdit_86.sizePolicy().hasHeightForWidth())
        self.lineEdit_86.setSizePolicy(sizePolicy4)
        self.lineEdit_86.setMinimumSize(QSize(300, 0))
        self.lineEdit_86.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_86.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"padding-left:10px;")

        self.horizontalLayout_359.addWidget(self.lineEdit_86)


        self.verticalLayout_260.addWidget(self.widget_449)

        self.verticalSpacer_87 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_260.addItem(self.verticalSpacer_87)


        self.horizontalLayout_355.addWidget(self.widget_456)


        self.verticalLayout_261.addWidget(self.widget_454)

        self.widget_451 = QWidget(self.widget_444)
        self.widget_451.setObjectName(u"widget_451")
        self.widget_451.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-radius:5px;\n"
"")
        self.horizontalLayout_361 = QHBoxLayout(self.widget_451)
        self.horizontalLayout_361.setObjectName(u"horizontalLayout_361")
        self.widget_453 = QWidget(self.widget_451)
        self.widget_453.setObjectName(u"widget_453")
        self.verticalLayout_256 = QVBoxLayout(self.widget_453)
        self.verticalLayout_256.setObjectName(u"verticalLayout_256")
        self.label_198 = QLabel(self.widget_453)
        self.label_198.setObjectName(u"label_198")
        self.label_198.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 12pt \"Segoe UI\";")

        self.verticalLayout_256.addWidget(self.label_198)

        self.verticalSpacer_84 = QSpacerItem(20, 143, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_256.addItem(self.verticalSpacer_84)


        self.horizontalLayout_361.addWidget(self.widget_453)

        self.widget_452 = QWidget(self.widget_451)
        self.widget_452.setObjectName(u"widget_452")
        self.widget_452.setLayoutDirection(Qt.RightToLeft)
        self.verticalLayout_262 = QVBoxLayout(self.widget_452)
        self.verticalLayout_262.setObjectName(u"verticalLayout_262")
        self.widget_457 = QWidget(self.widget_452)
        self.widget_457.setObjectName(u"widget_457")
        self.widget_457.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_257 = QVBoxLayout(self.widget_457)
        self.verticalLayout_257.setObjectName(u"verticalLayout_257")
        self.label_200 = QLabel(self.widget_457)
        self.label_200.setObjectName(u"label_200")
        font8 = QFont()
        font8.setFamilies([u"Segoe UI"])
        font8.setPointSize(9)
        font8.setBold(True)
        font8.setItalic(False)
        self.label_200.setFont(font8)
        self.label_200.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 9pt \"Segoe UI\";")
        self.label_200.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_257.addWidget(self.label_200)

        self.widget_533 = QWidget(self.widget_457)
        self.widget_533.setObjectName(u"widget_533")
        self.widget_533.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"background-color: rgb(245, 245, 245);\n"
"font: 700 10pt \"Segoe UI\";")
        self.horizontalLayout_352 = QHBoxLayout(self.widget_533)
        self.horizontalLayout_352.setObjectName(u"horizontalLayout_352")
        self.label_235 = QLabel(self.widget_533)
        self.label_235.setObjectName(u"label_235")

        self.horizontalLayout_352.addWidget(self.label_235)

        self.dateEdit_2 = QDateEdit(self.widget_533)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setStyleSheet(u"color: rgb(58, 58, 58);\n"
"font: 12pt \"Segoe UI\";\n"
"background-color: rgb(245, 245, 245);\n"
"border-top-left-radius:7px;\n"
"border-bottom-left-radius:7px;")
        self.dateEdit_2.setDateTime(QDateTime(QDate(2024, 10, 31), QTime(17, 0, 0)))
        self.dateEdit_2.setCalendarPopup(True)

        self.horizontalLayout_352.addWidget(self.dateEdit_2)

        self.label_239 = QLabel(self.widget_533)
        self.label_239.setObjectName(u"label_239")
        self.label_239.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_352.addWidget(self.label_239)

        self.dateEdit_10 = QDateEdit(self.widget_533)
        self.dateEdit_10.setObjectName(u"dateEdit_10")
        self.dateEdit_10.setStyleSheet(u"color: rgb(58, 58, 58);\n"
"font: 12pt \"Segoe UI\";\n"
"background-color: rgb(245, 245, 245);\n"
"border-top-left-radius:7px;\n"
"border-bottom-left-radius:7px;")
        self.dateEdit_10.setDateTime(QDateTime(QDate(2024, 10, 31), QTime(17, 0, 0)))
        self.dateEdit_10.setCalendarPopup(True)

        self.horizontalLayout_352.addWidget(self.dateEdit_10)


        self.verticalLayout_257.addWidget(self.widget_533)


        self.verticalLayout_262.addWidget(self.widget_457)

        self.widget_445 = QWidget(self.widget_452)
        self.widget_445.setObjectName(u"widget_445")
        self.widget_445.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_353 = QHBoxLayout(self.widget_445)
        self.horizontalLayout_353.setSpacing(34)
        self.horizontalLayout_353.setObjectName(u"horizontalLayout_353")
        self.label_192 = QLabel(self.widget_445)
        self.label_192.setObjectName(u"label_192")
        self.label_192.setFont(font6)
        self.label_192.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_192.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_353.addWidget(self.label_192)

        self.lineEdit_70 = QLineEdit(self.widget_445)
        self.lineEdit_70.setObjectName(u"lineEdit_70")
        self.lineEdit_70.setMinimumSize(QSize(200, 0))
        self.lineEdit_70.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"padding-left:10px;")

        self.horizontalLayout_353.addWidget(self.lineEdit_70)


        self.verticalLayout_262.addWidget(self.widget_445)

        self.widget_446 = QWidget(self.widget_452)
        self.widget_446.setObjectName(u"widget_446")
        self.widget_446.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_300 = QHBoxLayout(self.widget_446)
        self.horizontalLayout_300.setObjectName(u"horizontalLayout_300")
        self.pushButton_159 = QPushButton(self.widget_446)
        self.pushButton_159.setObjectName(u"pushButton_159")
        self.pushButton_159.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_159.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/assets/icons/count-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_159.setIcon(icon17)
        self.pushButton_159.setCheckable(True)

        self.horizontalLayout_300.addWidget(self.pushButton_159)

        self.label_193 = QLabel(self.widget_446)
        self.label_193.setObjectName(u"label_193")
        font9 = QFont()
        font9.setFamilies([u"Segoe UI"])
        font9.setPointSize(12)
        font9.setBold(True)
        font9.setItalic(False)
        self.label_193.setFont(font9)
        self.label_193.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 12pt \"Segoe UI\";")
        self.label_193.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_300.addWidget(self.label_193)

        self.label_166 = QLabel(self.widget_446)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"padding-left:10px;")
        self.label_166.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_300.addWidget(self.label_166)


        self.verticalLayout_262.addWidget(self.widget_446)


        self.horizontalLayout_361.addWidget(self.widget_452)


        self.verticalLayout_261.addWidget(self.widget_451)


        self.horizontalLayout_360.addWidget(self.widget_444)

        self.horizontalSpacer_295 = QSpacerItem(250, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_360.addItem(self.horizontalSpacer_295)


        self.verticalLayout_302.addWidget(self.widget_443)

        self.widget_450 = QWidget(self.widget_442)
        self.widget_450.setObjectName(u"widget_450")
        self.widget_450.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius:5px;")
        self.horizontalLayout_287 = QHBoxLayout(self.widget_450)
        self.horizontalLayout_287.setObjectName(u"horizontalLayout_287")
        self.widget_warning_5 = QWidget(self.widget_450)
        self.widget_warning_5.setObjectName(u"widget_warning_5")
        self.widget_warning_5.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_337 = QHBoxLayout(self.widget_warning_5)
        self.horizontalLayout_337.setSpacing(0)
        self.horizontalLayout_337.setObjectName(u"horizontalLayout_337")
        self.horizontalLayout_337.setContentsMargins(10, 5, 5, 5)
        self.label_221 = QLabel(self.widget_warning_5)
        self.label_221.setObjectName(u"label_221")
        self.label_221.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_337.addWidget(self.label_221)

        self.label_298 = QLabel(self.widget_warning_5)
        self.label_298.setObjectName(u"label_298")
        self.label_298.setMinimumSize(QSize(150, 0))
        self.label_298.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_298.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_337.addWidget(self.label_298)


        self.horizontalLayout_287.addWidget(self.widget_warning_5)

        self.horizontalSpacer_296 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_287.addItem(self.horizontalSpacer_296)

        self.pushButton_154 = QPushButton(self.widget_450)
        self.pushButton_154.setObjectName(u"pushButton_154")
        self.pushButton_154.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_154.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(36, 38, 140);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:10px;\n"
"padding-right:40px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"}")
        self.pushButton_154.setIcon(icon16)
        self.pushButton_154.setCheckable(True)

        self.horizontalLayout_287.addWidget(self.pushButton_154)


        self.verticalLayout_302.addWidget(self.widget_450)


        self.verticalLayout_303.addWidget(self.widget_442)


        self.gridLayout_18.addWidget(self.widget_436, 2, 0, 1, 1)

        self.widget_606 = QWidget(self.scrollAreaWidgetContents_8)
        self.widget_606.setObjectName(u"widget_606")
        self.widget_606.setStyleSheet(u"")
        self.horizontalLayout_386 = QHBoxLayout(self.widget_606)
        self.horizontalLayout_386.setObjectName(u"horizontalLayout_386")
        self.Equipement_widget_74 = QWidget(self.widget_606)
        self.Equipement_widget_74.setObjectName(u"Equipement_widget_74")
        sizePolicy6.setHeightForWidth(self.Equipement_widget_74.sizePolicy().hasHeightForWidth())
        self.Equipement_widget_74.setSizePolicy(sizePolicy6)
        self.Equipement_widget_74.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(236, 234, 234);\n"
"border-radius:10px;\n"
"color: white;\n"
"}\n"
"")
        self.verticalLayout_249 = QVBoxLayout(self.Equipement_widget_74)
        self.verticalLayout_249.setSpacing(20)
        self.verticalLayout_249.setObjectName(u"verticalLayout_249")
        self.verticalLayout_249.setContentsMargins(2, 2, 20, 2)
        self.label_158 = QLabel(self.Equipement_widget_74)
        self.label_158.setObjectName(u"label_158")
        self.label_158.setStyleSheet(u"color: rgb(36, 38, 140);\n"
"font: 700 7pt \"Segoe UI\";")

        self.verticalLayout_249.addWidget(self.label_158)

        self.pushButton_198 = QPushButton(self.Equipement_widget_74)
        self.pushButton_198.setObjectName(u"pushButton_198")
        sizePolicy2.setHeightForWidth(self.pushButton_198.sizePolicy().hasHeightForWidth())
        self.pushButton_198.setSizePolicy(sizePolicy2)
        self.pushButton_198.setFont(font5)
        self.pushButton_198.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_198.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(200, 131, 131);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:4px;\n"
"padding-right:4px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(226, 148, 148);\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(226, 148, 148);\n"
"}\n"
"")
        icon18 = QIcon()
        icon18.addFile(u":/assets/icons/back-arrow-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_198.setIcon(icon18)
        self.pushButton_198.setIconSize(QSize(24, 24))
        self.pushButton_198.setCheckable(True)

        self.verticalLayout_249.addWidget(self.pushButton_198)


        self.horizontalLayout_386.addWidget(self.Equipement_widget_74)

        self.horizontalSpacer_409 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_386.addItem(self.horizontalSpacer_409)

        self.Equipement_widget_75 = QWidget(self.widget_606)
        self.Equipement_widget_75.setObjectName(u"Equipement_widget_75")
        sizePolicy6.setHeightForWidth(self.Equipement_widget_75.sizePolicy().hasHeightForWidth())
        self.Equipement_widget_75.setSizePolicy(sizePolicy6)
        self.Equipement_widget_75.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(236, 234, 234);\n"
"border-radius:10px;\n"
"color: white;\n"
"}\n"
"")
        self.verticalLayout_248 = QVBoxLayout(self.Equipement_widget_75)
        self.verticalLayout_248.setSpacing(20)
        self.verticalLayout_248.setObjectName(u"verticalLayout_248")
        self.verticalLayout_248.setContentsMargins(20, 4, 2, 2)
        self.label_157 = QLabel(self.Equipement_widget_75)
        self.label_157.setObjectName(u"label_157")
        font10 = QFont()
        font10.setFamilies([u"Segoe UI"])
        font10.setPointSize(7)
        font10.setBold(True)
        font10.setItalic(False)
        self.label_157.setFont(font10)
        self.label_157.setStyleSheet(u"color: rgb(36, 38, 140);\n"
"font: 700 7pt \"Segoe UI\";")

        self.verticalLayout_248.addWidget(self.label_157)

        self.pushButton_199 = QPushButton(self.Equipement_widget_75)
        self.pushButton_199.setObjectName(u"pushButton_199")
        sizePolicy2.setHeightForWidth(self.pushButton_199.sizePolicy().hasHeightForWidth())
        self.pushButton_199.setSizePolicy(sizePolicy2)
        self.pushButton_199.setFont(font5)
        self.pushButton_199.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_199.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(165, 214, 167);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:10px;\n"
"padding-right:20px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(177, 229, 179);\n"
"}\n"
"QPushButton:checked{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(177, 229, 179);\n"
"}\n"
"")
        self.pushButton_199.setIcon(icon9)
        self.pushButton_199.setIconSize(QSize(24, 24))
        self.pushButton_199.setCheckable(True)
        self.pushButton_199.setChecked(False)

        self.verticalLayout_248.addWidget(self.pushButton_199)


        self.horizontalLayout_386.addWidget(self.Equipement_widget_75)


        self.gridLayout_18.addWidget(self.widget_606, 3, 0, 1, 1)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)

        self.gridLayout_8.addWidget(self.scrollArea_8, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.data_newEquipement_page)
        self.data_newPersonne_page = QWidget()
        self.data_newPersonne_page.setObjectName(u"data_newPersonne_page")
        self.gridLayout_6 = QGridLayout(self.data_newPersonne_page)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.scrollArea_6 = QScrollArea(self.data_newPersonne_page)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 844, 1681))
        self.verticalLayout_224 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_224.setObjectName(u"verticalLayout_224")
        self.widget_385 = QWidget(self.scrollAreaWidgetContents_6)
        self.widget_385.setObjectName(u"widget_385")
        self.horizontalLayout_251 = QHBoxLayout(self.widget_385)
        self.horizontalLayout_251.setObjectName(u"horizontalLayout_251")
        self.label_137 = QLabel(self.widget_385)
        self.label_137.setObjectName(u"label_137")
        sizePolicy6.setHeightForWidth(self.label_137.sizePolicy().hasHeightForWidth())
        self.label_137.setSizePolicy(sizePolicy6)
        self.label_137.setFont(font4)
        self.label_137.setStyleSheet(u"QLabel{\n"
"background-color: rgb(36, 38, 140);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:10px;\n"
"padding-right:40px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"}")

        self.horizontalLayout_251.addWidget(self.label_137)

        self.horizontalSpacer_257 = QSpacerItem(364, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_251.addItem(self.horizontalSpacer_257)

        self.horizontalSpacer_258 = QSpacerItem(364, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_251.addItem(self.horizontalSpacer_258)


        self.verticalLayout_224.addWidget(self.widget_385)

        self.widget_402 = QWidget(self.scrollAreaWidgetContents_6)
        self.widget_402.setObjectName(u"widget_402")
        self.verticalLayout_235 = QVBoxLayout(self.widget_402)
        self.verticalLayout_235.setObjectName(u"verticalLayout_235")
        self.widget_403 = QWidget(self.widget_402)
        self.widget_403.setObjectName(u"widget_403")
        self.horizontalLayout_262 = QHBoxLayout(self.widget_403)
        self.horizontalLayout_262.setObjectName(u"horizontalLayout_262")
        self.horizontalLayout_262.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_51 = QWidget(self.widget_403)
        self.Equipement_widget_51.setObjectName(u"Equipement_widget_51")
        sizePolicy6.setHeightForWidth(self.Equipement_widget_51.sizePolicy().hasHeightForWidth())
        self.Equipement_widget_51.setSizePolicy(sizePolicy6)
        self.Equipement_widget_51.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_263 = QHBoxLayout(self.Equipement_widget_51)
        self.horizontalLayout_263.setObjectName(u"horizontalLayout_263")
        self.label_144 = QLabel(self.Equipement_widget_51)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setPixmap(QPixmap(u":/assets/icons/employee-30.png"))

        self.horizontalLayout_263.addWidget(self.label_144, 0, Qt.AlignLeft)

        self.pushButton_147 = QPushButton(self.Equipement_widget_51)
        self.pushButton_147.setObjectName(u"pushButton_147")
        sizePolicy2.setHeightForWidth(self.pushButton_147.sizePolicy().hasHeightForWidth())
        self.pushButton_147.setSizePolicy(sizePolicy2)
        self.pushButton_147.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_147.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(245, 245, 245);\n"
"}\n"
"")
        self.pushButton_147.setIconSize(QSize(24, 24))
        self.pushButton_147.setCheckable(False)

        self.horizontalLayout_263.addWidget(self.pushButton_147)


        self.horizontalLayout_262.addWidget(self.Equipement_widget_51)

        self.horizontalSpacer_269 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_262.addItem(self.horizontalSpacer_269)


        self.verticalLayout_235.addWidget(self.widget_403)

        self.widget_404 = QWidget(self.widget_402)
        self.widget_404.setObjectName(u"widget_404")
        self.widget_404.setMinimumSize(QSize(450, 0))
        self.widget_404.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(245, 245, 245);")
        self.verticalLayout_233 = QVBoxLayout(self.widget_404)
        self.verticalLayout_233.setSpacing(0)
        self.verticalLayout_233.setObjectName(u"verticalLayout_233")
        self.widget_418 = QWidget(self.widget_404)
        self.widget_418.setObjectName(u"widget_418")
        self.horizontalLayout_276 = QHBoxLayout(self.widget_418)
        self.horizontalLayout_276.setObjectName(u"horizontalLayout_276")
        self.horizontalSpacer_271 = QSpacerItem(251, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_276.addItem(self.horizontalSpacer_271)

        self.widget_details_data_personel = QWidget(self.widget_418)
        self.widget_details_data_personel.setObjectName(u"widget_details_data_personel")
        sizePolicy5.setHeightForWidth(self.widget_details_data_personel.sizePolicy().hasHeightForWidth())
        self.widget_details_data_personel.setSizePolicy(sizePolicy5)
        self.widget_details_data_personel.setMinimumSize(QSize(600, 0))
        self.widget_details_data_personel.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_234 = QVBoxLayout(self.widget_details_data_personel)
        self.verticalLayout_234.setSpacing(10)
        self.verticalLayout_234.setObjectName(u"verticalLayout_234")
        self.verticalLayout_234.setContentsMargins(14, 14, 14, 14)
        self.widget_405 = QWidget(self.widget_details_data_personel)
        self.widget_405.setObjectName(u"widget_405")
        sizePolicy5.setHeightForWidth(self.widget_405.sizePolicy().hasHeightForWidth())
        self.widget_405.setSizePolicy(sizePolicy5)
        self.widget_405.setMinimumSize(QSize(580, 0))
        self.widget_405.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-radius:5px;")
        self.horizontalLayout_264 = QHBoxLayout(self.widget_405)
        self.horizontalLayout_264.setSpacing(100)
        self.horizontalLayout_264.setObjectName(u"horizontalLayout_264")
        self.label_138 = QLabel(self.widget_405)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setFont(font6)
        self.label_138.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_138.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_264.addWidget(self.label_138)

        self.lineEdit_63 = QLineEdit(self.widget_405)
        self.lineEdit_63.setObjectName(u"lineEdit_63")
        sizePolicy4.setHeightForWidth(self.lineEdit_63.sizePolicy().hasHeightForWidth())
        self.lineEdit_63.setSizePolicy(sizePolicy4)
        self.lineEdit_63.setMinimumSize(QSize(400, 0))
        self.lineEdit_63.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"padding-left:10px;")

        self.horizontalLayout_264.addWidget(self.lineEdit_63)


        self.verticalLayout_234.addWidget(self.widget_405)

        self.widget_406 = QWidget(self.widget_details_data_personel)
        self.widget_406.setObjectName(u"widget_406")
        sizePolicy5.setHeightForWidth(self.widget_406.sizePolicy().hasHeightForWidth())
        self.widget_406.setSizePolicy(sizePolicy5)
        self.widget_406.setMinimumSize(QSize(580, 0))
        self.widget_406.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-radius:5px;")
        self.horizontalLayout_265 = QHBoxLayout(self.widget_406)
        self.horizontalLayout_265.setSpacing(83)
        self.horizontalLayout_265.setObjectName(u"horizontalLayout_265")
        self.label_139 = QLabel(self.widget_406)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setFont(font6)
        self.label_139.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_139.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_265.addWidget(self.label_139)

        self.lineEdit_64 = QLineEdit(self.widget_406)
        self.lineEdit_64.setObjectName(u"lineEdit_64")
        sizePolicy4.setHeightForWidth(self.lineEdit_64.sizePolicy().hasHeightForWidth())
        self.lineEdit_64.setSizePolicy(sizePolicy4)
        self.lineEdit_64.setMinimumSize(QSize(400, 0))
        self.lineEdit_64.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"padding-left:10px;")

        self.horizontalLayout_265.addWidget(self.lineEdit_64)


        self.verticalLayout_234.addWidget(self.widget_406)

        self.widget_details_data_perso_date = QWidget(self.widget_details_data_personel)
        self.widget_details_data_perso_date.setObjectName(u"widget_details_data_perso_date")
        sizePolicy3.setHeightForWidth(self.widget_details_data_perso_date.sizePolicy().hasHeightForWidth())
        self.widget_details_data_perso_date.setSizePolicy(sizePolicy3)
        self.widget_details_data_perso_date.setMinimumSize(QSize(380, 0))
        self.horizontalLayout_288 = QHBoxLayout(self.widget_details_data_perso_date)
        self.horizontalLayout_288.setObjectName(u"horizontalLayout_288")
        self.horizontalSpacer_285 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_288.addItem(self.horizontalSpacer_285)

        self.widget_407 = QWidget(self.widget_details_data_perso_date)
        self.widget_407.setObjectName(u"widget_407")
        sizePolicy3.setHeightForWidth(self.widget_407.sizePolicy().hasHeightForWidth())
        self.widget_407.setSizePolicy(sizePolicy3)
        self.widget_407.setMinimumSize(QSize(500, 0))
        self.widget_407.setMaximumSize(QSize(550, 16777215))
        self.widget_407.setStyleSheet(u"background-color: rgb(245, 245, 245);")
        self.horizontalLayout_266 = QHBoxLayout(self.widget_407)
        self.horizontalLayout_266.setSpacing(0)
        self.horizontalLayout_266.setObjectName(u"horizontalLayout_266")
        self.horizontalLayout_266.setContentsMargins(15, 15, 15, 15)
        self.label_147 = QLabel(self.widget_407)
        self.label_147.setObjectName(u"label_147")
        sizePolicy3.setHeightForWidth(self.label_147.sizePolicy().hasHeightForWidth())
        self.label_147.setSizePolicy(sizePolicy3)
        self.label_147.setFont(font6)
        self.label_147.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 10pt \"Segoe UI\";")

        self.horizontalLayout_266.addWidget(self.label_147)

        self.dateEdit_person = QDateEdit(self.widget_407)
        self.dateEdit_person.setObjectName(u"dateEdit_person")
        sizePolicy4.setHeightForWidth(self.dateEdit_person.sizePolicy().hasHeightForWidth())
        self.dateEdit_person.setSizePolicy(sizePolicy4)
        self.dateEdit_person.setMinimumSize(QSize(380, 0))
        self.dateEdit_person.setStyleSheet(u"\n"
"background-color: rgb(245, 245, 245);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";\n"
"border-radius:5px;")
        self.dateEdit_person.setAlignment(Qt.AlignCenter)
        self.dateEdit_person.setDateTime(QDateTime(QDate(2024, 10, 31), QTime(17, 0, 0)))
        self.dateEdit_person.setCalendarPopup(True)

        self.horizontalLayout_266.addWidget(self.dateEdit_person)


        self.horizontalLayout_288.addWidget(self.widget_407)

        self.horizontalSpacer_286 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_288.addItem(self.horizontalSpacer_286)


        self.verticalLayout_234.addWidget(self.widget_details_data_perso_date)

        self.widget_408 = QWidget(self.widget_details_data_personel)
        self.widget_408.setObjectName(u"widget_408")
        sizePolicy5.setHeightForWidth(self.widget_408.sizePolicy().hasHeightForWidth())
        self.widget_408.setSizePolicy(sizePolicy5)
        self.widget_408.setMinimumSize(QSize(580, 0))
        self.widget_408.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-radius:5px;")
        self.horizontalLayout_273 = QHBoxLayout(self.widget_408)
        self.horizontalLayout_273.setSpacing(100)
        self.horizontalLayout_273.setObjectName(u"horizontalLayout_273")
        self.label_146 = QLabel(self.widget_408)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setFont(font6)
        self.label_146.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_146.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_273.addWidget(self.label_146)

        self.lineEdit_65 = QLineEdit(self.widget_408)
        self.lineEdit_65.setObjectName(u"lineEdit_65")
        sizePolicy4.setHeightForWidth(self.lineEdit_65.sizePolicy().hasHeightForWidth())
        self.lineEdit_65.setSizePolicy(sizePolicy4)
        self.lineEdit_65.setMinimumSize(QSize(400, 0))
        self.lineEdit_65.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"padding-left:10px;")

        self.horizontalLayout_273.addWidget(self.lineEdit_65)


        self.verticalLayout_234.addWidget(self.widget_408)


        self.horizontalLayout_276.addWidget(self.widget_details_data_personel)

        self.horizontalSpacer_273 = QSpacerItem(250, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_276.addItem(self.horizontalSpacer_273)


        self.verticalLayout_233.addWidget(self.widget_418)

        self.widget_419 = QWidget(self.widget_404)
        self.widget_419.setObjectName(u"widget_419")
        self.widget_419.setStyleSheet(u"background-color: rgb(236, 234, 234);\n"
"border-radius:5px;")
        self.horizontalLayout_275 = QHBoxLayout(self.widget_419)
        self.horizontalLayout_275.setObjectName(u"horizontalLayout_275")
        self.widget_warning_6 = QWidget(self.widget_419)
        self.widget_warning_6.setObjectName(u"widget_warning_6")
        self.widget_warning_6.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_338 = QHBoxLayout(self.widget_warning_6)
        self.horizontalLayout_338.setSpacing(0)
        self.horizontalLayout_338.setObjectName(u"horizontalLayout_338")
        self.horizontalLayout_338.setContentsMargins(10, 5, 5, 5)
        self.label_222 = QLabel(self.widget_warning_6)
        self.label_222.setObjectName(u"label_222")
        self.label_222.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_338.addWidget(self.label_222)

        self.label_303 = QLabel(self.widget_warning_6)
        self.label_303.setObjectName(u"label_303")
        self.label_303.setMinimumSize(QSize(150, 0))
        self.label_303.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_303.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_338.addWidget(self.label_303)


        self.horizontalLayout_275.addWidget(self.widget_warning_6)

        self.horizontalSpacer_272 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_275.addItem(self.horizontalSpacer_272)

        self.pushButton_149 = QPushButton(self.widget_419)
        self.pushButton_149.setObjectName(u"pushButton_149")
        self.pushButton_149.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_149.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(36, 38, 140);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:10px;\n"
"padding-right:40px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"}")
        self.pushButton_149.setIcon(icon16)
        self.pushButton_149.setCheckable(True)

        self.horizontalLayout_275.addWidget(self.pushButton_149)


        self.verticalLayout_233.addWidget(self.widget_419)


        self.verticalLayout_235.addWidget(self.widget_404)


        self.verticalLayout_224.addWidget(self.widget_402)

        self.widget_386 = QWidget(self.scrollAreaWidgetContents_6)
        self.widget_386.setObjectName(u"widget_386")
        self.widget_386.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_225 = QVBoxLayout(self.widget_386)
        self.verticalLayout_225.setObjectName(u"verticalLayout_225")
        self.verticalLayout_225.setContentsMargins(-1, 0, -1, 0)
        self.widget_409 = QWidget(self.widget_386)
        self.widget_409.setObjectName(u"widget_409")
        self.verticalLayout_236 = QVBoxLayout(self.widget_409)
        self.verticalLayout_236.setSpacing(0)
        self.verticalLayout_236.setObjectName(u"verticalLayout_236")
        self.verticalLayout_236.setContentsMargins(0, 0, 0, 0)
        self.widget_410 = QWidget(self.widget_409)
        self.widget_410.setObjectName(u"widget_410")
        self.widget_410.setStyleSheet(u"")
        self.horizontalLayout_267 = QHBoxLayout(self.widget_410)
        self.horizontalLayout_267.setObjectName(u"horizontalLayout_267")
        self.horizontalLayout_267.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_52 = QWidget(self.widget_410)
        self.Equipement_widget_52.setObjectName(u"Equipement_widget_52")
        sizePolicy6.setHeightForWidth(self.Equipement_widget_52.sizePolicy().hasHeightForWidth())
        self.Equipement_widget_52.setSizePolicy(sizePolicy6)
        self.Equipement_widget_52.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_268 = QHBoxLayout(self.Equipement_widget_52)
        self.horizontalLayout_268.setObjectName(u"horizontalLayout_268")
        self.label_145 = QLabel(self.Equipement_widget_52)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setPixmap(QPixmap(u":/assets/icons/equippement-30.png"))

        self.horizontalLayout_268.addWidget(self.label_145, 0, Qt.AlignLeft)

        self.pushButton_150 = QPushButton(self.Equipement_widget_52)
        self.pushButton_150.setObjectName(u"pushButton_150")
        sizePolicy2.setHeightForWidth(self.pushButton_150.sizePolicy().hasHeightForWidth())
        self.pushButton_150.setSizePolicy(sizePolicy2)
        self.pushButton_150.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_150.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_150.setIcon(icon9)
        self.pushButton_150.setIconSize(QSize(24, 24))
        self.pushButton_150.setCheckable(True)

        self.horizontalLayout_268.addWidget(self.pushButton_150)


        self.horizontalLayout_267.addWidget(self.Equipement_widget_52)

        self.horizontalSpacer_274 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_267.addItem(self.horizontalSpacer_274)


        self.verticalLayout_236.addWidget(self.widget_410)

        self.widget_411 = QWidget(self.widget_409)
        self.widget_411.setObjectName(u"widget_411")
        self.widget_411.setMinimumSize(QSize(450, 0))
        self.widget_411.setStyleSheet(u"")
        self.gridLayout_15 = QGridLayout(self.widget_411)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setVerticalSpacing(0)
        self.widget_post = QWidget(self.widget_411)
        self.widget_post.setObjectName(u"widget_post")
        sizePolicy3.setHeightForWidth(self.widget_post.sizePolicy().hasHeightForWidth())
        self.widget_post.setSizePolicy(sizePolicy3)
        self.widget_post.setStyleSheet(u"color: rgb(92, 124, 250);\n"
"background-color: rgb(245, 245, 245);")
        self.verticalLayout_250 = QVBoxLayout(self.widget_post)
        self.verticalLayout_250.setSpacing(0)
        self.verticalLayout_250.setObjectName(u"verticalLayout_250")
        self.widget_post_details = QWidget(self.widget_post)
        self.widget_post_details.setObjectName(u"widget_post_details")
        self.horizontalLayout_281 = QHBoxLayout(self.widget_post_details)
        self.horizontalLayout_281.setObjectName(u"horizontalLayout_281")
        self.horizontalSpacer_279 = QSpacerItem(183, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_281.addItem(self.horizontalSpacer_279)

        self.widget_412 = QWidget(self.widget_post_details)
        self.widget_412.setObjectName(u"widget_412")
        self.widget_412.setMinimumSize(QSize(600, 0))
        self.widget_412.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_242 = QVBoxLayout(self.widget_412)
        self.verticalLayout_242.setSpacing(10)
        self.verticalLayout_242.setObjectName(u"verticalLayout_242")
        self.verticalLayout_242.setContentsMargins(14, 14, 14, 14)
        self.widget_413 = QWidget(self.widget_412)
        self.widget_413.setObjectName(u"widget_413")
        self.widget_413.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-radius:5px;")
        self.horizontalLayout_269 = QHBoxLayout(self.widget_413)
        self.horizontalLayout_269.setSpacing(100)
        self.horizontalLayout_269.setObjectName(u"horizontalLayout_269")
        self.label_150 = QLabel(self.widget_413)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setFont(font6)
        self.label_150.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_150.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_269.addWidget(self.label_150)

        self.lineEdit_66 = QLineEdit(self.widget_413)
        self.lineEdit_66.setObjectName(u"lineEdit_66")
        self.lineEdit_66.setMinimumSize(QSize(200, 0))
        self.lineEdit_66.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"padding-left:10px;")

        self.horizontalLayout_269.addWidget(self.lineEdit_66)


        self.verticalLayout_242.addWidget(self.widget_413)

        self.widget_414 = QWidget(self.widget_412)
        self.widget_414.setObjectName(u"widget_414")
        self.widget_414.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-radius:5px;")
        self.horizontalLayout_270 = QHBoxLayout(self.widget_414)
        self.horizontalLayout_270.setObjectName(u"horizontalLayout_270")
        self.widget_420 = QWidget(self.widget_414)
        self.widget_420.setObjectName(u"widget_420")
        self.verticalLayout_238 = QVBoxLayout(self.widget_420)
        self.verticalLayout_238.setObjectName(u"verticalLayout_238")
        self.label_151 = QLabel(self.widget_420)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 12pt \"Segoe UI\";")

        self.verticalLayout_238.addWidget(self.label_151)

        self.verticalSpacer_77 = QSpacerItem(20, 35, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_238.addItem(self.verticalSpacer_77)


        self.horizontalLayout_270.addWidget(self.widget_420)

        self.horizontalSpacer_275 = QSpacerItem(180, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_270.addItem(self.horizontalSpacer_275)

        self.widget_415 = QWidget(self.widget_414)
        self.widget_415.setObjectName(u"widget_415")
        self.widget_415.setMinimumSize(QSize(200, 0))
        self.widget_415.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";\n"
"border-radius:5px;")
        self.verticalLayout_237 = QVBoxLayout(self.widget_415)
        self.verticalLayout_237.setObjectName(u"verticalLayout_237")
        self.checkBox_51 = QCheckBox(self.widget_415)
        self.checkBox_51.setObjectName(u"checkBox_51")
        self.checkBox_51.setChecked(True)
        self.checkBox_51.setAutoExclusive(True)

        self.verticalLayout_237.addWidget(self.checkBox_51)

        self.checkBox_49 = QCheckBox(self.widget_415)
        self.checkBox_49.setObjectName(u"checkBox_49")
        self.checkBox_49.setAutoExclusive(True)

        self.verticalLayout_237.addWidget(self.checkBox_49)

        self.checkBox_50 = QCheckBox(self.widget_415)
        self.checkBox_50.setObjectName(u"checkBox_50")
        self.checkBox_50.setAutoExclusive(True)

        self.verticalLayout_237.addWidget(self.checkBox_50)


        self.horizontalLayout_270.addWidget(self.widget_415)

        self.horizontalSpacer_276 = QSpacerItem(123, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_270.addItem(self.horizontalSpacer_276)


        self.verticalLayout_242.addWidget(self.widget_414)

        self.widget_421 = QWidget(self.widget_412)
        self.widget_421.setObjectName(u"widget_421")
        self.widget_421.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-radius:5px;")
        self.horizontalLayout_271 = QHBoxLayout(self.widget_421)
        self.horizontalLayout_271.setObjectName(u"horizontalLayout_271")
        self.widget_422 = QWidget(self.widget_421)
        self.widget_422.setObjectName(u"widget_422")
        self.verticalLayout_240 = QVBoxLayout(self.widget_422)
        self.verticalLayout_240.setObjectName(u"verticalLayout_240")
        self.label_152 = QLabel(self.widget_422)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 12pt \"Segoe UI\";")

        self.verticalLayout_240.addWidget(self.label_152)

        self.verticalSpacer_78 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_240.addItem(self.verticalSpacer_78)


        self.horizontalLayout_271.addWidget(self.widget_422)

        self.horizontalSpacer_277 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_271.addItem(self.horizontalSpacer_277)

        self.widget_423 = QWidget(self.widget_421)
        self.widget_423.setObjectName(u"widget_423")
        self.widget_423.setMinimumSize(QSize(200, 0))
        self.widget_423.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";\n"
"border-radius:5px;")
        self.verticalLayout_241 = QVBoxLayout(self.widget_423)
        self.verticalLayout_241.setObjectName(u"verticalLayout_241")
        self.checkBox_52 = QCheckBox(self.widget_423)
        self.checkBox_52.setObjectName(u"checkBox_52")
        self.checkBox_52.setChecked(True)
        self.checkBox_52.setAutoExclusive(True)

        self.verticalLayout_241.addWidget(self.checkBox_52)

        self.checkBox_53 = QCheckBox(self.widget_423)
        self.checkBox_53.setObjectName(u"checkBox_53")
        self.checkBox_53.setAutoExclusive(True)

        self.verticalLayout_241.addWidget(self.checkBox_53)


        self.horizontalLayout_271.addWidget(self.widget_423)

        self.horizontalSpacer_278 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_271.addItem(self.horizontalSpacer_278)


        self.verticalLayout_242.addWidget(self.widget_421)

        self.widget_424 = QWidget(self.widget_412)
        self.widget_424.setObjectName(u"widget_424")
        self.widget_424.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-radius:5px;")
        self.horizontalLayout_277 = QHBoxLayout(self.widget_424)
        self.horizontalLayout_277.setObjectName(u"horizontalLayout_277")
        self.label_153 = QLabel(self.widget_424)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 10pt \"Segoe UI\";")

        self.horizontalLayout_277.addWidget(self.label_153)

        self.comboBox_personne = QComboBox(self.widget_424)
        self.comboBox_personne.addItem("")
        self.comboBox_personne.addItem("")
        self.comboBox_personne.addItem("")
        self.comboBox_personne.addItem("")
        self.comboBox_personne.addItem("")
        self.comboBox_personne.setObjectName(u"comboBox_personne")
        self.comboBox_personne.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";\n"
"border-radius:5px;\n"
"padding-left:10px;")

        self.horizontalLayout_277.addWidget(self.comboBox_personne)


        self.verticalLayout_242.addWidget(self.widget_424)


        self.horizontalLayout_281.addWidget(self.widget_412)

        self.horizontalSpacer_280 = QSpacerItem(183, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_281.addItem(self.horizontalSpacer_280)


        self.verticalLayout_250.addWidget(self.widget_post_details)

        self.widget_426 = QWidget(self.widget_post)
        self.widget_426.setObjectName(u"widget_426")
        self.widget_426.setStyleSheet(u"background-color: rgb(236, 234, 234);\n"
"border-radius:5px;")
        self.horizontalLayout_278 = QHBoxLayout(self.widget_426)
        self.horizontalLayout_278.setObjectName(u"horizontalLayout_278")
        self.widget_warning_7 = QWidget(self.widget_426)
        self.widget_warning_7.setObjectName(u"widget_warning_7")
        self.widget_warning_7.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_339 = QHBoxLayout(self.widget_warning_7)
        self.horizontalLayout_339.setSpacing(0)
        self.horizontalLayout_339.setObjectName(u"horizontalLayout_339")
        self.horizontalLayout_339.setContentsMargins(10, 5, 5, 5)
        self.label_223 = QLabel(self.widget_warning_7)
        self.label_223.setObjectName(u"label_223")
        self.label_223.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_339.addWidget(self.label_223)

        self.label_304 = QLabel(self.widget_warning_7)
        self.label_304.setObjectName(u"label_304")
        self.label_304.setMinimumSize(QSize(150, 0))
        self.label_304.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_304.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_339.addWidget(self.label_304)


        self.horizontalLayout_278.addWidget(self.widget_warning_7)

        self.horizontalSpacer_282 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_278.addItem(self.horizontalSpacer_282)

        self.pushButton_151 = QPushButton(self.widget_426)
        self.pushButton_151.setObjectName(u"pushButton_151")
        self.pushButton_151.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_151.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(36, 38, 140);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:10px;\n"
"padding-right:40px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"}")
        self.pushButton_151.setIcon(icon16)
        self.pushButton_151.setCheckable(True)

        self.horizontalLayout_278.addWidget(self.pushButton_151)


        self.verticalLayout_250.addWidget(self.widget_426)


        self.gridLayout_15.addWidget(self.widget_post, 0, 0, 1, 1)


        self.verticalLayout_236.addWidget(self.widget_411)

        self.widget_416 = QWidget(self.widget_409)
        self.widget_416.setObjectName(u"widget_416")
        self.widget_416.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_239 = QVBoxLayout(self.widget_416)
        self.verticalLayout_239.setSpacing(0)
        self.verticalLayout_239.setObjectName(u"verticalLayout_239")
        self.verticalLayout_239.setContentsMargins(0, 0, 0, 0)
        self.widget_417 = QWidget(self.widget_416)
        self.widget_417.setObjectName(u"widget_417")
        self.horizontalLayout_272 = QHBoxLayout(self.widget_417)
        self.horizontalLayout_272.setSpacing(0)
        self.horizontalLayout_272.setObjectName(u"horizontalLayout_272")
        self.horizontalLayout_272.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_239.addWidget(self.widget_417)


        self.verticalLayout_236.addWidget(self.widget_416)


        self.verticalLayout_225.addWidget(self.widget_409)

        self.widget_387 = QWidget(self.widget_386)
        self.widget_387.setObjectName(u"widget_387")
        self.horizontalLayout_252 = QHBoxLayout(self.widget_387)
        self.horizontalLayout_252.setObjectName(u"horizontalLayout_252")
        self.horizontalLayout_252.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_49 = QWidget(self.widget_387)
        self.Equipement_widget_49.setObjectName(u"Equipement_widget_49")
        sizePolicy6.setHeightForWidth(self.Equipement_widget_49.sizePolicy().hasHeightForWidth())
        self.Equipement_widget_49.setSizePolicy(sizePolicy6)
        self.Equipement_widget_49.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_253 = QHBoxLayout(self.Equipement_widget_49)
        self.horizontalLayout_253.setObjectName(u"horizontalLayout_253")
        self.label_140 = QLabel(self.Equipement_widget_49)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setPixmap(QPixmap(u":/assets/icons/employee-30.png"))

        self.horizontalLayout_253.addWidget(self.label_140, 0, Qt.AlignLeft)

        self.pushButton_143 = QPushButton(self.Equipement_widget_49)
        self.pushButton_143.setObjectName(u"pushButton_143")
        sizePolicy2.setHeightForWidth(self.pushButton_143.sizePolicy().hasHeightForWidth())
        self.pushButton_143.setSizePolicy(sizePolicy2)
        self.pushButton_143.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_143.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(92, 124, 250);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(236, 234, 234);\n"
"color: rgb(92, 124, 250);\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(236, 234, 234);\n"
"color: rgb(92, 124, 250);\n"
"}\n"
"")
        self.pushButton_143.setIcon(icon9)
        self.pushButton_143.setIconSize(QSize(24, 24))
        self.pushButton_143.setCheckable(True)

        self.horizontalLayout_253.addWidget(self.pushButton_143)


        self.horizontalLayout_252.addWidget(self.Equipement_widget_49)

        self.horizontalSpacer_259 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_252.addItem(self.horizontalSpacer_259)


        self.verticalLayout_225.addWidget(self.widget_387)

        self.widget_388 = QWidget(self.widget_386)
        self.widget_388.setObjectName(u"widget_388")
        self.widget_388.setMinimumSize(QSize(0, 0))
        self.widget_388.setMaximumSize(QSize(16777215, 16777215))
        self.widget_388.setStyleSheet(u"color: rgb(92, 124, 250);\n"
"background-color: rgb(245, 245, 245);")
        self.horizontalLayout_280 = QHBoxLayout(self.widget_388)
        self.horizontalLayout_280.setObjectName(u"horizontalLayout_280")
        self.horizontalSpacer_260 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_280.addItem(self.horizontalSpacer_260)

        self.widget_detils_perso_date = QWidget(self.widget_388)
        self.widget_detils_perso_date.setObjectName(u"widget_detils_perso_date")
        self.verticalLayout_229 = QVBoxLayout(self.widget_detils_perso_date)
        self.verticalLayout_229.setSpacing(10)
        self.verticalLayout_229.setObjectName(u"verticalLayout_229")
        self.widget2 = QWidget(self.widget_detils_perso_date)
        self.widget2.setObjectName(u"widget2")
        self.horizontalLayout_279 = QHBoxLayout(self.widget2)
        self.horizontalLayout_279.setSpacing(0)
        self.horizontalLayout_279.setObjectName(u"horizontalLayout_279")
        self.horizontalLayout_279.setContentsMargins(0, 0, 0, 0)
        self.widget_389 = QWidget(self.widget2)
        self.widget_389.setObjectName(u"widget_389")
        sizePolicy5.setHeightForWidth(self.widget_389.sizePolicy().hasHeightForWidth())
        self.widget_389.setSizePolicy(sizePolicy5)
        self.widget_389.setMinimumSize(QSize(350, 0))
        self.widget_389.setStyleSheet(u"background-color: rgb(236, 234, 234);\n"
"border-bottom-left-radius:7px;\n"
"border-bottom-right-radius:7px;")
        self.verticalLayout_226 = QVBoxLayout(self.widget_389)
        self.verticalLayout_226.setObjectName(u"verticalLayout_226")
        self.textEdit_58 = QTextEdit(self.widget_389)
        self.textEdit_58.setObjectName(u"textEdit_58")
        sizePolicy4.setHeightForWidth(self.textEdit_58.sizePolicy().hasHeightForWidth())
        self.textEdit_58.setSizePolicy(sizePolicy4)
        self.textEdit_58.setMinimumSize(QSize(0, 0))
        self.textEdit_58.setMaximumSize(QSize(16777215, 40))
        self.textEdit_58.setStyleSheet(u"color: rgb(52, 56, 199);\n"
"font: 8pt \"Microsoft JhengHei UI\";")

        self.verticalLayout_226.addWidget(self.textEdit_58)

        self.textEdit_59 = QTextEdit(self.widget_389)
        self.textEdit_59.setObjectName(u"textEdit_59")
        sizePolicy4.setHeightForWidth(self.textEdit_59.sizePolicy().hasHeightForWidth())
        self.textEdit_59.setSizePolicy(sizePolicy4)
        self.textEdit_59.setMinimumSize(QSize(0, 0))
        self.textEdit_59.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_226.addWidget(self.textEdit_59)

        self.widget_390 = QWidget(self.widget_389)
        self.widget_390.setObjectName(u"widget_390")
        self.widget_390.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(211, 211, 211);\n"
"border-radius:0px;")
        self.verticalLayout_227 = QVBoxLayout(self.widget_390)
        self.verticalLayout_227.setObjectName(u"verticalLayout_227")
        self.checkBox_DateAujourdui = QCheckBox(self.widget_390)
        self.checkBox_DateAujourdui.setObjectName(u"checkBox_DateAujourdui")
        self.checkBox_DateAujourdui.setChecked(True)
        self.checkBox_DateAujourdui.setAutoExclusive(True)

        self.verticalLayout_227.addWidget(self.checkBox_DateAujourdui)

        self.checkBox_22 = QCheckBox(self.widget_390)
        self.checkBox_22.setObjectName(u"checkBox_22")
        self.checkBox_22.setAutoExclusive(True)

        self.verticalLayout_227.addWidget(self.checkBox_22)


        self.verticalLayout_226.addWidget(self.widget_390)

        self.widget_391 = QWidget(self.widget_389)
        self.widget_391.setObjectName(u"widget_391")
        self.widget_391.setStyleSheet(u"color: rgb(58, 58, 58);\n"
"font: 12pt \"Segoe UI\";\n"
"background-color: rgb(245, 245, 245);\n"
"border-top-left-radius:7px;\n"
"border-bottom-left-radius:7px;")
        self.horizontalLayout_255 = QHBoxLayout(self.widget_391)
        self.horizontalLayout_255.setObjectName(u"horizontalLayout_255")
        self.dateEdit_8 = QDateEdit(self.widget_391)
        self.dateEdit_8.setObjectName(u"dateEdit_8")
        self.dateEdit_8.setCalendarPopup(True)

        self.horizontalLayout_255.addWidget(self.dateEdit_8)


        self.verticalLayout_226.addWidget(self.widget_391)


        self.horizontalLayout_279.addWidget(self.widget_389)

        self.horizontalSpacer_262 = QSpacerItem(37, 207, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_279.addItem(self.horizontalSpacer_262)

        self.widget_392 = QWidget(self.widget2)
        self.widget_392.setObjectName(u"widget_392")
        sizePolicy5.setHeightForWidth(self.widget_392.sizePolicy().hasHeightForWidth())
        self.widget_392.setSizePolicy(sizePolicy5)
        self.widget_392.setMinimumSize(QSize(350, 0))
        self.widget_392.setMaximumSize(QSize(400, 16777215))
        self.widget_392.setStyleSheet(u"background-color: rgb(236, 234, 234);\n"
"border-bottom-left-radius:7px;\n"
"border-bottom-right-radius:7px;")
        self.verticalLayout_228 = QVBoxLayout(self.widget_392)
        self.verticalLayout_228.setObjectName(u"verticalLayout_228")
        self.verticalSpacer_79 = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_228.addItem(self.verticalSpacer_79)

        self.widget_425 = QWidget(self.widget_392)
        self.widget_425.setObjectName(u"widget_425")
        self.widget_425.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(211, 211, 211);\n"
"border-radius:0px;")
        self.horizontalLayout_254 = QHBoxLayout(self.widget_425)
        self.horizontalLayout_254.setObjectName(u"horizontalLayout_254")
        self.checkBox_23 = QCheckBox(self.widget_425)
        self.checkBox_23.setObjectName(u"checkBox_23")

        self.horizontalLayout_254.addWidget(self.checkBox_23)

        self.textEdit_60 = QTextEdit(self.widget_425)
        self.textEdit_60.setObjectName(u"textEdit_60")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.textEdit_60.sizePolicy().hasHeightForWidth())
        self.textEdit_60.setSizePolicy(sizePolicy7)
        self.textEdit_60.setMinimumSize(QSize(0, 0))
        self.textEdit_60.setMaximumSize(QSize(16777215, 20))
        self.textEdit_60.setFont(font8)
        self.textEdit_60.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.horizontalLayout_254.addWidget(self.textEdit_60)


        self.verticalLayout_228.addWidget(self.widget_425)

        self.verticalSpacer_80 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_228.addItem(self.verticalSpacer_80)

        self.textEdit_64 = QTextEdit(self.widget_392)
        self.textEdit_64.setObjectName(u"textEdit_64")
        sizePolicy4.setHeightForWidth(self.textEdit_64.sizePolicy().hasHeightForWidth())
        self.textEdit_64.setSizePolicy(sizePolicy4)
        self.textEdit_64.setMinimumSize(QSize(0, 0))
        self.textEdit_64.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_228.addWidget(self.textEdit_64)

        self.widget_393 = QWidget(self.widget_392)
        self.widget_393.setObjectName(u"widget_393")
        self.widget_393.setStyleSheet(u"color: rgb(58, 58, 58);\n"
"font: 12pt \"Segoe UI\";\n"
"background-color: rgb(245, 245, 245);\n"
"border-top-left-radius:7px;\n"
"border-bottom-left-radius:7px;")
        self.horizontalLayout_256 = QHBoxLayout(self.widget_393)
        self.horizontalLayout_256.setObjectName(u"horizontalLayout_256")
        self.dateEdit_15 = QDateEdit(self.widget_393)
        self.dateEdit_15.setObjectName(u"dateEdit_15")
        self.dateEdit_15.setCalendarPopup(True)

        self.horizontalLayout_256.addWidget(self.dateEdit_15)


        self.verticalLayout_228.addWidget(self.widget_393)

        self.verticalSpacer_81 = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_228.addItem(self.verticalSpacer_81)


        self.horizontalLayout_279.addWidget(self.widget_392)


        self.verticalLayout_229.addWidget(self.widget2)

        self.widget_395 = QWidget(self.widget_detils_perso_date)
        self.widget_395.setObjectName(u"widget_395")
        self.widget_395.setStyleSheet(u"background-color: rgb(236, 234, 234);\n"
"border-radius:5px;")
        self.horizontalLayout_257 = QHBoxLayout(self.widget_395)
        self.horizontalLayout_257.setObjectName(u"horizontalLayout_257")
        self.widget_warning_8 = QWidget(self.widget_395)
        self.widget_warning_8.setObjectName(u"widget_warning_8")
        self.widget_warning_8.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_348 = QHBoxLayout(self.widget_warning_8)
        self.horizontalLayout_348.setSpacing(0)
        self.horizontalLayout_348.setObjectName(u"horizontalLayout_348")
        self.horizontalLayout_348.setContentsMargins(10, 5, 5, 5)
        self.label_224 = QLabel(self.widget_warning_8)
        self.label_224.setObjectName(u"label_224")
        self.label_224.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_348.addWidget(self.label_224)

        self.label_305 = QLabel(self.widget_warning_8)
        self.label_305.setObjectName(u"label_305")
        self.label_305.setMinimumSize(QSize(150, 0))
        self.label_305.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_305.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_348.addWidget(self.label_305)


        self.horizontalLayout_257.addWidget(self.widget_warning_8)

        self.horizontalSpacer_264 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_257.addItem(self.horizontalSpacer_264)

        self.pushButton_144 = QPushButton(self.widget_395)
        self.pushButton_144.setObjectName(u"pushButton_144")
        self.pushButton_144.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_144.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(36, 38, 140);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:10px;\n"
"padding-right:40px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"}")
        self.pushButton_144.setCheckable(True)

        self.horizontalLayout_257.addWidget(self.pushButton_144)


        self.verticalLayout_229.addWidget(self.widget_395)


        self.horizontalLayout_280.addWidget(self.widget_detils_perso_date)

        self.horizontalSpacer_265 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_280.addItem(self.horizontalSpacer_265)


        self.verticalLayout_225.addWidget(self.widget_388)


        self.verticalLayout_224.addWidget(self.widget_386)

        self.widget_396 = QWidget(self.scrollAreaWidgetContents_6)
        self.widget_396.setObjectName(u"widget_396")
        self.verticalLayout_230 = QVBoxLayout(self.widget_396)
        self.verticalLayout_230.setObjectName(u"verticalLayout_230")
        self.widget_397 = QWidget(self.widget_396)
        self.widget_397.setObjectName(u"widget_397")
        self.horizontalLayout_258 = QHBoxLayout(self.widget_397)
        self.horizontalLayout_258.setObjectName(u"horizontalLayout_258")
        self.horizontalLayout_258.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_50 = QWidget(self.widget_397)
        self.Equipement_widget_50.setObjectName(u"Equipement_widget_50")
        sizePolicy6.setHeightForWidth(self.Equipement_widget_50.sizePolicy().hasHeightForWidth())
        self.Equipement_widget_50.setSizePolicy(sizePolicy6)
        self.Equipement_widget_50.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_259 = QHBoxLayout(self.Equipement_widget_50)
        self.horizontalLayout_259.setObjectName(u"horizontalLayout_259")
        self.label_143 = QLabel(self.Equipement_widget_50)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setPixmap(QPixmap(u":/assets/icons/employee-30.png"))

        self.horizontalLayout_259.addWidget(self.label_143, 0, Qt.AlignLeft)

        self.pushButton_145 = QPushButton(self.Equipement_widget_50)
        self.pushButton_145.setObjectName(u"pushButton_145")
        sizePolicy2.setHeightForWidth(self.pushButton_145.sizePolicy().hasHeightForWidth())
        self.pushButton_145.setSizePolicy(sizePolicy2)
        self.pushButton_145.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_145.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_145.setIcon(icon9)
        self.pushButton_145.setIconSize(QSize(24, 24))
        self.pushButton_145.setCheckable(True)

        self.horizontalLayout_259.addWidget(self.pushButton_145)


        self.horizontalLayout_258.addWidget(self.Equipement_widget_50)

        self.horizontalSpacer_266 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_258.addItem(self.horizontalSpacer_266)


        self.verticalLayout_230.addWidget(self.widget_397)

        self.widget_398 = QWidget(self.widget_396)
        self.widget_398.setObjectName(u"widget_398")
        self.widget_398.setMinimumSize(QSize(450, 0))
        self.widget_398.setStyleSheet(u"color: rgb(92, 124, 250);\n"
"background-color: rgb(245, 245, 245);")
        self.horizontalLayout_260 = QHBoxLayout(self.widget_398)
        self.horizontalLayout_260.setObjectName(u"horizontalLayout_260")
        self.horizontalSpacer_281 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_260.addItem(self.horizontalSpacer_281)

        self.widget_399 = QWidget(self.widget_398)
        self.widget_399.setObjectName(u"widget_399")
        self.widget_399.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"border-bottom-left-radius:7px;\n"
"border-bottom-right-radius:7px;")
        self.verticalLayout_231 = QVBoxLayout(self.widget_399)
        self.verticalLayout_231.setObjectName(u"verticalLayout_231")
        self.label_154 = QLabel(self.widget_399)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 12pt \"Segoe UI\";")

        self.verticalLayout_231.addWidget(self.label_154)

        self.verticalSpacer_76 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_231.addItem(self.verticalSpacer_76)


        self.horizontalLayout_260.addWidget(self.widget_399)

        self.widget_400 = QWidget(self.widget_398)
        self.widget_400.setObjectName(u"widget_400")
        self.widget_400.setMinimumSize(QSize(400, 0))
        self.widget_400.setStyleSheet(u"background-color: rgb(236, 234, 234);\n"
"border-bottom-left-radius:7px;\n"
"border-bottom-right-radius:7px;")
        self.verticalLayout_232 = QVBoxLayout(self.widget_400)
        self.verticalLayout_232.setObjectName(u"verticalLayout_232")
        self.verticalLayout_232.setContentsMargins(14, 14, 14, 0)
        self.label_159 = QLabel(self.widget_400)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 7pt \"Segoe UI\";")

        self.verticalLayout_232.addWidget(self.label_159)

        self.horizontalSpacer_318 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_232.addItem(self.horizontalSpacer_318)

        self.plainTextEdit_63 = QPlainTextEdit(self.widget_400)
        self.plainTextEdit_63.setObjectName(u"plainTextEdit_63")
        self.plainTextEdit_63.setStyleSheet(u"color: rgb(58, 58, 58);\n"
"font: 12pt \"Segoe UI\";\n"
"background-color: rgb(245, 245, 245);\n"
"border-radius:4px;\n"
"")

        self.verticalLayout_232.addWidget(self.plainTextEdit_63)

        self.widget_401 = QWidget(self.widget_400)
        self.widget_401.setObjectName(u"widget_401")
        self.horizontalLayout_261 = QHBoxLayout(self.widget_401)
        self.horizontalLayout_261.setObjectName(u"horizontalLayout_261")
        self.horizontalSpacer_267 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_261.addItem(self.horizontalSpacer_267)


        self.verticalLayout_232.addWidget(self.widget_401)


        self.horizontalLayout_260.addWidget(self.widget_400)

        self.horizontalSpacer_268 = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_260.addItem(self.horizontalSpacer_268)


        self.verticalLayout_230.addWidget(self.widget_398)


        self.verticalLayout_224.addWidget(self.widget_396)

        self.widget_458 = QWidget(self.scrollAreaWidgetContents_6)
        self.widget_458.setObjectName(u"widget_458")
        self.widget_458.setStyleSheet(u"")
        self.horizontalLayout_294 = QHBoxLayout(self.widget_458)
        self.horizontalLayout_294.setObjectName(u"horizontalLayout_294")
        self.Equipement_widget_56 = QWidget(self.widget_458)
        self.Equipement_widget_56.setObjectName(u"Equipement_widget_56")
        sizePolicy6.setHeightForWidth(self.Equipement_widget_56.sizePolicy().hasHeightForWidth())
        self.Equipement_widget_56.setSizePolicy(sizePolicy6)
        self.Equipement_widget_56.setStyleSheet(u"QWidget{\n"
"background-color: rgb(236, 234, 234);\n"
"border-radius:10px;\n"
"color: white;\n"
"}")
        self.verticalLayout_271 = QVBoxLayout(self.Equipement_widget_56)
        self.verticalLayout_271.setSpacing(20)
        self.verticalLayout_271.setObjectName(u"verticalLayout_271")
        self.verticalLayout_271.setContentsMargins(2, 2, 20, 2)
        self.label_149 = QLabel(self.Equipement_widget_56)
        self.label_149.setObjectName(u"label_149")

        self.verticalLayout_271.addWidget(self.label_149)

        self.pushButton_160 = QPushButton(self.Equipement_widget_56)
        self.pushButton_160.setObjectName(u"pushButton_160")
        sizePolicy2.setHeightForWidth(self.pushButton_160.sizePolicy().hasHeightForWidth())
        self.pushButton_160.setSizePolicy(sizePolicy2)
        self.pushButton_160.setFont(font5)
        self.pushButton_160.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_160.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(200, 131, 131);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:4px;\n"
"padding-right:4px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(226, 148, 148);\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(226, 148, 148);\n"
"}")
        self.pushButton_160.setIcon(icon9)
        self.pushButton_160.setIconSize(QSize(24, 24))
        self.pushButton_160.setCheckable(True)

        self.verticalLayout_271.addWidget(self.pushButton_160)


        self.horizontalLayout_294.addWidget(self.Equipement_widget_56)

        self.horizontalSpacer_307 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_294.addItem(self.horizontalSpacer_307)

        self.Equipement_widget_57 = QWidget(self.widget_458)
        self.Equipement_widget_57.setObjectName(u"Equipement_widget_57")
        sizePolicy6.setHeightForWidth(self.Equipement_widget_57.sizePolicy().hasHeightForWidth())
        self.Equipement_widget_57.setSizePolicy(sizePolicy6)
        self.Equipement_widget_57.setStyleSheet(u"QWidget{\n"
"background-color: rgb(236, 234, 234);\n"
"border-radius:10px;\n"
"color: white;\n"
"}")
        self.verticalLayout_254 = QVBoxLayout(self.Equipement_widget_57)
        self.verticalLayout_254.setSpacing(20)
        self.verticalLayout_254.setObjectName(u"verticalLayout_254")
        self.verticalLayout_254.setContentsMargins(20, 4, 2, 2)
        self.label_142 = QLabel(self.Equipement_widget_57)
        self.label_142.setObjectName(u"label_142")

        self.verticalLayout_254.addWidget(self.label_142)

        self.pushButton_161 = QPushButton(self.Equipement_widget_57)
        self.pushButton_161.setObjectName(u"pushButton_161")
        sizePolicy2.setHeightForWidth(self.pushButton_161.sizePolicy().hasHeightForWidth())
        self.pushButton_161.setSizePolicy(sizePolicy2)
        self.pushButton_161.setFont(font5)
        self.pushButton_161.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_161.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(165, 214, 167);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:10px;\n"
"padding-right:20px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(177, 229, 179);\n"
"}\n"
"QPushButton:checked{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(177, 229, 179);\n"
"}")
        self.pushButton_161.setIcon(icon9)
        self.pushButton_161.setIconSize(QSize(24, 24))
        self.pushButton_161.setCheckable(True)

        self.verticalLayout_254.addWidget(self.pushButton_161)


        self.horizontalLayout_294.addWidget(self.Equipement_widget_57)


        self.verticalLayout_224.addWidget(self.widget_458)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.gridLayout_6.addWidget(self.scrollArea_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.data_newPersonne_page)
        self.data_newFournisseur_page = QWidget()
        self.data_newFournisseur_page.setObjectName(u"data_newFournisseur_page")
        self.gridLayout_7 = QGridLayout(self.data_newFournisseur_page)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.scrollArea_7 = QScrollArea(self.data_newFournisseur_page)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 486, 827))
        self.gridLayout_20 = QGridLayout(self.scrollAreaWidgetContents_7)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.widget_459 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_459.setObjectName(u"widget_459")
        self.gridLayout_19 = QGridLayout(self.widget_459)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.widget_460 = QWidget(self.widget_459)
        self.widget_460.setObjectName(u"widget_460")
        self.horizontalLayout_297 = QHBoxLayout(self.widget_460)
        self.horizontalLayout_297.setObjectName(u"horizontalLayout_297")
        self.horizontalLayout_297.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_55 = QWidget(self.widget_460)
        self.Equipement_widget_55.setObjectName(u"Equipement_widget_55")
        sizePolicy6.setHeightForWidth(self.Equipement_widget_55.sizePolicy().hasHeightForWidth())
        self.Equipement_widget_55.setSizePolicy(sizePolicy6)
        self.Equipement_widget_55.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_298 = QHBoxLayout(self.Equipement_widget_55)
        self.horizontalLayout_298.setObjectName(u"horizontalLayout_298")
        self.label_161 = QLabel(self.Equipement_widget_55)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setPixmap(QPixmap(u":/assets/icons/employee-30.png"))

        self.horizontalLayout_298.addWidget(self.label_161, 0, Qt.AlignLeft)

        self.pushButton_155 = QPushButton(self.Equipement_widget_55)
        self.pushButton_155.setObjectName(u"pushButton_155")
        sizePolicy2.setHeightForWidth(self.pushButton_155.sizePolicy().hasHeightForWidth())
        self.pushButton_155.setSizePolicy(sizePolicy2)
        self.pushButton_155.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_155.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(245, 245, 245);\n"
"}\n"
"")
        self.pushButton_155.setIconSize(QSize(24, 24))
        self.pushButton_155.setCheckable(False)

        self.horizontalLayout_298.addWidget(self.pushButton_155)


        self.horizontalLayout_297.addWidget(self.Equipement_widget_55)

        self.horizontalSpacer_299 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_297.addItem(self.horizontalSpacer_299)


        self.gridLayout_19.addWidget(self.widget_460, 0, 0, 1, 1)

        self.widget_461 = QWidget(self.widget_459)
        self.widget_461.setObjectName(u"widget_461")
        self.widget_461.setMinimumSize(QSize(450, 0))
        self.widget_461.setStyleSheet(u"color: rgb(92, 124, 250);\n"
"background-color: rgb(245, 245, 245);")
        self.verticalLayout_263 = QVBoxLayout(self.widget_461)
        self.verticalLayout_263.setObjectName(u"verticalLayout_263")
        self.widget_462 = QWidget(self.widget_461)
        self.widget_462.setObjectName(u"widget_462")
        self.horizontalLayout_363 = QHBoxLayout(self.widget_462)
        self.horizontalLayout_363.setObjectName(u"horizontalLayout_363")
        self.horizontalSpacer_300 = QSpacerItem(251, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_363.addItem(self.horizontalSpacer_300)

        self.widget_463 = QWidget(self.widget_462)
        self.widget_463.setObjectName(u"widget_463")
        sizePolicy5.setHeightForWidth(self.widget_463.sizePolicy().hasHeightForWidth())
        self.widget_463.setSizePolicy(sizePolicy5)
        self.widget_463.setMinimumSize(QSize(600, 0))
        self.widget_463.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_264 = QVBoxLayout(self.widget_463)
        self.verticalLayout_264.setObjectName(u"verticalLayout_264")
        self.widget_464 = QWidget(self.widget_463)
        self.widget_464.setObjectName(u"widget_464")
        self.widget_464.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-radius:5px;")
        self.horizontalLayout_364 = QHBoxLayout(self.widget_464)
        self.horizontalLayout_364.setSpacing(90)
        self.horizontalLayout_364.setObjectName(u"horizontalLayout_364")
        self.label_202 = QLabel(self.widget_464)
        self.label_202.setObjectName(u"label_202")
        sizePolicy3.setHeightForWidth(self.label_202.sizePolicy().hasHeightForWidth())
        self.label_202.setSizePolicy(sizePolicy3)
        self.label_202.setFont(font6)
        self.label_202.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_202.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_364.addWidget(self.label_202)

        self.lineEdit_74 = QLineEdit(self.widget_464)
        self.lineEdit_74.setObjectName(u"lineEdit_74")
        sizePolicy4.setHeightForWidth(self.lineEdit_74.sizePolicy().hasHeightForWidth())
        self.lineEdit_74.setSizePolicy(sizePolicy4)
        self.lineEdit_74.setMinimumSize(QSize(300, 0))
        self.lineEdit_74.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"padding-left:10px;")

        self.horizontalLayout_364.addWidget(self.lineEdit_74)


        self.verticalLayout_264.addWidget(self.widget_464)

        self.widget_465 = QWidget(self.widget_463)
        self.widget_465.setObjectName(u"widget_465")
        self.widget_465.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-radius:5px;")
        self.horizontalLayout_365 = QHBoxLayout(self.widget_465)
        self.horizontalLayout_365.setSpacing(73)
        self.horizontalLayout_365.setObjectName(u"horizontalLayout_365")
        self.label_203 = QLabel(self.widget_465)
        self.label_203.setObjectName(u"label_203")
        sizePolicy3.setHeightForWidth(self.label_203.sizePolicy().hasHeightForWidth())
        self.label_203.setSizePolicy(sizePolicy3)
        self.label_203.setFont(font6)
        self.label_203.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_203.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_365.addWidget(self.label_203)

        self.lineEdit_87 = QLineEdit(self.widget_465)
        self.lineEdit_87.setObjectName(u"lineEdit_87")
        sizePolicy4.setHeightForWidth(self.lineEdit_87.sizePolicy().hasHeightForWidth())
        self.lineEdit_87.setSizePolicy(sizePolicy4)
        self.lineEdit_87.setMinimumSize(QSize(300, 0))
        self.lineEdit_87.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"padding-left:10px;")

        self.horizontalLayout_365.addWidget(self.lineEdit_87)


        self.verticalLayout_264.addWidget(self.widget_465)

        self.widget_466 = QWidget(self.widget_463)
        self.widget_466.setObjectName(u"widget_466")
        sizePolicy.setHeightForWidth(self.widget_466.sizePolicy().hasHeightForWidth())
        self.widget_466.setSizePolicy(sizePolicy)
        self.widget_466.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-radius:5px;")
        self.horizontalLayout_366 = QHBoxLayout(self.widget_466)
        self.horizontalLayout_366.setSpacing(73)
        self.horizontalLayout_366.setObjectName(u"horizontalLayout_366")
        self.label_204 = QLabel(self.widget_466)
        self.label_204.setObjectName(u"label_204")
        sizePolicy3.setHeightForWidth(self.label_204.sizePolicy().hasHeightForWidth())
        self.label_204.setSizePolicy(sizePolicy3)
        self.label_204.setFont(font6)
        self.label_204.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_204.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_366.addWidget(self.label_204)

        self.lineEdit_88 = QLineEdit(self.widget_466)
        self.lineEdit_88.setObjectName(u"lineEdit_88")
        sizePolicy4.setHeightForWidth(self.lineEdit_88.sizePolicy().hasHeightForWidth())
        self.lineEdit_88.setSizePolicy(sizePolicy4)
        self.lineEdit_88.setMinimumSize(QSize(300, 0))
        self.lineEdit_88.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"padding-left:10px;")

        self.horizontalLayout_366.addWidget(self.lineEdit_88)


        self.verticalLayout_264.addWidget(self.widget_466)

        self.widget_468 = QWidget(self.widget_463)
        self.widget_468.setObjectName(u"widget_468")
        self.widget_468.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-radius:5px;")
        self.horizontalLayout_368 = QHBoxLayout(self.widget_468)
        self.horizontalLayout_368.setSpacing(73)
        self.horizontalLayout_368.setObjectName(u"horizontalLayout_368")
        self.label_206 = QLabel(self.widget_468)
        self.label_206.setObjectName(u"label_206")
        sizePolicy3.setHeightForWidth(self.label_206.sizePolicy().hasHeightForWidth())
        self.label_206.setSizePolicy(sizePolicy3)
        self.label_206.setFont(font6)
        self.label_206.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_206.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_368.addWidget(self.label_206)

        self.lineEdit_89 = QLineEdit(self.widget_468)
        self.lineEdit_89.setObjectName(u"lineEdit_89")
        sizePolicy4.setHeightForWidth(self.lineEdit_89.sizePolicy().hasHeightForWidth())
        self.lineEdit_89.setSizePolicy(sizePolicy4)
        self.lineEdit_89.setMinimumSize(QSize(300, 0))
        self.lineEdit_89.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"padding-left:10px;")

        self.horizontalLayout_368.addWidget(self.lineEdit_89)


        self.verticalLayout_264.addWidget(self.widget_468)


        self.horizontalLayout_363.addWidget(self.widget_463)

        self.horizontalSpacer_301 = QSpacerItem(250, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_363.addItem(self.horizontalSpacer_301)


        self.verticalLayout_263.addWidget(self.widget_462)

        self.widget_469 = QWidget(self.widget_461)
        self.widget_469.setObjectName(u"widget_469")
        self.widget_469.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.horizontalLayout_289 = QHBoxLayout(self.widget_469)
        self.horizontalLayout_289.setObjectName(u"horizontalLayout_289")
        self.widget_warning_9 = QWidget(self.widget_469)
        self.widget_warning_9.setObjectName(u"widget_warning_9")
        self.widget_warning_9.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_354 = QHBoxLayout(self.widget_warning_9)
        self.horizontalLayout_354.setSpacing(0)
        self.horizontalLayout_354.setObjectName(u"horizontalLayout_354")
        self.horizontalLayout_354.setContentsMargins(10, 5, 5, 5)
        self.label_225 = QLabel(self.widget_warning_9)
        self.label_225.setObjectName(u"label_225")
        self.label_225.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_354.addWidget(self.label_225)

        self.label_309 = QLabel(self.widget_warning_9)
        self.label_309.setObjectName(u"label_309")
        self.label_309.setMinimumSize(QSize(150, 0))
        self.label_309.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_309.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_354.addWidget(self.label_309)


        self.horizontalLayout_289.addWidget(self.widget_warning_9)

        self.horizontalSpacer_302 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_289.addItem(self.horizontalSpacer_302)

        self.pushButton_156 = QPushButton(self.widget_469)
        self.pushButton_156.setObjectName(u"pushButton_156")
        self.pushButton_156.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_156.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(36, 38, 140);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:10px;\n"
"padding-right:40px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"\n"
"}")
        self.pushButton_156.setCheckable(True)

        self.horizontalLayout_289.addWidget(self.pushButton_156)


        self.verticalLayout_263.addWidget(self.widget_469)


        self.gridLayout_19.addWidget(self.widget_461, 1, 0, 1, 1)


        self.gridLayout_20.addWidget(self.widget_459, 1, 0, 1, 1)

        self.widget_536 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_536.setObjectName(u"widget_536")
        self.horizontalLayout_382 = QHBoxLayout(self.widget_536)
        self.horizontalLayout_382.setObjectName(u"horizontalLayout_382")
        self.label_269 = QLabel(self.widget_536)
        self.label_269.setObjectName(u"label_269")
        sizePolicy6.setHeightForWidth(self.label_269.sizePolicy().hasHeightForWidth())
        self.label_269.setSizePolicy(sizePolicy6)
        self.label_269.setFont(font4)
        self.label_269.setStyleSheet(u"QLabel{\n"
"background-color: rgb(36, 38, 140);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:10px;\n"
"padding-right:40px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"}")

        self.horizontalLayout_382.addWidget(self.label_269)

        self.horizontalSpacer_308 = QSpacerItem(364, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_382.addItem(self.horizontalSpacer_308)

        self.label_270 = QLabel(self.widget_536)
        self.label_270.setObjectName(u"label_270")
        self.label_270.setFont(font5)

        self.horizontalLayout_382.addWidget(self.label_270)

        self.horizontalSpacer_309 = QSpacerItem(364, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_382.addItem(self.horizontalSpacer_309)

        self.label_271 = QLabel(self.widget_536)
        self.label_271.setObjectName(u"label_271")
        self.label_271.setFont(font5)

        self.horizontalLayout_382.addWidget(self.label_271)


        self.gridLayout_20.addWidget(self.widget_536, 0, 0, 1, 1)

        self.widget_470 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_470.setObjectName(u"widget_470")
        self.verticalLayout_304 = QVBoxLayout(self.widget_470)
        self.verticalLayout_304.setObjectName(u"verticalLayout_304")
        self.widget_471 = QWidget(self.widget_470)
        self.widget_471.setObjectName(u"widget_471")
        self.horizontalLayout_370 = QHBoxLayout(self.widget_471)
        self.horizontalLayout_370.setObjectName(u"horizontalLayout_370")
        self.horizontalLayout_370.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_58 = QWidget(self.widget_471)
        self.Equipement_widget_58.setObjectName(u"Equipement_widget_58")
        sizePolicy6.setHeightForWidth(self.Equipement_widget_58.sizePolicy().hasHeightForWidth())
        self.Equipement_widget_58.setSizePolicy(sizePolicy6)
        self.Equipement_widget_58.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_371 = QHBoxLayout(self.Equipement_widget_58)
        self.horizontalLayout_371.setObjectName(u"horizontalLayout_371")
        self.label_208 = QLabel(self.Equipement_widget_58)
        self.label_208.setObjectName(u"label_208")
        self.label_208.setPixmap(QPixmap(u":/assets/icons/employee-30.png"))

        self.horizontalLayout_371.addWidget(self.label_208, 0, Qt.AlignLeft)

        self.pushButton_157 = QPushButton(self.Equipement_widget_58)
        self.pushButton_157.setObjectName(u"pushButton_157")
        sizePolicy2.setHeightForWidth(self.pushButton_157.sizePolicy().hasHeightForWidth())
        self.pushButton_157.setSizePolicy(sizePolicy2)
        self.pushButton_157.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_157.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_157.setIcon(icon9)
        self.pushButton_157.setIconSize(QSize(24, 24))
        self.pushButton_157.setCheckable(True)

        self.horizontalLayout_371.addWidget(self.pushButton_157)


        self.horizontalLayout_370.addWidget(self.Equipement_widget_58)

        self.horizontalSpacer_303 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_370.addItem(self.horizontalSpacer_303)


        self.verticalLayout_304.addWidget(self.widget_471)

        self.widget_472 = QWidget(self.widget_470)
        self.widget_472.setObjectName(u"widget_472")
        self.widget_472.setMinimumSize(QSize(450, 0))
        self.widget_472.setStyleSheet(u"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.verticalLayout_305 = QVBoxLayout(self.widget_472)
        self.verticalLayout_305.setObjectName(u"verticalLayout_305")
        self.widget_473 = QWidget(self.widget_472)
        self.widget_473.setObjectName(u"widget_473")
        self.horizontalLayout_372 = QHBoxLayout(self.widget_473)
        self.horizontalLayout_372.setObjectName(u"horizontalLayout_372")
        self.horizontalSpacer_304 = QSpacerItem(251, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_372.addItem(self.horizontalSpacer_304)

        self.widget_474 = QWidget(self.widget_473)
        self.widget_474.setObjectName(u"widget_474")
        self.widget_474.setMinimumSize(QSize(700, 0))
        self.widget_474.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_266 = QVBoxLayout(self.widget_474)
        self.verticalLayout_266.setObjectName(u"verticalLayout_266")
        self.widget_476 = QWidget(self.widget_474)
        self.widget_476.setObjectName(u"widget_476")
        self.horizontalLayout_374 = QHBoxLayout(self.widget_476)
        self.horizontalLayout_374.setSpacing(10)
        self.horizontalLayout_374.setObjectName(u"horizontalLayout_374")
        self.horizontalLayout_374.setContentsMargins(0, 0, 0, 0)
        self.widget_477 = QWidget(self.widget_476)
        self.widget_477.setObjectName(u"widget_477")
        self.widget_477.setMinimumSize(QSize(100, 0))
        self.widget_477.setStyleSheet(u"background-color: rgb(236, 234, 234);\n"
"border-radius:5px;")
        self.verticalLayout_268 = QVBoxLayout(self.widget_477)
        self.verticalLayout_268.setObjectName(u"verticalLayout_268")
        self.label_259 = QLabel(self.widget_477)
        self.label_259.setObjectName(u"label_259")
        self.label_259.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 12pt \"Segoe UI\";")
        self.label_259.setAlignment(Qt.AlignCenter)

        self.verticalLayout_268.addWidget(self.label_259)

        self.verticalSpacer_88 = QSpacerItem(20, 111, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_268.addItem(self.verticalSpacer_88)


        self.horizontalLayout_374.addWidget(self.widget_477)

        self.widget_478 = QWidget(self.widget_476)
        self.widget_478.setObjectName(u"widget_478")
        self.widget_478.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-radius:5px;")
        self.verticalLayout_269 = QVBoxLayout(self.widget_478)
        self.verticalLayout_269.setObjectName(u"verticalLayout_269")
        self.verticalSpacer_89 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_269.addItem(self.verticalSpacer_89)

        self.widget_479 = QWidget(self.widget_478)
        self.widget_479.setObjectName(u"widget_479")
        self.horizontalLayout_375 = QHBoxLayout(self.widget_479)
        self.horizontalLayout_375.setSpacing(47)
        self.horizontalLayout_375.setObjectName(u"horizontalLayout_375")
        self.label_260 = QLabel(self.widget_479)
        self.label_260.setObjectName(u"label_260")
        sizePolicy3.setHeightForWidth(self.label_260.sizePolicy().hasHeightForWidth())
        self.label_260.setSizePolicy(sizePolicy3)
        self.label_260.setFont(font6)
        self.label_260.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_260.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_375.addWidget(self.label_260)

        self.lineEdit_90 = QLineEdit(self.widget_479)
        self.lineEdit_90.setObjectName(u"lineEdit_90")
        sizePolicy4.setHeightForWidth(self.lineEdit_90.sizePolicy().hasHeightForWidth())
        self.lineEdit_90.setSizePolicy(sizePolicy4)
        self.lineEdit_90.setMinimumSize(QSize(300, 0))
        self.lineEdit_90.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"padding-left:10px;")

        self.horizontalLayout_375.addWidget(self.lineEdit_90)


        self.verticalLayout_269.addWidget(self.widget_479)

        self.widget_480 = QWidget(self.widget_478)
        self.widget_480.setObjectName(u"widget_480")
        self.horizontalLayout_376 = QHBoxLayout(self.widget_480)
        self.horizontalLayout_376.setSpacing(72)
        self.horizontalLayout_376.setObjectName(u"horizontalLayout_376")
        self.label_261 = QLabel(self.widget_480)
        self.label_261.setObjectName(u"label_261")
        sizePolicy3.setHeightForWidth(self.label_261.sizePolicy().hasHeightForWidth())
        self.label_261.setSizePolicy(sizePolicy3)
        self.label_261.setFont(font6)
        self.label_261.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_261.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_376.addWidget(self.label_261)

        self.lineEdit_91 = QLineEdit(self.widget_480)
        self.lineEdit_91.setObjectName(u"lineEdit_91")
        sizePolicy4.setHeightForWidth(self.lineEdit_91.sizePolicy().hasHeightForWidth())
        self.lineEdit_91.setSizePolicy(sizePolicy4)
        self.lineEdit_91.setMinimumSize(QSize(300, 0))
        self.lineEdit_91.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"padding-left:10px;")

        self.horizontalLayout_376.addWidget(self.lineEdit_91)


        self.verticalLayout_269.addWidget(self.widget_480)

        self.verticalSpacer_90 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_269.addItem(self.verticalSpacer_90)


        self.horizontalLayout_374.addWidget(self.widget_478)


        self.verticalLayout_266.addWidget(self.widget_476)


        self.horizontalLayout_372.addWidget(self.widget_474)

        self.horizontalSpacer_305 = QSpacerItem(250, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_372.addItem(self.horizontalSpacer_305)


        self.verticalLayout_305.addWidget(self.widget_473)

        self.widget_487 = QWidget(self.widget_472)
        self.widget_487.setObjectName(u"widget_487")
        self.horizontalLayout_295 = QHBoxLayout(self.widget_487)
        self.horizontalLayout_295.setObjectName(u"horizontalLayout_295")
        self.widget_warning_10 = QWidget(self.widget_487)
        self.widget_warning_10.setObjectName(u"widget_warning_10")
        self.widget_warning_10.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_358 = QHBoxLayout(self.widget_warning_10)
        self.horizontalLayout_358.setSpacing(0)
        self.horizontalLayout_358.setObjectName(u"horizontalLayout_358")
        self.horizontalLayout_358.setContentsMargins(10, 5, 5, 5)
        self.label_226 = QLabel(self.widget_warning_10)
        self.label_226.setObjectName(u"label_226")
        self.label_226.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_358.addWidget(self.label_226)

        self.label_310 = QLabel(self.widget_warning_10)
        self.label_310.setObjectName(u"label_310")
        self.label_310.setMinimumSize(QSize(150, 0))
        self.label_310.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_310.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_358.addWidget(self.label_310)


        self.horizontalLayout_295.addWidget(self.widget_warning_10)

        self.horizontalSpacer_306 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_295.addItem(self.horizontalSpacer_306)

        self.pushButton_158 = QPushButton(self.widget_487)
        self.pushButton_158.setObjectName(u"pushButton_158")
        self.pushButton_158.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_158.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(36, 38, 140);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:10px;\n"
"padding-right:40px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"\n"
"}")
        self.pushButton_158.setCheckable(True)

        self.horizontalLayout_295.addWidget(self.pushButton_158)


        self.verticalLayout_305.addWidget(self.widget_487)


        self.verticalLayout_304.addWidget(self.widget_472)


        self.gridLayout_20.addWidget(self.widget_470, 2, 0, 1, 1)

        self.widget_532 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_532.setObjectName(u"widget_532")
        self.widget_532.setStyleSheet(u"")
        self.horizontalLayout_340 = QHBoxLayout(self.widget_532)
        self.horizontalLayout_340.setObjectName(u"horizontalLayout_340")
        self.Equipement_widget_65 = QWidget(self.widget_532)
        self.Equipement_widget_65.setObjectName(u"Equipement_widget_65")
        sizePolicy6.setHeightForWidth(self.Equipement_widget_65.sizePolicy().hasHeightForWidth())
        self.Equipement_widget_65.setSizePolicy(sizePolicy6)
        self.Equipement_widget_65.setStyleSheet(u"QWidget{\n"
"background-color: rgb(236, 234, 234);\n"
"border-radius:10px;\n"
"color: white;\n"
"}")
        self.verticalLayout_272 = QVBoxLayout(self.Equipement_widget_65)
        self.verticalLayout_272.setSpacing(20)
        self.verticalLayout_272.setObjectName(u"verticalLayout_272")
        self.verticalLayout_272.setContentsMargins(2, 2, 20, 2)
        self.label_174 = QLabel(self.Equipement_widget_65)
        self.label_174.setObjectName(u"label_174")

        self.verticalLayout_272.addWidget(self.label_174)

        self.pushButton_179 = QPushButton(self.Equipement_widget_65)
        self.pushButton_179.setObjectName(u"pushButton_179")
        sizePolicy2.setHeightForWidth(self.pushButton_179.sizePolicy().hasHeightForWidth())
        self.pushButton_179.setSizePolicy(sizePolicy2)
        self.pushButton_179.setFont(font5)
        self.pushButton_179.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_179.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(200, 131, 131);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:4px;\n"
"padding-right:4px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(226, 148, 148);\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(226, 148, 148);\n"
"}")
        self.pushButton_179.setIcon(icon9)
        self.pushButton_179.setIconSize(QSize(24, 24))
        self.pushButton_179.setCheckable(True)

        self.verticalLayout_272.addWidget(self.pushButton_179)


        self.horizontalLayout_340.addWidget(self.Equipement_widget_65)

        self.horizontalSpacer_358 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_340.addItem(self.horizontalSpacer_358)

        self.Equipement_widget_66 = QWidget(self.widget_532)
        self.Equipement_widget_66.setObjectName(u"Equipement_widget_66")
        sizePolicy6.setHeightForWidth(self.Equipement_widget_66.sizePolicy().hasHeightForWidth())
        self.Equipement_widget_66.setSizePolicy(sizePolicy6)
        self.Equipement_widget_66.setStyleSheet(u"QWidget{\n"
"background-color: rgb(236, 234, 234);\n"
"border-radius:10px;\n"
"color: white;\n"
"}")
        self.verticalLayout_288 = QVBoxLayout(self.Equipement_widget_66)
        self.verticalLayout_288.setSpacing(20)
        self.verticalLayout_288.setObjectName(u"verticalLayout_288")
        self.verticalLayout_288.setContentsMargins(20, 4, 2, 2)
        self.label_175 = QLabel(self.Equipement_widget_66)
        self.label_175.setObjectName(u"label_175")

        self.verticalLayout_288.addWidget(self.label_175, 0, Qt.AlignTop)

        self.pushButton_180 = QPushButton(self.Equipement_widget_66)
        self.pushButton_180.setObjectName(u"pushButton_180")
        sizePolicy2.setHeightForWidth(self.pushButton_180.sizePolicy().hasHeightForWidth())
        self.pushButton_180.setSizePolicy(sizePolicy2)
        self.pushButton_180.setFont(font5)
        self.pushButton_180.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_180.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(165, 214, 167);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:10px;\n"
"padding-right:20px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(177, 229, 179);\n"
"}\n"
"QPushButton:checked{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(177, 229, 179);\n"
"}")
        self.pushButton_180.setIcon(icon9)
        self.pushButton_180.setIconSize(QSize(24, 24))
        self.pushButton_180.setCheckable(True)

        self.verticalLayout_288.addWidget(self.pushButton_180)


        self.horizontalLayout_340.addWidget(self.Equipement_widget_66)


        self.gridLayout_20.addWidget(self.widget_532, 3, 0, 1, 1)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)

        self.gridLayout_7.addWidget(self.scrollArea_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.data_newFournisseur_page)
        self.data_newClient_page = QWidget()
        self.data_newClient_page.setObjectName(u"data_newClient_page")
        self.gridLayout_9 = QGridLayout(self.data_newClient_page)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.scrollArea_9 = QScrollArea(self.data_newClient_page)
        self.scrollArea_9.setObjectName(u"scrollArea_9")
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 486, 867))
        self.gridLayout_23 = QGridLayout(self.scrollAreaWidgetContents_9)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.widget_537 = QWidget(self.scrollAreaWidgetContents_9)
        self.widget_537.setObjectName(u"widget_537")
        self.horizontalLayout_397 = QHBoxLayout(self.widget_537)
        self.horizontalLayout_397.setObjectName(u"horizontalLayout_397")
        self.label_276 = QLabel(self.widget_537)
        self.label_276.setObjectName(u"label_276")
        sizePolicy6.setHeightForWidth(self.label_276.sizePolicy().hasHeightForWidth())
        self.label_276.setSizePolicy(sizePolicy6)
        self.label_276.setFont(font4)
        self.label_276.setStyleSheet(u"QLabel{\n"
"background-color: rgb(36, 38, 140);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:10px;\n"
"padding-right:40px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"}")

        self.horizontalLayout_397.addWidget(self.label_276)

        self.horizontalSpacer_320 = QSpacerItem(364, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_397.addItem(self.horizontalSpacer_320)

        self.label_277 = QLabel(self.widget_537)
        self.label_277.setObjectName(u"label_277")
        self.label_277.setFont(font5)

        self.horizontalLayout_397.addWidget(self.label_277)

        self.horizontalSpacer_321 = QSpacerItem(364, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_397.addItem(self.horizontalSpacer_321)

        self.label_278 = QLabel(self.widget_537)
        self.label_278.setObjectName(u"label_278")
        self.label_278.setFont(font5)

        self.horizontalLayout_397.addWidget(self.label_278)


        self.gridLayout_23.addWidget(self.widget_537, 0, 0, 1, 1)

        self.widget_467 = QWidget(self.scrollAreaWidgetContents_9)
        self.widget_467.setObjectName(u"widget_467")
        self.gridLayout_22 = QGridLayout(self.widget_467)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.widget_511 = QWidget(self.widget_467)
        self.widget_511.setObjectName(u"widget_511")
        self.horizontalLayout_301 = QHBoxLayout(self.widget_511)
        self.horizontalLayout_301.setObjectName(u"horizontalLayout_301")
        self.horizontalLayout_301.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_62 = QWidget(self.widget_511)
        self.Equipement_widget_62.setObjectName(u"Equipement_widget_62")
        self.Equipement_widget_62.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_302 = QHBoxLayout(self.Equipement_widget_62)
        self.horizontalLayout_302.setObjectName(u"horizontalLayout_302")
        self.label_163 = QLabel(self.Equipement_widget_62)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setPixmap(QPixmap(u":/assets/icons/employee-30.png"))

        self.horizontalLayout_302.addWidget(self.label_163, 0, Qt.AlignLeft)

        self.pushButton_167 = QPushButton(self.Equipement_widget_62)
        self.pushButton_167.setObjectName(u"pushButton_167")
        sizePolicy2.setHeightForWidth(self.pushButton_167.sizePolicy().hasHeightForWidth())
        self.pushButton_167.setSizePolicy(sizePolicy2)
        self.pushButton_167.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_167.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(245, 245, 245);\n"
"}\n"
"")
        self.pushButton_167.setIconSize(QSize(24, 24))
        self.pushButton_167.setCheckable(False)

        self.horizontalLayout_302.addWidget(self.pushButton_167)


        self.horizontalLayout_301.addWidget(self.Equipement_widget_62)

        self.horizontalSpacer_326 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_301.addItem(self.horizontalSpacer_326)


        self.gridLayout_22.addWidget(self.widget_511, 0, 0, 1, 1)

        self.widget_512 = QWidget(self.widget_467)
        self.widget_512.setObjectName(u"widget_512")
        self.widget_512.setMinimumSize(QSize(450, 0))
        self.widget_512.setStyleSheet(u"color: rgb(92, 124, 250);\n"
"background-color: rgb(245, 245, 245);")
        self.verticalLayout_276 = QVBoxLayout(self.widget_512)
        self.verticalLayout_276.setObjectName(u"verticalLayout_276")
        self.widget_513 = QWidget(self.widget_512)
        self.widget_513.setObjectName(u"widget_513")
        self.horizontalLayout_408 = QHBoxLayout(self.widget_513)
        self.horizontalLayout_408.setObjectName(u"horizontalLayout_408")
        self.horizontalSpacer_327 = QSpacerItem(251, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_408.addItem(self.horizontalSpacer_327)

        self.widget_514 = QWidget(self.widget_513)
        self.widget_514.setObjectName(u"widget_514")
        self.widget_514.setMinimumSize(QSize(600, 0))
        self.widget_514.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_277 = QVBoxLayout(self.widget_514)
        self.verticalLayout_277.setSpacing(10)
        self.verticalLayout_277.setObjectName(u"verticalLayout_277")
        self.verticalLayout_277.setContentsMargins(14, 14, 14, 14)
        self.widget_515 = QWidget(self.widget_514)
        self.widget_515.setObjectName(u"widget_515")
        self.widget_515.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-radius:5px;")
        self.horizontalLayout_409 = QHBoxLayout(self.widget_515)
        self.horizontalLayout_409.setSpacing(10)
        self.horizontalLayout_409.setObjectName(u"horizontalLayout_409")
        self.label_215 = QLabel(self.widget_515)
        self.label_215.setObjectName(u"label_215")
        sizePolicy3.setHeightForWidth(self.label_215.sizePolicy().hasHeightForWidth())
        self.label_215.setSizePolicy(sizePolicy3)
        self.label_215.setFont(font6)
        self.label_215.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_215.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_409.addWidget(self.label_215)

        self.lineEdit_76 = QLineEdit(self.widget_515)
        self.lineEdit_76.setObjectName(u"lineEdit_76")
        sizePolicy4.setHeightForWidth(self.lineEdit_76.sizePolicy().hasHeightForWidth())
        self.lineEdit_76.setSizePolicy(sizePolicy4)
        self.lineEdit_76.setMinimumSize(QSize(300, 0))
        self.lineEdit_76.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"padding-left:10px;")

        self.horizontalLayout_409.addWidget(self.lineEdit_76)


        self.verticalLayout_277.addWidget(self.widget_515)

        self.widget_516 = QWidget(self.widget_514)
        self.widget_516.setObjectName(u"widget_516")
        self.widget_516.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-radius:5px;")
        self.horizontalLayout_410 = QHBoxLayout(self.widget_516)
        self.horizontalLayout_410.setSpacing(10)
        self.horizontalLayout_410.setObjectName(u"horizontalLayout_410")
        self.label_216 = QLabel(self.widget_516)
        self.label_216.setObjectName(u"label_216")
        sizePolicy3.setHeightForWidth(self.label_216.sizePolicy().hasHeightForWidth())
        self.label_216.setSizePolicy(sizePolicy3)
        self.label_216.setFont(font6)
        self.label_216.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_216.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_410.addWidget(self.label_216)

        self.lineEdit_99 = QLineEdit(self.widget_516)
        self.lineEdit_99.setObjectName(u"lineEdit_99")
        sizePolicy4.setHeightForWidth(self.lineEdit_99.sizePolicy().hasHeightForWidth())
        self.lineEdit_99.setSizePolicy(sizePolicy4)
        self.lineEdit_99.setMinimumSize(QSize(300, 0))
        self.lineEdit_99.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"padding-left:10px;")

        self.horizontalLayout_410.addWidget(self.lineEdit_99)


        self.verticalLayout_277.addWidget(self.widget_516)

        self.widget_517 = QWidget(self.widget_514)
        self.widget_517.setObjectName(u"widget_517")
        self.widget_517.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-radius:5px;")
        self.horizontalLayout_411 = QHBoxLayout(self.widget_517)
        self.horizontalLayout_411.setSpacing(10)
        self.horizontalLayout_411.setObjectName(u"horizontalLayout_411")
        self.label_217 = QLabel(self.widget_517)
        self.label_217.setObjectName(u"label_217")
        sizePolicy3.setHeightForWidth(self.label_217.sizePolicy().hasHeightForWidth())
        self.label_217.setSizePolicy(sizePolicy3)
        self.label_217.setFont(font6)
        self.label_217.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_217.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_411.addWidget(self.label_217)

        self.lineEdit_100 = QLineEdit(self.widget_517)
        self.lineEdit_100.setObjectName(u"lineEdit_100")
        sizePolicy4.setHeightForWidth(self.lineEdit_100.sizePolicy().hasHeightForWidth())
        self.lineEdit_100.setSizePolicy(sizePolicy4)
        self.lineEdit_100.setMinimumSize(QSize(300, 0))
        self.lineEdit_100.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"padding-left:10px;")

        self.horizontalLayout_411.addWidget(self.lineEdit_100)


        self.verticalLayout_277.addWidget(self.widget_517)

        self.widget_518 = QWidget(self.widget_514)
        self.widget_518.setObjectName(u"widget_518")
        self.widget_518.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-radius:5px;")
        self.horizontalLayout_412 = QHBoxLayout(self.widget_518)
        self.horizontalLayout_412.setSpacing(10)
        self.horizontalLayout_412.setObjectName(u"horizontalLayout_412")
        self.label_218 = QLabel(self.widget_518)
        self.label_218.setObjectName(u"label_218")
        sizePolicy3.setHeightForWidth(self.label_218.sizePolicy().hasHeightForWidth())
        self.label_218.setSizePolicy(sizePolicy3)
        self.label_218.setFont(font6)
        self.label_218.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_218.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_412.addWidget(self.label_218)

        self.lineEdit_101 = QLineEdit(self.widget_518)
        self.lineEdit_101.setObjectName(u"lineEdit_101")
        sizePolicy4.setHeightForWidth(self.lineEdit_101.sizePolicy().hasHeightForWidth())
        self.lineEdit_101.setSizePolicy(sizePolicy4)
        self.lineEdit_101.setMinimumSize(QSize(300, 0))
        self.lineEdit_101.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"padding-left:10px;")

        self.horizontalLayout_412.addWidget(self.lineEdit_101)


        self.verticalLayout_277.addWidget(self.widget_518)


        self.horizontalLayout_408.addWidget(self.widget_514)

        self.horizontalSpacer_328 = QSpacerItem(250, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_408.addItem(self.horizontalSpacer_328)


        self.verticalLayout_276.addWidget(self.widget_513)

        self.widget_519 = QWidget(self.widget_512)
        self.widget_519.setObjectName(u"widget_519")
        self.widget_519.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.horizontalLayout_296 = QHBoxLayout(self.widget_519)
        self.horizontalLayout_296.setObjectName(u"horizontalLayout_296")
        self.widget_warning_11 = QWidget(self.widget_519)
        self.widget_warning_11.setObjectName(u"widget_warning_11")
        self.widget_warning_11.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_367 = QHBoxLayout(self.widget_warning_11)
        self.horizontalLayout_367.setSpacing(0)
        self.horizontalLayout_367.setObjectName(u"horizontalLayout_367")
        self.horizontalLayout_367.setContentsMargins(10, 5, 5, 5)
        self.label_227 = QLabel(self.widget_warning_11)
        self.label_227.setObjectName(u"label_227")
        self.label_227.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_367.addWidget(self.label_227)

        self.label_311 = QLabel(self.widget_warning_11)
        self.label_311.setObjectName(u"label_311")
        self.label_311.setMinimumSize(QSize(150, 0))
        self.label_311.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_311.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_367.addWidget(self.label_311)


        self.horizontalLayout_296.addWidget(self.widget_warning_11)

        self.horizontalSpacer_329 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_296.addItem(self.horizontalSpacer_329)

        self.pushButton_168 = QPushButton(self.widget_519)
        self.pushButton_168.setObjectName(u"pushButton_168")
        self.pushButton_168.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_168.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(36, 38, 140);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:10px;\n"
"padding-right:40px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"}")
        self.pushButton_168.setIcon(icon16)
        self.pushButton_168.setCheckable(True)

        self.horizontalLayout_296.addWidget(self.pushButton_168)


        self.verticalLayout_276.addWidget(self.widget_519)


        self.gridLayout_22.addWidget(self.widget_512, 1, 0, 1, 1)


        self.gridLayout_23.addWidget(self.widget_467, 1, 0, 1, 1)

        self.widget_475 = QWidget(self.scrollAreaWidgetContents_9)
        self.widget_475.setObjectName(u"widget_475")
        self.verticalLayout_308 = QVBoxLayout(self.widget_475)
        self.verticalLayout_308.setObjectName(u"verticalLayout_308")
        self.widget_501 = QWidget(self.widget_475)
        self.widget_501.setObjectName(u"widget_501")
        self.horizontalLayout_401 = QHBoxLayout(self.widget_501)
        self.horizontalLayout_401.setObjectName(u"horizontalLayout_401")
        self.horizontalLayout_401.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_61 = QWidget(self.widget_501)
        self.Equipement_widget_61.setObjectName(u"Equipement_widget_61")
        sizePolicy6.setHeightForWidth(self.Equipement_widget_61.sizePolicy().hasHeightForWidth())
        self.Equipement_widget_61.setSizePolicy(sizePolicy6)
        self.Equipement_widget_61.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_402 = QHBoxLayout(self.Equipement_widget_61)
        self.horizontalLayout_402.setObjectName(u"horizontalLayout_402")
        self.label_214 = QLabel(self.Equipement_widget_61)
        self.label_214.setObjectName(u"label_214")
        self.label_214.setPixmap(QPixmap(u":/assets/icons/employee-30.png"))

        self.horizontalLayout_402.addWidget(self.label_214, 0, Qt.AlignLeft)

        self.pushButton_165 = QPushButton(self.Equipement_widget_61)
        self.pushButton_165.setObjectName(u"pushButton_165")
        sizePolicy2.setHeightForWidth(self.pushButton_165.sizePolicy().hasHeightForWidth())
        self.pushButton_165.setSizePolicy(sizePolicy2)
        self.pushButton_165.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_165.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_165.setIcon(icon9)
        self.pushButton_165.setIconSize(QSize(24, 24))
        self.pushButton_165.setCheckable(True)

        self.horizontalLayout_402.addWidget(self.pushButton_165)


        self.horizontalLayout_401.addWidget(self.Equipement_widget_61)

        self.horizontalSpacer_322 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_401.addItem(self.horizontalSpacer_322)


        self.verticalLayout_308.addWidget(self.widget_501)

        self.widget_502 = QWidget(self.widget_475)
        self.widget_502.setObjectName(u"widget_502")
        self.widget_502.setMinimumSize(QSize(450, 0))
        self.widget_502.setStyleSheet(u"color: rgb(92, 124, 250);\n"
"background-color: rgb(245, 245, 245);")
        self.verticalLayout_309 = QVBoxLayout(self.widget_502)
        self.verticalLayout_309.setObjectName(u"verticalLayout_309")
        self.widget_503 = QWidget(self.widget_502)
        self.widget_503.setObjectName(u"widget_503")
        self.horizontalLayout_403 = QHBoxLayout(self.widget_503)
        self.horizontalLayout_403.setObjectName(u"horizontalLayout_403")
        self.horizontalSpacer_323 = QSpacerItem(251, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_403.addItem(self.horizontalSpacer_323)

        self.widget_504 = QWidget(self.widget_503)
        self.widget_504.setObjectName(u"widget_504")
        self.widget_504.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_273 = QVBoxLayout(self.widget_504)
        self.verticalLayout_273.setObjectName(u"verticalLayout_273")
        self.widget_505 = QWidget(self.widget_504)
        self.widget_505.setObjectName(u"widget_505")
        self.horizontalLayout_404 = QHBoxLayout(self.widget_505)
        self.horizontalLayout_404.setObjectName(u"horizontalLayout_404")
        self.widget_506 = QWidget(self.widget_505)
        self.widget_506.setObjectName(u"widget_506")
        self.verticalLayout_274 = QVBoxLayout(self.widget_506)
        self.verticalLayout_274.setObjectName(u"verticalLayout_274")
        self.label_265 = QLabel(self.widget_506)
        self.label_265.setObjectName(u"label_265")
        self.label_265.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 12pt \"Segoe UI\";")

        self.verticalLayout_274.addWidget(self.label_265)

        self.verticalSpacer_94 = QSpacerItem(20, 111, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_274.addItem(self.verticalSpacer_94)


        self.horizontalLayout_404.addWidget(self.widget_506)

        self.widget_507 = QWidget(self.widget_505)
        self.widget_507.setObjectName(u"widget_507")
        self.verticalLayout_275 = QVBoxLayout(self.widget_507)
        self.verticalLayout_275.setObjectName(u"verticalLayout_275")
        self.verticalSpacer_95 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_275.addItem(self.verticalSpacer_95)

        self.widget_508 = QWidget(self.widget_507)
        self.widget_508.setObjectName(u"widget_508")
        self.widget_508.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-radius:5px;")
        self.horizontalLayout_405 = QHBoxLayout(self.widget_508)
        self.horizontalLayout_405.setSpacing(47)
        self.horizontalLayout_405.setObjectName(u"horizontalLayout_405")
        self.label_266 = QLabel(self.widget_508)
        self.label_266.setObjectName(u"label_266")
        self.label_266.setFont(font6)
        self.label_266.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_266.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_405.addWidget(self.label_266)

        self.lineEdit_97 = QLineEdit(self.widget_508)
        self.lineEdit_97.setObjectName(u"lineEdit_97")
        sizePolicy4.setHeightForWidth(self.lineEdit_97.sizePolicy().hasHeightForWidth())
        self.lineEdit_97.setSizePolicy(sizePolicy4)
        self.lineEdit_97.setMinimumSize(QSize(300, 0))
        self.lineEdit_97.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"padding-left:10px;")

        self.horizontalLayout_405.addWidget(self.lineEdit_97)


        self.verticalLayout_275.addWidget(self.widget_508)

        self.widget_509 = QWidget(self.widget_507)
        self.widget_509.setObjectName(u"widget_509")
        self.widget_509.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-radius:5px;")
        self.horizontalLayout_406 = QHBoxLayout(self.widget_509)
        self.horizontalLayout_406.setSpacing(72)
        self.horizontalLayout_406.setObjectName(u"horizontalLayout_406")
        self.label_267 = QLabel(self.widget_509)
        self.label_267.setObjectName(u"label_267")
        self.label_267.setFont(font6)
        self.label_267.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_267.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_406.addWidget(self.label_267)

        self.lineEdit_98 = QLineEdit(self.widget_509)
        self.lineEdit_98.setObjectName(u"lineEdit_98")
        self.lineEdit_98.setMinimumSize(QSize(200, 0))
        self.lineEdit_98.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"padding-left:10px;")

        self.horizontalLayout_406.addWidget(self.lineEdit_98)


        self.verticalLayout_275.addWidget(self.widget_509)

        self.verticalSpacer_96 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_275.addItem(self.verticalSpacer_96)


        self.horizontalLayout_404.addWidget(self.widget_507)


        self.verticalLayout_273.addWidget(self.widget_505)


        self.horizontalLayout_403.addWidget(self.widget_504)

        self.horizontalSpacer_324 = QSpacerItem(250, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_403.addItem(self.horizontalSpacer_324)


        self.verticalLayout_309.addWidget(self.widget_503)

        self.widget_510 = QWidget(self.widget_502)
        self.widget_510.setObjectName(u"widget_510")
        self.widget_510.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.horizontalLayout_314 = QHBoxLayout(self.widget_510)
        self.horizontalLayout_314.setObjectName(u"horizontalLayout_314")
        self.widget_warning_12 = QWidget(self.widget_510)
        self.widget_warning_12.setObjectName(u"widget_warning_12")
        self.widget_warning_12.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_369 = QHBoxLayout(self.widget_warning_12)
        self.horizontalLayout_369.setSpacing(0)
        self.horizontalLayout_369.setObjectName(u"horizontalLayout_369")
        self.horizontalLayout_369.setContentsMargins(10, 5, 5, 5)
        self.label_228 = QLabel(self.widget_warning_12)
        self.label_228.setObjectName(u"label_228")
        self.label_228.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_369.addWidget(self.label_228)

        self.label_312 = QLabel(self.widget_warning_12)
        self.label_312.setObjectName(u"label_312")
        self.label_312.setMinimumSize(QSize(150, 0))
        self.label_312.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_312.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_369.addWidget(self.label_312)


        self.horizontalLayout_314.addWidget(self.widget_warning_12)

        self.horizontalSpacer_325 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_314.addItem(self.horizontalSpacer_325)

        self.pushButton_166 = QPushButton(self.widget_510)
        self.pushButton_166.setObjectName(u"pushButton_166")
        self.pushButton_166.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_166.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(36, 38, 140);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:10px;\n"
"padding-right:40px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"}")
        self.pushButton_166.setIcon(icon16)
        self.pushButton_166.setCheckable(True)

        self.horizontalLayout_314.addWidget(self.pushButton_166)


        self.verticalLayout_309.addWidget(self.widget_510)


        self.verticalLayout_308.addWidget(self.widget_502)


        self.gridLayout_23.addWidget(self.widget_475, 2, 0, 1, 1)

        self.widget_535 = QWidget(self.scrollAreaWidgetContents_9)
        self.widget_535.setObjectName(u"widget_535")
        self.widget_535.setStyleSheet(u"")
        self.horizontalLayout_398 = QHBoxLayout(self.widget_535)
        self.horizontalLayout_398.setObjectName(u"horizontalLayout_398")
        self.Equipement_widget_69 = QWidget(self.widget_535)
        self.Equipement_widget_69.setObjectName(u"Equipement_widget_69")
        sizePolicy6.setHeightForWidth(self.Equipement_widget_69.sizePolicy().hasHeightForWidth())
        self.Equipement_widget_69.setSizePolicy(sizePolicy6)
        self.Equipement_widget_69.setStyleSheet(u"QWidget{\n"
"background-color: rgb(236, 234, 234);\n"
"border-radius:10px;\n"
"color: white;\n"
"}")
        self.verticalLayout_289 = QVBoxLayout(self.Equipement_widget_69)
        self.verticalLayout_289.setSpacing(20)
        self.verticalLayout_289.setObjectName(u"verticalLayout_289")
        self.verticalLayout_289.setContentsMargins(2, 2, 20, 2)
        self.label_176 = QLabel(self.Equipement_widget_69)
        self.label_176.setObjectName(u"label_176")

        self.verticalLayout_289.addWidget(self.label_176)

        self.pushButton_183 = QPushButton(self.Equipement_widget_69)
        self.pushButton_183.setObjectName(u"pushButton_183")
        sizePolicy2.setHeightForWidth(self.pushButton_183.sizePolicy().hasHeightForWidth())
        self.pushButton_183.setSizePolicy(sizePolicy2)
        self.pushButton_183.setFont(font5)
        self.pushButton_183.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_183.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(200, 131, 131);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:4px;\n"
"padding-right:4px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(226, 148, 148);\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(226, 148, 148);\n"
"}\n"
"")
        self.pushButton_183.setIcon(icon9)
        self.pushButton_183.setIconSize(QSize(24, 24))
        self.pushButton_183.setCheckable(True)

        self.verticalLayout_289.addWidget(self.pushButton_183)


        self.horizontalLayout_398.addWidget(self.Equipement_widget_69)

        self.horizontalSpacer_360 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_398.addItem(self.horizontalSpacer_360)

        self.Equipement_widget_70 = QWidget(self.widget_535)
        self.Equipement_widget_70.setObjectName(u"Equipement_widget_70")
        sizePolicy6.setHeightForWidth(self.Equipement_widget_70.sizePolicy().hasHeightForWidth())
        self.Equipement_widget_70.setSizePolicy(sizePolicy6)
        self.Equipement_widget_70.setStyleSheet(u"QWidget{\n"
"background-color: rgb(236, 234, 234);\n"
"border-radius:10px;\n"
"color: white;\n"
"}")
        self.verticalLayout_290 = QVBoxLayout(self.Equipement_widget_70)
        self.verticalLayout_290.setSpacing(20)
        self.verticalLayout_290.setObjectName(u"verticalLayout_290")
        self.verticalLayout_290.setContentsMargins(20, 4, 2, 2)
        self.label_177 = QLabel(self.Equipement_widget_70)
        self.label_177.setObjectName(u"label_177")

        self.verticalLayout_290.addWidget(self.label_177)

        self.pushButton_184 = QPushButton(self.Equipement_widget_70)
        self.pushButton_184.setObjectName(u"pushButton_184")
        sizePolicy2.setHeightForWidth(self.pushButton_184.sizePolicy().hasHeightForWidth())
        self.pushButton_184.setSizePolicy(sizePolicy2)
        self.pushButton_184.setFont(font5)
        self.pushButton_184.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_184.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(165, 214, 167);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:10px;\n"
"padding-right:20px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(177, 229, 179);\n"
"}\n"
"QPushButton:checked{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(177, 229, 179);\n"
"}")
        self.pushButton_184.setIcon(icon9)
        self.pushButton_184.setIconSize(QSize(24, 24))
        self.pushButton_184.setCheckable(True)

        self.verticalLayout_290.addWidget(self.pushButton_184)


        self.horizontalLayout_398.addWidget(self.Equipement_widget_70)


        self.gridLayout_23.addWidget(self.widget_535, 3, 0, 1, 1)

        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_9)

        self.gridLayout_9.addWidget(self.scrollArea_9, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.data_newClient_page)
        self.autre_newBandeCommande_page = QWidget()
        self.autre_newBandeCommande_page.setObjectName(u"autre_newBandeCommande_page")
        self.gridLayout_12 = QGridLayout(self.autre_newBandeCommande_page)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.scrollArea_12 = QScrollArea(self.autre_newBandeCommande_page)
        self.scrollArea_12.setObjectName(u"scrollArea_12")
        self.scrollArea_12.setWidgetResizable(True)
        self.scrollAreaWidgetContents_12 = QWidget()
        self.scrollAreaWidgetContents_12.setObjectName(u"scrollAreaWidgetContents_12")
        self.scrollAreaWidgetContents_12.setGeometry(QRect(0, 0, 878, 1227))
        self.gridLayout_14 = QGridLayout(self.scrollAreaWidgetContents_12)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.widget_394 = QWidget(self.scrollAreaWidgetContents_12)
        self.widget_394.setObjectName(u"widget_394")
        self.horizontalLayout_282 = QHBoxLayout(self.widget_394)
        self.horizontalLayout_282.setObjectName(u"horizontalLayout_282")
        self.label_141 = QLabel(self.widget_394)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setFont(font4)
        self.label_141.setStyleSheet(u"QLabel{\n"
"background-color: rgb(36, 38, 140);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:10px;\n"
"padding-right:40px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"}")

        self.horizontalLayout_282.addWidget(self.label_141)

        self.horizontalSpacer_283 = QSpacerItem(364, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_282.addItem(self.horizontalSpacer_283)


        self.gridLayout_14.addWidget(self.widget_394, 0, 0, 1, 1)

        self.widget_830 = QWidget(self.scrollAreaWidgetContents_12)
        self.widget_830.setObjectName(u"widget_830")
        self.verticalLayout_459 = QVBoxLayout(self.widget_830)
        self.verticalLayout_459.setObjectName(u"verticalLayout_459")
        self.widget_831 = QWidget(self.widget_830)
        self.widget_831.setObjectName(u"widget_831")
        self.horizontalLayout_528 = QHBoxLayout(self.widget_831)
        self.horizontalLayout_528.setObjectName(u"horizontalLayout_528")
        self.horizontalLayout_528.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_103 = QWidget(self.widget_831)
        self.Equipement_widget_103.setObjectName(u"Equipement_widget_103")
        self.Equipement_widget_103.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_529 = QHBoxLayout(self.Equipement_widget_103)
        self.horizontalLayout_529.setObjectName(u"horizontalLayout_529")
        self.label_284 = QLabel(self.Equipement_widget_103)
        self.label_284.setObjectName(u"label_284")
        self.label_284.setPixmap(QPixmap(u":/assets/icons/schedule-30.png"))

        self.horizontalLayout_529.addWidget(self.label_284, 0, Qt.AlignLeft)

        self.pushButton_257 = QPushButton(self.Equipement_widget_103)
        self.pushButton_257.setObjectName(u"pushButton_257")
        sizePolicy2.setHeightForWidth(self.pushButton_257.sizePolicy().hasHeightForWidth())
        self.pushButton_257.setSizePolicy(sizePolicy2)
        self.pushButton_257.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_257.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(245, 245, 245);\n"
"}\n"
"")
        self.pushButton_257.setIconSize(QSize(24, 24))
        self.pushButton_257.setCheckable(False)

        self.horizontalLayout_529.addWidget(self.pushButton_257)


        self.horizontalLayout_528.addWidget(self.Equipement_widget_103)

        self.horizontalSpacer_565 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_528.addItem(self.horizontalSpacer_565)


        self.verticalLayout_459.addWidget(self.widget_831)

        self.widget_832 = QWidget(self.widget_830)
        self.widget_832.setObjectName(u"widget_832")
        self.widget_832.setMinimumSize(QSize(0, 0))
        self.widget_832.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(245, 245, 245);")
        self.horizontalLayout_530 = QHBoxLayout(self.widget_832)
        self.horizontalLayout_530.setObjectName(u"horizontalLayout_530")
        self.horizontalSpacer_566 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_530.addItem(self.horizontalSpacer_566)

        self.widget_833 = QWidget(self.widget_832)
        self.widget_833.setObjectName(u"widget_833")
        sizePolicy.setHeightForWidth(self.widget_833.sizePolicy().hasHeightForWidth())
        self.widget_833.setSizePolicy(sizePolicy)
        self.widget_833.setMinimumSize(QSize(400, 206))
        self.widget_833.setStyleSheet(u"background-color: rgb(236, 234, 234);\n"
"border-bottom-left-radius:7px;\n"
"border-bottom-right-radius:7px;")
        self.verticalLayout_460 = QVBoxLayout(self.widget_833)
        self.verticalLayout_460.setObjectName(u"verticalLayout_460")
        self.label_155 = QLabel(self.widget_833)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setStyleSheet(u"color: rgb(52, 56, 199);\n"
"\n"
"font: 8pt \"Microsoft JhengHei UI\";")

        self.verticalLayout_460.addWidget(self.label_155)

        self.label_156 = QLabel(self.widget_833)
        self.label_156.setObjectName(u"label_156")
        self.label_156.setWordWrap(True)

        self.verticalLayout_460.addWidget(self.label_156)

        self.widget_834 = QWidget(self.widget_833)
        self.widget_834.setObjectName(u"widget_834")
        self.widget_834.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(211, 211, 211);\n"
"border-radius:0px;")
        self.verticalLayout_461 = QVBoxLayout(self.widget_834)
        self.verticalLayout_461.setObjectName(u"verticalLayout_461")
        self.verticalLayout_461.setContentsMargins(15, 15, 15, 15)
        self.checkBox_45 = QCheckBox(self.widget_834)
        self.checkBox_45.setObjectName(u"checkBox_45")
        self.checkBox_45.setChecked(True)
        self.checkBox_45.setAutoExclusive(True)

        self.verticalLayout_461.addWidget(self.checkBox_45)

        self.checkBox_46 = QCheckBox(self.widget_834)
        self.checkBox_46.setObjectName(u"checkBox_46")
        self.checkBox_46.setAutoExclusive(True)

        self.verticalLayout_461.addWidget(self.checkBox_46)


        self.verticalLayout_460.addWidget(self.widget_834)

        self.widget_835 = QWidget(self.widget_833)
        self.widget_835.setObjectName(u"widget_835")
        self.horizontalLayout_531 = QHBoxLayout(self.widget_835)
        self.horizontalLayout_531.setObjectName(u"horizontalLayout_531")
        self.dateEdit_14 = QDateEdit(self.widget_835)
        self.dateEdit_14.setObjectName(u"dateEdit_14")
        font11 = QFont()
        font11.setFamilies([u"Segoe UI"])
        font11.setPointSize(12)
        font11.setBold(False)
        font11.setItalic(False)
        self.dateEdit_14.setFont(font11)
        self.dateEdit_14.setStyleSheet(u"color: rgb(58, 58, 58);\n"
"font: 12pt \"Segoe UI\";\n"
"background-color: rgb(245, 245, 245);\n"
"border-top-left-radius:7px;\n"
"border-bottom-left-radius:7px;")
        self.dateEdit_14.setAlignment(Qt.AlignCenter)
        self.dateEdit_14.setDateTime(QDateTime(QDate(2024, 10, 31), QTime(17, 0, 0)))
        self.dateEdit_14.setCalendarPopup(True)

        self.horizontalLayout_531.addWidget(self.dateEdit_14)


        self.verticalLayout_460.addWidget(self.widget_835)


        self.horizontalLayout_530.addWidget(self.widget_833)

        self.horizontalSpacer_568 = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_530.addItem(self.horizontalSpacer_568)

        self.widget_836 = QWidget(self.widget_832)
        self.widget_836.setObjectName(u"widget_836")
        self.widget_836.setMinimumSize(QSize(400, 206))
        self.widget_836.setMaximumSize(QSize(300, 16777215))
        self.widget_836.setStyleSheet(u"background-color: rgb(236, 234, 234);\n"
"border-bottom-left-radius:7px;\n"
"border-bottom-right-radius:7px;")
        self.verticalLayout_462 = QVBoxLayout(self.widget_836)
        self.verticalLayout_462.setObjectName(u"verticalLayout_462")
        self.label_169 = QLabel(self.widget_836)
        self.label_169.setObjectName(u"label_169")

        self.verticalLayout_462.addWidget(self.label_169)

        self.widget_837 = QWidget(self.widget_836)
        self.widget_837.setObjectName(u"widget_837")
        self.widget_837.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(211, 211, 211);\n"
"border-radius:0px;")
        self.verticalLayout_463 = QVBoxLayout(self.widget_837)
        self.verticalLayout_463.setObjectName(u"verticalLayout_463")
        self.verticalLayout_463.setContentsMargins(15, 15, 15, 15)
        self.checkBox_47 = QCheckBox(self.widget_837)
        self.checkBox_47.setObjectName(u"checkBox_47")
        self.checkBox_47.setChecked(True)
        self.checkBox_47.setAutoExclusive(True)

        self.verticalLayout_463.addWidget(self.checkBox_47)

        self.checkBox_48 = QCheckBox(self.widget_837)
        self.checkBox_48.setObjectName(u"checkBox_48")
        self.checkBox_48.setAutoExclusive(True)

        self.verticalLayout_463.addWidget(self.checkBox_48)


        self.verticalLayout_462.addWidget(self.widget_837)

        self.widget_838 = QWidget(self.widget_836)
        self.widget_838.setObjectName(u"widget_838")
        self.widget_838.setStyleSheet(u"color: rgb(58, 58, 58);\n"
"font: 12pt \"Segoe UI\";\n"
"background-color: rgb(245, 245, 245);\n"
"border-top-left-radius:7px;\n"
"border-bottom-left-radius:7px;")
        self.horizontalLayout_532 = QHBoxLayout(self.widget_838)
        self.horizontalLayout_532.setObjectName(u"horizontalLayout_532")
        self.label_285 = QLabel(self.widget_838)
        self.label_285.setObjectName(u"label_285")
        self.label_285.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_532.addWidget(self.label_285)

        self.timeEdit = QTimeEdit(self.widget_838)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setAlignment(Qt.AlignCenter)
        self.timeEdit.setCalendarPopup(False)

        self.horizontalLayout_532.addWidget(self.timeEdit)


        self.verticalLayout_462.addWidget(self.widget_838)

        self.widget_839 = QWidget(self.widget_836)
        self.widget_839.setObjectName(u"widget_839")
        self.horizontalLayout_310 = QHBoxLayout(self.widget_839)
        self.horizontalLayout_310.setObjectName(u"horizontalLayout_310")
        self.horizontalLayout_310.setContentsMargins(0, -1, -1, -1)
        self.widget_warning = QWidget(self.widget_839)
        self.widget_warning.setObjectName(u"widget_warning")
        self.widget_warning.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_285 = QHBoxLayout(self.widget_warning)
        self.horizontalLayout_285.setSpacing(0)
        self.horizontalLayout_285.setObjectName(u"horizontalLayout_285")
        self.horizontalLayout_285.setContentsMargins(10, 5, 5, 5)
        self.label_170 = QLabel(self.widget_warning)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_285.addWidget(self.label_170)

        self.label_286 = QLabel(self.widget_warning)
        self.label_286.setObjectName(u"label_286")
        self.label_286.setMinimumSize(QSize(150, 0))
        self.label_286.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_286.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_285.addWidget(self.label_286)


        self.horizontalLayout_310.addWidget(self.widget_warning)

        self.horizontalSpacer_570 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_310.addItem(self.horizontalSpacer_570)

        self.pushButton_258 = QPushButton(self.widget_839)
        self.pushButton_258.setObjectName(u"pushButton_258")
        self.pushButton_258.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_258.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(36, 38, 140);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:10px;\n"
"padding-right:40px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"\n"
"}")
        self.pushButton_258.setIcon(icon16)
        self.pushButton_258.setCheckable(True)

        self.horizontalLayout_310.addWidget(self.pushButton_258)


        self.verticalLayout_462.addWidget(self.widget_839)


        self.horizontalLayout_530.addWidget(self.widget_836)

        self.horizontalSpacer_571 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_530.addItem(self.horizontalSpacer_571)


        self.verticalLayout_459.addWidget(self.widget_832)


        self.gridLayout_14.addWidget(self.widget_830, 1, 0, 1, 1)

        self.widget_876 = QWidget(self.scrollAreaWidgetContents_12)
        self.widget_876.setObjectName(u"widget_876")
        self.verticalLayout_246 = QVBoxLayout(self.widget_876)
        self.verticalLayout_246.setObjectName(u"verticalLayout_246")
        self.widget_877 = QWidget(self.widget_876)
        self.widget_877.setObjectName(u"widget_877")
        self.widget_877.setStyleSheet(u"")
        self.horizontalLayout_555 = QHBoxLayout(self.widget_877)
        self.horizontalLayout_555.setObjectName(u"horizontalLayout_555")
        self.horizontalLayout_555.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_108 = QWidget(self.widget_877)
        self.Equipement_widget_108.setObjectName(u"Equipement_widget_108")
        self.Equipement_widget_108.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_556 = QHBoxLayout(self.Equipement_widget_108)
        self.horizontalLayout_556.setObjectName(u"horizontalLayout_556")
        self.label_297 = QLabel(self.Equipement_widget_108)
        self.label_297.setObjectName(u"label_297")
        self.label_297.setPixmap(QPixmap(u":/assets/icons/order-30.png"))

        self.horizontalLayout_556.addWidget(self.label_297, 0, Qt.AlignLeft)

        self.pushButton_269 = QPushButton(self.Equipement_widget_108)
        self.pushButton_269.setObjectName(u"pushButton_269")
        sizePolicy2.setHeightForWidth(self.pushButton_269.sizePolicy().hasHeightForWidth())
        self.pushButton_269.setSizePolicy(sizePolicy2)
        self.pushButton_269.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_269.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_269.setIcon(icon9)
        self.pushButton_269.setIconSize(QSize(24, 24))
        self.pushButton_269.setCheckable(True)

        self.horizontalLayout_556.addWidget(self.pushButton_269)


        self.horizontalLayout_555.addWidget(self.Equipement_widget_108)

        self.horizontalSpacer_594 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_555.addItem(self.horizontalSpacer_594)


        self.verticalLayout_246.addWidget(self.widget_877)

        self.widget_878 = QWidget(self.widget_876)
        self.widget_878.setObjectName(u"widget_878")
        self.widget_878.setMinimumSize(QSize(450, 0))
        self.widget_878.setStyleSheet(u"")
        self.verticalLayout_244 = QVBoxLayout(self.widget_878)
        self.verticalLayout_244.setSpacing(0)
        self.verticalLayout_244.setObjectName(u"verticalLayout_244")
        self.widget_commande = QWidget(self.widget_878)
        self.widget_commande.setObjectName(u"widget_commande")
        self.widget_commande.setStyleSheet(u"QWidget{\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(245, 245, 245);\n"
"\n"
"}")
        self.horizontalLayout_283 = QHBoxLayout(self.widget_commande)
        self.horizontalLayout_283.setSpacing(0)
        self.horizontalLayout_283.setObjectName(u"horizontalLayout_283")
        self.horizontalLayout_283.setContentsMargins(14, 14, 14, 14)
        self.horizontalSpacer_311 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_283.addItem(self.horizontalSpacer_311)

        self.widget_884 = QWidget(self.widget_commande)
        self.widget_884.setObjectName(u"widget_884")
        sizePolicy.setHeightForWidth(self.widget_884.sizePolicy().hasHeightForWidth())
        self.widget_884.setSizePolicy(sizePolicy)
        self.widget_884.setMinimumSize(QSize(400, 0))
        self.widget_884.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_487 = QVBoxLayout(self.widget_884)
        self.verticalLayout_487.setObjectName(u"verticalLayout_487")
        self.verticalLayout_487.setContentsMargins(14, 14, 14, 0)
        self.widget_885 = QWidget(self.widget_884)
        self.widget_885.setObjectName(u"widget_885")
        self.verticalLayout_243 = QVBoxLayout(self.widget_885)
        self.verticalLayout_243.setObjectName(u"verticalLayout_243")
        self.widget_482 = QWidget(self.widget_885)
        self.widget_482.setObjectName(u"widget_482")
        self.horizontalLayout_309 = QHBoxLayout(self.widget_482)
        self.horizontalLayout_309.setObjectName(u"horizontalLayout_309")
        self.horizontalLayout_309.setContentsMargins(0, 0, 0, 0)
        self.pushButton_279 = QPushButton(self.widget_482)
        self.pushButton_279.setObjectName(u"pushButton_279")
        self.pushButton_279.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_279.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(36, 38, 140);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:10px;\n"
"padding-right:20px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"\n"
"}")
        icon19 = QIcon()
        icon19.addFile(u":/assets/icons/insert-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_279.setIcon(icon19)
        self.pushButton_279.setCheckable(True)

        self.horizontalLayout_309.addWidget(self.pushButton_279)

        self.horizontalSpacer_605 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_309.addItem(self.horizontalSpacer_605)

        self.label_168 = QLabel(self.widget_482)
        self.label_168.setObjectName(u"label_168")
        self.label_168.setFont(font5)

        self.horizontalLayout_309.addWidget(self.label_168)

        self.horizontalSpacer_314 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_309.addItem(self.horizontalSpacer_314)

        self.label_167 = QLabel(self.widget_482)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setFont(font5)

        self.horizontalLayout_309.addWidget(self.label_167)


        self.verticalLayout_243.addWidget(self.widget_482)

        self.widget_889 = QWidget(self.widget_885)
        self.widget_889.setObjectName(u"widget_889")
        self.verticalLayout_491 = QVBoxLayout(self.widget_889)
        self.verticalLayout_491.setObjectName(u"verticalLayout_491")
        self.label_302 = QLabel(self.widget_889)
        self.label_302.setObjectName(u"label_302")
        self.label_302.setAlignment(Qt.AlignCenter)

        self.verticalLayout_491.addWidget(self.label_302)

        self.plainText_commande = QPlainTextEdit(self.widget_889)
        self.plainText_commande.setObjectName(u"plainText_commande")
        self.plainText_commande.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:0px")

        self.verticalLayout_491.addWidget(self.plainText_commande)


        self.verticalLayout_243.addWidget(self.widget_889)

        self.horizontalSpacer_603 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_243.addItem(self.horizontalSpacer_603)

        self.widget_888 = QWidget(self.widget_885)
        self.widget_888.setObjectName(u"widget_888")
        self.horizontalLayout_307 = QHBoxLayout(self.widget_888)
        self.horizontalLayout_307.setObjectName(u"horizontalLayout_307")
        self.label_301 = QLabel(self.widget_888)
        self.label_301.setObjectName(u"label_301")
        self.label_301.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_307.addWidget(self.label_301)

        self.lineEdit_142 = QLineEdit(self.widget_888)
        self.lineEdit_142.setObjectName(u"lineEdit_142")
        self.lineEdit_142.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_142.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"}")

        self.horizontalLayout_307.addWidget(self.lineEdit_142)


        self.verticalLayout_243.addWidget(self.widget_888)

        self.horizontalSpacer_602 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_243.addItem(self.horizontalSpacer_602)

        self.widget_887 = QWidget(self.widget_885)
        self.widget_887.setObjectName(u"widget_887")
        self.horizontalLayout_306 = QHBoxLayout(self.widget_887)
        self.horizontalLayout_306.setObjectName(u"horizontalLayout_306")
        self.label_300 = QLabel(self.widget_887)
        self.label_300.setObjectName(u"label_300")
        self.label_300.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_306.addWidget(self.label_300)

        self.lineEdit_141 = QLineEdit(self.widget_887)
        self.lineEdit_141.setObjectName(u"lineEdit_141")
        self.lineEdit_141.setMinimumSize(QSize(31, 0))
        self.lineEdit_141.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_141.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"}")

        self.horizontalLayout_306.addWidget(self.lineEdit_141)


        self.verticalLayout_243.addWidget(self.widget_887)

        self.horizontalSpacer_599 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_243.addItem(self.horizontalSpacer_599)

        self.verticalSpacer_92 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_243.addItem(self.verticalSpacer_92)


        self.verticalLayout_487.addWidget(self.widget_885)

        self.widget_852 = QWidget(self.widget_884)
        self.widget_852.setObjectName(u"widget_852")
        self.horizontalLayout_541 = QHBoxLayout(self.widget_852)
        self.horizontalLayout_541.setObjectName(u"horizontalLayout_541")

        self.verticalLayout_487.addWidget(self.widget_852)

        self.widget_891 = QWidget(self.widget_884)
        self.widget_891.setObjectName(u"widget_891")
        self.horizontalLayout_308 = QHBoxLayout(self.widget_891)
        self.horizontalLayout_308.setObjectName(u"horizontalLayout_308")
        self.horizontalSpacer_312 = QSpacerItem(77, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_308.addItem(self.horizontalSpacer_312)

        self.pushButton_272 = QPushButton(self.widget_891)
        self.pushButton_272.setObjectName(u"pushButton_272")
        self.pushButton_272.setMinimumSize(QSize(200, 0))
        self.pushButton_272.setStyleSheet(u"\n"
"QPushButton{\n"
"\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:2px;\n"
"padding-left:82px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"font: 700 10pt \"Segoe UI\";\n"
"}")
        self.pushButton_272.setCheckable(True)

        self.horizontalLayout_308.addWidget(self.pushButton_272)

        self.horizontalSpacer_313 = QSpacerItem(77, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_308.addItem(self.horizontalSpacer_313)


        self.verticalLayout_487.addWidget(self.widget_891)


        self.horizontalLayout_283.addWidget(self.widget_884)

        self.horizontalSpacer_315 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_283.addItem(self.horizontalSpacer_315)

        self.widget_882 = QWidget(self.widget_commande)
        self.widget_882.setObjectName(u"widget_882")
        self.widget_882.setMinimumSize(QSize(400, 0))
        self.widget_882.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_245 = QVBoxLayout(self.widget_882)
        self.verticalLayout_245.setObjectName(u"verticalLayout_245")
        self.verticalLayout_245.setContentsMargins(14, 14, 14, 0)
        self.tableWidget_commande = QTableWidget(self.widget_882)
        if (self.tableWidget_commande.columnCount() < 6):
            self.tableWidget_commande.setColumnCount(6)
        font12 = QFont()
        font12.setPointSize(9)
        font12.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font12);
        self.tableWidget_commande.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font12);
        self.tableWidget_commande.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font12);
        self.tableWidget_commande.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font12);
        self.tableWidget_commande.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font12);
        self.tableWidget_commande.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font3);
        self.tableWidget_commande.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget_commande.setObjectName(u"tableWidget_commande")
        font13 = QFont()
        font13.setPointSize(6)
        self.tableWidget_commande.setFont(font13)
        self.tableWidget_commande.setStyleSheet(u"\n"
"background-color: rgb(245, 245, 245);\n"
"color: rgb(39, 39, 39);")
        self.tableWidget_commande.horizontalHeader().setMinimumSectionSize(60)
        self.tableWidget_commande.verticalHeader().setMinimumSectionSize(24)

        self.verticalLayout_245.addWidget(self.tableWidget_commande)

        self.verticalSpacer_91 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_245.addItem(self.verticalSpacer_91)

        self.widget_883 = QWidget(self.widget_882)
        self.widget_883.setObjectName(u"widget_883")
        self.horizontalLayout_305 = QHBoxLayout(self.widget_883)
        self.horizontalLayout_305.setObjectName(u"horizontalLayout_305")
        self.pushButton_271 = QPushButton(self.widget_883)
        self.pushButton_271.setObjectName(u"pushButton_271")
        self.pushButton_271.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_271.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 137, 126);\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"	font: 700 10pt \"Segoe UI\";\n"
"}")
        self.pushButton_271.setCheckable(True)

        self.horizontalLayout_305.addWidget(self.pushButton_271)

        self.horizontalSpacer_597 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_305.addItem(self.horizontalSpacer_597)

        self.pushButton_263 = QPushButton(self.widget_883)
        self.pushButton_263.setObjectName(u"pushButton_263")
        self.pushButton_263.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_263.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(222, 255, 222);\n"
"	color: rgb(98, 98, 98);\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"	font: 700 10pt \"Segoe UI\";\n"
"}")
        self.pushButton_263.setCheckable(True)

        self.horizontalLayout_305.addWidget(self.pushButton_263)

        self.horizontalSpacer_310 = QSpacerItem(78, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_305.addItem(self.horizontalSpacer_310)


        self.verticalLayout_245.addWidget(self.widget_883)


        self.horizontalLayout_283.addWidget(self.widget_882)

        self.horizontalSpacer_316 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_283.addItem(self.horizontalSpacer_316)


        self.verticalLayout_244.addWidget(self.widget_commande)

        self.widget_840 = QWidget(self.widget_878)
        self.widget_840.setObjectName(u"widget_840")
        self.widget_840.setStyleSheet(u"background-color: rgb(236, 234, 234);\n"
"border-bottom-left-radius:7px;\n"
"border-bottom-right-radius:7px;")
        self.horizontalLayout_284 = QHBoxLayout(self.widget_840)
        self.horizontalLayout_284.setObjectName(u"horizontalLayout_284")
        self.widget_483 = QWidget(self.widget_840)
        self.widget_483.setObjectName(u"widget_483")
        self.widget_483.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_311 = QHBoxLayout(self.widget_483)
        self.horizontalLayout_311.setSpacing(0)
        self.horizontalLayout_311.setObjectName(u"horizontalLayout_311")
        self.horizontalLayout_311.setContentsMargins(10, 5, 5, 5)
        self.label_171 = QLabel(self.widget_483)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_311.addWidget(self.label_171)

        self.label_291 = QLabel(self.widget_483)
        self.label_291.setObjectName(u"label_291")
        self.label_291.setMinimumSize(QSize(150, 0))
        self.label_291.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_291.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_311.addWidget(self.label_291)


        self.horizontalLayout_284.addWidget(self.widget_483)

        self.horizontalSpacer_573 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_284.addItem(self.horizontalSpacer_573)

        self.pushButton_262 = QPushButton(self.widget_840)
        self.pushButton_262.setObjectName(u"pushButton_262")
        self.pushButton_262.setMinimumSize(QSize(150, 0))
        self.pushButton_262.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_262.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(36, 38, 140);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:10px;\n"
"padding-right:40px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"\n"
"}")
        self.pushButton_262.setIcon(icon16)
        self.pushButton_262.setCheckable(True)

        self.horizontalLayout_284.addWidget(self.pushButton_262)


        self.verticalLayout_244.addWidget(self.widget_840)


        self.verticalLayout_246.addWidget(self.widget_878)

        self.widget_892 = QWidget(self.widget_876)
        self.widget_892.setObjectName(u"widget_892")
        self.widget_892.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_493 = QVBoxLayout(self.widget_892)
        self.verticalLayout_493.setSpacing(0)
        self.verticalLayout_493.setObjectName(u"verticalLayout_493")
        self.verticalLayout_493.setContentsMargins(0, 0, 0, 0)
        self.widget_893 = QWidget(self.widget_892)
        self.widget_893.setObjectName(u"widget_893")
        self.horizontalLayout_562 = QHBoxLayout(self.widget_893)
        self.horizontalLayout_562.setSpacing(0)
        self.horizontalLayout_562.setObjectName(u"horizontalLayout_562")
        self.horizontalLayout_562.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_493.addWidget(self.widget_893)


        self.verticalLayout_246.addWidget(self.widget_892)


        self.gridLayout_14.addWidget(self.widget_876, 2, 0, 1, 1)

        self.verticalSpacer_93 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_93, 3, 0, 1, 1)

        self.widget_902 = QWidget(self.scrollAreaWidgetContents_12)
        self.widget_902.setObjectName(u"widget_902")
        self.widget_902.setMaximumSize(QSize(16777215, 16777215))
        self.widget_902.setStyleSheet(u"background-color: rgb(245, 245, 245);")
        self.horizontalLayout_313 = QHBoxLayout(self.widget_902)
        self.horizontalLayout_313.setObjectName(u"horizontalLayout_313")
        self.horizontalSpacer_284 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_313.addItem(self.horizontalSpacer_284)

        self.widget3 = QWidget(self.widget_902)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setMaximumSize(QSize(925, 16777215))
        self.horizontalLayout_312 = QHBoxLayout(self.widget3)
        self.horizontalLayout_312.setObjectName(u"horizontalLayout_312")
        self.Equipement_widget_110 = QWidget(self.widget3)
        self.Equipement_widget_110.setObjectName(u"Equipement_widget_110")
        self.Equipement_widget_110.setMinimumSize(QSize(200, 0))
        self.Equipement_widget_110.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(236, 234, 234);\n"
"border-radius:10px;\n"
"color: white;\n"
"}\n"
"")
        self.verticalLayout_270 = QVBoxLayout(self.Equipement_widget_110)
        self.verticalLayout_270.setSpacing(20)
        self.verticalLayout_270.setObjectName(u"verticalLayout_270")
        self.verticalLayout_270.setContentsMargins(2, 2, 20, 2)
        self.label_173 = QLabel(self.Equipement_widget_110)
        self.label_173.setObjectName(u"label_173")
        self.label_173.setFont(font7)
        self.label_173.setStyleSheet(u"color: rgb(36, 38, 140);")
        self.label_173.setWordWrap(True)

        self.verticalLayout_270.addWidget(self.label_173)

        self.pushButton_274 = QPushButton(self.Equipement_widget_110)
        self.pushButton_274.setObjectName(u"pushButton_274")
        sizePolicy2.setHeightForWidth(self.pushButton_274.sizePolicy().hasHeightForWidth())
        self.pushButton_274.setSizePolicy(sizePolicy2)
        self.pushButton_274.setFont(font5)
        self.pushButton_274.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_274.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(200, 131, 131);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:4px;\n"
"padding-right:4px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(226, 148, 148);\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(226, 148, 148);\n"
"}\n"
"")
        self.pushButton_274.setIcon(icon18)
        self.pushButton_274.setIconSize(QSize(24, 24))
        self.pushButton_274.setCheckable(True)

        self.verticalLayout_270.addWidget(self.pushButton_274)


        self.horizontalLayout_312.addWidget(self.Equipement_widget_110)

        self.horizontalSpacer_613 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_312.addItem(self.horizontalSpacer_613)

        self.Equipement_widget_111 = QWidget(self.widget3)
        self.Equipement_widget_111.setObjectName(u"Equipement_widget_111")
        self.Equipement_widget_111.setMinimumSize(QSize(200, 0))
        self.Equipement_widget_111.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(236, 234, 234);\n"
"border-radius:10px;\n"
"color: white;\n"
"}\n"
"")
        self.verticalLayout_267 = QVBoxLayout(self.Equipement_widget_111)
        self.verticalLayout_267.setSpacing(20)
        self.verticalLayout_267.setObjectName(u"verticalLayout_267")
        self.verticalLayout_267.setContentsMargins(20, 4, 2, 2)
        self.label_172 = QLabel(self.Equipement_widget_111)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setFont(font7)
        self.label_172.setLayoutDirection(Qt.LeftToRight)
        self.label_172.setStyleSheet(u"color: rgb(36, 38, 140);")
        self.label_172.setWordWrap(True)

        self.verticalLayout_267.addWidget(self.label_172)

        self.pushButton_275 = QPushButton(self.Equipement_widget_111)
        self.pushButton_275.setObjectName(u"pushButton_275")
        sizePolicy2.setHeightForWidth(self.pushButton_275.sizePolicy().hasHeightForWidth())
        self.pushButton_275.setSizePolicy(sizePolicy2)
        self.pushButton_275.setFont(font5)
        self.pushButton_275.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_275.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(165, 214, 167);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:10px;\n"
"padding-right:20px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(177, 229, 179);\n"
"}\n"
"QPushButton:checked{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(177, 229, 179);\n"
"}\n"
"")
        self.pushButton_275.setIcon(icon9)
        self.pushButton_275.setIconSize(QSize(24, 24))
        self.pushButton_275.setCheckable(True)

        self.verticalLayout_267.addWidget(self.pushButton_275)


        self.horizontalLayout_312.addWidget(self.Equipement_widget_111)


        self.horizontalLayout_313.addWidget(self.widget3)

        self.horizontalSpacer_317 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_313.addItem(self.horizontalSpacer_317)


        self.gridLayout_14.addWidget(self.widget_902, 4, 0, 1, 1)

        self.scrollArea_12.setWidget(self.scrollAreaWidgetContents_12)

        self.gridLayout_12.addWidget(self.scrollArea_12, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.autre_newBandeCommande_page)
        self.autre_newDevis_page = QWidget()
        self.autre_newDevis_page.setObjectName(u"autre_newDevis_page")
        self.gridLayout_11 = QGridLayout(self.autre_newDevis_page)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.scrollArea_14 = QScrollArea(self.autre_newDevis_page)
        self.scrollArea_14.setObjectName(u"scrollArea_14")
        self.scrollArea_14.setWidgetResizable(True)
        self.scrollAreaWidgetContents_14 = QWidget()
        self.scrollAreaWidgetContents_14.setObjectName(u"scrollAreaWidgetContents_14")
        self.scrollAreaWidgetContents_14.setGeometry(QRect(0, 0, 878, 1215))
        self.gridLayout_21 = QGridLayout(self.scrollAreaWidgetContents_14)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.widget_488 = QWidget(self.scrollAreaWidgetContents_14)
        self.widget_488.setObjectName(u"widget_488")
        self.horizontalLayout_323 = QHBoxLayout(self.widget_488)
        self.horizontalLayout_323.setObjectName(u"horizontalLayout_323")
        self.label_181 = QLabel(self.widget_488)
        self.label_181.setObjectName(u"label_181")
        self.label_181.setFont(font4)
        self.label_181.setStyleSheet(u"QLabel{\n"
"background-color: rgb(36, 38, 140);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:10px;\n"
"padding-right:40px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"}")

        self.horizontalLayout_323.addWidget(self.label_181)

        self.horizontalSpacer_339 = QSpacerItem(364, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_323.addItem(self.horizontalSpacer_339)


        self.gridLayout_21.addWidget(self.widget_488, 0, 0, 1, 1)

        self.widget_854 = QWidget(self.scrollAreaWidgetContents_14)
        self.widget_854.setObjectName(u"widget_854")
        self.verticalLayout_469 = QVBoxLayout(self.widget_854)
        self.verticalLayout_469.setObjectName(u"verticalLayout_469")
        self.widget_855 = QWidget(self.widget_854)
        self.widget_855.setObjectName(u"widget_855")
        self.horizontalLayout_538 = QHBoxLayout(self.widget_855)
        self.horizontalLayout_538.setObjectName(u"horizontalLayout_538")
        self.horizontalLayout_538.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_105 = QWidget(self.widget_855)
        self.Equipement_widget_105.setObjectName(u"Equipement_widget_105")
        self.Equipement_widget_105.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_539 = QHBoxLayout(self.Equipement_widget_105)
        self.horizontalLayout_539.setObjectName(u"horizontalLayout_539")
        self.label_290 = QLabel(self.Equipement_widget_105)
        self.label_290.setObjectName(u"label_290")
        self.label_290.setPixmap(QPixmap(u":/assets/icons/schedule-30.png"))

        self.horizontalLayout_539.addWidget(self.label_290, 0, Qt.AlignLeft)

        self.pushButton_261 = QPushButton(self.Equipement_widget_105)
        self.pushButton_261.setObjectName(u"pushButton_261")
        sizePolicy2.setHeightForWidth(self.pushButton_261.sizePolicy().hasHeightForWidth())
        self.pushButton_261.setSizePolicy(sizePolicy2)
        self.pushButton_261.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_261.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(245, 245, 245);\n"
"}\n"
"")
        self.pushButton_261.setIconSize(QSize(24, 24))
        self.pushButton_261.setCheckable(False)

        self.horizontalLayout_539.addWidget(self.pushButton_261)


        self.horizontalLayout_538.addWidget(self.Equipement_widget_105)

        self.horizontalSpacer_577 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_538.addItem(self.horizontalSpacer_577)


        self.verticalLayout_469.addWidget(self.widget_855)

        self.widget_856 = QWidget(self.widget_854)
        self.widget_856.setObjectName(u"widget_856")
        self.widget_856.setMinimumSize(QSize(0, 0))
        self.widget_856.setStyleSheet(u"color: rgb(92, 124, 250);\n"
"background-color: rgb(245, 245, 245);")
        self.horizontalLayout_540 = QHBoxLayout(self.widget_856)
        self.horizontalLayout_540.setObjectName(u"horizontalLayout_540")
        self.horizontalSpacer_578 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_540.addItem(self.horizontalSpacer_578)

        self.widget_857 = QWidget(self.widget_856)
        self.widget_857.setObjectName(u"widget_857")
        sizePolicy.setHeightForWidth(self.widget_857.sizePolicy().hasHeightForWidth())
        self.widget_857.setSizePolicy(sizePolicy)
        self.widget_857.setMinimumSize(QSize(400, 206))
        self.widget_857.setStyleSheet(u"background-color: rgb(236, 234, 234);\n"
"border-bottom-left-radius:7px;\n"
"border-bottom-right-radius:7px;")
        self.verticalLayout_470 = QVBoxLayout(self.widget_857)
        self.verticalLayout_470.setObjectName(u"verticalLayout_470")
        self.label_182 = QLabel(self.widget_857)
        self.label_182.setObjectName(u"label_182")
        self.label_182.setStyleSheet(u"color: rgb(52, 56, 199);\n"
"\n"
"font: 8pt \"Microsoft JhengHei UI\";")

        self.verticalLayout_470.addWidget(self.label_182)

        self.label_183 = QLabel(self.widget_857)
        self.label_183.setObjectName(u"label_183")
        self.label_183.setWordWrap(True)

        self.verticalLayout_470.addWidget(self.label_183)

        self.widget_858 = QWidget(self.widget_857)
        self.widget_858.setObjectName(u"widget_858")
        self.widget_858.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(211, 211, 211);\n"
"border-radius:0px;")
        self.verticalLayout_471 = QVBoxLayout(self.widget_858)
        self.verticalLayout_471.setObjectName(u"verticalLayout_471")
        self.verticalLayout_471.setContentsMargins(15, 15, 15, 15)
        self.checkBox_58 = QCheckBox(self.widget_858)
        self.checkBox_58.setObjectName(u"checkBox_58")
        self.checkBox_58.setChecked(True)
        self.checkBox_58.setAutoExclusive(True)

        self.verticalLayout_471.addWidget(self.checkBox_58)

        self.checkBox_59 = QCheckBox(self.widget_858)
        self.checkBox_59.setObjectName(u"checkBox_59")
        self.checkBox_59.setAutoExclusive(True)

        self.verticalLayout_471.addWidget(self.checkBox_59)


        self.verticalLayout_470.addWidget(self.widget_858)

        self.widget_859 = QWidget(self.widget_857)
        self.widget_859.setObjectName(u"widget_859")
        self.horizontalLayout_543 = QHBoxLayout(self.widget_859)
        self.horizontalLayout_543.setObjectName(u"horizontalLayout_543")
        self.dateEdit_17 = QDateEdit(self.widget_859)
        self.dateEdit_17.setObjectName(u"dateEdit_17")
        self.dateEdit_17.setFont(font11)
        self.dateEdit_17.setStyleSheet(u"color: rgb(58, 58, 58);\n"
"font: 12pt \"Segoe UI\";\n"
"background-color: rgb(245, 245, 245);\n"
"border-top-left-radius:7px;\n"
"border-bottom-left-radius:7px;")
        self.dateEdit_17.setAlignment(Qt.AlignCenter)
        self.dateEdit_17.setDateTime(QDateTime(QDate(2024, 10, 31), QTime(16, 0, 0)))
        self.dateEdit_17.setCalendarPopup(True)

        self.horizontalLayout_543.addWidget(self.dateEdit_17)


        self.verticalLayout_470.addWidget(self.widget_859)


        self.horizontalLayout_540.addWidget(self.widget_857)

        self.horizontalSpacer_579 = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_540.addItem(self.horizontalSpacer_579)

        self.widget_860 = QWidget(self.widget_856)
        self.widget_860.setObjectName(u"widget_860")
        self.widget_860.setMinimumSize(QSize(400, 206))
        self.widget_860.setMaximumSize(QSize(300, 16777215))
        self.widget_860.setStyleSheet(u"background-color: rgb(236, 234, 234);\n"
"border-bottom-left-radius:7px;\n"
"border-bottom-right-radius:7px;")
        self.verticalLayout_472 = QVBoxLayout(self.widget_860)
        self.verticalLayout_472.setObjectName(u"verticalLayout_472")
        self.label_184 = QLabel(self.widget_860)
        self.label_184.setObjectName(u"label_184")

        self.verticalLayout_472.addWidget(self.label_184)

        self.widget_861 = QWidget(self.widget_860)
        self.widget_861.setObjectName(u"widget_861")
        self.widget_861.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(211, 211, 211);\n"
"border-radius:0px;")
        self.verticalLayout_473 = QVBoxLayout(self.widget_861)
        self.verticalLayout_473.setObjectName(u"verticalLayout_473")
        self.verticalLayout_473.setContentsMargins(15, 15, 15, 15)
        self.checkBox_60 = QCheckBox(self.widget_861)
        self.checkBox_60.setObjectName(u"checkBox_60")
        self.checkBox_60.setChecked(True)
        self.checkBox_60.setAutoExclusive(True)

        self.verticalLayout_473.addWidget(self.checkBox_60)

        self.checkBox_61 = QCheckBox(self.widget_861)
        self.checkBox_61.setObjectName(u"checkBox_61")
        self.checkBox_61.setAutoExclusive(True)

        self.verticalLayout_473.addWidget(self.checkBox_61)


        self.verticalLayout_472.addWidget(self.widget_861)

        self.widget_862 = QWidget(self.widget_860)
        self.widget_862.setObjectName(u"widget_862")
        self.widget_862.setStyleSheet(u"color: rgb(58, 58, 58);\n"
"font: 12pt \"Segoe UI\";\n"
"background-color: rgb(245, 245, 245);\n"
"border-top-left-radius:7px;\n"
"border-bottom-left-radius:7px;")
        self.horizontalLayout_544 = QHBoxLayout(self.widget_862)
        self.horizontalLayout_544.setObjectName(u"horizontalLayout_544")
        self.label_293 = QLabel(self.widget_862)
        self.label_293.setObjectName(u"label_293")
        self.label_293.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_544.addWidget(self.label_293)

        self.timeEdit_3 = QTimeEdit(self.widget_862)
        self.timeEdit_3.setObjectName(u"timeEdit_3")
        self.timeEdit_3.setAlignment(Qt.AlignCenter)
        self.timeEdit_3.setCalendarPopup(False)

        self.horizontalLayout_544.addWidget(self.timeEdit_3)


        self.verticalLayout_472.addWidget(self.widget_862)

        self.widget_863 = QWidget(self.widget_860)
        self.widget_863.setObjectName(u"widget_863")
        self.horizontalLayout_324 = QHBoxLayout(self.widget_863)
        self.horizontalLayout_324.setObjectName(u"horizontalLayout_324")
        self.horizontalLayout_324.setContentsMargins(0, -1, -1, -1)
        self.widget_warning_3 = QWidget(self.widget_863)
        self.widget_warning_3.setObjectName(u"widget_warning_3")
        self.widget_warning_3.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_325 = QHBoxLayout(self.widget_warning_3)
        self.horizontalLayout_325.setSpacing(0)
        self.horizontalLayout_325.setObjectName(u"horizontalLayout_325")
        self.horizontalLayout_325.setContentsMargins(10, 5, 5, 5)
        self.label_205 = QLabel(self.widget_warning_3)
        self.label_205.setObjectName(u"label_205")
        self.label_205.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_325.addWidget(self.label_205)

        self.label_294 = QLabel(self.widget_warning_3)
        self.label_294.setObjectName(u"label_294")
        self.label_294.setMinimumSize(QSize(150, 0))
        self.label_294.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_294.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_325.addWidget(self.label_294)


        self.horizontalLayout_324.addWidget(self.widget_warning_3)

        self.horizontalSpacer_580 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_324.addItem(self.horizontalSpacer_580)

        self.pushButton_266 = QPushButton(self.widget_863)
        self.pushButton_266.setObjectName(u"pushButton_266")
        self.pushButton_266.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_266.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(36, 38, 140);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:10px;\n"
"padding-right:40px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"\n"
"}")
        self.pushButton_266.setIcon(icon16)
        self.pushButton_266.setCheckable(True)

        self.horizontalLayout_324.addWidget(self.pushButton_266)


        self.verticalLayout_472.addWidget(self.widget_863)


        self.horizontalLayout_540.addWidget(self.widget_860)

        self.horizontalSpacer_581 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_540.addItem(self.horizontalSpacer_581)


        self.verticalLayout_469.addWidget(self.widget_856)


        self.gridLayout_21.addWidget(self.widget_854, 1, 0, 1, 1)

        self.widget_904 = QWidget(self.scrollAreaWidgetContents_14)
        self.widget_904.setObjectName(u"widget_904")
        self.verticalLayout_282 = QVBoxLayout(self.widget_904)
        self.verticalLayout_282.setObjectName(u"verticalLayout_282")
        self.widget_905 = QWidget(self.widget_904)
        self.widget_905.setObjectName(u"widget_905")
        self.widget_905.setStyleSheet(u"")
        self.horizontalLayout_559 = QHBoxLayout(self.widget_905)
        self.horizontalLayout_559.setObjectName(u"horizontalLayout_559")
        self.horizontalLayout_559.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_114 = QWidget(self.widget_905)
        self.Equipement_widget_114.setObjectName(u"Equipement_widget_114")
        self.Equipement_widget_114.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_560 = QHBoxLayout(self.Equipement_widget_114)
        self.horizontalLayout_560.setObjectName(u"horizontalLayout_560")
        self.label_299 = QLabel(self.Equipement_widget_114)
        self.label_299.setObjectName(u"label_299")
        self.label_299.setPixmap(QPixmap(u":/assets/icons/order-30.png"))

        self.horizontalLayout_560.addWidget(self.label_299, 0, Qt.AlignLeft)

        self.pushButton_281 = QPushButton(self.Equipement_widget_114)
        self.pushButton_281.setObjectName(u"pushButton_281")
        sizePolicy2.setHeightForWidth(self.pushButton_281.sizePolicy().hasHeightForWidth())
        self.pushButton_281.setSizePolicy(sizePolicy2)
        self.pushButton_281.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_281.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_281.setIcon(icon9)
        self.pushButton_281.setIconSize(QSize(24, 24))
        self.pushButton_281.setCheckable(True)

        self.horizontalLayout_560.addWidget(self.pushButton_281)


        self.horizontalLayout_559.addWidget(self.Equipement_widget_114)

        self.horizontalSpacer_596 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_559.addItem(self.horizontalSpacer_596)


        self.verticalLayout_282.addWidget(self.widget_905)

        self.widget_906 = QWidget(self.widget_904)
        self.widget_906.setObjectName(u"widget_906")
        self.widget_906.setMinimumSize(QSize(450, 0))
        self.widget_906.setStyleSheet(u"")
        self.verticalLayout_283 = QVBoxLayout(self.widget_906)
        self.verticalLayout_283.setSpacing(0)
        self.verticalLayout_283.setObjectName(u"verticalLayout_283")
        self.widget_commande_3 = QWidget(self.widget_906)
        self.widget_commande_3.setObjectName(u"widget_commande_3")
        self.widget_commande_3.setStyleSheet(u"QWidget{\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(245, 245, 245);\n"
"\n"
"}")
        self.horizontalLayout_326 = QHBoxLayout(self.widget_commande_3)
        self.horizontalLayout_326.setSpacing(0)
        self.horizontalLayout_326.setObjectName(u"horizontalLayout_326")
        self.horizontalLayout_326.setContentsMargins(14, 14, 14, 14)
        self.horizontalSpacer_340 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_326.addItem(self.horizontalSpacer_340)

        self.widget_907 = QWidget(self.widget_commande_3)
        self.widget_907.setObjectName(u"widget_907")
        sizePolicy.setHeightForWidth(self.widget_907.sizePolicy().hasHeightForWidth())
        self.widget_907.setSizePolicy(sizePolicy)
        self.widget_907.setMinimumSize(QSize(400, 0))
        self.widget_907.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_489 = QVBoxLayout(self.widget_907)
        self.verticalLayout_489.setObjectName(u"verticalLayout_489")
        self.verticalLayout_489.setContentsMargins(14, 14, 14, 0)
        self.widget_908 = QWidget(self.widget_907)
        self.widget_908.setObjectName(u"widget_908")
        self.verticalLayout_284 = QVBoxLayout(self.widget_908)
        self.verticalLayout_284.setObjectName(u"verticalLayout_284")
        self.widget_489 = QWidget(self.widget_908)
        self.widget_489.setObjectName(u"widget_489")
        self.horizontalLayout_327 = QHBoxLayout(self.widget_489)
        self.horizontalLayout_327.setObjectName(u"horizontalLayout_327")
        self.horizontalLayout_327.setContentsMargins(0, 0, 0, 0)
        self.pushButton_282 = QPushButton(self.widget_489)
        self.pushButton_282.setObjectName(u"pushButton_282")
        self.pushButton_282.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_282.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(36, 38, 140);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:10px;\n"
"padding-right:20px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"\n"
"}")
        self.pushButton_282.setIcon(icon19)
        self.pushButton_282.setCheckable(True)

        self.horizontalLayout_327.addWidget(self.pushButton_282)

        self.horizontalSpacer_608 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_327.addItem(self.horizontalSpacer_608)

        self.label_209 = QLabel(self.widget_489)
        self.label_209.setObjectName(u"label_209")
        self.label_209.setFont(font5)

        self.horizontalLayout_327.addWidget(self.label_209)

        self.horizontalSpacer_341 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_327.addItem(self.horizontalSpacer_341)

        self.label_210 = QLabel(self.widget_489)
        self.label_210.setObjectName(u"label_210")
        self.label_210.setFont(font5)

        self.horizontalLayout_327.addWidget(self.label_210)


        self.verticalLayout_284.addWidget(self.widget_489)

        self.widget_909 = QWidget(self.widget_908)
        self.widget_909.setObjectName(u"widget_909")
        self.verticalLayout_495 = QVBoxLayout(self.widget_909)
        self.verticalLayout_495.setObjectName(u"verticalLayout_495")
        self.label_306 = QLabel(self.widget_909)
        self.label_306.setObjectName(u"label_306")
        self.label_306.setAlignment(Qt.AlignCenter)

        self.verticalLayout_495.addWidget(self.label_306)

        self.plainText_devis = QPlainTextEdit(self.widget_909)
        self.plainText_devis.setObjectName(u"plainText_devis")
        self.plainText_devis.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:0px")

        self.verticalLayout_495.addWidget(self.plainText_devis)


        self.verticalLayout_284.addWidget(self.widget_909)

        self.horizontalSpacer_609 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_284.addItem(self.horizontalSpacer_609)

        self.widget_910 = QWidget(self.widget_908)
        self.widget_910.setObjectName(u"widget_910")
        self.horizontalLayout_328 = QHBoxLayout(self.widget_910)
        self.horizontalLayout_328.setObjectName(u"horizontalLayout_328")
        self.label_307 = QLabel(self.widget_910)
        self.label_307.setObjectName(u"label_307")
        self.label_307.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_328.addWidget(self.label_307)

        self.lineEdit_145 = QLineEdit(self.widget_910)
        self.lineEdit_145.setObjectName(u"lineEdit_145")
        self.lineEdit_145.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_145.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"}")

        self.horizontalLayout_328.addWidget(self.lineEdit_145)


        self.verticalLayout_284.addWidget(self.widget_910)

        self.horizontalSpacer_610 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_284.addItem(self.horizontalSpacer_610)

        self.widget_911 = QWidget(self.widget_908)
        self.widget_911.setObjectName(u"widget_911")
        self.horizontalLayout_329 = QHBoxLayout(self.widget_911)
        self.horizontalLayout_329.setObjectName(u"horizontalLayout_329")
        self.label_308 = QLabel(self.widget_911)
        self.label_308.setObjectName(u"label_308")
        self.label_308.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_329.addWidget(self.label_308)

        self.lineEdit_146 = QLineEdit(self.widget_911)
        self.lineEdit_146.setObjectName(u"lineEdit_146")
        self.lineEdit_146.setMinimumSize(QSize(31, 0))
        self.lineEdit_146.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_146.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"}")

        self.horizontalLayout_329.addWidget(self.lineEdit_146)


        self.verticalLayout_284.addWidget(self.widget_911)

        self.horizontalSpacer_601 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_284.addItem(self.horizontalSpacer_601)

        self.verticalSpacer_105 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_284.addItem(self.verticalSpacer_105)


        self.verticalLayout_489.addWidget(self.widget_908)

        self.widget_864 = QWidget(self.widget_907)
        self.widget_864.setObjectName(u"widget_864")
        self.horizontalLayout_545 = QHBoxLayout(self.widget_864)
        self.horizontalLayout_545.setObjectName(u"horizontalLayout_545")

        self.verticalLayout_489.addWidget(self.widget_864)

        self.widget_912 = QWidget(self.widget_907)
        self.widget_912.setObjectName(u"widget_912")
        self.horizontalLayout_330 = QHBoxLayout(self.widget_912)
        self.horizontalLayout_330.setObjectName(u"horizontalLayout_330")
        self.horizontalSpacer_342 = QSpacerItem(77, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_330.addItem(self.horizontalSpacer_342)

        self.pushButton_283 = QPushButton(self.widget_912)
        self.pushButton_283.setObjectName(u"pushButton_283")
        self.pushButton_283.setMinimumSize(QSize(200, 0))
        self.pushButton_283.setStyleSheet(u"\n"
"QPushButton{\n"
"\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:2px;\n"
"padding-left:82px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"font: 700 10pt \"Segoe UI\";\n"
"}")
        self.pushButton_283.setCheckable(True)

        self.horizontalLayout_330.addWidget(self.pushButton_283)

        self.horizontalSpacer_343 = QSpacerItem(77, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_330.addItem(self.horizontalSpacer_343)


        self.verticalLayout_489.addWidget(self.widget_912)


        self.horizontalLayout_326.addWidget(self.widget_907)

        self.horizontalSpacer_344 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_326.addItem(self.horizontalSpacer_344)

        self.widget_913 = QWidget(self.widget_commande_3)
        self.widget_913.setObjectName(u"widget_913")
        self.widget_913.setMinimumSize(QSize(400, 0))
        self.widget_913.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_285 = QVBoxLayout(self.widget_913)
        self.verticalLayout_285.setObjectName(u"verticalLayout_285")
        self.verticalLayout_285.setContentsMargins(14, 14, 14, 0)
        self.tableWidget_commande_3 = QTableWidget(self.widget_913)
        if (self.tableWidget_commande_3.columnCount() < 6):
            self.tableWidget_commande_3.setColumnCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font12);
        self.tableWidget_commande_3.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font12);
        self.tableWidget_commande_3.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font12);
        self.tableWidget_commande_3.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font12);
        self.tableWidget_commande_3.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font12);
        self.tableWidget_commande_3.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font3);
        self.tableWidget_commande_3.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        self.tableWidget_commande_3.setObjectName(u"tableWidget_commande_3")
        self.tableWidget_commande_3.setFont(font13)
        self.tableWidget_commande_3.setStyleSheet(u"\n"
"background-color: rgb(245, 245, 245);\n"
"color: rgb(39, 39, 39);")
        self.tableWidget_commande_3.horizontalHeader().setMinimumSectionSize(60)
        self.tableWidget_commande_3.verticalHeader().setMinimumSectionSize(24)

        self.verticalLayout_285.addWidget(self.tableWidget_commande_3)

        self.verticalSpacer_106 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_285.addItem(self.verticalSpacer_106)

        self.widget_914 = QWidget(self.widget_913)
        self.widget_914.setObjectName(u"widget_914")
        self.horizontalLayout_331 = QHBoxLayout(self.widget_914)
        self.horizontalLayout_331.setObjectName(u"horizontalLayout_331")
        self.pushButton_284 = QPushButton(self.widget_914)
        self.pushButton_284.setObjectName(u"pushButton_284")
        self.pushButton_284.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_284.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 137, 126);\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"	font: 700 10pt \"Segoe UI\";\n"
"}")
        self.pushButton_284.setCheckable(True)

        self.horizontalLayout_331.addWidget(self.pushButton_284)

        self.horizontalSpacer_611 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_331.addItem(self.horizontalSpacer_611)

        self.pushButton_267 = QPushButton(self.widget_914)
        self.pushButton_267.setObjectName(u"pushButton_267")
        self.pushButton_267.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_267.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(222, 255, 222);\n"
"	color: rgb(98, 98, 98);\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"	font: 700 10pt \"Segoe UI\";\n"
"}")
        self.pushButton_267.setCheckable(True)

        self.horizontalLayout_331.addWidget(self.pushButton_267)

        self.horizontalSpacer_345 = QSpacerItem(78, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_331.addItem(self.horizontalSpacer_345)


        self.verticalLayout_285.addWidget(self.widget_914)


        self.horizontalLayout_326.addWidget(self.widget_913)

        self.horizontalSpacer_346 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_326.addItem(self.horizontalSpacer_346)


        self.verticalLayout_283.addWidget(self.widget_commande_3)

        self.widget_865 = QWidget(self.widget_906)
        self.widget_865.setObjectName(u"widget_865")
        self.widget_865.setStyleSheet(u"background-color: rgb(236, 234, 234);\n"
"border-bottom-left-radius:7px;\n"
"border-bottom-right-radius:7px;")
        self.horizontalLayout_332 = QHBoxLayout(self.widget_865)
        self.horizontalLayout_332.setObjectName(u"horizontalLayout_332")
        self.widget_490 = QWidget(self.widget_865)
        self.widget_490.setObjectName(u"widget_490")
        self.widget_490.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_333 = QHBoxLayout(self.widget_490)
        self.horizontalLayout_333.setSpacing(0)
        self.horizontalLayout_333.setObjectName(u"horizontalLayout_333")
        self.horizontalLayout_333.setContentsMargins(10, 5, 5, 5)
        self.label_211 = QLabel(self.widget_490)
        self.label_211.setObjectName(u"label_211")
        self.label_211.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_333.addWidget(self.label_211)

        self.label_295 = QLabel(self.widget_490)
        self.label_295.setObjectName(u"label_295")
        self.label_295.setMinimumSize(QSize(150, 0))
        self.label_295.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_295.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_333.addWidget(self.label_295)


        self.horizontalLayout_332.addWidget(self.widget_490)

        self.horizontalSpacer_582 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_332.addItem(self.horizontalSpacer_582)

        self.pushButton_268 = QPushButton(self.widget_865)
        self.pushButton_268.setObjectName(u"pushButton_268")
        self.pushButton_268.setMinimumSize(QSize(150, 0))
        self.pushButton_268.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_268.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(36, 38, 140);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:10px;\n"
"padding-right:40px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"\n"
"}")
        self.pushButton_268.setIcon(icon16)
        self.pushButton_268.setCheckable(True)

        self.horizontalLayout_332.addWidget(self.pushButton_268)


        self.verticalLayout_283.addWidget(self.widget_865)


        self.verticalLayout_282.addWidget(self.widget_906)

        self.widget_915 = QWidget(self.widget_904)
        self.widget_915.setObjectName(u"widget_915")
        self.widget_915.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_496 = QVBoxLayout(self.widget_915)
        self.verticalLayout_496.setSpacing(0)
        self.verticalLayout_496.setObjectName(u"verticalLayout_496")
        self.verticalLayout_496.setContentsMargins(0, 0, 0, 0)
        self.widget_916 = QWidget(self.widget_915)
        self.widget_916.setObjectName(u"widget_916")
        self.horizontalLayout_564 = QHBoxLayout(self.widget_916)
        self.horizontalLayout_564.setSpacing(0)
        self.horizontalLayout_564.setObjectName(u"horizontalLayout_564")
        self.horizontalLayout_564.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_496.addWidget(self.widget_916)


        self.verticalLayout_282.addWidget(self.widget_915)


        self.gridLayout_21.addWidget(self.widget_904, 2, 0, 1, 1)

        self.verticalSpacer_107 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_21.addItem(self.verticalSpacer_107, 3, 0, 1, 1)

        self.widget_917 = QWidget(self.scrollAreaWidgetContents_14)
        self.widget_917.setObjectName(u"widget_917")
        self.widget_917.setMaximumSize(QSize(16777215, 16777215))
        self.widget_917.setStyleSheet(u"background-color: rgb(245, 245, 245);")
        self.horizontalLayout_334 = QHBoxLayout(self.widget_917)
        self.horizontalLayout_334.setObjectName(u"horizontalLayout_334")
        self.horizontalSpacer_347 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_334.addItem(self.horizontalSpacer_347)

        self.widget_491 = QWidget(self.widget_917)
        self.widget_491.setObjectName(u"widget_491")
        self.widget_491.setMaximumSize(QSize(925, 16777215))
        self.horizontalLayout_335 = QHBoxLayout(self.widget_491)
        self.horizontalLayout_335.setObjectName(u"horizontalLayout_335")
        self.Equipement_widget_115 = QWidget(self.widget_491)
        self.Equipement_widget_115.setObjectName(u"Equipement_widget_115")
        self.Equipement_widget_115.setMinimumSize(QSize(200, 0))
        self.Equipement_widget_115.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(236, 234, 234);\n"
"border-radius:10px;\n"
"color: white;\n"
"}\n"
"")
        self.verticalLayout_286 = QVBoxLayout(self.Equipement_widget_115)
        self.verticalLayout_286.setSpacing(20)
        self.verticalLayout_286.setObjectName(u"verticalLayout_286")
        self.verticalLayout_286.setContentsMargins(2, 2, 20, 2)
        self.label_212 = QLabel(self.Equipement_widget_115)
        self.label_212.setObjectName(u"label_212")
        self.label_212.setFont(font7)
        self.label_212.setStyleSheet(u"color: rgb(36, 38, 140);")
        self.label_212.setWordWrap(True)

        self.verticalLayout_286.addWidget(self.label_212)

        self.pushButton_285 = QPushButton(self.Equipement_widget_115)
        self.pushButton_285.setObjectName(u"pushButton_285")
        sizePolicy2.setHeightForWidth(self.pushButton_285.sizePolicy().hasHeightForWidth())
        self.pushButton_285.setSizePolicy(sizePolicy2)
        self.pushButton_285.setFont(font5)
        self.pushButton_285.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_285.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(200, 131, 131);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:4px;\n"
"padding-right:4px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(226, 148, 148);\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(226, 148, 148);\n"
"}\n"
"")
        self.pushButton_285.setIcon(icon18)
        self.pushButton_285.setIconSize(QSize(24, 24))
        self.pushButton_285.setCheckable(True)

        self.verticalLayout_286.addWidget(self.pushButton_285)


        self.horizontalLayout_335.addWidget(self.Equipement_widget_115)

        self.horizontalSpacer_615 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_335.addItem(self.horizontalSpacer_615)

        self.Equipement_widget_116 = QWidget(self.widget_491)
        self.Equipement_widget_116.setObjectName(u"Equipement_widget_116")
        self.Equipement_widget_116.setMinimumSize(QSize(200, 0))
        self.Equipement_widget_116.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(236, 234, 234);\n"
"border-radius:10px;\n"
"color: white;\n"
"}\n"
"")
        self.verticalLayout_287 = QVBoxLayout(self.Equipement_widget_116)
        self.verticalLayout_287.setSpacing(20)
        self.verticalLayout_287.setObjectName(u"verticalLayout_287")
        self.verticalLayout_287.setContentsMargins(20, 4, 2, 2)
        self.label_213 = QLabel(self.Equipement_widget_116)
        self.label_213.setObjectName(u"label_213")
        self.label_213.setFont(font7)
        self.label_213.setLayoutDirection(Qt.LeftToRight)
        self.label_213.setStyleSheet(u"color: rgb(36, 38, 140);")
        self.label_213.setWordWrap(True)

        self.verticalLayout_287.addWidget(self.label_213)

        self.pushButton_286 = QPushButton(self.Equipement_widget_116)
        self.pushButton_286.setObjectName(u"pushButton_286")
        sizePolicy2.setHeightForWidth(self.pushButton_286.sizePolicy().hasHeightForWidth())
        self.pushButton_286.setSizePolicy(sizePolicy2)
        self.pushButton_286.setFont(font5)
        self.pushButton_286.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_286.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(165, 214, 167);\n"
"color: rgb(239, 239, 239);\n"
"padding-left:10px;\n"
"padding-right:20px;\n"
"padding-top:4px;\n"
"padding-bottom:4px;\n"
"border-radius:7px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(177, 229, 179);\n"
"}\n"
"QPushButton:checked{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(177, 229, 179);\n"
"}\n"
"")
        self.pushButton_286.setIcon(icon9)
        self.pushButton_286.setIconSize(QSize(24, 24))
        self.pushButton_286.setCheckable(True)

        self.verticalLayout_287.addWidget(self.pushButton_286)


        self.horizontalLayout_335.addWidget(self.Equipement_widget_116)


        self.horizontalLayout_334.addWidget(self.widget_491)

        self.horizontalSpacer_348 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_334.addItem(self.horizontalSpacer_348)


        self.gridLayout_21.addWidget(self.widget_917, 4, 0, 1, 1)

        self.scrollArea_14.setWidget(self.scrollAreaWidgetContents_14)

        self.gridLayout_11.addWidget(self.scrollArea_14, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.autre_newDevis_page)
        self.nv_dossier_autre_page = QWidget()
        self.nv_dossier_autre_page.setObjectName(u"nv_dossier_autre_page")
        self.gridLayout_4 = QGridLayout(self.nv_dossier_autre_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.scrollArea_4 = QScrollArea(self.nv_dossier_autre_page)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 634, 2296))
        self.verticalLayout_146 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_146.setObjectName(u"verticalLayout_146")
        self.widget_237 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_237.setObjectName(u"widget_237")
        self.horizontalLayout_67 = QHBoxLayout(self.widget_237)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.label_86 = QLabel(self.widget_237)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setFont(font4)

        self.horizontalLayout_67.addWidget(self.label_86)

        self.horizontalSpacer_252 = QSpacerItem(355, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_67.addItem(self.horizontalSpacer_252)

        self.label_87 = QLabel(self.widget_237)
        self.label_87.setObjectName(u"label_87")

        self.horizontalLayout_67.addWidget(self.label_87)

        self.horizontalSpacer_251 = QSpacerItem(355, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_67.addItem(self.horizontalSpacer_251)

        self.label_135 = QLabel(self.widget_237)
        self.label_135.setObjectName(u"label_135")

        self.horizontalLayout_67.addWidget(self.label_135)


        self.verticalLayout_146.addWidget(self.widget_237)

        self.widget_238 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_238.setObjectName(u"widget_238")
        self.verticalLayout_147 = QVBoxLayout(self.widget_238)
        self.verticalLayout_147.setObjectName(u"verticalLayout_147")
        self.widget_239 = QWidget(self.widget_238)
        self.widget_239.setObjectName(u"widget_239")
        self.horizontalLayout_160 = QHBoxLayout(self.widget_239)
        self.horizontalLayout_160.setObjectName(u"horizontalLayout_160")
        self.horizontalLayout_160.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_31 = QWidget(self.widget_239)
        self.Equipement_widget_31.setObjectName(u"Equipement_widget_31")
        self.Equipement_widget_31.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_161 = QHBoxLayout(self.Equipement_widget_31)
        self.horizontalLayout_161.setObjectName(u"horizontalLayout_161")
        self.label_88 = QLabel(self.Equipement_widget_31)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setPixmap(QPixmap(u":/assets/icons/employee-30.png"))

        self.horizontalLayout_161.addWidget(self.label_88, 0, Qt.AlignLeft)

        self.pushButton_105 = QPushButton(self.Equipement_widget_31)
        self.pushButton_105.setObjectName(u"pushButton_105")
        sizePolicy2.setHeightForWidth(self.pushButton_105.sizePolicy().hasHeightForWidth())
        self.pushButton_105.setSizePolicy(sizePolicy2)
        self.pushButton_105.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_105.setStyleSheet(u"")
        self.pushButton_105.setIconSize(QSize(24, 24))
        self.pushButton_105.setCheckable(True)

        self.horizontalLayout_161.addWidget(self.pushButton_105)


        self.horizontalLayout_160.addWidget(self.Equipement_widget_31)

        self.horizontalSpacer_149 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_160.addItem(self.horizontalSpacer_149)


        self.verticalLayout_147.addWidget(self.widget_239)

        self.widget_240 = QWidget(self.widget_238)
        self.widget_240.setObjectName(u"widget_240")
        self.widget_240.setMinimumSize(QSize(0, 0))
        self.widget_240.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.verticalLayout_315 = QVBoxLayout(self.widget_240)
        self.verticalLayout_315.setObjectName(u"verticalLayout_315")
        self.horizontalLayout_162 = QHBoxLayout()
        self.horizontalLayout_162.setObjectName(u"horizontalLayout_162")
        self.horizontalSpacer_150 = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_162.addItem(self.horizontalSpacer_150)

        self.widget_241 = QWidget(self.widget_240)
        self.widget_241.setObjectName(u"widget_241")
        sizePolicy.setHeightForWidth(self.widget_241.sizePolicy().hasHeightForWidth())
        self.widget_241.setSizePolicy(sizePolicy)
        self.widget_241.setMinimumSize(QSize(0, 0))
        self.verticalLayout_148 = QVBoxLayout(self.widget_241)
        self.verticalLayout_148.setObjectName(u"verticalLayout_148")
        self.textEdit_36 = QTextEdit(self.widget_241)
        self.textEdit_36.setObjectName(u"textEdit_36")
        sizePolicy4.setHeightForWidth(self.textEdit_36.sizePolicy().hasHeightForWidth())
        self.textEdit_36.setSizePolicy(sizePolicy4)
        self.textEdit_36.setMinimumSize(QSize(0, 0))
        self.textEdit_36.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_148.addWidget(self.textEdit_36)

        self.textEdit_37 = QTextEdit(self.widget_241)
        self.textEdit_37.setObjectName(u"textEdit_37")
        sizePolicy4.setHeightForWidth(self.textEdit_37.sizePolicy().hasHeightForWidth())
        self.textEdit_37.setSizePolicy(sizePolicy4)
        self.textEdit_37.setMinimumSize(QSize(0, 0))
        self.textEdit_37.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_148.addWidget(self.textEdit_37)

        self.widget_242 = QWidget(self.widget_241)
        self.widget_242.setObjectName(u"widget_242")
        self.verticalLayout_149 = QVBoxLayout(self.widget_242)
        self.verticalLayout_149.setObjectName(u"verticalLayout_149")
        self.checkBox_13 = QCheckBox(self.widget_242)
        self.checkBox_13.setObjectName(u"checkBox_13")
        self.checkBox_13.setChecked(True)

        self.verticalLayout_149.addWidget(self.checkBox_13)

        self.checkBox_14 = QCheckBox(self.widget_242)
        self.checkBox_14.setObjectName(u"checkBox_14")

        self.verticalLayout_149.addWidget(self.checkBox_14)


        self.verticalLayout_148.addWidget(self.widget_242)

        self.widget_243 = QWidget(self.widget_241)
        self.widget_243.setObjectName(u"widget_243")
        self.horizontalLayout_163 = QHBoxLayout(self.widget_243)
        self.horizontalLayout_163.setObjectName(u"horizontalLayout_163")
        self.dateEdit_6 = QDateEdit(self.widget_243)
        self.dateEdit_6.setObjectName(u"dateEdit_6")
        self.dateEdit_6.setDateTime(QDateTime(QDate(2024, 10, 31), QTime(17, 0, 0)))
        self.dateEdit_6.setCalendarPopup(True)

        self.horizontalLayout_163.addWidget(self.dateEdit_6)

        self.horizontalSpacer_151 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_163.addItem(self.horizontalSpacer_151)


        self.verticalLayout_148.addWidget(self.widget_243)


        self.horizontalLayout_162.addWidget(self.widget_241)

        self.horizontalSpacer_152 = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_162.addItem(self.horizontalSpacer_152)

        self.horizontalSpacer_153 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_162.addItem(self.horizontalSpacer_153)

        self.widget_244 = QWidget(self.widget_240)
        self.widget_244.setObjectName(u"widget_244")
        self.widget_244.setMinimumSize(QSize(0, 0))
        self.widget_244.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_150 = QVBoxLayout(self.widget_244)
        self.verticalLayout_150.setObjectName(u"verticalLayout_150")
        self.textEdit_38 = QTextEdit(self.widget_244)
        self.textEdit_38.setObjectName(u"textEdit_38")
        sizePolicy4.setHeightForWidth(self.textEdit_38.sizePolicy().hasHeightForWidth())
        self.textEdit_38.setSizePolicy(sizePolicy4)
        self.textEdit_38.setMinimumSize(QSize(0, 0))
        self.textEdit_38.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_150.addWidget(self.textEdit_38)

        self.widget_245 = QWidget(self.widget_244)
        self.widget_245.setObjectName(u"widget_245")
        self.verticalLayout_151 = QVBoxLayout(self.widget_245)
        self.verticalLayout_151.setObjectName(u"verticalLayout_151")
        self.checkBox_15 = QCheckBox(self.widget_245)
        self.checkBox_15.setObjectName(u"checkBox_15")
        self.checkBox_15.setChecked(True)

        self.verticalLayout_151.addWidget(self.checkBox_15)

        self.checkBox_16 = QCheckBox(self.widget_245)
        self.checkBox_16.setObjectName(u"checkBox_16")

        self.verticalLayout_151.addWidget(self.checkBox_16)


        self.verticalLayout_150.addWidget(self.widget_245)

        self.widget_246 = QWidget(self.widget_244)
        self.widget_246.setObjectName(u"widget_246")
        self.horizontalLayout_164 = QHBoxLayout(self.widget_246)
        self.horizontalLayout_164.setObjectName(u"horizontalLayout_164")
        self.label_89 = QLabel(self.widget_246)
        self.label_89.setObjectName(u"label_89")

        self.horizontalLayout_164.addWidget(self.label_89)

        self.lineEdit_38 = QLineEdit(self.widget_246)
        self.lineEdit_38.setObjectName(u"lineEdit_38")
        self.lineEdit_38.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_164.addWidget(self.lineEdit_38)


        self.verticalLayout_150.addWidget(self.widget_246)


        self.horizontalLayout_162.addWidget(self.widget_244)

        self.horizontalSpacer_155 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_162.addItem(self.horizontalSpacer_155)


        self.verticalLayout_315.addLayout(self.horizontalLayout_162)

        self.widget_247 = QWidget(self.widget_240)
        self.widget_247.setObjectName(u"widget_247")
        self.horizontalLayout_165 = QHBoxLayout(self.widget_247)
        self.horizontalLayout_165.setObjectName(u"horizontalLayout_165")
        self.widget_warning_41 = QWidget(self.widget_247)
        self.widget_warning_41.setObjectName(u"widget_warning_41")
        self.widget_warning_41.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_424 = QHBoxLayout(self.widget_warning_41)
        self.horizontalLayout_424.setSpacing(0)
        self.horizontalLayout_424.setObjectName(u"horizontalLayout_424")
        self.horizontalLayout_424.setContentsMargins(10, 5, 5, 5)
        self.label_347 = QLabel(self.widget_warning_41)
        self.label_347.setObjectName(u"label_347")
        self.label_347.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_424.addWidget(self.label_347)

        self.label_348 = QLabel(self.widget_warning_41)
        self.label_348.setObjectName(u"label_348")
        self.label_348.setMinimumSize(QSize(150, 0))
        self.label_348.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_348.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_424.addWidget(self.label_348)


        self.horizontalLayout_165.addWidget(self.widget_warning_41)

        self.horizontalSpacer_154 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_165.addItem(self.horizontalSpacer_154)

        self.pushButton_106 = QPushButton(self.widget_247)
        self.pushButton_106.setObjectName(u"pushButton_106")
        self.pushButton_106.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_106.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_165.addWidget(self.pushButton_106)


        self.verticalLayout_315.addWidget(self.widget_247)


        self.verticalLayout_147.addWidget(self.widget_240)


        self.verticalLayout_146.addWidget(self.widget_238)

        self.widget_248 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_248.setObjectName(u"widget_248")
        self.verticalLayout_152 = QVBoxLayout(self.widget_248)
        self.verticalLayout_152.setObjectName(u"verticalLayout_152")
        self.widget_249 = QWidget(self.widget_248)
        self.widget_249.setObjectName(u"widget_249")
        self.horizontalLayout_166 = QHBoxLayout(self.widget_249)
        self.horizontalLayout_166.setObjectName(u"horizontalLayout_166")
        self.horizontalLayout_166.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_32 = QWidget(self.widget_249)
        self.Equipement_widget_32.setObjectName(u"Equipement_widget_32")
        self.Equipement_widget_32.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_167 = QHBoxLayout(self.Equipement_widget_32)
        self.horizontalLayout_167.setObjectName(u"horizontalLayout_167")
        self.label_91 = QLabel(self.Equipement_widget_32)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setPixmap(QPixmap(u":/assets/icons/employee-30.png"))

        self.horizontalLayout_167.addWidget(self.label_91, 0, Qt.AlignLeft)

        self.pushButton_107 = QPushButton(self.Equipement_widget_32)
        self.pushButton_107.setObjectName(u"pushButton_107")
        sizePolicy2.setHeightForWidth(self.pushButton_107.sizePolicy().hasHeightForWidth())
        self.pushButton_107.setSizePolicy(sizePolicy2)
        self.pushButton_107.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_107.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_107.setIcon(icon9)
        self.pushButton_107.setIconSize(QSize(24, 24))
        self.pushButton_107.setCheckable(True)

        self.horizontalLayout_167.addWidget(self.pushButton_107)


        self.horizontalLayout_166.addWidget(self.Equipement_widget_32)

        self.horizontalSpacer_156 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_166.addItem(self.horizontalSpacer_156)


        self.verticalLayout_152.addWidget(self.widget_249)

        self.widget_250 = QWidget(self.widget_248)
        self.widget_250.setObjectName(u"widget_250")
        self.widget_250.setMinimumSize(QSize(450, 0))
        self.widget_250.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.verticalLayout_316 = QVBoxLayout(self.widget_250)
        self.verticalLayout_316.setObjectName(u"verticalLayout_316")
        self.horizontalLayout_168 = QHBoxLayout()
        self.horizontalLayout_168.setObjectName(u"horizontalLayout_168")
        self.widget_251 = QWidget(self.widget_250)
        self.widget_251.setObjectName(u"widget_251")
        self.verticalLayout_153 = QVBoxLayout(self.widget_251)
        self.verticalLayout_153.setObjectName(u"verticalLayout_153")
        self.textEdit_39 = QTextEdit(self.widget_251)
        self.textEdit_39.setObjectName(u"textEdit_39")
        sizePolicy4.setHeightForWidth(self.textEdit_39.sizePolicy().hasHeightForWidth())
        self.textEdit_39.setSizePolicy(sizePolicy4)
        self.textEdit_39.setMinimumSize(QSize(0, 0))
        self.textEdit_39.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_153.addWidget(self.textEdit_39)

        self.verticalSpacer_48 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_153.addItem(self.verticalSpacer_48)


        self.horizontalLayout_168.addWidget(self.widget_251)

        self.widget_252 = QWidget(self.widget_250)
        self.widget_252.setObjectName(u"widget_252")
        self.widget_252.setMinimumSize(QSize(400, 0))
        self.verticalLayout_154 = QVBoxLayout(self.widget_252)
        self.verticalLayout_154.setObjectName(u"verticalLayout_154")
        self.verticalLayout_154.setContentsMargins(4, 4, 4, 4)
        self.textEdit_40 = QTextEdit(self.widget_252)
        self.textEdit_40.setObjectName(u"textEdit_40")
        sizePolicy4.setHeightForWidth(self.textEdit_40.sizePolicy().hasHeightForWidth())
        self.textEdit_40.setSizePolicy(sizePolicy4)
        self.textEdit_40.setMinimumSize(QSize(0, 0))
        self.textEdit_40.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_154.addWidget(self.textEdit_40)

        self.textEdit_41 = QTextEdit(self.widget_252)
        self.textEdit_41.setObjectName(u"textEdit_41")
        self.textEdit_41.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_154.addWidget(self.textEdit_41)

        self.widget_253 = QWidget(self.widget_252)
        self.widget_253.setObjectName(u"widget_253")
        self.horizontalLayout_169 = QHBoxLayout(self.widget_253)
        self.horizontalLayout_169.setObjectName(u"horizontalLayout_169")
        self.horizontalSpacer_157 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_169.addItem(self.horizontalSpacer_157)

        self.pushButton_108 = QPushButton(self.widget_253)
        self.pushButton_108.setObjectName(u"pushButton_108")
        self.pushButton_108.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_108.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_169.addWidget(self.pushButton_108)


        self.verticalLayout_154.addWidget(self.widget_253)


        self.horizontalLayout_168.addWidget(self.widget_252)

        self.horizontalSpacer_158 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_168.addItem(self.horizontalSpacer_158)


        self.verticalLayout_316.addLayout(self.horizontalLayout_168)

        self.widget_498 = QWidget(self.widget_250)
        self.widget_498.setObjectName(u"widget_498")
        self.horizontalLayout_425 = QHBoxLayout(self.widget_498)
        self.horizontalLayout_425.setObjectName(u"horizontalLayout_425")
        self.widget_warning_42 = QWidget(self.widget_498)
        self.widget_warning_42.setObjectName(u"widget_warning_42")
        self.widget_warning_42.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_380 = QHBoxLayout(self.widget_warning_42)
        self.horizontalLayout_380.setSpacing(0)
        self.horizontalLayout_380.setObjectName(u"horizontalLayout_380")
        self.horizontalLayout_380.setContentsMargins(10, 5, 5, 5)
        self.label_274 = QLabel(self.widget_warning_42)
        self.label_274.setObjectName(u"label_274")
        self.label_274.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_380.addWidget(self.label_274)

        self.label_349 = QLabel(self.widget_warning_42)
        self.label_349.setObjectName(u"label_349")
        self.label_349.setMinimumSize(QSize(150, 0))
        self.label_349.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_349.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_380.addWidget(self.label_349)


        self.horizontalLayout_425.addWidget(self.widget_warning_42)

        self.horizontalSpacer_289 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_425.addItem(self.horizontalSpacer_289)

        self.pushButton_178 = QPushButton(self.widget_498)
        self.pushButton_178.setObjectName(u"pushButton_178")
        self.pushButton_178.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_178.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_425.addWidget(self.pushButton_178)


        self.verticalLayout_316.addWidget(self.widget_498)


        self.verticalLayout_152.addWidget(self.widget_250)


        self.verticalLayout_146.addWidget(self.widget_248)

        self.widget_254 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_254.setObjectName(u"widget_254")
        self.verticalLayout_155 = QVBoxLayout(self.widget_254)
        self.verticalLayout_155.setObjectName(u"verticalLayout_155")
        self.widget_255 = QWidget(self.widget_254)
        self.widget_255.setObjectName(u"widget_255")
        self.horizontalLayout_170 = QHBoxLayout(self.widget_255)
        self.horizontalLayout_170.setObjectName(u"horizontalLayout_170")
        self.horizontalLayout_170.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_33 = QWidget(self.widget_255)
        self.Equipement_widget_33.setObjectName(u"Equipement_widget_33")
        self.Equipement_widget_33.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_171 = QHBoxLayout(self.Equipement_widget_33)
        self.horizontalLayout_171.setObjectName(u"horizontalLayout_171")
        self.label_92 = QLabel(self.Equipement_widget_33)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setPixmap(QPixmap(u":/assets/icons/employee-30.png"))

        self.horizontalLayout_171.addWidget(self.label_92, 0, Qt.AlignLeft)

        self.pushButton_109 = QPushButton(self.Equipement_widget_33)
        self.pushButton_109.setObjectName(u"pushButton_109")
        sizePolicy2.setHeightForWidth(self.pushButton_109.sizePolicy().hasHeightForWidth())
        self.pushButton_109.setSizePolicy(sizePolicy2)
        self.pushButton_109.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_109.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_109.setIcon(icon9)
        self.pushButton_109.setIconSize(QSize(24, 24))
        self.pushButton_109.setCheckable(True)

        self.horizontalLayout_171.addWidget(self.pushButton_109)


        self.horizontalLayout_170.addWidget(self.Equipement_widget_33)

        self.horizontalSpacer_159 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_170.addItem(self.horizontalSpacer_159)


        self.verticalLayout_155.addWidget(self.widget_255)

        self.widget_256 = QWidget(self.widget_254)
        self.widget_256.setObjectName(u"widget_256")
        self.widget_256.setMinimumSize(QSize(450, 0))
        self.widget_256.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.verticalLayout_317 = QVBoxLayout(self.widget_256)
        self.verticalLayout_317.setObjectName(u"verticalLayout_317")
        self.horizontalLayout_172 = QHBoxLayout()
        self.horizontalLayout_172.setObjectName(u"horizontalLayout_172")
        self.widget_257 = QWidget(self.widget_256)
        self.widget_257.setObjectName(u"widget_257")
        sizePolicy.setHeightForWidth(self.widget_257.sizePolicy().hasHeightForWidth())
        self.widget_257.setSizePolicy(sizePolicy)
        self.widget_257.setMinimumSize(QSize(0, 0))
        self.verticalLayout_156 = QVBoxLayout(self.widget_257)
        self.verticalLayout_156.setSpacing(10)
        self.verticalLayout_156.setObjectName(u"verticalLayout_156")
        self.verticalLayout_156.setContentsMargins(4, 4, 4, 4)
        self.textEdit_42 = QTextEdit(self.widget_257)
        self.textEdit_42.setObjectName(u"textEdit_42")
        sizePolicy4.setHeightForWidth(self.textEdit_42.sizePolicy().hasHeightForWidth())
        self.textEdit_42.setSizePolicy(sizePolicy4)
        self.textEdit_42.setMinimumSize(QSize(0, 0))
        self.textEdit_42.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_156.addWidget(self.textEdit_42)

        self.comboBox_15 = QComboBox(self.widget_257)
        self.comboBox_15.setObjectName(u"comboBox_15")
        self.comboBox_15.setMinimumSize(QSize(400, 0))
        self.comboBox_15.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_156.addWidget(self.comboBox_15)

        self.widget_258 = QWidget(self.widget_257)
        self.widget_258.setObjectName(u"widget_258")
        self.horizontalLayout_173 = QHBoxLayout(self.widget_258)
        self.horizontalLayout_173.setObjectName(u"horizontalLayout_173")
        self.horizontalSpacer_160 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_173.addItem(self.horizontalSpacer_160)

        self.pushButton_110 = QPushButton(self.widget_258)
        self.pushButton_110.setObjectName(u"pushButton_110")
        self.pushButton_110.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_173.addWidget(self.pushButton_110)


        self.verticalLayout_156.addWidget(self.widget_258)

        self.verticalSpacer_49 = QSpacerItem(20, 148, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_156.addItem(self.verticalSpacer_49)


        self.horizontalLayout_172.addWidget(self.widget_257)

        self.horizontalSpacer_161 = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_172.addItem(self.horizontalSpacer_161)

        self.widget_259 = QWidget(self.widget_256)
        self.widget_259.setObjectName(u"widget_259")
        self.widget_259.setMinimumSize(QSize(400, 0))
        self.verticalLayout_157 = QVBoxLayout(self.widget_259)
        self.verticalLayout_157.setObjectName(u"verticalLayout_157")
        self.verticalLayout_157.setContentsMargins(4, 4, 4, 4)
        self.listView_10 = QListView(self.widget_259)
        self.listView_10.setObjectName(u"listView_10")
        self.listView_10.setMinimumSize(QSize(500, 0))
        self.listView_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_157.addWidget(self.listView_10)

        self.widget_260 = QWidget(self.widget_259)
        self.widget_260.setObjectName(u"widget_260")
        self.horizontalLayout_174 = QHBoxLayout(self.widget_260)
        self.horizontalLayout_174.setObjectName(u"horizontalLayout_174")
        self.pushButton_111 = QPushButton(self.widget_260)
        self.pushButton_111.setObjectName(u"pushButton_111")
        self.pushButton_111.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_111.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_174.addWidget(self.pushButton_111)

        self.horizontalSpacer_162 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_174.addItem(self.horizontalSpacer_162)


        self.verticalLayout_157.addWidget(self.widget_260)


        self.horizontalLayout_172.addWidget(self.widget_259)

        self.horizontalSpacer_163 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_172.addItem(self.horizontalSpacer_163)


        self.verticalLayout_317.addLayout(self.horizontalLayout_172)

        self.widget_499 = QWidget(self.widget_256)
        self.widget_499.setObjectName(u"widget_499")
        self.horizontalLayout_426 = QHBoxLayout(self.widget_499)
        self.horizontalLayout_426.setObjectName(u"horizontalLayout_426")
        self.widget_warning_43 = QWidget(self.widget_499)
        self.widget_warning_43.setObjectName(u"widget_warning_43")
        self.widget_warning_43.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_381 = QHBoxLayout(self.widget_warning_43)
        self.horizontalLayout_381.setSpacing(0)
        self.horizontalLayout_381.setObjectName(u"horizontalLayout_381")
        self.horizontalLayout_381.setContentsMargins(10, 5, 5, 5)
        self.label_275 = QLabel(self.widget_warning_43)
        self.label_275.setObjectName(u"label_275")
        self.label_275.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_381.addWidget(self.label_275)

        self.label_350 = QLabel(self.widget_warning_43)
        self.label_350.setObjectName(u"label_350")
        self.label_350.setMinimumSize(QSize(150, 0))
        self.label_350.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_350.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_381.addWidget(self.label_350)


        self.horizontalLayout_426.addWidget(self.widget_warning_43)

        self.horizontalSpacer_350 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_426.addItem(self.horizontalSpacer_350)

        self.pushButton_181 = QPushButton(self.widget_499)
        self.pushButton_181.setObjectName(u"pushButton_181")
        self.pushButton_181.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_181.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_426.addWidget(self.pushButton_181)


        self.verticalLayout_317.addWidget(self.widget_499)


        self.verticalLayout_155.addWidget(self.widget_256)


        self.verticalLayout_146.addWidget(self.widget_254)

        self.widget_261 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_261.setObjectName(u"widget_261")
        self.verticalLayout_158 = QVBoxLayout(self.widget_261)
        self.verticalLayout_158.setObjectName(u"verticalLayout_158")
        self.widget_262 = QWidget(self.widget_261)
        self.widget_262.setObjectName(u"widget_262")
        self.widget_262.setStyleSheet(u"")
        self.horizontalLayout_175 = QHBoxLayout(self.widget_262)
        self.horizontalLayout_175.setObjectName(u"horizontalLayout_175")
        self.horizontalLayout_175.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_34 = QWidget(self.widget_262)
        self.Equipement_widget_34.setObjectName(u"Equipement_widget_34")
        self.Equipement_widget_34.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_176 = QHBoxLayout(self.Equipement_widget_34)
        self.horizontalLayout_176.setObjectName(u"horizontalLayout_176")
        self.label_93 = QLabel(self.Equipement_widget_34)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setPixmap(QPixmap(u":/assets/icons/equippement-30.png"))

        self.horizontalLayout_176.addWidget(self.label_93, 0, Qt.AlignLeft)

        self.pushButton_112 = QPushButton(self.Equipement_widget_34)
        self.pushButton_112.setObjectName(u"pushButton_112")
        sizePolicy2.setHeightForWidth(self.pushButton_112.sizePolicy().hasHeightForWidth())
        self.pushButton_112.setSizePolicy(sizePolicy2)
        self.pushButton_112.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_112.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_112.setIcon(icon9)
        self.pushButton_112.setIconSize(QSize(24, 24))
        self.pushButton_112.setCheckable(True)

        self.horizontalLayout_176.addWidget(self.pushButton_112)


        self.horizontalLayout_175.addWidget(self.Equipement_widget_34)

        self.horizontalSpacer_164 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_175.addItem(self.horizontalSpacer_164)


        self.verticalLayout_158.addWidget(self.widget_262)

        self.widget_263 = QWidget(self.widget_261)
        self.widget_263.setObjectName(u"widget_263")
        self.widget_263.setMinimumSize(QSize(450, 0))
        self.widget_263.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.verticalLayout_318 = QVBoxLayout(self.widget_263)
        self.verticalLayout_318.setObjectName(u"verticalLayout_318")
        self.horizontalLayout_177 = QHBoxLayout()
        self.horizontalLayout_177.setObjectName(u"horizontalLayout_177")
        self.widget_264 = QWidget(self.widget_263)
        self.widget_264.setObjectName(u"widget_264")
        sizePolicy.setHeightForWidth(self.widget_264.sizePolicy().hasHeightForWidth())
        self.widget_264.setSizePolicy(sizePolicy)
        self.widget_264.setMinimumSize(QSize(0, 0))
        self.verticalLayout_159 = QVBoxLayout(self.widget_264)
        self.verticalLayout_159.setSpacing(10)
        self.verticalLayout_159.setObjectName(u"verticalLayout_159")
        self.verticalLayout_159.setContentsMargins(4, 4, 4, 4)
        self.textEdit_43 = QTextEdit(self.widget_264)
        self.textEdit_43.setObjectName(u"textEdit_43")
        sizePolicy4.setHeightForWidth(self.textEdit_43.sizePolicy().hasHeightForWidth())
        self.textEdit_43.setSizePolicy(sizePolicy4)
        self.textEdit_43.setMinimumSize(QSize(0, 0))
        self.textEdit_43.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_159.addWidget(self.textEdit_43)

        self.comboBox_16 = QComboBox(self.widget_264)
        self.comboBox_16.setObjectName(u"comboBox_16")
        self.comboBox_16.setMinimumSize(QSize(400, 0))
        self.comboBox_16.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_159.addWidget(self.comboBox_16)

        self.widget_265 = QWidget(self.widget_264)
        self.widget_265.setObjectName(u"widget_265")
        self.horizontalLayout_178 = QHBoxLayout(self.widget_265)
        self.horizontalLayout_178.setObjectName(u"horizontalLayout_178")
        self.horizontalSpacer_165 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_178.addItem(self.horizontalSpacer_165)

        self.pushButton_113 = QPushButton(self.widget_265)
        self.pushButton_113.setObjectName(u"pushButton_113")
        self.pushButton_113.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_178.addWidget(self.pushButton_113)


        self.verticalLayout_159.addWidget(self.widget_265)

        self.verticalSpacer_50 = QSpacerItem(20, 148, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_159.addItem(self.verticalSpacer_50)


        self.horizontalLayout_177.addWidget(self.widget_264)

        self.horizontalSpacer_166 = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_177.addItem(self.horizontalSpacer_166)

        self.widget_266 = QWidget(self.widget_263)
        self.widget_266.setObjectName(u"widget_266")
        self.widget_266.setMinimumSize(QSize(400, 0))
        self.verticalLayout_160 = QVBoxLayout(self.widget_266)
        self.verticalLayout_160.setObjectName(u"verticalLayout_160")
        self.verticalLayout_160.setContentsMargins(4, 4, 4, 4)
        self.listView_11 = QListView(self.widget_266)
        self.listView_11.setObjectName(u"listView_11")
        self.listView_11.setMinimumSize(QSize(500, 0))
        self.listView_11.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_160.addWidget(self.listView_11)

        self.widget_267 = QWidget(self.widget_266)
        self.widget_267.setObjectName(u"widget_267")
        self.horizontalLayout_179 = QHBoxLayout(self.widget_267)
        self.horizontalLayout_179.setObjectName(u"horizontalLayout_179")
        self.pushButton_114 = QPushButton(self.widget_267)
        self.pushButton_114.setObjectName(u"pushButton_114")
        self.pushButton_114.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_114.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_179.addWidget(self.pushButton_114)

        self.horizontalSpacer_167 = QSpacerItem(361, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_179.addItem(self.horizontalSpacer_167)


        self.verticalLayout_160.addWidget(self.widget_267)


        self.horizontalLayout_177.addWidget(self.widget_266)

        self.horizontalSpacer_168 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_177.addItem(self.horizontalSpacer_168)


        self.verticalLayout_318.addLayout(self.horizontalLayout_177)

        self.widget_500 = QWidget(self.widget_263)
        self.widget_500.setObjectName(u"widget_500")
        self.horizontalLayout_427 = QHBoxLayout(self.widget_500)
        self.horizontalLayout_427.setObjectName(u"horizontalLayout_427")
        self.widget_warning_44 = QWidget(self.widget_500)
        self.widget_warning_44.setObjectName(u"widget_warning_44")
        self.widget_warning_44.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_383 = QHBoxLayout(self.widget_warning_44)
        self.horizontalLayout_383.setSpacing(0)
        self.horizontalLayout_383.setObjectName(u"horizontalLayout_383")
        self.horizontalLayout_383.setContentsMargins(10, 5, 5, 5)
        self.label_279 = QLabel(self.widget_warning_44)
        self.label_279.setObjectName(u"label_279")
        self.label_279.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_383.addWidget(self.label_279)

        self.label_351 = QLabel(self.widget_warning_44)
        self.label_351.setObjectName(u"label_351")
        self.label_351.setMinimumSize(QSize(150, 0))
        self.label_351.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_351.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_383.addWidget(self.label_351)


        self.horizontalLayout_427.addWidget(self.widget_warning_44)

        self.horizontalSpacer_351 = QSpacerItem(402, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_427.addItem(self.horizontalSpacer_351)

        self.pushButton_182 = QPushButton(self.widget_500)
        self.pushButton_182.setObjectName(u"pushButton_182")
        self.pushButton_182.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_182.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_427.addWidget(self.pushButton_182)


        self.verticalLayout_318.addWidget(self.widget_500)


        self.verticalLayout_158.addWidget(self.widget_263)

        self.widget_268 = QWidget(self.widget_261)
        self.widget_268.setObjectName(u"widget_268")
        self.widget_268.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_161 = QVBoxLayout(self.widget_268)
        self.verticalLayout_161.setSpacing(0)
        self.verticalLayout_161.setObjectName(u"verticalLayout_161")
        self.verticalLayout_161.setContentsMargins(0, 0, 0, 0)
        self.widget_269 = QWidget(self.widget_268)
        self.widget_269.setObjectName(u"widget_269")
        self.horizontalLayout_180 = QHBoxLayout(self.widget_269)
        self.horizontalLayout_180.setSpacing(0)
        self.horizontalLayout_180.setObjectName(u"horizontalLayout_180")
        self.horizontalLayout_180.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_161.addWidget(self.widget_269)


        self.verticalLayout_158.addWidget(self.widget_268)


        self.verticalLayout_146.addWidget(self.widget_261)

        self.widget_270 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_270.setObjectName(u"widget_270")
        self.verticalLayout_162 = QVBoxLayout(self.widget_270)
        self.verticalLayout_162.setObjectName(u"verticalLayout_162")
        self.widget_271 = QWidget(self.widget_270)
        self.widget_271.setObjectName(u"widget_271")
        self.widget_271.setStyleSheet(u"")
        self.horizontalLayout_181 = QHBoxLayout(self.widget_271)
        self.horizontalLayout_181.setObjectName(u"horizontalLayout_181")
        self.horizontalLayout_181.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_35 = QWidget(self.widget_271)
        self.Equipement_widget_35.setObjectName(u"Equipement_widget_35")
        self.Equipement_widget_35.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_182 = QHBoxLayout(self.Equipement_widget_35)
        self.horizontalLayout_182.setObjectName(u"horizontalLayout_182")
        self.label_94 = QLabel(self.Equipement_widget_35)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setPixmap(QPixmap(u":/assets/icons/equippement-30.png"))

        self.horizontalLayout_182.addWidget(self.label_94, 0, Qt.AlignLeft)

        self.pushButton_115 = QPushButton(self.Equipement_widget_35)
        self.pushButton_115.setObjectName(u"pushButton_115")
        sizePolicy2.setHeightForWidth(self.pushButton_115.sizePolicy().hasHeightForWidth())
        self.pushButton_115.setSizePolicy(sizePolicy2)
        self.pushButton_115.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_115.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_115.setIcon(icon9)
        self.pushButton_115.setIconSize(QSize(24, 24))
        self.pushButton_115.setCheckable(True)

        self.horizontalLayout_182.addWidget(self.pushButton_115)


        self.horizontalLayout_181.addWidget(self.Equipement_widget_35)

        self.horizontalSpacer_169 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_181.addItem(self.horizontalSpacer_169)


        self.verticalLayout_162.addWidget(self.widget_271)

        self.widget_272 = QWidget(self.widget_270)
        self.widget_272.setObjectName(u"widget_272")
        self.widget_272.setMinimumSize(QSize(450, 0))
        self.widget_272.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.horizontalLayout_183 = QHBoxLayout(self.widget_272)
        self.horizontalLayout_183.setObjectName(u"horizontalLayout_183")
        self.horizontalLayout_183.setContentsMargins(10, 10, 10, 10)
        self.widget_273 = QWidget(self.widget_272)
        self.widget_273.setObjectName(u"widget_273")
        sizePolicy.setHeightForWidth(self.widget_273.sizePolicy().hasHeightForWidth())
        self.widget_273.setSizePolicy(sizePolicy)
        self.widget_273.setMinimumSize(QSize(400, 0))
        self.verticalLayout_163 = QVBoxLayout(self.widget_273)
        self.verticalLayout_163.setObjectName(u"verticalLayout_163")
        self.textEdit_44 = QTextEdit(self.widget_273)
        self.textEdit_44.setObjectName(u"textEdit_44")
        sizePolicy4.setHeightForWidth(self.textEdit_44.sizePolicy().hasHeightForWidth())
        self.textEdit_44.setSizePolicy(sizePolicy4)
        self.textEdit_44.setMinimumSize(QSize(0, 0))
        self.textEdit_44.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_163.addWidget(self.textEdit_44)

        self.widget_274 = QWidget(self.widget_273)
        self.widget_274.setObjectName(u"widget_274")
        self.horizontalLayout_184 = QHBoxLayout(self.widget_274)
        self.horizontalLayout_184.setObjectName(u"horizontalLayout_184")
        self.horizontalLayout_184.setContentsMargins(10, 10, 10, 10)
        self.horizontalSpacer_170 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_184.addItem(self.horizontalSpacer_170)

        self.widget_275 = QWidget(self.widget_274)
        self.widget_275.setObjectName(u"widget_275")
        sizePolicy5.setHeightForWidth(self.widget_275.sizePolicy().hasHeightForWidth())
        self.widget_275.setSizePolicy(sizePolicy5)
        self.widget_275.setMinimumSize(QSize(300, 0))
        self.verticalLayout_164 = QVBoxLayout(self.widget_275)
        self.verticalLayout_164.setObjectName(u"verticalLayout_164")
        self.label_95 = QLabel(self.widget_275)
        self.label_95.setObjectName(u"label_95")

        self.verticalLayout_164.addWidget(self.label_95)

        self.verticalSpacer_51 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_164.addItem(self.verticalSpacer_51)

        self.comboBox_17 = QComboBox(self.widget_275)
        self.comboBox_17.setObjectName(u"comboBox_17")
        self.comboBox_17.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_164.addWidget(self.comboBox_17)


        self.horizontalLayout_184.addWidget(self.widget_275)

        self.horizontalSpacer_171 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_184.addItem(self.horizontalSpacer_171)

        self.widget_276 = QWidget(self.widget_274)
        self.widget_276.setObjectName(u"widget_276")
        self.verticalLayout_165 = QVBoxLayout(self.widget_276)
        self.verticalLayout_165.setObjectName(u"verticalLayout_165")
        self.label_96 = QLabel(self.widget_276)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setAlignment(Qt.AlignCenter)

        self.verticalLayout_165.addWidget(self.label_96)

        self.verticalSpacer_52 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_165.addItem(self.verticalSpacer_52)

        self.lineEdit_39 = QLineEdit(self.widget_276)
        self.lineEdit_39.setObjectName(u"lineEdit_39")
        self.lineEdit_39.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_165.addWidget(self.lineEdit_39)


        self.horizontalLayout_184.addWidget(self.widget_276)

        self.horizontalSpacer_172 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_184.addItem(self.horizontalSpacer_172)

        self.widget_277 = QWidget(self.widget_274)
        self.widget_277.setObjectName(u"widget_277")
        self.verticalLayout_166 = QVBoxLayout(self.widget_277)
        self.verticalLayout_166.setObjectName(u"verticalLayout_166")
        self.label_97 = QLabel(self.widget_277)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setAlignment(Qt.AlignCenter)

        self.verticalLayout_166.addWidget(self.label_97)

        self.verticalSpacer_53 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_166.addItem(self.verticalSpacer_53)

        self.lineEdit_40 = QLineEdit(self.widget_277)
        self.lineEdit_40.setObjectName(u"lineEdit_40")
        self.lineEdit_40.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_166.addWidget(self.lineEdit_40)


        self.horizontalLayout_184.addWidget(self.widget_277)

        self.horizontalSpacer_173 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_184.addItem(self.horizontalSpacer_173)

        self.widget_278 = QWidget(self.widget_274)
        self.widget_278.setObjectName(u"widget_278")
        self.verticalLayout_167 = QVBoxLayout(self.widget_278)
        self.verticalLayout_167.setObjectName(u"verticalLayout_167")
        self.label_98 = QLabel(self.widget_278)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setAlignment(Qt.AlignCenter)

        self.verticalLayout_167.addWidget(self.label_98)

        self.verticalSpacer_54 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_167.addItem(self.verticalSpacer_54)

        self.lineEdit_41 = QLineEdit(self.widget_278)
        self.lineEdit_41.setObjectName(u"lineEdit_41")
        self.lineEdit_41.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_167.addWidget(self.lineEdit_41)


        self.horizontalLayout_184.addWidget(self.widget_278)

        self.horizontalSpacer_174 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_184.addItem(self.horizontalSpacer_174)

        self.widget_279 = QWidget(self.widget_274)
        self.widget_279.setObjectName(u"widget_279")
        self.verticalLayout_168 = QVBoxLayout(self.widget_279)
        self.verticalLayout_168.setObjectName(u"verticalLayout_168")
        self.label_99 = QLabel(self.widget_279)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setAlignment(Qt.AlignCenter)

        self.verticalLayout_168.addWidget(self.label_99)

        self.verticalSpacer_55 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_168.addItem(self.verticalSpacer_55)

        self.lineEdit_42 = QLineEdit(self.widget_279)
        self.lineEdit_42.setObjectName(u"lineEdit_42")
        self.lineEdit_42.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_168.addWidget(self.lineEdit_42)


        self.horizontalLayout_184.addWidget(self.widget_279)

        self.horizontalSpacer_175 = QSpacerItem(11, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_184.addItem(self.horizontalSpacer_175)

        self.widget_280 = QWidget(self.widget_274)
        self.widget_280.setObjectName(u"widget_280")
        self.verticalLayout_169 = QVBoxLayout(self.widget_280)
        self.verticalLayout_169.setObjectName(u"verticalLayout_169")
        self.label_100 = QLabel(self.widget_280)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setLayoutDirection(Qt.LeftToRight)
        self.label_100.setAlignment(Qt.AlignCenter)

        self.verticalLayout_169.addWidget(self.label_100)

        self.verticalSpacer_56 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_169.addItem(self.verticalSpacer_56)

        self.lineEdit_43 = QLineEdit(self.widget_280)
        self.lineEdit_43.setObjectName(u"lineEdit_43")
        self.lineEdit_43.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_169.addWidget(self.lineEdit_43)


        self.horizontalLayout_184.addWidget(self.widget_280)

        self.horizontalSpacer_176 = QSpacerItem(171, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_184.addItem(self.horizontalSpacer_176)


        self.verticalLayout_163.addWidget(self.widget_274)

        self.widget_281 = QWidget(self.widget_273)
        self.widget_281.setObjectName(u"widget_281")
        self.horizontalLayout_185 = QHBoxLayout(self.widget_281)
        self.horizontalLayout_185.setObjectName(u"horizontalLayout_185")
        self.widget_warning_45 = QWidget(self.widget_281)
        self.widget_warning_45.setObjectName(u"widget_warning_45")
        self.widget_warning_45.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_428 = QHBoxLayout(self.widget_warning_45)
        self.horizontalLayout_428.setSpacing(0)
        self.horizontalLayout_428.setObjectName(u"horizontalLayout_428")
        self.horizontalLayout_428.setContentsMargins(10, 5, 5, 5)
        self.label_352 = QLabel(self.widget_warning_45)
        self.label_352.setObjectName(u"label_352")
        self.label_352.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_428.addWidget(self.label_352)

        self.label_353 = QLabel(self.widget_warning_45)
        self.label_353.setObjectName(u"label_353")
        self.label_353.setMinimumSize(QSize(150, 0))
        self.label_353.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_353.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_428.addWidget(self.label_353)


        self.horizontalLayout_185.addWidget(self.widget_warning_45)

        self.horizontalSpacer_177 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_185.addItem(self.horizontalSpacer_177)

        self.pushButton_116 = QPushButton(self.widget_281)
        self.pushButton_116.setObjectName(u"pushButton_116")
        self.pushButton_116.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_185.addWidget(self.pushButton_116)


        self.verticalLayout_163.addWidget(self.widget_281)

        self.verticalSpacer_57 = QSpacerItem(20, 148, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_163.addItem(self.verticalSpacer_57)


        self.horizontalLayout_183.addWidget(self.widget_273)


        self.verticalLayout_162.addWidget(self.widget_272)

        self.widget_282 = QWidget(self.widget_270)
        self.widget_282.setObjectName(u"widget_282")
        self.widget_282.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_170 = QVBoxLayout(self.widget_282)
        self.verticalLayout_170.setSpacing(0)
        self.verticalLayout_170.setObjectName(u"verticalLayout_170")
        self.verticalLayout_170.setContentsMargins(0, 0, 0, 0)
        self.widget_283 = QWidget(self.widget_282)
        self.widget_283.setObjectName(u"widget_283")
        self.horizontalLayout_186 = QHBoxLayout(self.widget_283)
        self.horizontalLayout_186.setSpacing(0)
        self.horizontalLayout_186.setObjectName(u"horizontalLayout_186")
        self.horizontalLayout_186.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_170.addWidget(self.widget_283)


        self.verticalLayout_162.addWidget(self.widget_282)


        self.verticalLayout_146.addWidget(self.widget_270)

        self.widget_284 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_284.setObjectName(u"widget_284")
        self.verticalLayout_171 = QVBoxLayout(self.widget_284)
        self.verticalLayout_171.setObjectName(u"verticalLayout_171")
        self.widget_285 = QWidget(self.widget_284)
        self.widget_285.setObjectName(u"widget_285")
        self.widget_285.setStyleSheet(u"")
        self.horizontalLayout_187 = QHBoxLayout(self.widget_285)
        self.horizontalLayout_187.setObjectName(u"horizontalLayout_187")
        self.horizontalLayout_187.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_36 = QWidget(self.widget_285)
        self.Equipement_widget_36.setObjectName(u"Equipement_widget_36")
        self.Equipement_widget_36.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_188 = QHBoxLayout(self.Equipement_widget_36)
        self.horizontalLayout_188.setObjectName(u"horizontalLayout_188")
        self.label_101 = QLabel(self.Equipement_widget_36)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setPixmap(QPixmap(u":/assets/icons/equippement-30.png"))

        self.horizontalLayout_188.addWidget(self.label_101, 0, Qt.AlignLeft)

        self.pushButton_117 = QPushButton(self.Equipement_widget_36)
        self.pushButton_117.setObjectName(u"pushButton_117")
        sizePolicy2.setHeightForWidth(self.pushButton_117.sizePolicy().hasHeightForWidth())
        self.pushButton_117.setSizePolicy(sizePolicy2)
        self.pushButton_117.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_117.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_117.setIcon(icon9)
        self.pushButton_117.setIconSize(QSize(24, 24))
        self.pushButton_117.setCheckable(True)

        self.horizontalLayout_188.addWidget(self.pushButton_117)


        self.horizontalLayout_187.addWidget(self.Equipement_widget_36)

        self.horizontalSpacer_178 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_187.addItem(self.horizontalSpacer_178)


        self.verticalLayout_171.addWidget(self.widget_285)

        self.widget_286 = QWidget(self.widget_284)
        self.widget_286.setObjectName(u"widget_286")
        self.widget_286.setMinimumSize(QSize(450, 0))
        self.widget_286.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.horizontalLayout_189 = QHBoxLayout(self.widget_286)
        self.horizontalLayout_189.setObjectName(u"horizontalLayout_189")
        self.horizontalSpacer_179 = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_189.addItem(self.horizontalSpacer_179)

        self.widget_287 = QWidget(self.widget_286)
        self.widget_287.setObjectName(u"widget_287")
        self.verticalLayout_172 = QVBoxLayout(self.widget_287)
        self.verticalLayout_172.setObjectName(u"verticalLayout_172")
        self.textEdit_45 = QTextEdit(self.widget_287)
        self.textEdit_45.setObjectName(u"textEdit_45")
        sizePolicy4.setHeightForWidth(self.textEdit_45.sizePolicy().hasHeightForWidth())
        self.textEdit_45.setSizePolicy(sizePolicy4)
        self.textEdit_45.setMinimumSize(QSize(0, 0))
        self.textEdit_45.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_172.addWidget(self.textEdit_45)

        self.verticalSpacer_58 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_172.addItem(self.verticalSpacer_58)

        self.widget_288 = QWidget(self.widget_287)
        self.widget_288.setObjectName(u"widget_288")
        sizePolicy5.setHeightForWidth(self.widget_288.sizePolicy().hasHeightForWidth())
        self.widget_288.setSizePolicy(sizePolicy5)
        self.widget_288.setMinimumSize(QSize(300, 0))
        self.verticalLayout_173 = QVBoxLayout(self.widget_288)
        self.verticalLayout_173.setObjectName(u"verticalLayout_173")
        self.label_102 = QLabel(self.widget_288)
        self.label_102.setObjectName(u"label_102")

        self.verticalLayout_173.addWidget(self.label_102)

        self.verticalSpacer_59 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_173.addItem(self.verticalSpacer_59)

        self.comboBox_18 = QComboBox(self.widget_288)
        self.comboBox_18.setObjectName(u"comboBox_18")
        self.comboBox_18.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_173.addWidget(self.comboBox_18)


        self.verticalLayout_172.addWidget(self.widget_288)

        self.widget_289 = QWidget(self.widget_287)
        self.widget_289.setObjectName(u"widget_289")
        self.horizontalLayout_190 = QHBoxLayout(self.widget_289)
        self.horizontalLayout_190.setObjectName(u"horizontalLayout_190")
        self.horizontalSpacer_180 = QSpacerItem(361, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_190.addItem(self.horizontalSpacer_180)

        self.pushButton_118 = QPushButton(self.widget_289)
        self.pushButton_118.setObjectName(u"pushButton_118")
        self.pushButton_118.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_118.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_190.addWidget(self.pushButton_118)


        self.verticalLayout_172.addWidget(self.widget_289)


        self.horizontalLayout_189.addWidget(self.widget_287)

        self.widget_290 = QWidget(self.widget_286)
        self.widget_290.setObjectName(u"widget_290")
        self.widget_290.setMinimumSize(QSize(0, 0))
        self.verticalLayout_174 = QVBoxLayout(self.widget_290)
        self.verticalLayout_174.setObjectName(u"verticalLayout_174")
        self.verticalLayout_174.setContentsMargins(4, 4, 4, 4)
        self.listView_12 = QListView(self.widget_290)
        self.listView_12.setObjectName(u"listView_12")
        self.listView_12.setMinimumSize(QSize(0, 0))
        self.listView_12.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_174.addWidget(self.listView_12)

        self.widget_291 = QWidget(self.widget_290)
        self.widget_291.setObjectName(u"widget_291")
        self.horizontalLayout_191 = QHBoxLayout(self.widget_291)
        self.horizontalLayout_191.setObjectName(u"horizontalLayout_191")
        self.pushButton_119 = QPushButton(self.widget_291)
        self.pushButton_119.setObjectName(u"pushButton_119")
        self.pushButton_119.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_119.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_191.addWidget(self.pushButton_119)

        self.horizontalSpacer_181 = QSpacerItem(361, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_191.addItem(self.horizontalSpacer_181)


        self.verticalLayout_174.addWidget(self.widget_291)


        self.horizontalLayout_189.addWidget(self.widget_290)

        self.horizontalSpacer_182 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_189.addItem(self.horizontalSpacer_182)

        self.widget_292 = QWidget(self.widget_286)
        self.widget_292.setObjectName(u"widget_292")
        sizePolicy.setHeightForWidth(self.widget_292.sizePolicy().hasHeightForWidth())
        self.widget_292.setSizePolicy(sizePolicy)
        self.widget_292.setMinimumSize(QSize(400, 0))
        self.verticalLayout_175 = QVBoxLayout(self.widget_292)
        self.verticalLayout_175.setObjectName(u"verticalLayout_175")
        self.widget_293 = QWidget(self.widget_292)
        self.widget_293.setObjectName(u"widget_293")
        self.horizontalLayout_192 = QHBoxLayout(self.widget_293)
        self.horizontalLayout_192.setSpacing(0)
        self.horizontalLayout_192.setObjectName(u"horizontalLayout_192")
        self.horizontalLayout_192.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_183 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_192.addItem(self.horizontalSpacer_183)

        self.horizontalSpacer_184 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_192.addItem(self.horizontalSpacer_184)

        self.widget_294 = QWidget(self.widget_293)
        self.widget_294.setObjectName(u"widget_294")
        self.verticalLayout_176 = QVBoxLayout(self.widget_294)
        self.verticalLayout_176.setObjectName(u"verticalLayout_176")
        self.label_103 = QLabel(self.widget_294)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setAlignment(Qt.AlignCenter)

        self.verticalLayout_176.addWidget(self.label_103)

        self.lineEdit_44 = QLineEdit(self.widget_294)
        self.lineEdit_44.setObjectName(u"lineEdit_44")
        self.lineEdit_44.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_176.addWidget(self.lineEdit_44)


        self.horizontalLayout_192.addWidget(self.widget_294)

        self.horizontalSpacer_185 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_192.addItem(self.horizontalSpacer_185)

        self.widget_295 = QWidget(self.widget_293)
        self.widget_295.setObjectName(u"widget_295")
        self.verticalLayout_177 = QVBoxLayout(self.widget_295)
        self.verticalLayout_177.setObjectName(u"verticalLayout_177")
        self.label_104 = QLabel(self.widget_295)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setAlignment(Qt.AlignCenter)

        self.verticalLayout_177.addWidget(self.label_104)

        self.lineEdit_45 = QLineEdit(self.widget_295)
        self.lineEdit_45.setObjectName(u"lineEdit_45")
        self.lineEdit_45.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_177.addWidget(self.lineEdit_45)


        self.horizontalLayout_192.addWidget(self.widget_295)

        self.horizontalSpacer_186 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_192.addItem(self.horizontalSpacer_186)

        self.widget_296 = QWidget(self.widget_293)
        self.widget_296.setObjectName(u"widget_296")
        self.verticalLayout_178 = QVBoxLayout(self.widget_296)
        self.verticalLayout_178.setObjectName(u"verticalLayout_178")
        self.label_105 = QLabel(self.widget_296)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setAlignment(Qt.AlignCenter)

        self.verticalLayout_178.addWidget(self.label_105)

        self.lineEdit_46 = QLineEdit(self.widget_296)
        self.lineEdit_46.setObjectName(u"lineEdit_46")
        self.lineEdit_46.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_178.addWidget(self.lineEdit_46)


        self.horizontalLayout_192.addWidget(self.widget_296)

        self.horizontalSpacer_187 = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_192.addItem(self.horizontalSpacer_187)

        self.widget_297 = QWidget(self.widget_293)
        self.widget_297.setObjectName(u"widget_297")
        self.verticalLayout_179 = QVBoxLayout(self.widget_297)
        self.verticalLayout_179.setObjectName(u"verticalLayout_179")
        self.label_106 = QLabel(self.widget_297)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setAlignment(Qt.AlignCenter)

        self.verticalLayout_179.addWidget(self.label_106)

        self.lineEdit_47 = QLineEdit(self.widget_297)
        self.lineEdit_47.setObjectName(u"lineEdit_47")
        self.lineEdit_47.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_179.addWidget(self.lineEdit_47)


        self.horizontalLayout_192.addWidget(self.widget_297)

        self.horizontalSpacer_188 = QSpacerItem(11, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_192.addItem(self.horizontalSpacer_188)

        self.widget_298 = QWidget(self.widget_293)
        self.widget_298.setObjectName(u"widget_298")
        self.verticalLayout_180 = QVBoxLayout(self.widget_298)
        self.verticalLayout_180.setObjectName(u"verticalLayout_180")
        self.label_107 = QLabel(self.widget_298)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setLayoutDirection(Qt.LeftToRight)
        self.label_107.setAlignment(Qt.AlignCenter)

        self.verticalLayout_180.addWidget(self.label_107)

        self.lineEdit_48 = QLineEdit(self.widget_298)
        self.lineEdit_48.setObjectName(u"lineEdit_48")
        self.lineEdit_48.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_180.addWidget(self.lineEdit_48)


        self.horizontalLayout_192.addWidget(self.widget_298)


        self.verticalLayout_175.addWidget(self.widget_293)

        self.verticalSpacer_60 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_175.addItem(self.verticalSpacer_60)

        self.widget_299 = QWidget(self.widget_292)
        self.widget_299.setObjectName(u"widget_299")
        self.horizontalLayout_193 = QHBoxLayout(self.widget_299)
        self.horizontalLayout_193.setObjectName(u"horizontalLayout_193")
        self.widget_warning_46 = QWidget(self.widget_299)
        self.widget_warning_46.setObjectName(u"widget_warning_46")
        self.widget_warning_46.setStyleSheet(u"background-color: rgb(249, 247, 233);\n"
"border-radius:7px;")
        self.horizontalLayout_429 = QHBoxLayout(self.widget_warning_46)
        self.horizontalLayout_429.setSpacing(0)
        self.horizontalLayout_429.setObjectName(u"horizontalLayout_429")
        self.horizontalLayout_429.setContentsMargins(10, 5, 5, 5)
        self.label_354 = QLabel(self.widget_warning_46)
        self.label_354.setObjectName(u"label_354")
        self.label_354.setPixmap(QPixmap(u":/assets/icons/warning-30.png"))

        self.horizontalLayout_429.addWidget(self.label_354)

        self.label_355 = QLabel(self.widget_warning_46)
        self.label_355.setObjectName(u"label_355")
        self.label_355.setMinimumSize(QSize(150, 0))
        self.label_355.setStyleSheet(u"color: rgb(255, 58, 19);\n"
"\n"
"background-color: rgb(249, 247, 233);")
        self.label_355.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_429.addWidget(self.label_355)


        self.horizontalLayout_193.addWidget(self.widget_warning_46)

        self.horizontalSpacer_189 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_193.addItem(self.horizontalSpacer_189)

        self.pushButton_120 = QPushButton(self.widget_299)
        self.pushButton_120.setObjectName(u"pushButton_120")
        self.pushButton_120.setStyleSheet(u"QPushButton{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}")

        self.horizontalLayout_193.addWidget(self.pushButton_120)


        self.verticalLayout_175.addWidget(self.widget_299)


        self.horizontalLayout_189.addWidget(self.widget_292)


        self.verticalLayout_171.addWidget(self.widget_286)

        self.widget_300 = QWidget(self.widget_284)
        self.widget_300.setObjectName(u"widget_300")
        self.widget_300.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_181 = QVBoxLayout(self.widget_300)
        self.verticalLayout_181.setSpacing(0)
        self.verticalLayout_181.setObjectName(u"verticalLayout_181")
        self.verticalLayout_181.setContentsMargins(0, 0, 0, 0)
        self.widget_301 = QWidget(self.widget_300)
        self.widget_301.setObjectName(u"widget_301")
        self.horizontalLayout_194 = QHBoxLayout(self.widget_301)
        self.horizontalLayout_194.setSpacing(0)
        self.horizontalLayout_194.setObjectName(u"horizontalLayout_194")
        self.horizontalLayout_194.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_181.addWidget(self.widget_301)


        self.verticalLayout_171.addWidget(self.widget_300)


        self.verticalLayout_146.addWidget(self.widget_284)

        self.widget_302 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_302.setObjectName(u"widget_302")
        self.verticalLayout_182 = QVBoxLayout(self.widget_302)
        self.verticalLayout_182.setObjectName(u"verticalLayout_182")
        self.widget_303 = QWidget(self.widget_302)
        self.widget_303.setObjectName(u"widget_303")
        self.widget_303.setStyleSheet(u"")
        self.horizontalLayout_195 = QHBoxLayout(self.widget_303)
        self.horizontalLayout_195.setSpacing(0)
        self.horizontalLayout_195.setObjectName(u"horizontalLayout_195")
        self.horizontalLayout_195.setContentsMargins(0, 0, 0, 0)
        self.Equipement_widget_37 = QWidget(self.widget_303)
        self.Equipement_widget_37.setObjectName(u"Equipement_widget_37")
        self.Equipement_widget_37.setStyleSheet(u"QWidget{\n"
"background-color: rgb(92, 124, 250);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_196 = QHBoxLayout(self.Equipement_widget_37)
        self.horizontalLayout_196.setObjectName(u"horizontalLayout_196")
        self.label_108 = QLabel(self.Equipement_widget_37)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setPixmap(QPixmap(u":/assets/icons/equippement-30.png"))

        self.horizontalLayout_196.addWidget(self.label_108, 0, Qt.AlignLeft)

        self.pushButton_121 = QPushButton(self.Equipement_widget_37)
        self.pushButton_121.setObjectName(u"pushButton_121")
        sizePolicy2.setHeightForWidth(self.pushButton_121.sizePolicy().hasHeightForWidth())
        self.pushButton_121.setSizePolicy(sizePolicy2)
        self.pushButton_121.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_121.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"")
        self.pushButton_121.setIcon(icon9)
        self.pushButton_121.setIconSize(QSize(24, 24))
        self.pushButton_121.setCheckable(True)

        self.horizontalLayout_196.addWidget(self.pushButton_121)


        self.horizontalLayout_195.addWidget(self.Equipement_widget_37)

        self.horizontalSpacer_190 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_195.addItem(self.horizontalSpacer_190)


        self.verticalLayout_182.addWidget(self.widget_303)

        self.widget_304 = QWidget(self.widget_302)
        self.widget_304.setObjectName(u"widget_304")
        self.widget_304.setMinimumSize(QSize(450, 0))
        self.widget_304.setStyleSheet(u"\n"
"color: rgb(92, 124, 250);\n"
"background-color: rgb(236, 234, 234);")
        self.horizontalLayout_197 = QHBoxLayout(self.widget_304)
        self.horizontalLayout_197.setObjectName(u"horizontalLayout_197")
        self.horizontalSpacer_191 = QSpacerItem(255, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_197.addItem(self.horizontalSpacer_191)

        self.widget_305 = QWidget(self.widget_304)
        self.widget_305.setObjectName(u"widget_305")
        sizePolicy.setHeightForWidth(self.widget_305.sizePolicy().hasHeightForWidth())
        self.widget_305.setSizePolicy(sizePolicy)
        self.widget_305.setMinimumSize(QSize(400, 0))
        self.verticalLayout_183 = QVBoxLayout(self.widget_305)
        self.verticalLayout_183.setObjectName(u"verticalLayout_183")
        self.widget_306 = QWidget(self.widget_305)
        self.widget_306.setObjectName(u"widget_306")
        self.horizontalLayout_198 = QHBoxLayout(self.widget_306)
        self.horizontalLayout_198.setObjectName(u"horizontalLayout_198")
        self.horizontalSpacer_192 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_198.addItem(self.horizontalSpacer_192)


        self.verticalLayout_183.addWidget(self.widget_306)

        self.horizontalLayout_199 = QHBoxLayout()
        self.horizontalLayout_199.setObjectName(u"horizontalLayout_199")
        self.horizontalSpacer_193 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_199.addItem(self.horizontalSpacer_193)

        self.textEdit_46 = QTextEdit(self.widget_305)
        self.textEdit_46.setObjectName(u"textEdit_46")
        sizePolicy4.setHeightForWidth(self.textEdit_46.sizePolicy().hasHeightForWidth())
        self.textEdit_46.setSizePolicy(sizePolicy4)
        self.textEdit_46.setMinimumSize(QSize(0, 0))
        self.textEdit_46.setMaximumSize(QSize(16777215, 40))
        self.textEdit_46.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.horizontalLayout_199.addWidget(self.textEdit_46)

        self.horizontalSpacer_194 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_199.addItem(self.horizontalSpacer_194)


        self.verticalLayout_183.addLayout(self.horizontalLayout_199)

        self.lineEdit_49 = QLineEdit(self.widget_305)
        self.lineEdit_49.setObjectName(u"lineEdit_49")
        self.lineEdit_49.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_183.addWidget(self.lineEdit_49)

        self.widget_307 = QWidget(self.widget_305)
        self.widget_307.setObjectName(u"widget_307")
        self.horizontalLayout_200 = QHBoxLayout(self.widget_307)
        self.horizontalLayout_200.setObjectName(u"horizontalLayout_200")
        self.horizontalSpacer_195 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_200.addItem(self.horizontalSpacer_195)


        self.verticalLayout_183.addWidget(self.widget_307)

        self.verticalSpacer_61 = QSpacerItem(20, 148, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_183.addItem(self.verticalSpacer_61)


        self.horizontalLayout_197.addWidget(self.widget_305)

        self.horizontalSpacer_196 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_197.addItem(self.horizontalSpacer_196)


        self.verticalLayout_182.addWidget(self.widget_304)

        self.widget_308 = QWidget(self.widget_302)
        self.widget_308.setObjectName(u"widget_308")
        self.widget_308.setStyleSheet(u"background-color: rgb(236, 234, 234);")
        self.verticalLayout_184 = QVBoxLayout(self.widget_308)
        self.verticalLayout_184.setSpacing(0)
        self.verticalLayout_184.setObjectName(u"verticalLayout_184")
        self.verticalLayout_184.setContentsMargins(0, 0, 0, 0)
        self.widget_309 = QWidget(self.widget_308)
        self.widget_309.setObjectName(u"widget_309")
        self.horizontalLayout_201 = QHBoxLayout(self.widget_309)
        self.horizontalLayout_201.setSpacing(0)
        self.horizontalLayout_201.setObjectName(u"horizontalLayout_201")
        self.horizontalLayout_201.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_184.addWidget(self.widget_309)


        self.verticalLayout_182.addWidget(self.widget_308)


        self.verticalLayout_146.addWidget(self.widget_302)

        self.widget_310 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_310.setObjectName(u"widget_310")
        self.widget_310.setStyleSheet(u"")
        self.horizontalLayout_202 = QHBoxLayout(self.widget_310)
        self.horizontalLayout_202.setObjectName(u"horizontalLayout_202")
        self.Equipement_widget_38 = QWidget(self.widget_310)
        self.Equipement_widget_38.setObjectName(u"Equipement_widget_38")
        self.Equipement_widget_38.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 191, 191);\n"
"border-radius:10px;\n"
"color: white;\n"
"}\n"
"")
        self.horizontalLayout_203 = QHBoxLayout(self.Equipement_widget_38)
        self.horizontalLayout_203.setObjectName(u"horizontalLayout_203")
        self.pushButton_122 = QPushButton(self.Equipement_widget_38)
        self.pushButton_122.setObjectName(u"pushButton_122")
        sizePolicy2.setHeightForWidth(self.pushButton_122.sizePolicy().hasHeightForWidth())
        self.pushButton_122.setSizePolicy(sizePolicy2)
        self.pushButton_122.setFont(font5)
        self.pushButton_122.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_122.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(255, 191, 191);\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 191, 191);\n"
"}\n"
"")
        self.pushButton_122.setIcon(icon9)
        self.pushButton_122.setIconSize(QSize(24, 24))
        self.pushButton_122.setCheckable(True)

        self.horizontalLayout_203.addWidget(self.pushButton_122)


        self.horizontalLayout_202.addWidget(self.Equipement_widget_38)

        self.horizontalSpacer_197 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_202.addItem(self.horizontalSpacer_197)

        self.Equipement_widget_39 = QWidget(self.widget_310)
        self.Equipement_widget_39.setObjectName(u"Equipement_widget_39")
        self.Equipement_widget_39.setStyleSheet(u"QWidget{\n"
"background-color: rgb(104, 246, 73);\n"
"border-radius:10px;\n"
"color: white;\n"
"}\n"
"")
        self.horizontalLayout_204 = QHBoxLayout(self.Equipement_widget_39)
        self.horizontalLayout_204.setObjectName(u"horizontalLayout_204")
        self.pushButton_123 = QPushButton(self.Equipement_widget_39)
        self.pushButton_123.setObjectName(u"pushButton_123")
        sizePolicy2.setHeightForWidth(self.pushButton_123.sizePolicy().hasHeightForWidth())
        self.pushButton_123.setSizePolicy(sizePolicy2)
        self.pushButton_123.setFont(font5)
        self.pushButton_123.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_123.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(104, 246, 73);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(104, 246, 73);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(104, 246, 73);\n"
"}\n"
"")
        self.pushButton_123.setIcon(icon9)
        self.pushButton_123.setIconSize(QSize(24, 24))
        self.pushButton_123.setCheckable(True)

        self.horizontalLayout_204.addWidget(self.pushButton_123)


        self.horizontalLayout_202.addWidget(self.Equipement_widget_39)


        self.verticalLayout_146.addWidget(self.widget_310)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_4.addWidget(self.scrollArea_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.nv_dossier_autre_page)

        self.verticalLayout_22.addWidget(self.stackedWidget)


        self.gridLayout_13.addWidget(self.main_body_container, 0, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_50.toggled.connect(self.widget_46.setVisible)
        self.pushButton_48.toggled.connect(self.widget_33.setVisible)
        self.pushButton_55.toggled.connect(self.widget_63.setVisible)
        self.pushButton_58.toggled.connect(self.widget_73.setVisible)
        self.pushButton_47.toggled.connect(self.widget_30.setVisible)
        self.pushButton_52.toggled.connect(self.widget_48.setVisible)
        self.pushButton.toggled.connect(self.widget_2.setVisible)
        self.pushButton_4.toggled.connect(self.widget_4.setVisible)
        self.pushButton_46.toggled.connect(self.widget_29.setVisible)
        self.pushButton_11.toggled.connect(self.widget_3.setVisible)
        self.pushButton_18.toggled.connect(self.widget_5.setVisible)
        self.pushButton_19.toggled.connect(self.widget_6.setVisible)
        self.pushButton_21.toggled.connect(self.widget_7.setVisible)
        self.pushButton_20.toggled.connect(self.widget_8.setVisible)
        self.pushButton_33.toggled.connect(self.widget_13.setVisible)
        self.pushButton_60.toggled.connect(self.widget_60.setVisible)
        self.pushButton_65.toggled.connect(self.widget_61.setVisible)
        self.pushButton_223.toggled.connect(self.widget_700.setVisible)
        self.pushButton_229.toggled.connect(self.widget_716.setVisible)
        self.pushButton_231.toggled.connect(self.widget_730.setVisible)
        self.pushButton_235.toggled.connect(self.widget_748.setVisible)
        self.pushButton_145.toggled.connect(self.widget_398.setVisible)
        self.pushButton_107.toggled.connect(self.widget_250.setVisible)
        self.pushButton_109.toggled.connect(self.widget_256.setVisible)
        self.pushButton_112.toggled.connect(self.widget_263.setVisible)
        self.pushButton_115.toggled.connect(self.widget_272.setVisible)
        self.pushButton_117.toggled.connect(self.widget_286.setVisible)
        self.pushButton_121.toggled.connect(self.widget_304.setVisible)
        self.pushButton_126.toggled.connect(self.widget_324.setVisible)
        self.pushButton_128.toggled.connect(self.widget_330.setVisible)
        self.pushButton_131.toggled.connect(self.widget_337.setVisible)
        self.pushButton_134.toggled.connect(self.widget_346.setVisible)
        self.pushButton_136.toggled.connect(self.widget_360.setVisible)
        self.pushButton_140.toggled.connect(self.widget_378.setVisible)
        self.pushButton_88.toggled.connect(self.widget_176.setVisible)
        self.pushButton_90.toggled.connect(self.widget_182.setVisible)
        self.pushButton_93.toggled.connect(self.widget_189.setVisible)
        self.pushButton_96.toggled.connect(self.widget_198.setVisible)
        self.pushButton_98.toggled.connect(self.widget_212.setVisible)
        self.pushButton_102.toggled.connect(self.widget_230.setVisible)
        self.pushButton_69.toggled.connect(self.widget_102.setVisible)
        self.pushButton_71.toggled.connect(self.widget_108.setVisible)
        self.pushButton_74.toggled.connect(self.widget_115.setVisible)
        self.pushButton_77.toggled.connect(self.widget_124.setVisible)
        self.pushButton_79.toggled.connect(self.widget_138.setVisible)
        self.pushButton_83.toggled.connect(self.widget_156.setVisible)
        self.quit_btn_2.clicked.connect(MainWindow.close)
        self.quit_btn.clicked.connect(MainWindow.close)
        self.pushButton_54.toggled.connect(self.widget_481.setVisible)
        self.checkBox_46.toggled.connect(self.widget_835.setVisible)
        self.checkBox_48.toggled.connect(self.widget_838.setVisible)
        self.checkBox_14.toggled.connect(self.widget_243.setVisible)
        self.checkBox_16.toggled.connect(self.widget_246.setVisible)
        self.checkBox_2.toggled.connect(self.widget_38.setVisible)
        self.checkBox_4.toggled.connect(self.widget_43.setVisible)
        self.checkBox_6.toggled.connect(self.widget_95.setVisible)
        self.checkBox_8.toggled.connect(self.widget_98.setVisible)
        self.checkBox_10.toggled.connect(self.widget_169.setVisible)
        self.checkBox_12.toggled.connect(self.widget_172.setVisible)
        self.checkBox_18.toggled.connect(self.widget_317.setVisible)
        self.checkBox_20.toggled.connect(self.widget_320.setVisible)
        self.checkBox_38.toggled.connect(self.widget_687.setVisible)
        self.checkBox_40.toggled.connect(self.widget_690.setVisible)
        self.pushButton_269.toggled.connect(self.widget_878.setVisible)
        self.checkBox_59.toggled.connect(self.widget_859.setVisible)
        self.checkBox_61.toggled.connect(self.widget_862.setVisible)
        self.pushButton_281.toggled.connect(self.widget_906.setVisible)
        self.pushButton_153.toggled.connect(self.widget_442.setVisible)
        self.checkBox_23.toggled.connect(self.widget_393.setVisible)
        self.checkBox_22.toggled.connect(self.widget_391.setVisible)
        self.pushButton_157.toggled.connect(self.widget_472.setVisible)
        self.pushButton_165.toggled.connect(self.widget_502.setVisible)
        self.checkBox_30.toggled.connect(self.widget_454.setVisible)
        self.checkBox_31.toggled.connect(self.widget_451.setVisible)
        self.pushButton_143.toggled.connect(self.widget_388.setVisible)
        self.pushButton_150.toggled.connect(self.widget_post.setVisible)

        self.menu_stackedWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SocialKeeper", None))
        self.actionOuvrir.setText(QCoreApplication.translate("MainWindow", u"Nouveau", None))
        self.actionOuvrire.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.actionFermer.setText(QCoreApplication.translate("MainWindow", u"Fermer", None))
        self.actionCouper.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.actionColler.setText(QCoreApplication.translate("MainWindow", u"Copier", None))
        self.actionColler_2.setText(QCoreApplication.translate("MainWindow", u"Couper", None))
        self.actionSupprimer.setText(QCoreApplication.translate("MainWindow", u"Coller", None))
        self.actionSuprimer.setText(QCoreApplication.translate("MainWindow", u"Suprimer", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
#if QT_CONFIG(tooltip)
        self.menu_btn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menu_btn_2.setText("")
#if QT_CONFIG(tooltip)
        self.home_btn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.home_btn_2.setText("")
#if QT_CONFIG(tooltip)
        self.new_btn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Nouveau", None))
#endif // QT_CONFIG(tooltip)
        self.new_btn_2.setText("")
#if QT_CONFIG(tooltip)
        self.data_btn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Donnees", None))
#endif // QT_CONFIG(tooltip)
        self.data_btn_2.setText("")
#if QT_CONFIG(tooltip)
        self.autre_btn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Donnees", None))
#endif // QT_CONFIG(tooltip)
        self.autre_btn_2.setText("")
#if QT_CONFIG(tooltip)
        self.settings_btn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Parametres", None))
#endif // QT_CONFIG(tooltip)
        self.settings_btn_2.setText("")
#if QT_CONFIG(tooltip)
        self.quit_btn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Fermer", None))
#endif // QT_CONFIG(tooltip)
        self.quit_btn_2.setText("")
#if QT_CONFIG(tooltip)
        self.menu_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menu_btn.setText(QCoreApplication.translate("MainWindow", u"    Menu", None))
#if QT_CONFIG(tooltip)
        self.home_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"    Home", None))
#if QT_CONFIG(tooltip)
        self.new_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Nouveau", None))
#endif // QT_CONFIG(tooltip)
        self.new_btn.setText(QCoreApplication.translate("MainWindow", u"    Nouveau", None))
#if QT_CONFIG(tooltip)
        self.data_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Donnees", None))
#endif // QT_CONFIG(tooltip)
        self.data_btn.setText(QCoreApplication.translate("MainWindow", u"    Donnees", None))
#if QT_CONFIG(tooltip)
        self.autre_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Donnees", None))
#endif // QT_CONFIG(tooltip)
        self.autre_btn.setText(QCoreApplication.translate("MainWindow", u"    Autres", None))
#if QT_CONFIG(tooltip)
        self.settings_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Parametres", None))
#endif // QT_CONFIG(tooltip)
        self.settings_btn.setText(QCoreApplication.translate("MainWindow", u"    Parametres    ", None))
#if QT_CONFIG(tooltip)
        self.quit_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Fermer", None))
#endif // QT_CONFIG(tooltip)
        self.quit_btn.setText(QCoreApplication.translate("MainWindow", u"    Fermer", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nouveau", None))
        self.pushButton_2.setText("")
        self.label_5.setText("")
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Prod EXT", None))
        self.nvDossier_EXT_btn.setText(QCoreApplication.translate("MainWindow", u"    Ajouter un nouveau dossier", None))
        self.allDossier_EXT_btn.setText(QCoreApplication.translate("MainWindow", u"    Consulter tout les dossiers le prodExt", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_6.setText("")
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Prod INW", None))
        self.nvDossier_IVW_btn.setText(QCoreApplication.translate("MainWindow", u"    Ajouter un nouveau dossier", None))
        self.allDossier_IVW_btn.setText(QCoreApplication.translate("MainWindow", u"    Consulter tout les dossiers le ProdINW", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_7.setText("")
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Prod IVD", None))
        self.nvDossier_IVD_btn.setText(QCoreApplication.translate("MainWindow", u"    Ajouter un nouveau dossier", None))
        self.allDossier_IVD_btn.setText(QCoreApplication.translate("MainWindow", u"    Consulter tout les dossiers le ProdIVD", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_9.setText("")
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Digital", None))
        self.nvDossier_Digital_btn.setText(QCoreApplication.translate("MainWindow", u"    Ajouter un nouveau dossier", None))
        self.allDossier_Digital_btn.setText(QCoreApplication.translate("MainWindow", u"    Consulter tout les dossiers le prod digital", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_8.setText("")
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Autres", None))
        self.nvDossier_Autre_btn.setText(QCoreApplication.translate("MainWindow", u"    Ajouter un nouveau dossier", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Donnees", None))
        self.pushButton_3.setText("")
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Equipement", None))
        self.nvEquipement_btn.setText(QCoreApplication.translate("MainWindow", u"    Ajouter un \u00e9quipement ", None))
        self.allEquipement_btn.setText(QCoreApplication.translate("MainWindow", u"    Consulter tout les \u00e9quipements", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_4.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Personelles", None))
        self.nvPersonne_btn.setText(QCoreApplication.translate("MainWindow", u"    Ajouter une personne ", None))
        self.allPersonne_btn.setText(QCoreApplication.translate("MainWindow", u"    Consulter tout le personnel", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_21.setText("")
        self.pushButton_46.setText(QCoreApplication.translate("MainWindow", u"Fournisseurs", None))
        self.nvFournisseur_btn.setText(QCoreApplication.translate("MainWindow", u"    Ajouter un fournisseur ", None))
        self.allFournisseur_btn.setText(QCoreApplication.translate("MainWindow", u"    Consulter tout les fournisseurs", None))
        self.pushButton_45.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_162.setText("")
        self.pushButton_54.setText(QCoreApplication.translate("MainWindow", u"Clients", None))
        self.nvClient_btn.setText(QCoreApplication.translate("MainWindow", u"    Ajouter un Client ", None))
        self.allFournisseur_btn_2.setText(QCoreApplication.translate("MainWindow", u"    Consulter tout les Clients", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Autre", None))
        self.pushButton_31.setText("")
        self.label_31.setText("")
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"Missions", None))
        self.mission_btn.setText(QCoreApplication.translate("MainWindow", u"   Ajouter une nouvelle mission", None))
        self.allMissions_btn.setText(QCoreApplication.translate("MainWindow", u"   Afficher les missions par dossier", None))
        self.searchMission_btn.setText(QCoreApplication.translate("MainWindow", u"   Chercher une mission", None))
        self.label_32.setText("")
        self.pushButton_60.setText(QCoreApplication.translate("MainWindow", u"Bande de commande", None))
        self.bC_btn.setText(QCoreApplication.translate("MainWindow", u"    Nouveau Bande de commande", None))
        self.allBC_btn.setText(QCoreApplication.translate("MainWindow", u"    Consulter tout les Bandes de commandes", None))
        self.label_33.setText("")
        self.pushButton_65.setText(QCoreApplication.translate("MainWindow", u"Devis", None))
        self.devis_btn.setText(QCoreApplication.translate("MainWindow", u"    Nouvelle Devis", None))
        self.searchDevisbtn.setText(QCoreApplication.translate("MainWindow", u"   Chercher une devis", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"REF", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"DATE", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"PROD", None))

        self.pushButton_39.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"   userName   ", None))
        self.label_11.setText("")
        self.pushButton_32.setText("")
        self.label_164.setText("")
        self.label_165.setText(QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.pushButton_173.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_172.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"Devis", None))
        self.pushButton_146.setText(QCoreApplication.translate("MainWindow", u"Dossier", None))
        self.pushButton_170.setText(QCoreApplication.translate("MainWindow", u"Missions", None))
        self.pushButton_171.setText(QCoreApplication.translate("MainWindow", u"Fournisseurs", None))
        self.pushButton_169.setText(QCoreApplication.translate("MainWindow", u"Clients", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"Bandes de commandes", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Reference du dossier:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"001", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"Prod EXT", None))
        self.label_24.setText("")
        self.pushButton_49.setText(QCoreApplication.translate("MainWindow", u"Date et heure", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">Date et heure de la creation du dossier</span></p></body></html>", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choisir la methode de saisie de la date de la creation du dossier</p></body></html>", None))
        self.checkBox_ext.setText(QCoreApplication.translate("MainWindow", u"Date d'aujourd'hui", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"choisir la date manuellement", None))
        self.textEdit_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choisir la methode de saisie de l'heure </p></body></html>", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"heure actuel", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"choisir l'heure manuellement", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Heure", None))
        self.timeEdit_2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h:mm", None))
        self.label_219.setText("")
        self.label_314.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_25.setText("")
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"Nature", None))
        self.textEdit_12.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">Nature de ce dossier</span></p></body></html>", None))
        self.textEdit_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#5c7cfa;\">Ecrivez quelque lignes pour decrire la nature de ce dossier</span></p></body></html>", None))
        self.label_229.setText("")
        self.label_315.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_43.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_23.setText("")
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"Personelles", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">choisir le nom du personnelle affecter a ce dossier</span></p></body></html>", None))
        self.comboBox_personel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"select Personel", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.label_207.setText("")
        self.label_313.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_44.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_29.setText("")
        self.pushButton_55.setText(QCoreApplication.translate("MainWindow", u"Equipement", None))
        self.textEdit_11.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">choisir un equipement pour ajouter un equipement a la base de donnes </span></p></body></html>", None))
        self.comboBox_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select equipement", None))
        self.pushButton_56.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.pushButton_57.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.label_232.setText("")
        self.label_318.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_62.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_30.setText("")
        self.pushButton_58.setText(QCoreApplication.translate("MainWindow", u"Charge", None))
        self.textEdit_13.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">choisir un equipement pour ajouter un equipement a la base de donnes </span></p></body></html>", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"REF:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Fournisseur", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Designation", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Montant", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"TVA", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"TVA (Montant)", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"TTC", None))
        self.pushButton_63.setText(QCoreApplication.translate("MainWindow", u"calculer", None))
        self.label_230.setText("")
        self.label_316.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_59.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_22.setText("")
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"Facturation", None))
        self.textEdit_15.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">choisir un equipement pour ajouter un equipement a la base de donnes </span></p></body></html>", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Designation", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Montant", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"TVA", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"TVA (Montant)", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"TTC", None))
        self.pushButton_66.setText(QCoreApplication.translate("MainWindow", u"calculer", None))
        self.label_231.setText("")
        self.label_317.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_61.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_27.setText("")
        self.pushButton_52.setText(QCoreApplication.translate("MainWindow", u"Marge", None))
        self.label_189.setText(QCoreApplication.translate("MainWindow", u"Marge", None))
        self.pushButton_67.setText(QCoreApplication.translate("MainWindow", u"calculer", None))
        self.pushButton_51.setText(QCoreApplication.translate("MainWindow", u"                   Annuler", None))
        self.pushButton_53.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Reference du dossier:", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"001", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"Prod INW", None))
        self.label_42.setText("")
        self.pushButton_64.setText(QCoreApplication.translate("MainWindow", u"Date et heure", None))
        self.textEdit_10.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">Date et heure de la creation du dossier</span></p></body></html>", None))
        self.textEdit_14.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choisir la methode de saisie de la date de la creation du dossier</p></body></html>", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Date d'aujourd'hui", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"choisir la date manuellement", None))
        self.textEdit_16.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choisir la methode de saisie de l'heure </p></body></html>", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"heure actuel", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"choisir l'heure manuellement", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"heure", None))
        self.label_280.setText("")
        self.label_319.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_68.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_45.setText("")
        self.pushButton_69.setText(QCoreApplication.translate("MainWindow", u"Nature", None))
        self.textEdit_17.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">Nature de ce dossier</span></p></body></html>", None))
        self.textEdit_18.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#5c7cfa;\">Ecrivez quelque lignes pour decrire la nature de ce dossier</span></p></body></html>", None))
        self.label_281.setText("")
        self.label_320.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_162.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_46.setText("")
        self.pushButton_71.setText(QCoreApplication.translate("MainWindow", u"Personelles", None))
        self.textEdit_20.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">choisir le nom du personnelle affecter a ce dossier</span></p></body></html>", None))
        self.pushButton_72.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.pushButton_73.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.label_282.setText("")
        self.label_321.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_70.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_47.setText("")
        self.pushButton_74.setText(QCoreApplication.translate("MainWindow", u"Equipement", None))
        self.textEdit_21.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">choisir un equipement pour ajouter un equipement a la base de donnes </span></p></body></html>", None))
        self.pushButton_75.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.pushButton_76.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.label_283.setText("")
        self.label_322.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_163.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_48.setText("")
        self.pushButton_77.setText(QCoreApplication.translate("MainWindow", u"Charge", None))
        self.textEdit_22.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">choisir un equipement pour ajouter un equipement a la base de donnes </span></p></body></html>", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Fournisseur", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Designation", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Montant", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"TVA", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"TVA (Montant)", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"TTC", None))
        self.label_287.setText("")
        self.label_323.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_78.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_55.setText("")
        self.pushButton_79.setText(QCoreApplication.translate("MainWindow", u"Facturation", None))
        self.textEdit_23.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">choisir un equipement pour ajouter un equipement a la base de donnes </span></p></body></html>", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.pushButton_80.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Designation", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Montant", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"TVA", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"TVA (Montant)", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"TTC", None))
        self.label_288.setText("")
        self.label_324.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_82.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_62.setText("")
        self.pushButton_83.setText(QCoreApplication.translate("MainWindow", u"Marge", None))
        self.label_197.setText(QCoreApplication.translate("MainWindow", u"Marge", None))
        self.pushButton_84.setText(QCoreApplication.translate("MainWindow", u"                   Annuler", None))
        self.pushButton_85.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Reference du dossier:", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"001", None))
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"Prod IVD", None))
        self.label_65.setText("")
        self.pushButton_86.setText(QCoreApplication.translate("MainWindow", u"Date et heure", None))
        self.textEdit_25.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">Date et heure de la creation du dossier</span></p></body></html>", None))
        self.textEdit_26.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choisir la methode de saisie de la date de la creation du dossier</p></body></html>", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"Date d'aujourd'hui", None))
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"choisir la date manuellement", None))
        self.textEdit_27.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choisir la methode de saisie de l'heure </p></body></html>", None))
        self.checkBox_11.setText(QCoreApplication.translate("MainWindow", u"heure actuel", None))
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u"choisir l'heure manuellement", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"heure", None))
        self.label_289.setText("")
        self.label_325.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_87.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_68.setText("")
        self.pushButton_88.setText(QCoreApplication.translate("MainWindow", u"Nature", None))
        self.textEdit_28.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">Nature de ce dossier</span></p></body></html>", None))
        self.textEdit_29.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#5c7cfa;\">Ecrivez quelque lignes pour decrire la nature de ce dossier</span></p></body></html>", None))
        self.label_258.setText("")
        self.label_326.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_164.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_69.setText("")
        self.pushButton_90.setText(QCoreApplication.translate("MainWindow", u"Personelles", None))
        self.textEdit_31.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">choisir le nom du personnelle affecter a ce dossier</span></p></body></html>", None))
        self.pushButton_91.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.pushButton_92.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.label_262.setText("")
        self.label_327.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_89.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_70.setText("")
        self.pushButton_93.setText(QCoreApplication.translate("MainWindow", u"Equipement", None))
        self.textEdit_32.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">choisir un equipement pour ajouter un equipement a la base de donnes </span></p></body></html>", None))
        self.pushButton_94.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.pushButton_95.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.label_263.setText("")
        self.label_328.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_174.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_71.setText("")
        self.pushButton_96.setText(QCoreApplication.translate("MainWindow", u"Charge", None))
        self.textEdit_33.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">choisir un equipement pour ajouter un equipement a la base de donnes </span></p></body></html>", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Fournisseur", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Designation", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Montant", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"TVA", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"TVA (Montant)", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"TTC", None))
        self.label_292.setText("")
        self.label_329.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_97.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_78.setText("")
        self.pushButton_98.setText(QCoreApplication.translate("MainWindow", u"Facturation", None))
        self.textEdit_34.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">choisir un equipement pour ajouter un equipement a la base de donnes </span></p></body></html>", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.pushButton_99.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.pushButton_100.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Designation", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Montant", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"TVA", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"TVA (Montant)", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"TTC", None))
        self.label_330.setText("")
        self.label_331.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_101.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_85.setText("")
        self.pushButton_102.setText(QCoreApplication.translate("MainWindow", u"Marge", None))
        self.textEdit_35.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">choisir un equipement pour ajouter un equipement a la base de donnes </span></p></body></html>", None))
        self.pushButton_103.setText(QCoreApplication.translate("MainWindow", u"                   Annuler", None))
        self.pushButton_104.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Reference du dossier:", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"001", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"Prod Digital", None))
        self.label_111.setText("")
        self.pushButton_124.setText(QCoreApplication.translate("MainWindow", u"Date et heure", None))
        self.textEdit_47.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">Date et heure de la creation du dossier</span></p></body></html>", None))
        self.textEdit_48.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choisir la methode de saisie de la date de la creation du dossier</p></body></html>", None))
        self.checkBox_17.setText(QCoreApplication.translate("MainWindow", u"Date d'aujourd'hui", None))
        self.checkBox_18.setText(QCoreApplication.translate("MainWindow", u"choisir la date manuellement", None))
        self.textEdit_49.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choisir la methode de saisie de l'heure </p></body></html>", None))
        self.checkBox_19.setText(QCoreApplication.translate("MainWindow", u"heure actuel", None))
        self.checkBox_20.setText(QCoreApplication.translate("MainWindow", u"choisir l'heure manuellement", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"heure", None))
        self.label_332.setText("")
        self.label_333.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_125.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_114.setText("")
        self.pushButton_126.setText(QCoreApplication.translate("MainWindow", u"Nature", None))
        self.textEdit_50.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">Nature de ce dossier</span></p></body></html>", None))
        self.textEdit_51.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#5c7cfa;\">Ecrivez quelque lignes pour decrire la nature de ce dossier</span></p></body></html>", None))
        self.pushButton_127.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_264.setText("")
        self.label_334.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_175.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_115.setText("")
        self.pushButton_128.setText(QCoreApplication.translate("MainWindow", u"Personelles", None))
        self.textEdit_53.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">choisir le nom du personnelle affecter a ce dossier</span></p></body></html>", None))
        self.pushButton_129.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.pushButton_130.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.label_268.setText("")
        self.label_335.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_176.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_116.setText("")
        self.pushButton_131.setText(QCoreApplication.translate("MainWindow", u"Equipement", None))
        self.textEdit_54.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">choisir un equipement pour ajouter un equipement a la base de donnes </span></p></body></html>", None))
        self.pushButton_132.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.pushButton_133.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.label_272.setText("")
        self.label_336.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_177.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_117.setText("")
        self.pushButton_134.setText(QCoreApplication.translate("MainWindow", u"Charge", None))
        self.textEdit_55.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">choisir un equipement pour ajouter un equipement a la base de donnes </span></p></body></html>", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"Fournisseur", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"Designation", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"Montant", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"TVA", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"TVA (Montant)", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"TTC", None))
        self.label_337.setText("")
        self.label_338.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_135.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_124.setText("")
        self.pushButton_136.setText(QCoreApplication.translate("MainWindow", u"Facturation", None))
        self.textEdit_56.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">choisir un equipement pour ajouter un equipement a la base de donnes </span></p></body></html>", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.pushButton_137.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.pushButton_138.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"Designation", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"Montant", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"TVA", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"TVA (Montant)", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"TTC", None))
        self.label_339.setText("")
        self.label_340.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_139.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_131.setText("")
        self.pushButton_140.setText(QCoreApplication.translate("MainWindow", u"Marge", None))
        self.textEdit_57.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">choisir un equipement pour ajouter un equipement a la base de donnes </span></p></body></html>", None))
        self.pushButton_141.setText(QCoreApplication.translate("MainWindow", u"                   Annuler", None))
        self.pushButton_142.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"Nouvelle Mission", None))
        self.label_233.setText(QCoreApplication.translate("MainWindow", u"Ref", None))
        self.label_234.setText(QCoreApplication.translate("MainWindow", u"001", None))
        self.label_236.setText("")
        self.pushButton_219.setText(QCoreApplication.translate("MainWindow", u"Date et heure", None))
        self.textEdit_102.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">Date et heure de la creation de la mission</span></p></body></html>", None))
        self.textEdit_103.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choisir la methode de saisie de la date de la creation du la mission</p></body></html>", None))
        self.checkBox_37.setText(QCoreApplication.translate("MainWindow", u"Date d'aujourd'hui", None))
        self.checkBox_38.setText(QCoreApplication.translate("MainWindow", u"choisir la date manuellement", None))
        self.textEdit_104.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choisir la methode de saisie de l'heure </p></body></html>", None))
        self.checkBox_39.setText(QCoreApplication.translate("MainWindow", u"heure actuel", None))
        self.checkBox_40.setText(QCoreApplication.translate("MainWindow", u"choisir l'heure manuellement", None))
        self.label_237.setText(QCoreApplication.translate("MainWindow", u"heure", None))
        self.label_238.setText("")
        self.label_341.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_220.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_240.setText("")
        self.pushButton_223.setText(QCoreApplication.translate("MainWindow", u"Reference dossier", None))
        self.textEdit_109.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">choisir le departement</span></p></body></html>", None))
        self.textEdit_108.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">reference du dossier</span></p></body></html>", None))
        self.pushButton_224.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.pushButton_225.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.label_273.setText("")
        self.label_342.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_221.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_242.setText("")
        self.pushButton_229.setText(QCoreApplication.translate("MainWindow", u"Charge", None))
        self.textEdit_110.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">choisir un equipement pour ajouter un equipement a la base de donnes </span></p></body></html>", None))
        self.label_243.setText(QCoreApplication.translate("MainWindow", u"Fournisseur", None))
        self.label_244.setText(QCoreApplication.translate("MainWindow", u"Designation", None))
        self.label_245.setText(QCoreApplication.translate("MainWindow", u"Montant", None))
        self.label_246.setText(QCoreApplication.translate("MainWindow", u"TVA", None))
        self.label_247.setText(QCoreApplication.translate("MainWindow", u"TVA (Montant)", None))
        self.label_248.setText(QCoreApplication.translate("MainWindow", u"TTC", None))
        self.label_343.setText("")
        self.label_344.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_230.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_249.setText("")
        self.pushButton_231.setText(QCoreApplication.translate("MainWindow", u"Facturation", None))
        self.textEdit_111.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">choisir un equipement pour ajouter un equipement a la base de donnes </span></p></body></html>", None))
        self.label_250.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.pushButton_232.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.pushButton_233.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.label_251.setText(QCoreApplication.translate("MainWindow", u"Designation", None))
        self.label_252.setText(QCoreApplication.translate("MainWindow", u"Montant", None))
        self.label_253.setText(QCoreApplication.translate("MainWindow", u"TVA", None))
        self.label_254.setText(QCoreApplication.translate("MainWindow", u"TVA (Montant)", None))
        self.label_255.setText(QCoreApplication.translate("MainWindow", u"TTC", None))
        self.label_345.setText("")
        self.label_346.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_234.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_256.setText("")
        self.pushButton_235.setText(QCoreApplication.translate("MainWindow", u"Marge", None))
        self.textEdit_112.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">choisir un equipement pour ajouter un equipement a la base de donnes </span></p></body></html>", None))
        self.pushButton_236.setText(QCoreApplication.translate("MainWindow", u"                   Annuler", None))
        self.pushButton_237.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_201.setText(QCoreApplication.translate("MainWindow", u"Ajouter nouveau Equipement", None))
        self.label_241.setText(QCoreApplication.translate("MainWindow", u"Ref", None))
        self.label_257.setText(QCoreApplication.translate("MainWindow", u"001", None))
        self.label_148.setText("")
        self.pushButton_148.setText(QCoreApplication.translate("MainWindow", u"Donnees de l'equiment", None))
        self.label_185.setText(QCoreApplication.translate("MainWindow", u"Nom de l'equipement", None))
        self.label_186.setText(QCoreApplication.translate("MainWindow", u"Marque", None))
        self.label_188.setText(QCoreApplication.translate("MainWindow", u"Couleur", None))
        self.label_190.setText(QCoreApplication.translate("MainWindow", u"Etas", None))
        self.checkBox_24.setText(QCoreApplication.translate("MainWindow", u"Neuf", None))
        self.checkBox_29.setText(QCoreApplication.translate("MainWindow", u"Occasion", None))
        self.label_191.setText(QCoreApplication.translate("MainWindow", u"Numero de series", None))
        self.label_220.setText("")
        self.label_296.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_152.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_187.setText("")
        self.pushButton_153.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_195.setText(QCoreApplication.translate("MainWindow", u"Equipement", None))
        self.checkBox_30.setText(QCoreApplication.translate("MainWindow", u"Acheter", None))
        self.checkBox_31.setText(QCoreApplication.translate("MainWindow", u"Empreinter", None))
        self.label_199.setText(QCoreApplication.translate("MainWindow", u"Acheter", None))
        self.label_194.setText(QCoreApplication.translate("MainWindow", u"Cout a l'achat (TTC)", None))
        self.label_196.setText(QCoreApplication.translate("MainWindow", u"TVA %", None))
        self.label_198.setText(QCoreApplication.translate("MainWindow", u"Empreinter", None))
        self.label_200.setText(QCoreApplication.translate("MainWindow", u"Duret de l'empreint", None))
        self.label_235.setText(QCoreApplication.translate("MainWindow", u"du", None))
        self.label_239.setText(QCoreApplication.translate("MainWindow", u"au", None))
        self.label_192.setText(QCoreApplication.translate("MainWindow", u"Cout par jours", None))
        self.pushButton_159.setText(QCoreApplication.translate("MainWindow", u"Calculer", None))
        self.label_193.setText(QCoreApplication.translate("MainWindow", u"Cout Total", None))
        self.label_166.setText("")
        self.label_221.setText("")
        self.label_298.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_154.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_158.setText(QCoreApplication.translate("MainWindow", u"Annuler l'ajout de l'equipement", None))
        self.pushButton_198.setText(QCoreApplication.translate("MainWindow", u"                   Annuler", None))
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"Enregistrer un equipement", None))
        self.pushButton_199.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"Ajouter une nouvelle persone a l'equipe", None))
        self.label_144.setText("")
        self.pushButton_147.setText(QCoreApplication.translate("MainWindow", u"Donnees Personelles", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"Prenom", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"date de naissance", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"C.I.N. ", None))
        self.label_222.setText("")
        self.label_303.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_149.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_145.setText("")
        self.pushButton_150.setText(QCoreApplication.translate("MainWindow", u"Details du poste", None))
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"Nom du poste affecter", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"Status :", None))
        self.checkBox_51.setText(QCoreApplication.translate("MainWindow", u"Permanant", None))
        self.checkBox_49.setText(QCoreApplication.translate("MainWindow", u"Contractuel", None))
        self.checkBox_50.setText(QCoreApplication.translate("MainWindow", u"Saisonier", None))
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"Temps affecter", None))
        self.checkBox_52.setText(QCoreApplication.translate("MainWindow", u"Plein-Temps", None))
        self.checkBox_53.setText(QCoreApplication.translate("MainWindow", u"Temps Partiel", None))
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"departement affecter", None))
        self.comboBox_personne.setItemText(0, QCoreApplication.translate("MainWindow", u"EXT", None))
        self.comboBox_personne.setItemText(1, QCoreApplication.translate("MainWindow", u"INW", None))
        self.comboBox_personne.setItemText(2, QCoreApplication.translate("MainWindow", u"IVD", None))
        self.comboBox_personne.setItemText(3, QCoreApplication.translate("MainWindow", u"Digital", None))
        self.comboBox_personne.setItemText(4, QCoreApplication.translate("MainWindow", u"Autre", None))

        self.label_223.setText("")
        self.label_304.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_151.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_140.setText("")
        self.pushButton_143.setText(QCoreApplication.translate("MainWindow", u"Duree du contrat", None))
        self.textEdit_58.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft JhengHei UI'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:9pt; color:#8f94dd;\">Date et heure de la creation du contrat</span></p></body></html>", None))
        self.textEdit_59.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choisir la methode de saisie de la date de la creation du dossier</p></body></html>", None))
        self.checkBox_DateAujourdui.setText(QCoreApplication.translate("MainWindow", u"Date d'aujourd'hui", None))
        self.checkBox_22.setText(QCoreApplication.translate("MainWindow", u"choisir la date manuellement", None))
        self.checkBox_23.setText("")
        self.textEdit_60.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:400;\">contrat a fin determiner</span></p></body></html>", None))
        self.textEdit_64.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">Si la case ci-dessus est cocher alor veuiller choisir une date de la r\u00e9siliation du contrat</span></p></body></html>", None))
        self.label_224.setText("")
        self.label_305.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_144.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_143.setText("")
        self.pushButton_145.setText(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"Notes sur cette personne", None))
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"( facultatif )", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_160.setText(QCoreApplication.translate("MainWindow", u"                   Annuler", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_161.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_161.setText("")
        self.pushButton_155.setText(QCoreApplication.translate("MainWindow", u"Donnees du fournisseur", None))
        self.label_202.setText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self.label_203.setText(QCoreApplication.translate("MainWindow", u"Prenom", None))
        self.label_204.setText(QCoreApplication.translate("MainWindow", u"Adresse", None))
        self.label_206.setText(QCoreApplication.translate("MainWindow", u"ID fiscal", None))
        self.label_225.setText("")
        self.label_309.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_156.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_269.setText(QCoreApplication.translate("MainWindow", u"Ajouter nouveau Fournisseur", None))
        self.label_270.setText(QCoreApplication.translate("MainWindow", u"Ref", None))
        self.label_271.setText(QCoreApplication.translate("MainWindow", u"001", None))
        self.label_208.setText("")
        self.pushButton_157.setText(QCoreApplication.translate("MainWindow", u"Informations bacaire", None))
        self.label_259.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.label_260.setText(QCoreApplication.translate("MainWindow", u"Nom de la Banque", None))
        self.label_261.setText(QCoreApplication.translate("MainWindow", u"Numero du RIB", None))
        self.label_226.setText("")
        self.label_310.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_158.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_174.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_179.setText(QCoreApplication.translate("MainWindow", u"                   Annuler", None))
        self.label_175.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_180.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_276.setText(QCoreApplication.translate("MainWindow", u"Ajouter nouveau Client", None))
        self.label_277.setText(QCoreApplication.translate("MainWindow", u"Ref", None))
        self.label_278.setText(QCoreApplication.translate("MainWindow", u"001", None))
        self.label_163.setText("")
        self.pushButton_167.setText(QCoreApplication.translate("MainWindow", u"Donnees du Client", None))
        self.label_215.setText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self.label_216.setText(QCoreApplication.translate("MainWindow", u"Prenom", None))
        self.label_217.setText(QCoreApplication.translate("MainWindow", u"Adresse", None))
        self.label_218.setText(QCoreApplication.translate("MainWindow", u"CIN", None))
        self.label_227.setText("")
        self.label_311.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_168.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_214.setText("")
        self.pushButton_165.setText(QCoreApplication.translate("MainWindow", u"Informations bacaire", None))
        self.label_265.setText(QCoreApplication.translate("MainWindow", u"Details bancaires du client", None))
        self.label_266.setText(QCoreApplication.translate("MainWindow", u"Nom de la Banque", None))
        self.label_267.setText(QCoreApplication.translate("MainWindow", u"Numero du RIB", None))
        self.label_228.setText("")
        self.label_312.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_166.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_176.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_183.setText(QCoreApplication.translate("MainWindow", u"                   Annuler", None))
        self.label_177.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_184.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"Nouvelle Bande de commande", None))
        self.label_284.setText("")
        self.pushButton_257.setText(QCoreApplication.translate("MainWindow", u"Date et heure", None))
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"Date et heure de la creation du dossier", None))
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"Choisir la methode de saisie de la date de la creation du dossier", None))
        self.checkBox_45.setText(QCoreApplication.translate("MainWindow", u"Date d'aujourd'hui", None))
        self.checkBox_46.setText(QCoreApplication.translate("MainWindow", u"choisir la date manuellement", None))
        self.label_169.setText(QCoreApplication.translate("MainWindow", u"Choisir la methode de saisie de l'heure ", None))
        self.checkBox_47.setText(QCoreApplication.translate("MainWindow", u"heure actuel", None))
        self.checkBox_48.setText(QCoreApplication.translate("MainWindow", u"choisir l'heure manuellement", None))
        self.label_285.setText(QCoreApplication.translate("MainWindow", u"Heure", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h:mm", None))
        self.label_170.setText("")
        self.label_286.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_258.setText(QCoreApplication.translate("MainWindow", u"Suivant     ", None))
        self.label_297.setText("")
        self.pushButton_269.setText(QCoreApplication.translate("MainWindow", u"Bande de Commande", None))
        self.pushButton_279.setText(QCoreApplication.translate("MainWindow", u"Creer un nouveau bande de commande          ", None))
        self.label_168.setText(QCoreApplication.translate("MainWindow", u"Ref:", None))
        self.label_167.setText(QCoreApplication.translate("MainWindow", u"000", None))
        self.label_302.setText(QCoreApplication.translate("MainWindow", u"Commande", None))
        self.label_301.setText(QCoreApplication.translate("MainWindow", u"Montant (ttc)", None))
        self.label_300.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.pushButton_272.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        ___qtablewidgetitem = self.tableWidget_commande.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget_commande.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Commande", None));
        ___qtablewidgetitem2 = self.tableWidget_commande.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"montant", None));
        ___qtablewidgetitem3 = self.tableWidget_commande.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"nombre", None));
        ___qtablewidgetitem4 = self.tableWidget_commande.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"total", None));
        ___qtablewidgetitem5 = self.tableWidget_commande.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Reference Bande de Commande", None));
        self.pushButton_271.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.pushButton_263.setText(QCoreApplication.translate("MainWindow", u"Actualiser", None))
        self.label_171.setText("")
        self.label_291.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_262.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_173.setText(QCoreApplication.translate("MainWindow", u"Annuler l'enregistrement la bande de commande", None))
        self.pushButton_274.setText(QCoreApplication.translate("MainWindow", u"                 Annuler", None))
        self.label_172.setText(QCoreApplication.translate("MainWindow", u"Valider pour enregistrer la bande de commande", None))
        self.pushButton_275.setText(QCoreApplication.translate("MainWindow", u"Valider", None))
        self.label_181.setText(QCoreApplication.translate("MainWindow", u"Nouvelle  Devis ", None))
        self.label_290.setText("")
        self.pushButton_261.setText(QCoreApplication.translate("MainWindow", u"Date et heure", None))
        self.label_182.setText(QCoreApplication.translate("MainWindow", u"Date et heure de la creation de la devis", None))
        self.label_183.setText(QCoreApplication.translate("MainWindow", u"Choisir la methode de saisie de la date de la creation  de la devis", None))
        self.checkBox_58.setText(QCoreApplication.translate("MainWindow", u"Date d'aujourd'hui", None))
        self.checkBox_59.setText(QCoreApplication.translate("MainWindow", u"choisir la date manuellement", None))
        self.label_184.setText(QCoreApplication.translate("MainWindow", u"Choisir la methode de saisie de l'heure ", None))
        self.checkBox_60.setText(QCoreApplication.translate("MainWindow", u"heure actuel", None))
        self.checkBox_61.setText(QCoreApplication.translate("MainWindow", u"choisir l'heure manuellement", None))
        self.label_293.setText(QCoreApplication.translate("MainWindow", u"Heure", None))
        self.timeEdit_3.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h:mm", None))
        self.label_205.setText("")
        self.label_294.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_266.setText(QCoreApplication.translate("MainWindow", u"Suivant     ", None))
        self.label_299.setText("")
        self.pushButton_281.setText(QCoreApplication.translate("MainWindow", u"Devis", None))
        self.pushButton_282.setText(QCoreApplication.translate("MainWindow", u"Creer une nouvelle devis         ", None))
        self.label_209.setText(QCoreApplication.translate("MainWindow", u"Ref:", None))
        self.label_210.setText(QCoreApplication.translate("MainWindow", u"000", None))
        self.label_306.setText(QCoreApplication.translate("MainWindow", u"devis", None))
        self.label_307.setText(QCoreApplication.translate("MainWindow", u"Montant (ttc)", None))
        self.label_308.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.pushButton_283.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        ___qtablewidgetitem6 = self.tableWidget_commande_3.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem7 = self.tableWidget_commande_3.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Devis", None));
        ___qtablewidgetitem8 = self.tableWidget_commande_3.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"montant", None));
        ___qtablewidgetitem9 = self.tableWidget_commande_3.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"nombre", None));
        ___qtablewidgetitem10 = self.tableWidget_commande_3.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"total", None));
        ___qtablewidgetitem11 = self.tableWidget_commande_3.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Reference devis dossier", None));
        self.pushButton_284.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.pushButton_267.setText(QCoreApplication.translate("MainWindow", u"Actualiser", None))
        self.label_211.setText("")
        self.label_295.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_268.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_212.setText(QCoreApplication.translate("MainWindow", u"Annuler l'enregistrement de la devis", None))
        self.pushButton_285.setText(QCoreApplication.translate("MainWindow", u"                 Annuler", None))
        self.label_213.setText(QCoreApplication.translate("MainWindow", u"Valider pour enregistrer la devis", None))
        self.pushButton_286.setText(QCoreApplication.translate("MainWindow", u"Valider", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Reference du dossier:", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"001", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"Autre", None))
        self.label_88.setText("")
        self.pushButton_105.setText(QCoreApplication.translate("MainWindow", u"Date et heure", None))
        self.textEdit_36.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">Date et heure de la creation du dossier</span></p></body></html>", None))
        self.textEdit_37.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choisir la methode de saisie de la date de la creation du dossier</p></body></html>", None))
        self.checkBox_13.setText(QCoreApplication.translate("MainWindow", u"Date d'aujourd'hui", None))
        self.checkBox_14.setText(QCoreApplication.translate("MainWindow", u"choisir la date manuellement", None))
        self.textEdit_38.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choisir la methode de saisie de l'heure </p></body></html>", None))
        self.checkBox_15.setText(QCoreApplication.translate("MainWindow", u"heure actuel", None))
        self.checkBox_16.setText(QCoreApplication.translate("MainWindow", u"choisir l'heure manuellement", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"heure", None))
        self.label_347.setText("")
        self.label_348.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_106.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_91.setText("")
        self.pushButton_107.setText(QCoreApplication.translate("MainWindow", u"Nature", None))
        self.textEdit_39.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">Nature de ce dossier</span></p></body></html>", None))
        self.textEdit_40.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#5c7cfa;\">Ecrivez quelque lignes pour decrire la nature de ce dossier</span></p></body></html>", None))
        self.pushButton_108.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_274.setText("")
        self.label_349.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_178.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_92.setText("")
        self.pushButton_109.setText(QCoreApplication.translate("MainWindow", u"Personelles", None))
        self.textEdit_42.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">choisir le nom du personnelle affecter a ce dossier</span></p></body></html>", None))
        self.pushButton_110.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.pushButton_111.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.label_275.setText("")
        self.label_350.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_181.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_93.setText("")
        self.pushButton_112.setText(QCoreApplication.translate("MainWindow", u"Equipement", None))
        self.textEdit_43.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">choisir un equipement pour ajouter un equipement a la base de donnes </span></p></body></html>", None))
        self.pushButton_113.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.pushButton_114.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.label_279.setText("")
        self.label_351.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_182.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_94.setText("")
        self.pushButton_115.setText(QCoreApplication.translate("MainWindow", u"Charge", None))
        self.textEdit_44.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">choisir un equipement pour ajouter un equipement a la base de donnes </span></p></body></html>", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Fournisseur", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Designation", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Montant", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"TVA", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"TVA (Montant)", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"TTC", None))
        self.label_352.setText("")
        self.label_353.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_116.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_101.setText("")
        self.pushButton_117.setText(QCoreApplication.translate("MainWindow", u"Facturation", None))
        self.textEdit_45.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">choisir un equipement pour ajouter un equipement a la base de donnes </span></p></body></html>", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.pushButton_118.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.pushButton_119.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Designation", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Montant", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"TVA", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"TVA (Montant)", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"TTC", None))
        self.label_354.setText("")
        self.label_355.setText(QCoreApplication.translate("MainWindow", u"msg", None))
        self.pushButton_120.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_108.setText("")
        self.pushButton_121.setText(QCoreApplication.translate("MainWindow", u"Marge", None))
        self.textEdit_46.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8f94dd;\">choisir un equipement pour ajouter un equipement a la base de donnes </span></p></body></html>", None))
        self.pushButton_122.setText(QCoreApplication.translate("MainWindow", u"                   Annuler", None))
        self.pushButton_123.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
    # retranslateUi

