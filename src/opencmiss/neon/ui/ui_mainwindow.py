# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'mainwindow.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(855, 447)
        icon = QIcon()
        icon.addFile(u":/neon/images/icons/neon-icon-v2.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.action_Open = QAction(MainWindow)
        self.action_Open.setObjectName(u"action_Open")
        icon1 = QIcon()
        icon1.addFile(u":/neon/images/icons/document-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Open.setIcon(icon1)
        self.action_Save = QAction(MainWindow)
        self.action_Save.setObjectName(u"action_Save")
        icon2 = QIcon()
        icon2.addFile(u":/neon/images/icons/document-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Save.setIcon(icon2)
        self.action_Clear = QAction(MainWindow)
        self.action_Clear.setObjectName(u"action_Clear")
        self.action_Quit = QAction(MainWindow)
        self.action_Quit.setObjectName(u"action_Quit")
        icon3 = QIcon()
        icon3.addFile(u":/neon/images/icons/application-exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Quit.setIcon(icon3)
        self.action_Snapshot = QAction(MainWindow)
        self.action_Snapshot.setObjectName(u"action_Snapshot")
        icon4 = QIcon()
        icon4.addFile(u":/neon/images/icons/devices-camera-photo-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Snapshot.setIcon(icon4)
        self.action_Undo = QAction(MainWindow)
        self.action_Undo.setObjectName(u"action_Undo")
        icon5 = QIcon()
        icon5.addFile(u":/neon/images/icons/edit-undo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Undo.setIcon(icon5)
        self.action_Redo = QAction(MainWindow)
        self.action_Redo.setObjectName(u"action_Redo")
        icon6 = QIcon()
        icon6.addFile(u":/neon/images/icons/edit-redo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Redo.setIcon(icon6)
        self.action_About = QAction(MainWindow)
        self.action_About.setObjectName(u"action_About")
        icon7 = QIcon()
        icon7.addFile(u":/neon/images/icons/help-about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_About.setIcon(icon7)
        self.action_RegionEditor = QAction(MainWindow)
        self.action_RegionEditor.setObjectName(u"action_RegionEditor")
        self.action_RegionEditor.setCheckable(True)
        self.action_RegionEditor.setChecked(True)
        self.action_ModelSourcesEditor = QAction(MainWindow)
        self.action_ModelSourcesEditor.setObjectName(u"action_ModelSourcesEditor")
        self.action_ModelSourcesEditor.setCheckable(True)
        self.action_ModelSourcesEditor.setChecked(True)
        self.action_SceneEditor = QAction(MainWindow)
        self.action_SceneEditor.setObjectName(u"action_SceneEditor")
        self.action_SceneEditor.setCheckable(True)
        self.action_SceneEditor.setChecked(True)
        self.action_Save_As = QAction(MainWindow)
        self.action_Save_As.setObjectName(u"action_Save_As")
        icon8 = QIcon()
        icon8.addFile(u":/neon/images/icons/document-save-as.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Save_As.setIcon(icon8)
        self.action_SpectrumEditor = QAction(MainWindow)
        self.action_SpectrumEditor.setObjectName(u"action_SpectrumEditor")
        self.action_SpectrumEditor.setCheckable(True)
        self.action_SpectrumEditor.setChecked(True)
        self.action_New = QAction(MainWindow)
        self.action_New.setObjectName(u"action_New")
        icon9 = QIcon()
        icon9.addFile(u":/neon/images/icons/document-new-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_New.setIcon(icon9)
        self.action_Preferences = QAction(MainWindow)
        self.action_Preferences.setObjectName(u"action_Preferences")
        icon10 = QIcon()
        icon10.addFile(u":/neon/images/icons/applications-system-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Preferences.setIcon(icon10)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.viewTabWidget = QTabWidget(self.centralwidget)
        self.viewTabWidget.setObjectName(u"viewTabWidget")

        self.horizontalLayout.addWidget(self.viewTabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 855, 22))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        self.menu_Open_Recent = QMenu(self.menu_File)
        self.menu_Open_Recent.setObjectName(u"menu_Open_Recent")
        self.menu_Edit = QMenu(self.menubar)
        self.menu_Edit.setObjectName(u"menu_Edit")
        self.menu_Help = QMenu(self.menubar)
        self.menu_Help.setObjectName(u"menu_Help")
        self.menu_View = QMenu(self.menubar)
        self.menu_View.setObjectName(u"menu_View")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(False)
        self.statusbar.setMaximumSize(QSize(16777215, 0))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.menu_File.addAction(self.action_New)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.menu_Open_Recent.menuAction())
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.action_Save_As)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Snapshot)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Preferences)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_Open_Recent.addSeparator()
        self.menu_Open_Recent.addAction(self.action_Clear)
        self.menu_Edit.addAction(self.action_Undo)
        self.menu_Edit.addAction(self.action_Redo)
        self.menu_Help.addAction(self.action_About)
        self.toolBar.addAction(self.action_New)
        self.toolBar.addAction(self.action_Open)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Save)
        self.toolBar.addAction(self.action_Save_As)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Redo)
        self.toolBar.addAction(self.action_Undo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Snapshot)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Neon", None))
        self.action_Open.setText(QCoreApplication.translate("MainWindow", u"&Open", None))
# if QT_CONFIG(shortcut)
        self.action_Open.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_Save.setText(QCoreApplication.translate("MainWindow", u"&Save", None))
# if QT_CONFIG(shortcut)
        self.action_Save.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_Clear.setText(QCoreApplication.translate("MainWindow", u"&Clear", None))
        self.action_Quit.setText(QCoreApplication.translate("MainWindow", u"&Quit", None))
# if QT_CONFIG(shortcut)
        self.action_Quit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.action_Snapshot.setText(QCoreApplication.translate("MainWindow", u"Sna&pshot", None))
# if QT_CONFIG(shortcut)
        self.action_Snapshot.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.action_Undo.setText(QCoreApplication.translate("MainWindow", u"&Undo", None))
# if QT_CONFIG(shortcut)
        self.action_Undo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.action_Redo.setText(QCoreApplication.translate("MainWindow", u"&Redo", None))
# if QT_CONFIG(shortcut)
        self.action_Redo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+Z", None))
#endif // QT_CONFIG(shortcut)
        self.action_About.setText(QCoreApplication.translate("MainWindow", u"&About", None))
        self.action_RegionEditor.setText(QCoreApplication.translate("MainWindow", u"Region Editor", None))
        self.action_ModelSourcesEditor.setText(QCoreApplication.translate("MainWindow", u"Model Sources Editor", None))
        self.action_SceneEditor.setText(QCoreApplication.translate("MainWindow", u"Scene Editor", None))
        self.action_Save_As.setText(QCoreApplication.translate("MainWindow", u"Save &As", None))
        self.action_SpectrumEditor.setText(QCoreApplication.translate("MainWindow", u"Spectrum Editor", None))
        self.action_New.setText(QCoreApplication.translate("MainWindow", u"&New", None))
        self.action_Preferences.setText(QCoreApplication.translate("MainWindow", u"Pr&eferences", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"Fi&le", None))
        self.menu_Open_Recent.setTitle(QCoreApplication.translate("MainWindow", u"Open &recent", None))
        self.menu_Edit.setTitle(QCoreApplication.translate("MainWindow", u"E&dit", None))
        self.menu_Help.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
        self.menu_View.setTitle(QCoreApplication.translate("MainWindow", u"&View", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi
