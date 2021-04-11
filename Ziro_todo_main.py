import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi
import psycopg2
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from create_new_db import *
from tab_widget import *


class login(QDialog):
    def __init__(self):
        super(login,self).__init__()
        loadUi('login.ui',self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)

    def messagebox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def warning(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def loginfunction(self):
        email=self.email.text()
        password=self.password.text()
        con = psycopg2.connect(db_config)
        cursor = con.cursor()
        query="select * from users where username=%s and password=%s"
        data=cursor.execute(query,(email,password))
        if (len(cursor.fetchall())>0):
            self.messagebox("Congratulations !", "Hi {} , You are sucessfully logged in".format(email))
            print("successfully logged in with email :", email, "and password", password)
            todo=ToDoWindow()
            widget.addWidget(todo)
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            self.warning("Incorrect ", "email or password")




    def gotocreate(self):
        Createacc=createacc()
        widget.addWidget(Createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)


class createacc(QDialog):
    def __init__(self):
        super(createacc,self).__init__()
        loadUi('createacc.ui',self)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)

        self.signupbutton.clicked.connect(self.createaccfunction)

    def messagebox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def warning(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def createaccfunction(self):
        email=self.email.text()
        if self.password.text()==self.confirmpass.text():
            password = self.password.text()
            confirm_password = self.confirmpass.text()
            con = psycopg2.connect(db_config)
            cursor = con.cursor()
            query="insert into users(username,password,confirm_password)values(%s,%s,%s)"
            data=cursor.execute(query,(email,password,confirm_password))
            con.commit()
            Login=login()
            widget.addWidget(Login)
            widget.setCurrentIndex(widget.currentIndex()+1)
            self.messagebox("successfully created account with {} !".format(email) ,"Kindly Login with your same credentials to access your ZIRO TODO List")
            print("successfully created account with email :", email, "and password", password)
        else:
            self.warning("Incorrect ","Password entered do not match")


class ToDoWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("ZIRO TODO LIST")
        self.setMinimumHeight(300)

        self.central_widget = TaskProjectTabs()
        self.setCentralWidget(self.central_widget)

        self.central_widget.task_exit_button.clicked.connect(self.close)
        self.central_widget.project_exit_button.clicked.connect(self.close)

if __name__ == "__main__":
    create_new_db(dbname='postgres')
    app = QApplication(sys.argv)
    mainwindow = login()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(780)
    widget.setFixedHeight(500)
    widget.show()
    app.exec()
    to_do = QApplication(sys.argv)


