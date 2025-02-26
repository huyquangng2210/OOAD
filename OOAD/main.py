from PyQt6 import QtCore, QtGui,QtWidgets,uic
from PyQt6.QtWidgets import QDialog,QApplication,QMessageBox,QMainWindow,QListWidgetItem
from PyQt6.uic import loadUi
import sys
import mysql.connector
import datetime

#xu ly

class loginUi(QMainWindow): #login window
    def __init__(self):
        super(loginUi,self).__init__()
        uic.loadUi('login.ui',self) #goi ui chuong trinh
        self.SignIn.clicked.connect(self.login) # nut signin
        self.SignUp.clicked.connect(self.register)#nut signup


    def login(self):
        un = self.UserName.text() #nhan ra ten tu man dang nhap
        pw = self.UserPW.text()#nhan ra mat khau tu man dang nhap
        db = mysql.connector.connect(user='root', password='root', host='localhost',database= 'OOAD')
        cs = db.cursor()
        cs.execute("select * from Users where Username = '"+un+"' and Password='"+pw+"'")  #chon tai khoan
        kt = cs.fetchone()
        if kt: #neu tai khoan co ton tai
            QMessageBox.information(self,"Loginouput","Login success") #hien thong bao dang nhap thanh cong
            cs.execute("select Role from Users where Username = '"+un+"' and Password='"+pw+"'") #chon role de hien ra cua so phu hop cho tung vi tri
            usercol=cs.fetchone() #
            if (usercol[0]=="Doctor"):
                doctor_l = doctorUi(un,pw)
                widget.addWidget(doctor_l)
                widget.setCurrentIndex(1)
            if(usercol[0]=="Patient"):
                patient_l = patientUi(un,pw)
                widget.addWidget(patient_l)
                widget.setCurrentIndex(1)
            if (usercol[0] == "Admin"):
                admin_l = adminUi(un, pw)
                widget.addWidget(admin_l)
                widget.setCurrentIndex(1)
        else:
            QMessageBox.information(self,"LoginOutput","Login fail")
    def register(self):
        form =formUi()
        widget.addWidget(form)
        widget.setCurrentIndex(1)
class adminUi(QMainWindow):
    def __init__(self,un:str,pw:str):
        super(adminUi, self).__init__()
        uic.loadUi('admin.ui', self)
        widget.setFixedHeight(900)
        widget.setFixedWidth(890)
        self.changeState.clicked.connect(self.deleteCalender)
        now = datetime.datetime.now()
        now = now.date()
        now.strftime('%Y-%M-%D')
        self.updateTaskList(now)
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.changeState.clicked.connect(self.deleteCalender)
        self.setBill()
        #setup table hoa don
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 100)
        self.tableWidget.setColumnWidth(5, 100)
        self.tableWidget.setHorizontalHeaderLabels(["Nha sỹ", "Bệnh nhân", "Dịch vụ","Số lượng","Đơn giá","Thành tiền"])
        self.setBill()
        #setup table lich
        self.tableWidget2.setColumnWidth(0, 80)
        self.tableWidget2.setColumnWidth(1, 80)
        self.tableWidget2.setColumnWidth(2, 80)
        self.tableWidget2.setColumnWidth(3, 80)
        self.tableWidget2.setHorizontalHeaderLabels(["Bệnh nhân", "Nha sỹ","Thời gian", "Trạng thái"])
    def calendarDateChanged(self):# sau moi lan thay doi cap nhat listwidget
        print("The calendar date was changed.")
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        print("Date selected:", dateSelected)
        self.updateTaskList(dateSelected)
        return dateSelected
    def updateTaskList(self, date): #doc du lieu tu database ve lich hen moi ngay
        self.tableWidget2.clear()
        db = mysql.connector.connect(user='root', password='root', host='localhost',database= 'OOAD')
        cs = db.cursor()
        formatted_date = date.strftime("%Y-%m-%d")
        #benh nhan , nha sy,thoi gian,trang thai
        cs.execute("select up.Username,ud.Username,a.time, a.Status from appointment a left join dentist d on a.DentistId = d.id left join patient p on a.PatientId = p.id left join Users ud on ud.id = d.userId left join Users up on up.id = p.userId where date = '"+formatted_date+"'order by a.time")

        results = cs.fetchall()
        self.tableWidget2.setRowCount(100)
        tablerow = 0
        #
        for row in results:
            self.tableWidget2.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget2.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget2.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            tablerow += 1
        self.tableWidget2.setHorizontalHeaderLabels(["Bệnh nhân", "Nha sỹ","Thời gian", "Trạng thái"])

    def deleteCalender(self):#chua xong
        index = self.tableWidget2.currentRow()
        selected_item = self.tableWidget2.currentItem()
        print(index)
        # Delete the item
        if selected_item is not None:
            db = mysql.connector.connect(user='root', password='root', host='localhost', database='OOAD')
            cs = db.cursor()
            bb = db.cursor()
            print()
            date = self.calendarDateChanged()
            formatted_date = date.strftime("%Y-%m-%d")

            cs.execute(
                "select a.id from appointment a left join dentist d on a.DentistId = d.id left join patient p on a.PatientId = p.id left join Users ud on ud.id = d.userId left join Users up on up.id = p.userId where date = '"+formatted_date+"'order by a.time")
            results = cs.fetchall()
            bb.execute("delete from bill where AppointmentId = '"+str(results[index][0])+"'")
            bb.execute("delete from appointment where id = '"+str(results[index][0])+"'")

            db.commit()
            self.updateTaskList(date)
            QMessageBox.information(self, "LoginOutput", "Update thanh cong")
        # selected_item = self.listWidget.currentItem()
        # print(selected_item)
        # date = self.calendarDateChanged()
        # formatted_date = date.strftime("%Y-%m-%d")
        # if selected_item is not None:
        #     index = self.listWidget.currentRow()# row(selected_item)
        # print(index)
        # db = mysql.connector.connect(user='root', password='root', host='localhost', database='OOAD')
        # cs = db.cursor()
        # bb = db.cursor()
        # formatted_date = date.strftime("%Y-%m-%d")
        #
        # cs.execute(
        #     "select up.Username, a.time, a.Status, a.PatientId, a.DentistId, a.date from appointment a left join dentist d on a.DentistId = d.id left join patient p on a.PatientId = p.id left join Users ud on ud.id = d.userId left join Users up on up.id = p.userId where date = %s and ud.Username = %s order by a.time",
        #     (formatted_date, self.un))
        # results = cs.fetchall()
        # lresults = list(results)
        # print(lresults)
        # print(index)
        # for i in range(len(results)):
        #     lresults[i] = list(results[i])
        # if results[index][2] == 'CF':
        #     lresults[index][2] = 'NCF'
        # else:
        #     lresults[index][2] = 'CF'
        # print(lresults[index][2], results[index][0], self.un, results[index][1], formatted_date)
        # bb.execute(
        #     "update appointment set Status = %s where PatientId = %s and DentistId = %s and time = %s and date = %s",
        #     (lresults[index][2], results[index][3], results[index][4], results[index][1], formatted_date))
        # db.commit()
        # self.updateTaskList(date)
        # QMessageBox.information(self, "LoginOutput", "Update thanh cong")
    def setBill(self):#hien bill ra
        db = mysql.connector.connect(user='root', password='root', host='localhost', database='OOAD')
        cs = db.cursor()
        #nha sy, benh nhan, dich vu, so luong, don gia, thanh tien
        cs.execute("select b.doctor,b.patient,s.ServiceName,B.quantity,s.price,B.Subtotal from bill b left join Billdetail B on b.BilldetailId = B.id left join services s on B.serviceId = s.id where b.Date = CURDATE()")
        results = cs.fetchall() #ma tran
        self.tableWidget.setRowCount(100)

        tablerow = 0
        # cs.execute("SELECT ServiceName , price, Description FROM services")
        # results = cs.fetchall()
        # self.tableWidget.setRowCount(40)
        for row in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            tablerow += 1

class doctorUi(QMainWindow) : # doctor window
    def __init__(self,un:str,pw:str):
        super(doctorUi, self).__init__()
        uic.loadUi('doctor2.ui', self) #
        widget.setFixedHeight(900)
        widget.setFixedWidth(890)
        self.un = un
        self.pw = pw
        now = datetime.datetime.now()
        now = now.date()
        now.strftime('%Y-%M-%D')
        self.updateTaskList(now)
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged) #voi moi thao tac thay doi tren lich se hien ra cac thong bao khac nhau
        self.changeState.clicked.connect(self.ChangestateCF) #nut thay doi trang thai
        self.cfRc.clicked.connect(self.CfRc)
        self.sendRc.clicked.connect(self.insertintoBill)
        #setup table hoa don
        self.tableWidget.setColumnWidth(0, 80)
        self.tableWidget.setColumnWidth(1, 80)
        self.tableWidget.setColumnWidth(2, 80)
        self.tableWidget.setColumnWidth(3, 80)
        self.tableWidget.setHorizontalHeaderLabels(["Bệnh nhân", "Thời gian", "Trạng thái", "ID cuộc hẹn"])

    def calendarDateChanged(self):# sau moi lan thay doi cap nhat listwidget
        print("The calendar date was changed.")
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        print("Date selected:", dateSelected)
        self.updateTaskList(dateSelected)
        return dateSelected
    def updateTaskList(self, date): #doc du lieu tu database ve lich hen moi ngay
        self.tableWidget.clear()
        db = mysql.connector.connect(user='root', password='root', host='localhost',database= 'OOAD')
        cs = db.cursor()
        formatted_date = date.strftime("%Y-%m-%d")
        #benh nhan , thoi gian, trang thai , id cuoc hen
        cs.execute("select up.Username,a.time, a.Status,a.id from appointment a left join dentist d on a.DentistId = d.id left join patient p on a.PatientId = p.id left join Users ud on ud.id = d.userId left join Users up on up.id = p.userId where date = %s and ud.Username = %s order by a.time",(formatted_date,self.un))
        results = cs.fetchall()
        self.tableWidget.setRowCount(100)

        tablerow = 0

        for row in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            tablerow += 1
        self.tableWidget.setHorizontalHeaderLabels(["Bệnh nhân", "Thời gian", "Trạng thái", "ID cuộc hẹn"])
    def ChangestateCF(self):#nut thay doi trang thai
            # Get the selected item
            index = self.tableWidget.currentRow()
            selected_item = self.tableWidget.currentItem()
            print(index)
            # Delete the item
            if selected_item is not None:
                db = mysql.connector.connect(user='root', password='root', host='localhost', database='OOAD')
                cs = db.cursor()
                bb = db.cursor()
                date = self.calendarDateChanged()
                formatted_date = date.strftime("%Y-%m-%d")

                cs.execute("select up.Username, a.time, a.Status, a.PatientId, a.DentistId, a.date from appointment a left join dentist d on a.DentistId = d.id left join patient p on a.PatientId = p.id left join Users ud on ud.id = d.userId left join Users up on up.id = p.userId where date = %s and ud.Username = %s order by a.time",(formatted_date,self.un))
                results = cs.fetchall()
                lresults = list(results)
                print(lresults)
                print(index)
                for i in range(len(results)):
                    lresults[i] = list(results[i])
                if results[index][2] =='CF':
                    lresults[index][2] = 'NCF'
                else:
                    lresults[index][2] = 'CF'
                print(lresults[index][2],results[index][0],self.un,results[index][1],formatted_date)
                bb.execute("update appointment set Status = %s where PatientId = %s and DentistId = %s and time = %s and date = %s",(lresults[index][2],results[index][3],results[index][4],results[index][1],formatted_date))
                db.commit()
                self.updateTaskList(date)
                QMessageBox.information(self, "LoginOutput", "Update thanh cong")

    def CfRc(self): #lay thong tin dien hoa don qua nut Xac nhan
        AI = self.apmID.text()
        Pt = self.ptName.text()
        Dt = self.dtName.text()
        Date = self.ngayKham.date()
        Date = Date.toPyDate()
        Date = Date.strftime("%Y-%m-%d")
        Time = self.timeEdit.time()
        Time = Time.toString()
        Sv = self.service.currentText()
        Qt = self.quantity.text()
        Qt = int(Qt)
        db = mysql.connector.connect(user='root', password='root', host='localhost', database='OOAD')
        cs = db.cursor()
        cs.execute("select * from services where ServiceName = '"+Sv+"'") #
        Sv = cs.fetchone()
        Sv = list(Sv)
        Psv = Sv[3]  # gia dich vu
        Psv = int(Psv)
        Isv = Sv[0]  # Id dich vu
        totalBill = Psv * Qt
        self.Tongtien.setText(f"Tổng số tiền là: {totalBill}")
        return AI,Pt,Dt,Date,Time,Sv,Qt,Psv,Isv,totalBill

    @staticmethod
    def insertintoBilldetail(ServiceId, quantity, Subtotal):#truyen gia tri vao bang Billdetail
        db = mysql.connector.connect(user='root', password='root', host='localhost', database='OOAD')
        cs = db.cursor()
        cs.execute("insert into Billdetail(ServiceId, quantity,Subtotal) values (%s,%s,%s)",
                   (ServiceId, quantity, Subtotal))
        db.commit()
        cs = db.cursor()
        cs.execute("select max(id) from Billdetail ")
        id = cs.fetchone()
        id = list(id)
        id = id[0]
        id = str(id)
        return id
    def insertintoBill(self): #truyen gia tri vao bang Bill
        AI,Pt,Dt,Date,Time,Sv,Qt,Psv,Isv,totalBill =self.CfRc()
        id = self.insertintoBilldetail(Isv,Qt,totalBill)
        db = mysql.connector.connect(user='root', password='root', host='localhost', database='OOAD')
        cs = db.cursor()
        print(type(AI))
        print(type(Date))
        print(Date)
        print(type(Time))
        print(type(Dt))
        print(type(Pt))
        print(type(id))


        cs.execute("insert into bill(AppointmentId, Date,time,doctor,patient,BilldetailId,Status) values (%s,%s,%s,%s,%s,%s,%s)",
                   (AI, Date, Time,Dt,Pt,id,'NCF'))
        db.commit()
        QMessageBox.information(self, "Hóa đơn", "Hóa đơn được gửi thành công")

class patientUi(QMainWindow) : # doctor window
    def __init__(self,un:str,pw:str):

        super(patientUi, self).__init__()
        uic.loadUi('patient.ui', self)
        self.un = un
        self.pw = pw

        widget.setFixedHeight(683)
        widget.setFixedWidth(907)
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        now = datetime.datetime.now()
        now = now.date()
        now.strftime('%Y-%M-%D')
        self.updateTaskList(now)
        #chinh tabbar
        self.tabWidget.setCurrentIndex(0)
        self.menubar.setVisible(True)
        self.menu1.triggered.connect(self.showLichHen)
        self.menu2.triggered.connect(self.showLichSu)
        self.menu3.triggered.connect(self.showDichVu)
        self.menu4.triggered.connect(self.showTaiKhoan)

        self.tabWidget.tabBar().setVisible(True)
        self.l01.setText(f"Lịch của {self.un}")
        self.updateinf.clicked.connect(self.fillBang)
        self.Push.clicked.connect(self.addNew)
        #bang dich vu
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 350)
        self.tableWidget.setHorizontalHeaderLabels(["Dịch vụ", "Giá", "Mô tả"])

        self.loaddata()
        #bang lich su
        self.tableWidget2.setColumnWidth(0, 100)
        self.tableWidget2.setColumnWidth(1, 100)
        self.tableWidget2.setColumnWidth(3, 100)
        self.tableWidget2.setColumnWidth(4, 100)
        self.tableWidget2.setColumnWidth(5, 100)
        self.tableWidget2.setHorizontalHeaderLabels(["Nha sỹ", "Bệnh nhân", "Dịch vụ", "Số lượng", "Đơn giá", "Thành tiền"])
        self.setHistory()

        self.update_inf.clicked.connect(self.update_info)
        self.signOut.clicked.connect(self.SignOut)
    #loi thu vien
    def showLichHen(self):
        self.tabWidget.setCurrentIndex(0)
    def showLichSu(self):
        self.tabWidget.setCurrentIndex(0)
    def showDichVu(self):
        self.tabWidget.setCurrentIndex(0)
    def showTaiKhoan(self):
        self.tabWidget.setCurrentIndex(0)

    def fillBang(self):  #nut dang ki lich hen moi
        DN = self.DoctorName.currentText()
        Time = self.gioHen.time()
        print(Time)
        item =DN
        self.showLich.addItem(Time.toString()+":"+DN+": Chưa được xác nhận")
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        formatted_date = dateSelected.strftime("%Y-%m-%d")
        return DN,Time,formatted_date

    def addNew(self ): #Nut luu thay doi

        DN, Time, formatted_date = self.fillBang()
        self.showLich.takeItem(self.showLich.count()-1)
        db = mysql.connector.connect(user='root', password='root', host='localhost', database='OOAD')

        cs = db.cursor()

        cs.execute("select p.id from patient p left join Users U on p.userId = U.id where Username ='"+self.un+"'")#tim id cua user patient tu ten patient
        idPT=cs.fetchone()
        cs.execute("select d.id from dentist d left join Users U on d.userId = U.id where Username ='"+DN+"'")#tim id cua user doctor tu ten doctor
        idDT=cs.fetchone()
        idPt = list(idPT)
        idDT = list(idDT)
        cs.execute("INSERT INTO appointment (DentistId, PatientId, Status, date, time) VALUES (%s, %s, %s, %s, %s)",
                   (idDT[0], idPT[0], 'NCF', formatted_date, Time.toString()))
        db.commit()
        QMessageBox.information(self, "LoginOutput", "Them lich thanh cong")

    def calendarDateChanged(self):
        print("The calendar date was changed.")
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        print("Date selected:", dateSelected)
        self.updateTaskList(dateSelected)

    def updateTaskList(self, date):
        self.showLich.clear()
        db = mysql.connector.connect(user='root', password='root', host='localhost',database= 'OOAD')
        cs = db.cursor()
        formatted_date = date.strftime("%Y-%m-%d")
        cs.execute("select ud.Username, a.Status, a.time from appointment a left join dentist d on a.DentistId = d.id left join patient p on a.PatientId = p.id left join Users ud on ud.id = d.userId left join Users up on up.id = p.userId where date = %s and up.Username = %s",(formatted_date,self.un))
        results = cs.fetchall()
        print(type(results))
        lresults =list(results)
        for i in range(len(results)):
            lresults[i]= list(results[i])
        for result in lresults:
            if result[2] == 'CF':
                result[2] = 'Đã được xác nhận'
            else:
                result[2] = 'Chưa được xác nhận'
            item = QListWidgetItem(str(result[1])+' :'+str(result[0])+': '+str(result[2]))
            print(str(result[0])+str(result[1]))
            self.showLich.addItem(item)
    def loaddata(self):
        db = mysql.connector.connect(user='root', password='root', host='localhost', database='OOAD')
        cs = db.cursor()

        tablerow = 0
        cs.execute("SELECT ServiceName , price, Description FROM services")
        results = cs.fetchall()
        self.tableWidget.setRowCount(40)
        for row in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            tablerow += 1
    def SignOut(self):
            login_f =loginUi()
            widget.addWidget(login_f)
            widget.setCurrentIndex(0)
    def setHistory(self): #lay tu database hien ra bang lichsu
        db = mysql.connector.connect(user='root', password='root', host='localhost', database='OOAD')
        cs = db.cursor()
        # nha sy, ngay, gio, dich vu, so luong, thanh tien cua cai thang benh nhan
        cs.execute("select b.doctor,b.Date,b.time,s.ServiceName,B.quantity,B.Subtotal from bill b left join Billdetail B on b.BilldetailId = B.id left join services s on B.serviceId = s.id where b.patient = '"+self.un+"'order by b.Date desc")
        results = cs.fetchall()
        self.tableWidget2.setRowCount(100)

        tablerow = 0
        for row in results:
            self.tableWidget2.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1].strftime('%Y-%m-%d')))
            self.tableWidget2.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget2.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget2.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableWidget2.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            tablerow += 1
    def update_info(self):
        Firstname =self.Firstname.text()
        Lastname=self.Lastname.text()
        sex=self.sex.currentText()
        password_ud=self.password_ud.text()
        email=self.email.text()
        address=self.address.text()
        phone=self.phone.text()
        db = mysql.connector.connect(user='root', password='root', host='localhost', database='OOAD')
        cs = db.cursor()
        cs.execute("update Users set Firstname = %s ,Lastname = %s,Email = %s,Phone = %s,Address = %s, Sex = %s, Password = %s where UserName = %s and Password = %s",(Firstname,Lastname,email,phone,address,sex,password_ud,self.un,self.pw))
        db.commit()
        QMessageBox.information(self, "Cap nhat", "Cap nhat thanh cong")
class formUi(QMainWindow) : # doctor window
    def __init__(self):
        super(formUi, self).__init__()
        uic.loadUi('formsignup.ui', self)
        self.dkibut.clicked.connect(self.dki)
    def dki(self):
        name = self.lineEdit.text()
        phone = self.lineEdit_2.text()
        sex = self.comboBox_4.currentText()
        firstname = self.lineEdit_5.text()
        lastname = self.lineEdit_6.text()
        password = self.lineEdit_3.text()
        email = self.lineEdit_4.text()
        address=self.lineEdit_7.text()
        db = mysql.connector.connect(user='root', password='root', host='localhost', database='OOAD')
        cs = db.cursor()
        cs.execute(
            "insert into Users(Username,Email,Phone,Address,Sex,Password,Firstname,Lastname) values(%s,%s,%s,%s,%s,%s,%s,%s)",
            (name,  email, phone, address, sex, password,firstname,lastname))
        db.commit()
        QMessageBox.information(self, "Cap nhat", "Cap nhat thanh cong")

app =QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
Login_f = loginUi()


widget.addWidget(Login_f)
widget.setCurrentIndex(0)
widget.setFixedHeight(602)
widget.setFixedWidth(804)
widget.show()
app.exec()
