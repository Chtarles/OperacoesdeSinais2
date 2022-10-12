# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'front_operacao_sinais_.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from mplwidget import MplWidget


class Ui_MainWindow_Operacao_Sinais_(object):
    def setupUi(self, MainWindow_Operacao_Sinais_):
        if not MainWindow_Operacao_Sinais_.objectName():
            MainWindow_Operacao_Sinais_.setObjectName(u"MainWindow_Operacao_Sinais_")
        MainWindow_Operacao_Sinais_.resize(1200, 802)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow_Operacao_Sinais_.sizePolicy().hasHeightForWidth())
        MainWindow_Operacao_Sinais_.setSizePolicy(sizePolicy)
        MainWindow_Operacao_Sinais_.setMinimumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow_Operacao_Sinais_)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(235, 235, 235);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget = QWidget(self.frame_4)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_X1 = QLabel(self.widget)
        self.label_X1.setObjectName(u"label_X1")
        font = QFont()
        font.setFamily(u"Montserrat Medium")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_X1.setFont(font)
        self.label_X1.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_6.addWidget(self.label_X1)

        self.label_Amplitude_1 = QLabel(self.widget)
        self.label_Amplitude_1.setObjectName(u"label_Amplitude_1")
        font1 = QFont()
        font1.setFamily(u"Montserrat Medium")
        font1.setPointSize(10)
        self.label_Amplitude_1.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_Amplitude_1)

        self.spinBox_Amplitude_1 = QSpinBox(self.widget)
        self.spinBox_Amplitude_1.setObjectName(u"spinBox_Amplitude_1")
        self.spinBox_Amplitude_1.setFont(font1)
        self.spinBox_Amplitude_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinBox_Amplitude_1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinBox_Amplitude_1.setMinimum(1)

        self.verticalLayout_6.addWidget(self.spinBox_Amplitude_1)

        self.label_Freq_in_1 = QLabel(self.widget)
        self.label_Freq_in_1.setObjectName(u"label_Freq_in_1")
        self.label_Freq_in_1.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_Freq_in_1)

        self.spinBox_Freq_in_1 = QSpinBox(self.widget)
        self.spinBox_Freq_in_1.setObjectName(u"spinBox_Freq_in_1")
        self.spinBox_Freq_in_1.setFont(font1)
        self.spinBox_Freq_in_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinBox_Freq_in_1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinBox_Freq_in_1.setMinimum(1)
        self.spinBox_Freq_in_1.setMaximum(1000)

        self.verticalLayout_6.addWidget(self.spinBox_Freq_in_1)

        self.label_Freq_out_1 = QLabel(self.widget)
        self.label_Freq_out_1.setObjectName(u"label_Freq_out_1")
        self.label_Freq_out_1.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_Freq_out_1)

        self.spinBox_Freq_out_1 = QSpinBox(self.widget)
        self.spinBox_Freq_out_1.setObjectName(u"spinBox_Freq_out_1")
        self.spinBox_Freq_out_1.setFont(font1)
        self.spinBox_Freq_out_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinBox_Freq_out_1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinBox_Freq_out_1.setMinimum(2)
        self.spinBox_Freq_out_1.setMaximum(1000)

        self.verticalLayout_6.addWidget(self.spinBox_Freq_out_1)

        self.label_Tempo_1 = QLabel(self.widget)
        self.label_Tempo_1.setObjectName(u"label_Tempo_1")
        self.label_Tempo_1.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_Tempo_1)

        self.spinBox_Tempo_1 = QSpinBox(self.widget)
        self.spinBox_Tempo_1.setObjectName(u"spinBox_Tempo_1")
        self.spinBox_Tempo_1.setFont(font1)
        self.spinBox_Tempo_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinBox_Tempo_1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinBox_Tempo_1.setMinimum(1)
        self.spinBox_Tempo_1.setMaximum(100)
        self.spinBox_Tempo_1.setValue(1)
        self.spinBox_Tempo_1.setDisplayIntegerBase(10)

        self.verticalLayout_6.addWidget(self.spinBox_Tempo_1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.pushButton_Plot_x1 = QPushButton(self.widget)
        self.pushButton_Plot_x1.setObjectName(u"pushButton_Plot_x1")
        font2 = QFont()
        font2.setFamily(u"Montserrat SemiBold")
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton_Plot_x1.setFont(font2)
        self.pushButton_Plot_x1.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_Plot_x1.setStyleSheet(u"background-color: rgb(165, 165, 165);")

        self.verticalLayout_6.addWidget(self.pushButton_Plot_x1)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)


        self.horizontalLayout_3.addWidget(self.widget)

        self.MplWidget_1 = MplWidget(self.frame_4)
        self.MplWidget_1.setObjectName(u"MplWidget_1")

        self.horizontalLayout_3.addWidget(self.MplWidget_1)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(235, 235, 235);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_2 = QWidget(self.frame_3)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.label.setFont(font3)

        self.verticalLayout_5.addWidget(self.label)

        self.label_Amplitude_2 = QLabel(self.widget_2)
        self.label_Amplitude_2.setObjectName(u"label_Amplitude_2")
        self.label_Amplitude_2.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_Amplitude_2)

        self.spinBox_Amplitude_2 = QSpinBox(self.widget_2)
        self.spinBox_Amplitude_2.setObjectName(u"spinBox_Amplitude_2")
        self.spinBox_Amplitude_2.setFont(font1)
        self.spinBox_Amplitude_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinBox_Amplitude_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinBox_Amplitude_2.setMinimum(1)

        self.verticalLayout_5.addWidget(self.spinBox_Amplitude_2)

        self.label_Freq_in_2 = QLabel(self.widget_2)
        self.label_Freq_in_2.setObjectName(u"label_Freq_in_2")
        self.label_Freq_in_2.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_Freq_in_2)

        self.spinBox_Freq_in_2 = QSpinBox(self.widget_2)
        self.spinBox_Freq_in_2.setObjectName(u"spinBox_Freq_in_2")
        self.spinBox_Freq_in_2.setFont(font1)
        self.spinBox_Freq_in_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinBox_Freq_in_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinBox_Freq_in_2.setMinimum(1)
        self.spinBox_Freq_in_2.setMaximum(1000)

        self.verticalLayout_5.addWidget(self.spinBox_Freq_in_2)

        self.label_Freq_out_2 = QLabel(self.widget_2)
        self.label_Freq_out_2.setObjectName(u"label_Freq_out_2")
        self.label_Freq_out_2.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_Freq_out_2)

        self.spinBox_Freq_out_2 = QSpinBox(self.widget_2)
        self.spinBox_Freq_out_2.setObjectName(u"spinBox_Freq_out_2")
        self.spinBox_Freq_out_2.setFont(font1)
        self.spinBox_Freq_out_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinBox_Freq_out_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinBox_Freq_out_2.setMinimum(2)
        self.spinBox_Freq_out_2.setMaximum(1000)

        self.verticalLayout_5.addWidget(self.spinBox_Freq_out_2)

        self.label_Tempo_2 = QLabel(self.widget_2)
        self.label_Tempo_2.setObjectName(u"label_Tempo_2")
        self.label_Tempo_2.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_Tempo_2)

        self.spinBox_Tempo_2 = QSpinBox(self.widget_2)
        self.spinBox_Tempo_2.setObjectName(u"spinBox_Tempo_2")
        self.spinBox_Tempo_2.setFont(font1)
        self.spinBox_Tempo_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinBox_Tempo_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinBox_Tempo_2.setMinimum(1)
        self.spinBox_Tempo_2.setMaximum(100)
        self.spinBox_Tempo_2.setValue(1)

        self.verticalLayout_5.addWidget(self.spinBox_Tempo_2)

        self.verticalSpacer_2 = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.pushButton_Plot_x2 = QPushButton(self.widget_2)
        self.pushButton_Plot_x2.setObjectName(u"pushButton_Plot_x2")
        self.pushButton_Plot_x2.setFont(font2)
        self.pushButton_Plot_x2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_Plot_x2.setStyleSheet(u"background-color: rgb(165, 165, 165);")

        self.verticalLayout_5.addWidget(self.pushButton_Plot_x2)

        self.verticalSpacer = QSpacerItem(20, 36, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.widget_2)

        self.MplWidget_2 = MplWidget(self.frame_3)
        self.MplWidget_2.setObjectName(u"MplWidget_2")

        self.horizontalLayout.addWidget(self.MplWidget_2)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.radioButton_continuo = QRadioButton(self.frame_2)
        self.radioButton_continuo.setObjectName(u"radioButton_continuo")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.radioButton_continuo.setFont(font4)

        self.horizontalLayout_5.addWidget(self.radioButton_continuo)

        self.radioButton_discreto = QRadioButton(self.frame_2)
        self.radioButton_discreto.setObjectName(u"radioButton_discreto")
        self.radioButton_discreto.setFont(font4)

        self.horizontalLayout_5.addWidget(self.radioButton_discreto)

        self.radioButton_quantizado = QRadioButton(self.frame_2)
        self.radioButton_quantizado.setObjectName(u"radioButton_quantizado")
        self.radioButton_quantizado.setFont(font4)

        self.horizontalLayout_5.addWidget(self.radioButton_quantizado)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setStyleSheet(u"background-color: rgb(235, 235, 235);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer_5 = QSpacerItem(10, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_5)

        self.MplWidget_Result = MplWidget(self.frame_6)
        self.MplWidget_Result.setObjectName(u"MplWidget_Result")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(40)
        sizePolicy2.setHeightForWidth(self.MplWidget_Result.sizePolicy().hasHeightForWidth())
        self.MplWidget_Result.setSizePolicy(sizePolicy2)

        self.verticalLayout_8.addWidget(self.MplWidget_Result)

        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(5)
        sizePolicy3.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy3)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.checkBox_Amplificacao = QCheckBox(self.frame_5)
        self.checkBox_Amplificacao.setObjectName(u"checkBox_Amplificacao")
        self.checkBox_Amplificacao.setFont(font1)
        self.checkBox_Amplificacao.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.checkBox_Amplificacao)

        self.spinBox_Amplificacao = QSpinBox(self.frame_5)
        self.spinBox_Amplificacao.setObjectName(u"spinBox_Amplificacao")
        self.spinBox_Amplificacao.setFont(font1)
        self.spinBox_Amplificacao.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinBox_Amplificacao.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinBox_Amplificacao.setMinimum(1)

        self.verticalLayout_9.addWidget(self.spinBox_Amplificacao)


        self.horizontalLayout_4.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.checkBox_Deslocamento = QCheckBox(self.frame_5)
        self.checkBox_Deslocamento.setObjectName(u"checkBox_Deslocamento")
        self.checkBox_Deslocamento.setFont(font1)
        self.checkBox_Deslocamento.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_10.addWidget(self.checkBox_Deslocamento)

        self.spinBox_Deslocamento = QSpinBox(self.frame_5)
        self.spinBox_Deslocamento.setObjectName(u"spinBox_Deslocamento")
        self.spinBox_Deslocamento.setFont(font1)
        self.spinBox_Deslocamento.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinBox_Deslocamento.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinBox_Deslocamento.setMinimum(-999)
        self.spinBox_Deslocamento.setMaximum(999)

        self.verticalLayout_10.addWidget(self.spinBox_Deslocamento)


        self.horizontalLayout_4.addLayout(self.verticalLayout_10)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.pushButton_Plot_result = QPushButton(self.frame_5)
        self.pushButton_Plot_result.setObjectName(u"pushButton_Plot_result")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_Plot_result.sizePolicy().hasHeightForWidth())
        self.pushButton_Plot_result.setSizePolicy(sizePolicy4)
        self.pushButton_Plot_result.setFont(font2)
        self.pushButton_Plot_result.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_Plot_result.setStyleSheet(u"background-color: rgb(165, 165, 165);")

        self.verticalLayout_11.addWidget(self.pushButton_Plot_result)


        self.horizontalLayout_4.addLayout(self.verticalLayout_11)


        self.verticalLayout_8.addWidget(self.frame_5)


        self.verticalLayout_4.addWidget(self.frame_6)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        MainWindow_Operacao_Sinais_.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_Operacao_Sinais_)

        QMetaObject.connectSlotsByName(MainWindow_Operacao_Sinais_)
    # setupUi

    def retranslateUi(self, MainWindow_Operacao_Sinais_):
        MainWindow_Operacao_Sinais_.setWindowTitle(QCoreApplication.translate("MainWindow_Operacao_Sinais_", u"MainWindow", None))
        self.label_X1.setText(QCoreApplication.translate("MainWindow_Operacao_Sinais_", u"X1[n]", None))
        self.label_Amplitude_1.setText(QCoreApplication.translate("MainWindow_Operacao_Sinais_", u"Amplitude:", None))
        self.label_Freq_in_1.setText(QCoreApplication.translate("MainWindow_Operacao_Sinais_", u"Frequ\u00eancia IN:", None))
        self.label_Freq_out_1.setText(QCoreApplication.translate("MainWindow_Operacao_Sinais_", u"Frequ\u00eancia OUT:", None))
        self.label_Tempo_1.setText(QCoreApplication.translate("MainWindow_Operacao_Sinais_", u"Tempo:", None))
        self.pushButton_Plot_x1.setText(QCoreApplication.translate("MainWindow_Operacao_Sinais_", u"PLOT X1", None))
        self.label.setText(QCoreApplication.translate("MainWindow_Operacao_Sinais_", u"X2[n]", None))
        self.label_Amplitude_2.setText(QCoreApplication.translate("MainWindow_Operacao_Sinais_", u"Amplitude:", None))
        self.label_Freq_in_2.setText(QCoreApplication.translate("MainWindow_Operacao_Sinais_", u"Frequ\u00eancia IN:", None))
        self.label_Freq_out_2.setText(QCoreApplication.translate("MainWindow_Operacao_Sinais_", u"Frequ\u00eancia OUT:", None))
        self.label_Tempo_2.setText(QCoreApplication.translate("MainWindow_Operacao_Sinais_", u"Tempo:", None))
        self.pushButton_Plot_x2.setText(QCoreApplication.translate("MainWindow_Operacao_Sinais_", u"PLOT X2", None))
        self.radioButton_continuo.setText(QCoreApplication.translate("MainWindow_Operacao_Sinais_", u"Cont\u00ednuo", None))
        self.radioButton_discreto.setText(QCoreApplication.translate("MainWindow_Operacao_Sinais_", u"Discreto", None))
        self.radioButton_quantizado.setText(QCoreApplication.translate("MainWindow_Operacao_Sinais_", u"Quantizado", None))
        self.checkBox_Amplificacao.setText(QCoreApplication.translate("MainWindow_Operacao_Sinais_", u"Amplifica\u00e7\u00e3o:", None))
        self.checkBox_Deslocamento.setText(QCoreApplication.translate("MainWindow_Operacao_Sinais_", u"Deslocamento:", None))
        self.pushButton_Plot_result.setText(QCoreApplication.translate("MainWindow_Operacao_Sinais_", u"PLOT", None))
    # retranslateUi

