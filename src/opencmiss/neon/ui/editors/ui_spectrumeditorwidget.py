# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res\designer\spectrumeditorwidget.ui'
#
# Created: Fri Feb 26 08:40:11 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SpectrumEditorWidget(object):
    def setupUi(self, SpectrumEditorWidget, shared_context):
        SpectrumEditorWidget.setObjectName("SpectrumEditorWidget")
        SpectrumEditorWidget.resize(300, 875)
        self.verticalLayout = QtGui.QVBoxLayout(SpectrumEditorWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtGui.QScrollArea(SpectrumEditorWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 298, 873))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setContentsMargins(7, 7, 7, 7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtGui.QWidget(self.groupBox)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButtonAddSpectrum = QtGui.QPushButton(self.widget_2)
        self.pushButtonAddSpectrum.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/neon/images/icons/list-add-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAddSpectrum.setIcon(icon)
        self.pushButtonAddSpectrum.setObjectName("pushButtonAddSpectrum")
        self.verticalLayout_3.addWidget(self.pushButtonAddSpectrum)
        self.pushButtonDeleteSpectrum = QtGui.QPushButton(self.widget_2)
        self.pushButtonDeleteSpectrum.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/neon/images/icons/list-remove-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonDeleteSpectrum.setIcon(icon1)
        self.pushButtonDeleteSpectrum.setObjectName("pushButtonDeleteSpectrum")
        self.verticalLayout_3.addWidget(self.pushButtonDeleteSpectrum)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.listWidgetSpectrums = QtGui.QListWidget(self.groupBox)
        self.listWidgetSpectrums.setObjectName("listWidgetSpectrums")
        self.horizontalLayout_2.addWidget(self.listWidgetSpectrums)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.sceneviewerWidgetPreview = SceneviewerWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.sceneviewerWidgetPreview.sizePolicy().hasHeightForWidth())
        self.sceneviewerWidgetPreview.setSizePolicy(sizePolicy)
        self.sceneviewerWidgetPreview.setMinimumSize(QtCore.QSize(0, 40))
        self.sceneviewerWidgetPreview.setObjectName("sceneviewerWidgetPreview")
        self.verticalLayout_2.addWidget(self.sceneviewerWidgetPreview)
        self.groupBoxSpectrumProperties = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxSpectrumProperties.setTitle("")
        self.groupBoxSpectrumProperties.setObjectName("groupBoxSpectrumProperties")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBoxSpectrumProperties)
        self.horizontalLayout_4.setContentsMargins(7, 7, 7, 7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBoxDefault = QtGui.QCheckBox(self.groupBoxSpectrumProperties)
        self.checkBoxDefault.setObjectName("checkBoxDefault")
        self.horizontalLayout_4.addWidget(self.checkBoxDefault)
        self.checkBoxOverwrite = QtGui.QCheckBox(self.groupBoxSpectrumProperties)
        self.checkBoxOverwrite.setObjectName("checkBoxOverwrite")
        self.horizontalLayout_4.addWidget(self.checkBoxOverwrite)
        self.pushButtonAutorange = QtGui.QPushButton(self.groupBoxSpectrumProperties)
        self.pushButtonAutorange.setObjectName("pushButtonAutorange")
        self.horizontalLayout_4.addWidget(self.pushButtonAutorange)
        self.verticalLayout_2.addWidget(self.groupBoxSpectrumProperties)
        self.groupBoxComponents = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBoxComponents.sizePolicy().hasHeightForWidth())
        self.groupBoxComponents.setSizePolicy(sizePolicy)
        self.groupBoxComponents.setObjectName("groupBoxComponents")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBoxComponents)
        self.horizontalLayout_3.setContentsMargins(7, 7, 7, 7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_4 = QtGui.QWidget(self.groupBoxComponents)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButtonAddSpectrumComponent = QtGui.QPushButton(self.widget_4)
        self.pushButtonAddSpectrumComponent.setText("")
        self.pushButtonAddSpectrumComponent.setIcon(icon)
        self.pushButtonAddSpectrumComponent.setObjectName("pushButtonAddSpectrumComponent")
        self.verticalLayout_5.addWidget(self.pushButtonAddSpectrumComponent)
        self.pushButtonDeleteSpectrumComponent = QtGui.QPushButton(self.widget_4)
        self.pushButtonDeleteSpectrumComponent.setText("")
        self.pushButtonDeleteSpectrumComponent.setIcon(icon1)
        self.pushButtonDeleteSpectrumComponent.setObjectName("pushButtonDeleteSpectrumComponent")
        self.verticalLayout_5.addWidget(self.pushButtonDeleteSpectrumComponent)
        self.pushButtonMoveUpSpectrumComponent = QtGui.QPushButton(self.widget_4)
        self.pushButtonMoveUpSpectrumComponent.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/neon/images/icons/go-up-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonMoveUpSpectrumComponent.setIcon(icon2)
        self.pushButtonMoveUpSpectrumComponent.setObjectName("pushButtonMoveUpSpectrumComponent")
        self.verticalLayout_5.addWidget(self.pushButtonMoveUpSpectrumComponent)
        self.pushButtonMoveDownSpectrumComponent = QtGui.QPushButton(self.widget_4)
        self.pushButtonMoveDownSpectrumComponent.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/neon/images/icons/go-down-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonMoveDownSpectrumComponent.setIcon(icon3)
        self.pushButtonMoveDownSpectrumComponent.setObjectName("pushButtonMoveDownSpectrumComponent")
        self.verticalLayout_5.addWidget(self.pushButtonMoveDownSpectrumComponent)
        self.horizontalLayout_3.addWidget(self.widget_4)
        self.listWidgetSpectrumComponents = QtGui.QListWidget(self.groupBoxComponents)
        self.listWidgetSpectrumComponents.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.listWidgetSpectrumComponents.setMovement(QtGui.QListView.Free)
        self.listWidgetSpectrumComponents.setObjectName("listWidgetSpectrumComponents")
        self.horizontalLayout_3.addWidget(self.listWidgetSpectrumComponents)
        self.verticalLayout_2.addWidget(self.groupBoxComponents)
        self.groupBoxComponentProperties = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxComponentProperties.setObjectName("groupBoxComponentProperties")
        self.formLayout_2 = QtGui.QFormLayout(self.groupBoxComponentProperties)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setContentsMargins(7, 7, 7, 7)
        self.formLayout_2.setObjectName("formLayout_2")
        self.labelFieldComponent = QtGui.QLabel(self.groupBoxComponentProperties)
        self.labelFieldComponent.setObjectName("labelFieldComponent")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelFieldComponent)
        self.spinBoxDataFieldComponent = QtGui.QSpinBox(self.groupBoxComponentProperties)
        self.spinBoxDataFieldComponent.setProperty("value", 1)
        self.spinBoxDataFieldComponent.setObjectName("spinBoxDataFieldComponent")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.spinBoxDataFieldComponent)
        self.labelColourMap = QtGui.QLabel(self.groupBoxComponentProperties)
        self.labelColourMap.setObjectName("labelColourMap")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelColourMap)
        self.comboBoxColourMap = QtGui.QComboBox(self.groupBoxComponentProperties)
        self.comboBoxColourMap.setObjectName("comboBoxColourMap")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.comboBoxColourMap)
        self.groupBox_3 = QtGui.QGroupBox(self.groupBoxComponentProperties)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout.setContentsMargins(7, 7, 7, 7)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBoxFixMinimum = QtGui.QCheckBox(self.groupBox_3)
        self.checkBoxFixMinimum.setText("")
        self.checkBoxFixMinimum.setObjectName("checkBoxFixMinimum")
        self.gridLayout.addWidget(self.checkBoxFixMinimum, 1, 1, 1, 1)
        self.checkBoxExtendBelow = QtGui.QCheckBox(self.groupBox_3)
        self.checkBoxExtendBelow.setText("")
        self.checkBoxExtendBelow.setObjectName("checkBoxExtendBelow")
        self.gridLayout.addWidget(self.checkBoxExtendBelow, 1, 4, 1, 1)
        self.lineEditDataRangeMax = QtGui.QLineEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditDataRangeMax.sizePolicy().hasHeightForWidth())
        self.lineEditDataRangeMax.setSizePolicy(sizePolicy)
        self.lineEditDataRangeMax.setObjectName("lineEditDataRangeMax")
        self.gridLayout.addWidget(self.lineEditDataRangeMax, 2, 2, 1, 1)
        self.labelRangeMaximum = QtGui.QLabel(self.groupBox_3)
        self.labelRangeMaximum.setObjectName("labelRangeMaximum")
        self.gridLayout.addWidget(self.labelRangeMaximum, 2, 0, 1, 1)
        self.labelRangeColour = QtGui.QLabel(self.groupBox_3)
        self.labelRangeColour.setObjectName("labelRangeColour")
        self.gridLayout.addWidget(self.labelRangeColour, 0, 3, 1, 1)
        self.labelRangeMinimum = QtGui.QLabel(self.groupBox_3)
        self.labelRangeMinimum.setObjectName("labelRangeMinimum")
        self.gridLayout.addWidget(self.labelRangeMinimum, 1, 0, 1, 1)
        self.lineEditDataRangeMin = QtGui.QLineEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditDataRangeMin.sizePolicy().hasHeightForWidth())
        self.lineEditDataRangeMin.setSizePolicy(sizePolicy)
        self.lineEditDataRangeMin.setObjectName("lineEditDataRangeMin")
        self.gridLayout.addWidget(self.lineEditDataRangeMin, 1, 2, 1, 1)
        self.checkBoxFixMaximum = QtGui.QCheckBox(self.groupBox_3)
        self.checkBoxFixMaximum.setText("")
        self.checkBoxFixMaximum.setObjectName("checkBoxFixMaximum")
        self.gridLayout.addWidget(self.checkBoxFixMaximum, 2, 1, 1, 1)
        self.lineEditColourRangeMax = QtGui.QLineEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditColourRangeMax.sizePolicy().hasHeightForWidth())
        self.lineEditColourRangeMax.setSizePolicy(sizePolicy)
        self.lineEditColourRangeMax.setObjectName("lineEditColourRangeMax")
        self.gridLayout.addWidget(self.lineEditColourRangeMax, 2, 3, 1, 1)
        self.checkBoxExtendAbove = QtGui.QCheckBox(self.groupBox_3)
        self.checkBoxExtendAbove.setText("")
        self.checkBoxExtendAbove.setObjectName("checkBoxExtendAbove")
        self.gridLayout.addWidget(self.checkBoxExtendAbove, 2, 4, 1, 1)
        self.labelRangeExtend = QtGui.QLabel(self.groupBox_3)
        self.labelRangeExtend.setObjectName("labelRangeExtend")
        self.gridLayout.addWidget(self.labelRangeExtend, 0, 4, 1, 1)
        self.lineEditColourRangeMin = QtGui.QLineEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditColourRangeMin.sizePolicy().hasHeightForWidth())
        self.lineEditColourRangeMin.setSizePolicy(sizePolicy)
        self.lineEditColourRangeMin.setObjectName("lineEditColourRangeMin")
        self.gridLayout.addWidget(self.lineEditColourRangeMin, 1, 3, 1, 1)
        self.labelRangeData = QtGui.QLabel(self.groupBox_3)
        self.labelRangeData.setObjectName("labelRangeData")
        self.gridLayout.addWidget(self.labelRangeData, 0, 2, 1, 1)
        self.labelRangeFix = QtGui.QLabel(self.groupBox_3)
        self.labelRangeFix.setObjectName("labelRangeFix")
        self.gridLayout.addWidget(self.labelRangeFix, 0, 1, 1, 1)
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.SpanningRole, self.groupBox_3)
        self.labelScaleType = QtGui.QLabel(self.groupBoxComponentProperties)
        self.labelScaleType.setObjectName("labelScaleType")
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.LabelRole, self.labelScaleType)
        self.comboBoxScale = QtGui.QComboBox(self.groupBoxComponentProperties)
        self.comboBoxScale.setObjectName("comboBoxScale")
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.FieldRole, self.comboBoxScale)
        self.labelExaggeration = QtGui.QLabel(self.groupBoxComponentProperties)
        self.labelExaggeration.setObjectName("labelExaggeration")
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.LabelRole, self.labelExaggeration)
        self.lineEditExaggeration = QtGui.QLineEdit(self.groupBoxComponentProperties)
        self.lineEditExaggeration.setObjectName("lineEditExaggeration")
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.FieldRole, self.lineEditExaggeration)
        self.pushButtonReverseColours = QtGui.QPushButton(self.groupBoxComponentProperties)
        self.pushButtonReverseColours.setObjectName("pushButtonReverseColours")
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.FieldRole, self.pushButtonReverseColours)
        self.verticalLayout_2.addWidget(self.groupBoxComponentProperties)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(SpectrumEditorWidget)
        QtCore.QMetaObject.connectSlotsByName(SpectrumEditorWidget)

    def retranslateUi(self, SpectrumEditorWidget):
        SpectrumEditorWidget.setWindowTitle(QtGui.QApplication.translate("SpectrumEditorWidget", "Spectrum Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("SpectrumEditorWidget", "Spectrums", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAddSpectrum.setToolTip(QtGui.QApplication.translate("SpectrumEditorWidget", "Add spectrum", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDeleteSpectrum.setToolTip(QtGui.QApplication.translate("SpectrumEditorWidget", "Remove spectrum", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxDefault.setText(QtGui.QApplication.translate("SpectrumEditorWidget", "Default", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxOverwrite.setToolTip(QtGui.QApplication.translate("SpectrumEditorWidget", "Overwrite graphics material colour with spectrum colour", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxOverwrite.setText(QtGui.QApplication.translate("SpectrumEditorWidget", "Overwrite", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAutorange.setText(QtGui.QApplication.translate("SpectrumEditorWidget", "Autorange", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxComponents.setTitle(QtGui.QApplication.translate("SpectrumEditorWidget", "Components", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAddSpectrumComponent.setToolTip(QtGui.QApplication.translate("SpectrumEditorWidget", "Add component", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDeleteSpectrumComponent.setToolTip(QtGui.QApplication.translate("SpectrumEditorWidget", "Remove component", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonMoveUpSpectrumComponent.setToolTip(QtGui.QApplication.translate("SpectrumEditorWidget", "Move component up", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonMoveDownSpectrumComponent.setToolTip(QtGui.QApplication.translate("SpectrumEditorWidget", "Move component down", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxComponentProperties.setTitle(QtGui.QApplication.translate("SpectrumEditorWidget", "Component Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFieldComponent.setToolTip(QtGui.QApplication.translate("SpectrumEditorWidget", "Index of component to use from data field", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFieldComponent.setText(QtGui.QApplication.translate("SpectrumEditorWidget", "Field component:", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBoxDataFieldComponent.setToolTip(QtGui.QApplication.translate("SpectrumEditorWidget", "Index of component to use from data field", None, QtGui.QApplication.UnicodeUTF8))
        self.labelColourMap.setText(QtGui.QApplication.translate("SpectrumEditorWidget", "Colour map:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("SpectrumEditorWidget", "Range", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditDataRangeMax.setText(QtGui.QApplication.translate("SpectrumEditorWidget", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.labelRangeMaximum.setToolTip(QtGui.QApplication.translate("SpectrumEditorWidget", "Component to use from data field", None, QtGui.QApplication.UnicodeUTF8))
        self.labelRangeMaximum.setText(QtGui.QApplication.translate("SpectrumEditorWidget", "Max:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelRangeColour.setText(QtGui.QApplication.translate("SpectrumEditorWidget", "Colour:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelRangeMinimum.setToolTip(QtGui.QApplication.translate("SpectrumEditorWidget", "Component to use from data field", None, QtGui.QApplication.UnicodeUTF8))
        self.labelRangeMinimum.setText(QtGui.QApplication.translate("SpectrumEditorWidget", "Min:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditDataRangeMin.setText(QtGui.QApplication.translate("SpectrumEditorWidget", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditColourRangeMax.setText(QtGui.QApplication.translate("SpectrumEditorWidget", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.labelRangeExtend.setText(QtGui.QApplication.translate("SpectrumEditorWidget", "Ext", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditColourRangeMin.setText(QtGui.QApplication.translate("SpectrumEditorWidget", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.labelRangeData.setToolTip(QtGui.QApplication.translate("SpectrumEditorWidget", "Component to use from data field", None, QtGui.QApplication.UnicodeUTF8))
        self.labelRangeData.setText(QtGui.QApplication.translate("SpectrumEditorWidget", "Data:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelRangeFix.setText(QtGui.QApplication.translate("SpectrumEditorWidget", "Fix", None, QtGui.QApplication.UnicodeUTF8))
        self.labelScaleType.setText(QtGui.QApplication.translate("SpectrumEditorWidget", "Scale type:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelExaggeration.setText(QtGui.QApplication.translate("SpectrumEditorWidget", "Exaggeration:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonReverseColours.setText(QtGui.QApplication.translate("SpectrumEditorWidget", "Reverse colours", None, QtGui.QApplication.UnicodeUTF8))

from opencmiss.neon.ui.zincwidgets.sceneviewerwidget import SceneviewerWidget
from opencmiss.neon.ui import icons_rc
