# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import math


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

# satellites database
satellites = dict()
satellites = {'Eutelsat10A': 10.0, 'Astra3B': 23.5, 'Eutelsat8WestB': -8.0, 'Eutelsat21B': 21.6, 'KazSat2': 86.5, 'Eutelsat33C/33D': 33.1, 'Yamal401': 90.0, 'Yamal402': 54.9, 'Intelsat10-02-Thor5/6Feeds': -1.0, 'Thaicom5/6': 78.5, 'Turksat2A/3A/4A': 42.0, 'Rascom-QAF1R': 2.9, 'Badr-4/5/6': 26.0, 'HotBird13B/13C/13D': 13.0, 'Badr-7': 26.0, 'AsiaSat8': 105.3, 'ABS-3': -16.0, 'AsiaSat7': 105.5, 'NSS-806': -47.5, 'AsiaSat5': 100.5, 'Eutelsat12WestB': -12.7, 'Eutelsat12WestA': -12.5, 'Afghansat1/Eutelsat48D': 48.1, 'Eutelsat9A': 9.0, 'Astra4A/SES-5': 4.9, 'Amos2/3': -4.0, 'Turksat2A/3A/4AFeeds': 42.0, 'Hispasat1D/1E': -30.0, 'Astra2E/2F/2G': 28.2, 'Telstar11N': -37.6, 'Astra5B': 31.5, 'Nimiq2': 44.4, 'Intelsat14': -45.0, 'Intelsat17': 66.0, 'Eutelsat10AFeeds': 10.0, 'Intelsat10': 47.5, 'Intelsat12': 45.0, 'Intelsat906': 64.2, 'Intelsat907': -27.5, 'Intelsat904': 60.0, 'Intelsat905': -24.5, 'Intelsat902': 62.0, 'Intelsat903': -34.5, 'G-Sat15': 93.5, 'NSS7': -20.0, 'Intelsat702': 32.9, 'Yahsat-1A': 52.5, 'Yahsat-1B': 47.6, 'Intelsat22': 72.1, 'Intelsat28': 32.8, 'Yamal202': 49.0, 'Intelsat20': 68.5, 'NSS-10': -37.5, 'Astra2D': 49.1, 'Intelsat23': -53.0, 'Astra2B': 31.3, 'Astra2C': 60.3, 'Intelsat26': 65.8, 'Astra2A': 28.0, 'NSS-12': 57.0, 'SES-4': -22.0, 'SES-6': -40.5, 'Eutelsat12WAFeeds': -12.5, 'Eutelsat3B': 3.1, 'AzerSpace1/Africasat-1A': 46.0, 'Paksat1R': 38.0, '\xef\xbb\xbfExpress-AM5': 140.0, 'Intelsat1R': -50.0, 'WGS-2': 60.2, 'Eutelsat8WBFeeds': -8.0, 'Intelsat34': -55.6, 'Arabsat-5A': 30.5, 'Arabsat-5C': 20.0, 'Intelsat25': -31.5, 'Raduga-1M3': 70.0, 'Express-AM44': -11.0, "Eutelsat25B/Es'hail-1": 25.5, 'Eutelsat16AFeeds': 16.0, 'Insat4A': 83.0, 'Intelsat7': -18.2, 'G-Sat8/16': 55.1, 'Hylas2': 31.0, 'Hylas1': -33.5, 'Insat3C/4CR': 74.0, 'ST-2': 88.0, 'Intelsat10-02-Thor5/6/7': -0.8, 'Astra1KR/1L/1M/1NRadios': 19.2, 'Sicral1B': 11.7, 'KazSat3': 58.5, 'Eutelsat70B': 70.5, 'Eutelsat33D': 33.0, 'TurkmenAlem/MonacoSat': 52.0, 'ABS-2': 74.9, 'Eutelsat16A': 16.0, 'ABS-7': 116.1, 'ABS-4': 61.0, 'Thor-3': -4.3, 'Turksat2A/3A/4ARadios': 42.0, 'ABS-3A': -3.0, 'Express-AM33': 96.5, 'Astra3BFeeds': 23.5, 'Express-AM6': 53.0, 'SES-7': 108.2, 'Turksat4B': 50.0, 'HellasSat2': 39.0, 'Apstar-7': 76.5, 'Astra1G': 59.8, 'Astra1F': 44.5, 'Astra1D': -47.2, 'NSS-6/SES-8': 95.0, 'Telstar12': -15.0, 'Astra1H': -47.7, 'Express-AM2': 80.0, 'Express-AM3': 103.0, 'Express-AT1': 56.0, 'Express-AM7': 40.0, 'Express-AT2': 139.9, 'Express-AM8': -14.0, 'Eutelsat7WA/8WB,Nile201': -7.2, 'Amos5': 17.0, 'Amos4': 65.0, 'Eutelsat5WestA': -5.0, 'Express-AM22': 80.1, 'Galaxy27': 66.2, 'Intelsat901': -18.0, 'Eutelsat36A/36B': 36.0, 'G-Sat10': 83.0, 'G-Sat12': 83.0, 'Chinasat12': 87.5, 'Astra1KR/1L/1M/1N': 19.2, 'Eutelsat7A/7B': 7.0, 'Eutelsat7A/7BFeeds': 7.0, 'Eutelsat21BFeeds': 21.6, 'Express-A4': -14.0, 'HotBird13B/13C/13DRadios': 13.0, 'Eutelsat31A': 30.8, 'Inmarsat-5F2': -55.0, 'Insat3A/4B': 93.5, 'Eutelsat48A': 48.3, 'EutelsatKa-Sat9A': 9.0, 'AMC-1': 29.5, 'G-Sat7/14': 74.0, 'Horizons-2/IS-15': 85.0}



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1562, 1001)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_5 = QtGui.QGridLayout(self.widget)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.groupBox = QtGui.QGroupBox(self.widget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.sname = QtGui.QComboBox(self.groupBox)
        self.sname.setObjectName(_fromUtf8("sname"))
        
        # adding Satellites' Names database to Combo Box
        self.sname.setEditable(True)
        for k,v in sorted(satellites.items()):
            self.sname.addItem(_fromUtf8(k))
        
        self.verticalLayout_3.addWidget(self.sname)
        self.stype = QtGui.QLineEdit(self.groupBox)
        self.stype.setObjectName(_fromUtf8("stype"))
        self.verticalLayout_3.addWidget(self.stype)
        self.phaiss = QtGui.QDoubleSpinBox(self.groupBox)
        self.phaiss.setMinimum(-180.0)
        self.phaiss.setMaximum(180.0)
        self.phaiss.setObjectName(_fromUtf8("phaiss"))
        self.verticalLayout_3.addWidget(self.phaiss)
        self.lineEdit_16 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.verticalLayout_3.addWidget(self.lineEdit_16)
        self.lineEdit_17 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.verticalLayout_3.addWidget(self.lineEdit_17)
        self.lineEdit_18 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.verticalLayout_3.addWidget(self.lineEdit_18)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.widget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.label_13 = QtGui.QLabel(self.groupBox_2)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_12.addWidget(self.label_13)
        self.label_14 = QtGui.QLabel(self.groupBox_2)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_12.addWidget(self.label_14)
        self.horizontalLayout_2.addLayout(self.verticalLayout_12)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.phaibs = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.phaibs.setMinimum(-180.0)
        self.phaibs.setMaximum(180.0)
        self.phaibs.setObjectName(_fromUtf8("phaibs"))
        self.verticalLayout_11.addWidget(self.phaibs)
        self.lbs = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.lbs.setMinimum(-90.0)
        self.lbs.setMaximum(90.0)
        self.lbs.setObjectName(_fromUtf8("lbs"))
        self.verticalLayout_11.addWidget(self.lbs)
        self.horizontalLayout_2.addLayout(self.verticalLayout_11)
        self.gridLayout_7.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.calc = QtGui.QPushButton(self.splitter)
        self.calc.setObjectName(_fromUtf8("calc"))
        self.groupBox_3 = QtGui.QGroupBox(self.splitter_2)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.webView = QtWebKit.QWebView(self.groupBox_3)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("file:///C:/Users/EngSh/Desktop/satellite_project/final/map.html")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.gridLayout_4.addWidget(self.webView, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.splitter_3 = QtGui.QSplitter(self.groupBox_4)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.widget1 = QtGui.QWidget(self.splitter_3)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_21 = QtGui.QLabel(self.widget1)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_5.addWidget(self.label_21)
        self.label_22 = QtGui.QLabel(self.widget1)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_5.addWidget(self.label_22)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_5)
        self.label_23 = QtGui.QLabel(self.widget1)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.horizontalLayout_12.addWidget(self.label_23)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_24 = QtGui.QLabel(self.widget1)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.horizontalLayout_8.addWidget(self.label_24)
        self.label_25 = QtGui.QLabel(self.widget1)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.horizontalLayout_8.addWidget(self.label_25)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_8)
        self.verticalLayout_13.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.Azlabel = QtGui.QLabel(self.widget1)
        self.Azlabel.setFrameShape(QtGui.QFrame.Box)
        self.Azlabel.setFrameShadow(QtGui.QFrame.Plain)
        self.Azlabel.setObjectName(_fromUtf8("Azlabel"))
        self.horizontalLayout_9.addWidget(self.Azlabel)
        self.Ellabel = QtGui.QLabel(self.widget1)
        self.Ellabel.setFrameShape(QtGui.QFrame.Box)
        self.Ellabel.setObjectName(_fromUtf8("Ellabel"))
        self.horizontalLayout_9.addWidget(self.Ellabel)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_9)
        self.Declabel = QtGui.QLabel(self.widget1)
        self.Declabel.setFrameShape(QtGui.QFrame.Box)
        self.Declabel.setObjectName(_fromUtf8("Declabel"))
        self.horizontalLayout_11.addWidget(self.Declabel)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.Dlabel = QtGui.QLabel(self.widget1)
        self.Dlabel.setFrameShape(QtGui.QFrame.Box)
        self.Dlabel.setObjectName(_fromUtf8("Dlabel"))
        self.horizontalLayout_10.addWidget(self.Dlabel)
        self.Rlabel = QtGui.QLabel(self.widget1)
        self.Rlabel.setFrameShape(QtGui.QFrame.Box)
        self.Rlabel.setObjectName(_fromUtf8("Rlabel"))
        self.horizontalLayout_10.addWidget(self.Rlabel)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)
        self.verticalLayout_13.addLayout(self.horizontalLayout_11)
        self.gridLayout_2.addWidget(self.splitter_3, 1, 0, 2, 2)
        self.gridLayout_3.addWidget(self.groupBox_4, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1562, 38))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.calc.clicked.connect(self.calculations)
        self.sname.currentIndexChanged.connect(self.combo)
        
    def combo(self):
        name = str(self.sname.currentText())
        value = float(satellites.get(name))
        self.phaiss.setValue(value)
        
    def calculations(self):
        print "Calculating... "
        Re=6378
        aGEO=42164
        C = 3 * 10**5
        #lamda= input("enter your Latitude: ")
        #Qe= input("enter your Longitude: ")
        #Qss= input("enter satellite Longitude: ")
        
        #name = self.sname.currentText()
        #self.phaiss.setValue(_fromUtf8(int(satellites[name])))
        Qss = self.phaiss.value()
        Qe = self.phaibs.value()
        lamda = self.lbs.value()
        
        B= float(Qe)-float(Qss)
        print "B= " ,B
        b=math.degrees(math.acos(math.cos(math.radians(B))*math.cos(math.radians(lamda))))
        print "b= ", b
        A=math.degrees(math.asin((math.degrees(math.sin(math.radians(abs(B)))))/(math.degrees(math.sin(math.radians(b))))))
        print "A= ",A
        if lamda>0 and B>0:
            Az= 180-A
        elif lamda<0 and B<0:
            Az=A
        elif lamda>0 and B<0:
            Az=180-A
        elif lamda<0 and B>0:
            Az=360-A
        print "The Azimuth angle is :", Az
        self.Azlabel.setText(_fromUtf8(str(Az)))
        x=math.cos(math.radians(b))
        z=(math.pow(Re,2)+math.pow(aGEO,2)-(2*Re*aGEO*x))
        d=math.sqrt(z)
        print "d= :",d
        self.Dlabel.setText(_fromUtf8(str(d)))
        EL=math.degrees(math.acos(math.radians((aGEO/d)*math.degrees(math.sin(math.radians(b))))))
        print "The Elevation angle is :",EL
        self.Ellabel.setText(_fromUtf8(str(EL)))
        R = 2 * (d/C)
        self.Rlabel.setText(_fromUtf8(str(R)))
        dec = 90 - lamda - EL
        self.Declabel.setText(_fromUtf8(str(dec)))
        print 'Declination Angle : ', dec
        print 'Round Trip = ', R

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Satellite (BETA 0.1)", None))
        self.groupBox.setTitle(_translate("MainWindow", "Satellite\'s Information", None))
        self.label.setText(_translate("MainWindow", "Name", None))
        self.label_2.setText(_translate("MainWindow", "Type", None))
        self.label_3.setText(_translate("MainWindow", "Longitude", None))
        self.label_4.setText(_translate("MainWindow", "Frequency", None))
        self.label_5.setText(_translate("MainWindow", "Dish Size", None))
        self.label_6.setText(_translate("MainWindow", "Parameter", None))
        self.stype.setPlaceholderText(_translate("MainWindow", "Enter Satellite\'s Type", None))
        self.lineEdit_16.setPlaceholderText(_translate("MainWindow", "Enter Operating Frequency", None))
        self.lineEdit_17.setPlaceholderText(_translate("MainWindow", "Enter Antenna Dish Size", None))
        self.lineEdit_18.setPlaceholderText(_translate("MainWindow", "Enter Orbital parameter", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "User\'s Information", None))
        self.label_13.setText(_translate("MainWindow", "User\'s Longitude", None))
        self.label_14.setText(_translate("MainWindow", "User\'s Latitude", None))
        self.calc.setText(_translate("MainWindow", "Calculate", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Google Map", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Output", None))
        self.label_21.setText(_translate("MainWindow", "Azimuth", None))
        self.label_22.setText(_translate("MainWindow", "Elevation", None))
        self.label_23.setText(_translate("MainWindow", "Declination Angle", None))
        self.label_24.setText(_translate("MainWindow", "Distance", None))
        self.label_25.setText(_translate("MainWindow", "Round Trip", None))

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

