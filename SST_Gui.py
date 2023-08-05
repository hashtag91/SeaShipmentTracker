from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon, QFont, QCursor, QPixmap
from PyQt5.QtCore import Qt, QSize, QCoreApplication
import sys
import airCargoTrack

air = {'Air France':"",'Air Royal':"",'Ethiopian':"",'Turkish Airlines':"",'DHL':"",'FedEx':"",'UPS Air Cargo' : "",'EgyptAir':"",'British Airways':""}

class Ui_self(QWidget):
    def __init__(self):
        super().__init__()
        if not self.objectName():
            self.setObjectName(u"self")
        self.verticalLayout_2 = QVBoxLayout(self)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(self)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, 10, 8, 10)
        self.trackingNumFrame = QFrame(self)
        self.trackingNumFrame.setObjectName(u"trackingNumFrame")
        self.trackingNumFrame.setMinimumSize(QSize(0, 0))
        self.trackingNumFrame.setMaximumSize(QSize(16777215, 30))
        self.trackingNumFrame.setStyleSheet(u"background-color : white;\n"
"border : 1px solid gray;\n"
"border-radius : 10px;")
        self.trackingNumFrame.setFrameShape(QFrame.StyledPanel)
        self.trackingNumFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.trackingNumFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.searchIco = QLabel(self.trackingNumFrame)
        self.searchIco.setObjectName(u"searchIco")
        self.searchIco.setSizeIncrement(QSize(0, 0))
        self.searchIco.setStyleSheet(u"background-color : transparent;\n"
"border : none;")
        self.searchIco.setPixmap(QPixmap(u":/icon/search.svg"))
        self.searchIco.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.searchIco)

        self.trackingNumberLine = QLineEdit(self.trackingNumFrame)
        self.trackingNumberLine.setObjectName(u"trackingNumberLine")
        self.trackingNumberLine.setStyleSheet(u"background-color : transparent;\n"
"border : none;")
        self.trackingNumberLine.textChanged.connect(self.textChamps)

        self.horizontalLayout_2.addWidget(self.trackingNumberLine)


        self.horizontalLayout.addWidget(self.trackingNumFrame)

        self.typeShipment = QComboBox(self)
        self.typeShipment.addItem("")
        self.typeShipment.addItem("")
        self.typeShipment.addItem("")
        self.typeShipment.setObjectName(u"typeShipment")
        self.typeShipment.setMinimumSize(QSize(0, 30))
        self.typeShipment.currentTextChanged.connect(self.AircompanyTextCombo)

        self.horizontalLayout.addWidget(self.typeShipment)

        self.airCompanyList = ['Air France','Air Royal','Ethiopian','Turkish Airlines','DHL','FedEx','UPS Air Cargo','EgyptAir','British Airways']
        self.seaCompanyList = ['Mediterranean Shipping Company (MSC)','Maers','CMA CGM','COSCO','Hapag-Lloyd','Pacific International Lines (PIL)']
        self.companiesBox = QComboBox(self)
        self.companiesBox.setObjectName(u"companiesBox")
        self.companiesBox.setMinimumSize(QSize(200, 30))
        self.companiesBox.currentTextChanged.connect(self.airCompanyAWB)

        self.horizontalLayout.addWidget(self.companiesBox)

        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.clicked.connect(self.commit)

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.groupBox = QGroupBox(self)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.typeLab = QLabel(self.groupBox)
        self.typeLab.setObjectName(u"typeLab")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.typeLab.setFont(font1)
        self.typeLab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.typeLab)

        self.typeTextLab = QLabel(self.groupBox)
        self.typeTextLab.setObjectName(u"typeTextLab")
        self.typeTextLab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.typeTextLab)


        self.horizontalLayout_3.addLayout(self.verticalLayout_11)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.qtyLabe = QLabel(self.groupBox)
        self.qtyLabe.setObjectName(u"qtyLabe")
        self.qtyLabe.setFont(font1)
        self.qtyLabe.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.qtyLabe)

        self.qtyTextLab = QLabel(self.groupBox)
        self.qtyTextLab.setObjectName(u"qtyTextLab")
        self.qtyTextLab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.qtyTextLab)


        self.horizontalLayout_3.addLayout(self.verticalLayout_10)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.weightLab = QLabel(self.groupBox)
        self.weightLab.setObjectName(u"weightLab")
        self.weightLab.setFont(font1)
        self.weightLab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.weightLab)

        self.weightTextLab = QLabel(self.groupBox)
        self.weightTextLab.setObjectName(u"weightTextLab")
        self.weightTextLab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.weightTextLab)


        self.horizontalLayout_3.addLayout(self.verticalLayout_12)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.originLab = QLabel(self.groupBox)
        self.originLab.setObjectName(u"originLab")
        self.originLab.setFont(font1)
        self.originLab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.originLab)

        self.originTextLab = QLabel(self.groupBox)
        self.originTextLab.setObjectName(u"originTextLab")
        self.originTextLab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.originTextLab)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.destinaLab = QLabel(self.groupBox)
        self.destinaLab.setObjectName(u"destinaLab")
        self.destinaLab.setFont(font1)
        self.destinaLab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.destinaLab)

        self.destinaTextLab = QLabel(self.groupBox)
        self.destinaTextLab.setObjectName(u"destinaTextLab")
        self.destinaTextLab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.destinaTextLab)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 2)
        self.horizontalLayout_3.setStretch(4, 2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.PODLab = QLabel(self.groupBox)
        self.PODLab.setObjectName(u"PODLab")
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.PODLab.setFont(font2)

        self.verticalLayout_14.addWidget(self.PODLab)

        self.PODTextLab = QLabel(self.groupBox)
        self.PODTextLab.setObjectName(u"PODTextLab")

        self.verticalLayout_14.addWidget(self.PODTextLab)


        self.horizontalLayout_5.addLayout(self.verticalLayout_14)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.POALab = QLabel(self.groupBox)
        self.POALab.setObjectName(u"POALab")
        self.POALab.setFont(font2)

        self.verticalLayout_13.addWidget(self.POALab)

        self.POATextLab = QLabel(self.groupBox)
        self.POATextLab.setObjectName(u"POATextLab")

        self.verticalLayout_13.addWidget(self.POATextLab)


        self.horizontalLayout_5.addLayout(self.verticalLayout_13)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.ship_Flight_Lab = QLabel(self.groupBox)
        self.ship_Flight_Lab.setObjectName(u"ship_Flight_Lab")
        self.ship_Flight_Lab.setFont(font2)

        self.verticalLayout_15.addWidget(self.ship_Flight_Lab)

        self.ship_Flight_Text_Lab = QLabel(self.groupBox)
        self.ship_Flight_Text_Lab.setObjectName(u"ship_Flight_Text_Lab")

        self.verticalLayout_15.addWidget(self.ship_Flight_Text_Lab)


        self.horizontalLayout_5.addLayout(self.verticalLayout_15)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.ATDLabe = QLabel(self.groupBox)
        self.ATDLabe.setObjectName(u"ATDLabe")
        self.ATDLabe.setFont(font1)
        self.ATDLabe.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.ATDLabe)

        self.ATDTextLab = QLabel(self.groupBox)
        self.ATDTextLab.setObjectName(u"ATDTextLab")
        self.ATDTextLab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.ATDTextLab)


        self.horizontalLayout_6.addLayout(self.verticalLayout_18)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.ETALab = QLabel(self.groupBox)
        self.ETALab.setObjectName(u"ETALab")
        self.ETALab.setFont(font1)
        self.ETALab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.ETALab)

        self.ETATextLab = QLabel(self.groupBox)
        self.ETATextLab.setObjectName(u"ETATextLab")
        self.ETATextLab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.ETATextLab)


        self.horizontalLayout_6.addLayout(self.verticalLayout_17)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.ATALab = QLabel(self.groupBox)
        self.ATALab.setObjectName(u"ATALab")
        self.ATALab.setFont(font1)
        self.ATALab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.ATALab)

        self.ATATextLab = QLabel(self.groupBox)
        self.ATATextLab.setObjectName(u"ATATextLab")
        self.ATATextLab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.ATATextLab)


        self.horizontalLayout_6.addLayout(self.verticalLayout_16)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.CurrentPLab = QLabel(self.groupBox)
        self.CurrentPLab.setObjectName(u"CurrentPLab")
        self.CurrentPLab.setFont(font1)
        self.CurrentPLab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.CurrentPLab)

        self.currentPTextLab = QLabel(self.groupBox)
        self.currentPTextLab.setObjectName(u"currentPTextLab")
        self.currentPTextLab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.currentPTextLab)


        self.horizontalLayout_6.addLayout(self.verticalLayout_19)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.moreButton = QPushButton(self.groupBox)
        self.moreButton.setObjectName(u"moreButton")
        self.moreButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.moreButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(4, 1)

        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.exportPDF = QPushButton(self)
        self.exportPDF.setObjectName(u"exportPDF")
        self.exportPDF.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.exportPDF)

        self.printButton = QPushButton(self)
        self.printButton.setObjectName(u"printButton")
        self.printButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.printButton)

        self.trackFlight = QPushButton(self)
        self.trackFlight.setObjectName(u"trackFlight")
        self.trackFlight.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.trackFlight)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.verticalLayout.setStretch(2, 3)

        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.AWB_list = ""


        self.retranslateUi()

        self.typeShipment.setCurrentIndex(0)
        
    def textChamps(self):
        self.AWB_list = self.trackingNumberLine.text()
        if self.AWB_list[:3] == '071':
            self.typeShipment.setCurrentText('Air')
            self.companiesBox.setCurrentText('Ethiopian')
        if self.AWB_list[:3] == '057':
            self.typeShipment.setCurrentText('Air')
            self.companiesBox.setCurrentText('Air France')
        if self.AWB_list[:3] == '235':
            self.typeShipment.setCurrentText('Air')
            self.companiesBox.setCurrentText('Turkish Airlines')
        if self.AWB_list[:3] == '406':
            self.typeShipment.setCurrentText('Air')
            self.companiesBox.setCurrentText('UPS Air Cargo')
        if self.AWB_list[:3] == '423':
            self.typeShipment.setCurrentText('Air')
            self.companiesBox.setCurrentText('DHL')
        if self.AWB_list[:3] == '023':
            self.typeShipment.setCurrentText('Air')
            self.companiesBox.setCurrentText('FedEx')
        if self.AWB_list[:3] == '077':
            self.typeShipment.setCurrentText('Air')
            self.companiesBox.setCurrentText('EgyptAir')
        if self.AWB_list[:3] == '125':
            self.typeShipment.setCurrentText('Air')
            self.companiesBox.setCurrentText('British Airways')
    def AircompanyTextCombo(self):
        self.companiesBox.clear()
        if self.typeShipment.currentText() == "Air":
            self.companiesBox.addItems(sorted(self.airCompanyList,reverse=False))
        elif self.typeShipment.currentText() == "Sea":
            self.companiesBox.addItems(sorted(self.seaCompanyList, reverse=False))
    def airCompanyAWB(self):
        if self.companiesBox.currentText() == "Air France":
            air["Air France"] = self.trackingNumberLine.text()
        if self.companiesBox.currentText() == "Air Royal":
            air['Air Royal'] = self.trackingNumberLine.text()
        if self.companiesBox.currentText() == "DHL":
            air['DHL'] = self.trackingNumberLine.text()
        if self.companiesBox.currentText() == "FedEx":
            air['FedEx'] = self.trackingNumberLine.text()
        if self.companiesBox.currentText() == 'Ethiopian':
            air['Ethiopian'] = self.trackingNumberLine.text()
        if self.companiesBox.currentText() == "Turkish Airlines":
            air['Turkish Airlines'] = self.trackingNumberLine.text()
        if self.companiesBox.currentText() == 'UPS Air Cargo':
            air['UPS Air Cargo'] = self.trackingNumberLine.text()
        if self.companiesBox.currentText() == 'UPS Air Cargo':
            air['EgyptAir'] = self.trackingNumberLine.text()
        if self.companiesBox.currentText() == 'British Airways':
            air['British Airways'] = self.trackingNumberLine.text()
    def commit(self):
        if self.typeShipment.currentText() == 'Air':
            self.typeTextLab.setText("Pieces")
        if self.companiesBox.currentText() == "Ethiopian":
            airCargoTrack.ethiopian(air['Ethiopian'])
            self.originTextLab.setText(airCargoTrack.ethiopian.resultFonction()[0])
            self.destinaTextLab.setText(airCargoTrack.ethiopian.resultFonction()[1])
            self.qtyTextLab.setText(airCargoTrack.ethiopian.resultFonction()[2])
            self.weightTextLab.setText(airCargoTrack.ethiopian.resultFonction()[5])
  

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("self", u"self", None))
        self.title.setText(QCoreApplication.translate("self", u"SHIPMENTS TRACKING", None))
        self.searchIco.setText("")
        self.trackingNumberLine.setPlaceholderText(QCoreApplication.translate("self", u"Tracking Number here", None))
        self.typeShipment.setItemText(0, QCoreApplication.translate("self", u"Select a mode...", None))
        self.typeShipment.setItemText(1, QCoreApplication.translate("self", u"Air", None))
        self.typeShipment.setItemText(2, QCoreApplication.translate("self", u"Sea", None))

        self.typeShipment.setPlaceholderText(QCoreApplication.translate("self", u"Sele", None))
        self.pushButton.setText(QCoreApplication.translate("self", u"Commit", None))
        self.groupBox.setTitle(QCoreApplication.translate("self", u"Result", None))
        self.typeLab.setText(QCoreApplication.translate("self", u"TYPE", None))
        self.typeTextLab.setText(QCoreApplication.translate("self", u"N/A", None))
        self.qtyLabe.setText(QCoreApplication.translate("self", u"QTY", None))
        self.qtyTextLab.setText(QCoreApplication.translate("self", u"N/A", None))
        self.weightLab.setText(QCoreApplication.translate("self", u"Weight", None))
        self.weightTextLab.setText(QCoreApplication.translate("self", u"N/A", None))
        self.originLab.setText(QCoreApplication.translate("self", u"Origin", None))
        self.originTextLab.setText(QCoreApplication.translate("self", u"N/A", None))
        self.destinaLab.setText(QCoreApplication.translate("self", u"Destination", None))
        self.destinaTextLab.setText(QCoreApplication.translate("self", u"N/A", None))
        self.PODLab.setText(QCoreApplication.translate("self", u"Port of Departure", None))
        self.PODTextLab.setText(QCoreApplication.translate("self", u"N/A", None))
        self.POALab.setText(QCoreApplication.translate("self", u"Port of Arrival", None))
        self.POATextLab.setText(QCoreApplication.translate("self", u"N/A", None))
        self.ship_Flight_Lab.setText(QCoreApplication.translate("self", u"Ship / Flight", None))
        self.ship_Flight_Text_Lab.setText(QCoreApplication.translate("self", u"N/A", None))
        self.ATDLabe.setText(QCoreApplication.translate("self", u"ATD", None))
        self.ATDTextLab.setText(QCoreApplication.translate("self", u"N/A", None))
        self.ETALab.setText(QCoreApplication.translate("self", u"ETA", None))
        self.ETATextLab.setText(QCoreApplication.translate("self", u"N/A", None))
        self.ATALab.setText(QCoreApplication.translate("self", u"ATA", None))
        self.ATATextLab.setText(QCoreApplication.translate("self", u"N/A", None))
        self.CurrentPLab.setText(QCoreApplication.translate("self", u"Current Position", None))
        self.currentPTextLab.setText(QCoreApplication.translate("self", u"N/A", None))
        self.moreButton.setText(QCoreApplication.translate("self", u"More", None))
        self.exportPDF.setText(QCoreApplication.translate("self", u"Export PDF", None))
        self.printButton.setText(QCoreApplication.translate("self", u"Print", None))
        self.trackFlight.setText(QCoreApplication.translate("self", u"Track Ship/Flight", None))
    # retranslateUi

class mainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shipments Tracking")
        self.resize(675,423)
        ico = QIcon("img/icon.png")
        self.setWindowIcon(ico)
        self.setCentralWidget(Ui_self())
        self.show()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    win = mainWin()
    sys.exit(App.exec())