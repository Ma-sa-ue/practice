# -*- coding: utf-8 -*-
# WARNING! All changes made in this file will be lost!
import baseball_1

from PyQt4 import QtCore, QtGui

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
##global_dic=[pitcher,catcher,first,second,third,rf,cf,LF,ss]

number_number = 1

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(607, 441)
        self.formLayout = QtGui.QFormLayout(Form)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pitcher_button = QtGui.QPushButton(Form)
        self.pitcher_button.setObjectName(_fromUtf8("pitcher_button"))
        self.verticalLayout.addWidget(self.pitcher_button)
        self.catcher_button = QtGui.QPushButton(Form)
        self.catcher_button.setObjectName(_fromUtf8("catcher_button"))
        self.verticalLayout.addWidget(self.catcher_button)
        self.first_button = QtGui.QPushButton(Form)
        self.first_button.setObjectName(_fromUtf8("first_button"))
        self.verticalLayout.addWidget(self.first_button)
        self.second_button = QtGui.QPushButton(Form)
        self.second_button.setObjectName(_fromUtf8("second_button"))
        self.verticalLayout.addWidget(self.second_button)
        self.third_button = QtGui.QPushButton(Form)
        self.third_button.setObjectName(_fromUtf8("third_button"))
        self.verticalLayout.addWidget(self.third_button)
        self.rf_button = QtGui.QPushButton(Form)
        self.rf_button.setObjectName(_fromUtf8("rf_button"))
        self.verticalLayout.addWidget(self.rf_button)
        self.cf_button = QtGui.QPushButton(Form)
        self.cf_button.setObjectName(_fromUtf8("cf_button"))
        self.verticalLayout.addWidget(self.cf_button)
        self.LF_button = QtGui.QPushButton(Form)
        self.LF_button.setObjectName(_fromUtf8("LF_button"))
        self.verticalLayout.addWidget(self.LF_button)
        self.ss_button = QtGui.QPushButton(Form)
        self.ss_button.setObjectName(_fromUtf8("ss_button"))
        self.verticalLayout.addWidget(self.ss_button)
        self.formLayout.setLayout(0, QtGui.QFormLayout.LabelRole, self.verticalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setText(_fromUtf8(""))
        self.label.setScaledContents(True)
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/unknown.jpg")))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setScaledContents(True)
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("images/unknown.jpg")))
        
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.textEdit_2 = QtGui.QTextEdit(Form)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.horizontalLayout_2.addWidget(self.textEdit_2)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.retranslateUi(Form)
        ##self.hello()
        ##QtCore.QObject.connect(self.pitcher_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pitcher_fan)
        QtCore.QObject.connect(self.pitcher_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_2.show)
        QtCore.QObject.connect(self.pitcher_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit.show)
        QtCore.QObject.connect(self.pitcher_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_2.show)
        QtCore.QObject.connect(self.pitcher_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textEdit.show)
        QtCore.QObject.connect(self.pitcher_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textEdit_2.show)
        #QtCore.QObject.connect(self.catcher_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.catcher_fun)
        QtCore.QObject.connect(self.catcher_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit.show)
        QtCore.QObject.connect(self.catcher_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textEdit.show)
        ##QtCore.QObject.connect(self.catcher_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_2.show)
        QtCore.QObject.connect(self.catcher_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textEdit_2.show)
        QtCore.QObject.connect(self.catcher_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_2.show)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pitcher_button.setText(_translate("Form", "Pitcher", None))
        self.catcher_button.setText(_translate("Form", "Catcher", None))
        self.first_button.setText(_translate("Form", "First baseman", None))
        self.second_button.setText(_translate("Form", "Second baseman", None))
        self.third_button.setText(_translate("Form", "Third baseman", None))
        self.rf_button.setText(_translate("Form", "Rightfielder", None))
        self.cf_button.setText(_translate("Form", "Centerfielder", None))
        self.LF_button.setText(_translate("Form", "Leftfielder", None))
        self.ss_button.setText(_translate("Form", "Shortstop", None))
        self.lineEdit.setText(_translate("Form", " Name", None))


class Trueclass(Ui_Form):
	def setupUi(self,Form):
		super(Trueclass,self).setupUi(Form)
		Form.setWindowTitle("MLB APP")
		self.linemyedit = QtGui.QLineEdit(Form)
		self.label.setScaledContents(True)
		self.label_2.setScaledContents(True)
		self.linemyedit.setObjectName(_fromUtf8("lineEdit"))
		self.verticalLayout.addWidget(self.linemyedit)
		self.linemyedit.setText(_translate("Form", " 1", None))
		self.textEdit_2.setText("DATA")
		self.textEdit.setText("DATA")
		self.lineEdit_2.setText("Name")
		QtCore.QObject.connect(self.pitcher_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pitcher_fun_1)
		##QtCore.QObject.connect(self.pitcher_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pitcher_fun_2)
		QtCore.QObject.connect(self.catcher_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.catcher_fun_1)
		##QtCore.QObject.connect(self.catcher_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.catcher_fun_2)
		QtCore.QObject.connect(self.first_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.first_fun_1)
		QtCore.QObject.connect(self.second_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.second_fun_1)
		QtCore.QObject.connect(self.third_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.third_fun_1)
		QtCore.QObject.connect(self.ss_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ss_fun_1)
		QtCore.QObject.connect(self.cf_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cf_fun_1)
		QtCore.QObject.connect(self.rf_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.rf_fun_1)
		QtCore.QObject.connect(self.LF_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.LF_fun_1)
		
	def catcher_fun_1(self):
		number_number = int(self.linemyedit.text())-1
		baseball_1.get_database2("c")
		name = baseball_1.get_name_batting("c",number_number)
		text_data = "AVERAGE "+str(name[1])+"\n"+"OEF "+str(name[2])+"\n"+"WAR "+str(name[4])
		self.textEdit.setText(text_data)
		judge = baseball_1.get_picture_2(name[0])
		self.label.setScaledContents(True)
		self.lineEdit.setText(name[0])
		if(judge==1):
			self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".jpg")))
		elif(judge==2):
			self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".png")))
		name = baseball_1.get_name_fielding("c",number_number)
		print name[0]
		judge = baseball_1.get_picture_2(str(name[0]))
		self.label_2.setScaledContents(True)
		self.lineEdit_2.setText(name[0])
		text_data = "AVERAGE "+str(name[1])+"\n"+"DEF "+str(name[3])+"\n"+"WAR "+str(name[4])
		self.textEdit_2.setText(text_data)
		if(judge==1):
			self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".jpg")))
		elif(judge==2):
			
			self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".png")))
				
	def first_fun_1(self):
		number_number = int(self.linemyedit.text())-1
		baseball_1.get_database2("1b")
		name = baseball_1.get_name_batting("1b",number_number)
		text_data = "AVERAGE "+str(name[1])+"\n"+"OEF "+str(name[2])+"\n"+"WAR "+str(name[4])
		self.textEdit.setText(text_data)
		judge = baseball_1.get_picture_2(name[0])
		self.label.setScaledContents(True)
		self.lineEdit.setText(name[0])
		if(judge==1):
			self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".jpg")))
		elif(judge==2):
			self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".png")))
		name = baseball_1.get_name_fielding("1b",number_number)
		print name[0]
		judge = baseball_1.get_picture_2(str(name[0]))
		self.label_2.setScaledContents(True)
		self.lineEdit_2.setText(name[0])
		text_data = "AVERAGE "+str(name[1])+"\n"+"DEF "+str(name[3])+"\n"+"WAR "+str(name[4])
		self.textEdit_2.setText(text_data)
		if(judge==1):
			self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".jpg")))
		elif(judge==2):
			
			self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".png")))
							
	def second_fun_1(self):
		number_number = int(self.linemyedit.text())-1
		baseball_1.get_database2("2b")
		name = baseball_1.get_name_batting("2b",number_number)
		text_data = "AVERAGE "+str(name[1])+"\n"+"OEF "+str(name[2])+"\n"+"WAR "+str(name[4])
		self.textEdit.setText(text_data)
		judge = baseball_1.get_picture_2(name[0])
		self.label.setScaledContents(True)
		self.lineEdit.setText(name[0])
		if(judge==1):
			self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".jpg")))
		elif(judge==2):
			self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".png")))
		name = baseball_1.get_name_fielding("2b",number_number)
		print name[0]
		judge = baseball_1.get_picture_2(str(name[0]))
		self.label_2.setScaledContents(True)
		self.lineEdit_2.setText(name[0])
		text_data = "AVERAGE "+str(name[1])+"\n"+"DEF "+str(name[3])+"\n"+"WAR "+str(name[4])
		self.textEdit_2.setText(text_data)
		if(judge==1):
			self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".jpg")))
		elif(judge==2):
			
			self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".png")))

	def third_fun_1(self):
		number_number = int(self.linemyedit.text())-1
		baseball_1.get_database2("3b")
		name = baseball_1.get_name_batting("3b",number_number)
		text_data = "AVERAGE "+str(name[1])+"\n"+"OEF "+str(name[2])+"\n"+"WAR "+str(name[4])
		self.textEdit.setText(text_data)
		judge = baseball_1.get_picture_2(name[0])
		self.label.setScaledContents(True)
		self.lineEdit.setText(name[0])
		if(judge==1):
			self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".jpg")))
		elif(judge==2):
			self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".png")))
		name = baseball_1.get_name_fielding("3b",number_number)
		print name[0]
		judge = baseball_1.get_picture_2(str(name[0]))
		self.label_2.setScaledContents(True)
		self.lineEdit_2.setText(name[0])
		text_data = "AVERAGE "+str(name[1])+"\n"+"DEF "+str(name[3])+"\n"+"WAR "+str(name[4])
		self.textEdit_2.setText(text_data)
		if(judge==1):
			self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".jpg")))
		elif(judge==2):
			
			self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".png")))

	def ss_fun_1(self):
		number_number = int(self.linemyedit.text())-1
		baseball_1.get_database2("ss")
		name = baseball_1.get_name_batting("ss",number_number)
		text_data = "AVERAGE "+str(name[1])+"\n"+"OEF "+str(name[2])+"\n"+"WAR "+str(name[4])
		self.textEdit.setText(text_data)
		judge = baseball_1.get_picture_2(name[0])
		self.label.setScaledContents(True)
		self.lineEdit.setText(name[0])
		if(judge==1):
			self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".jpg")))
		elif(judge==2):
			self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".png")))
		name = baseball_1.get_name_fielding("ss",number_number)
		print name[0]
		judge = baseball_1.get_picture_2(str(name[0]))
		self.label_2.setScaledContents(True)
		self.lineEdit_2.setText(name[0])
		text_data = "AVERAGE "+str(name[1])+"\n"+"DEF "+str(name[3])+"\n"+"WAR "+str(name[4])
		self.textEdit_2.setText(text_data)
		if(judge==1):
			self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".jpg")))
		elif(judge==2):
			
			self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".png")))
	def cf_fun_1(self):
		number_number = int(self.linemyedit.text())-1
		baseball_1.get_database2("cf")
		name = baseball_1.get_name_batting("cf",number_number)
		text_data = "AVERAGE "+str(name[1])+"\n"+"OEF "+str(name[2])+"\n"+"WAR "+str(name[4])
		self.textEdit.setText(text_data)
		judge = baseball_1.get_picture_2(name[0])
		self.label.setScaledContents(True)
		self.lineEdit.setText(name[0])
		if(judge==1):
			self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".jpg")))
		elif(judge==2):
			self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".png")))
		name = baseball_1.get_name_fielding("cf",number_number)
		print name[0]
		judge = baseball_1.get_picture_2(str(name[0]))
		self.label_2.setScaledContents(True)
		self.lineEdit_2.setText(name[0])
		text_data = "AVERAGE "+str(name[1])+"\n"+"DEF "+str(name[3])+"\n"+"WAR "+str(name[4])
		self.textEdit_2.setText(text_data)
		if(judge==1):
			self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".jpg")))
		elif(judge==2):
			
			self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".png")))

	def LF_fun_1(self):
		number_number = int(self.linemyedit.text())-1
		baseball_1.get_database2("lf")
		name = baseball_1.get_name_batting("lf",number_number)
		text_data = "AVERAGE "+str(name[1])+"\n"+"OEF "+str(name[2])+"\n"+"WAR "+str(name[4])
		self.textEdit.setText(text_data)
		judge = baseball_1.get_picture_2(name[0])
		self.label.setScaledContents(True)
		self.lineEdit.setText(name[0])
		if(judge==1):
			self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".jpg")))
		elif(judge==2):
			self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".png")))
		name = baseball_1.get_name_fielding("lf",number_number)
		print name[0]
		judge = baseball_1.get_picture_2(str(name[0]))
		self.label_2.setScaledContents(True)
		self.lineEdit_2.setText(name[0])
		text_data = "AVERAGE "+str(name[1])+"\n"+"DEF "+str(name[3])+"\n"+"WAR "+str(name[4])
		self.textEdit_2.setText(text_data)
		if(judge==1):
			self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".jpg")))
		elif(judge==2):
			self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".png")))
	def rf_fun_1(self):
		number_number = int(self.linemyedit.text())-1
		baseball_1.get_database2("rf")
		name = baseball_1.get_name_batting("rf",number_number)
		text_data = "AVERAGE "+str(name[1])+"\n"+"OEF "+str(name[2])+"\n"+"WAR "+str(name[4])
		self.textEdit.setText(text_data)
		judge = baseball_1.get_picture_2(name[0])
		self.label.setScaledContents(True)
		self.lineEdit.setText(name[0])
		if(judge==1):
			self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".jpg")))
		elif(judge==2):
			self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".png")))
		name = baseball_1.get_name_fielding("rf",number_number)
		print name[0]
		judge = baseball_1.get_picture_2(str(name[0]))
		self.label_2.setScaledContents(True)
		self.lineEdit_2.setText(name[0])
		text_data = "AVERAGE "+str(name[1])+"\n"+"DEF "+str(name[3])+"\n"+"WAR "+str(name[4])
		self.textEdit_2.setText(text_data)
		if(judge==1):
			self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".jpg")))
		elif(judge==2):
			
			self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name[0]+".png")))
	def pitcher_fun_1(self):
		baseball_1.get_database2("lf")
		name = baseball_1.get_name_batting("lf",number_number)
		judge = baseball_1.get_picture_2(name)
		self.label.setScaledContents(True)
		self.lineEdit.setText(name)
		if(judge==1):
			self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name+".jpg")))
		elif(judge==2):
			self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name+".png")))
		name = baseball_1.get_name_fielding("lf",number_number)
		judge = baseball_1.get_picture_2(name)
		self.label_2.setScaledContents(True)
		self.lineEdit_2.setText(name)
		if(judge==1):
			self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name+".jpg")))
		elif(judge==2):		
			self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("images/"+name+".png")))
		
	
		
		 
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Trueclass()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
