from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime

def main():
    root=Tk()
    app = Window1(root)
    root.config(bg="black")
    root.iconbitmap("E:/PROGRAMMING FUNDAMENTAL/PROGRAMMING FUNDAMENTAL/Projects/Pharmacy-Management-System/1665121.ico")
    #*********************************************window1********************************************
class Window1:
    def __init__(self, master):
        self.master= master
        self.master.title("Pharmacy Managment System")
        self.master.geometry("1350x750+0+0")
        self.frame = Frame(self.master,bg="black")
        self.frame.pack()
        self.username = StringVar()
        self.Password = StringVar()
        
        
        #*********************************************************LABELS**********************************************       
        
        self.LabelTitle = Label(self.frame,text=" '' Pharmacy Managment System''",
                                font=("Monotype Corsiva",50,"bold","italic","underline"),bd=20,bg="black",fg="white")
        self.LabelTitle.grid(row=0,columnspan=2,pady=20)
        
        self.LabelTitle = Label(self.frame,text="PROJECT BY MUHAMMAD RAFAY ",
                                font=("Monotype Corsiva",18,"bold","italic","bold","underline"),bd=20,bg="black",fg="white")
        self.LabelTitle.grid(row=15,columnspan=2,pady=10)
        
        #*************************************************LOGIN FRAME*******************************************
        
        self.loginframe1 = Frame (self.frame, width=1010,height=300 ,bd=20,relief="ridge",bg="black")
                                       
        self.loginframe1.grid(row=1,column=0)
        
        
        self.Loginframe2 = Frame (self.frame, width=1010,height=100 ,bd=20,relief="ridge",bg="black")
        self.Loginframe2.grid(row=2,column=0)
        
        
        self.Loginframe3 = Frame (self.frame, width=1010,height=200 ,bd=20,relief="ridge",bg="black")
        self.Loginframe3.grid(row=3,column=0,pady=2)
        #*******************************************************************************************************
        self.labelusername = Label(self.loginframe1,text="Username",
                                font=("Times new roman",30,"bold"),bd=20,bg="black",fg="white")
        self.labelusername.grid(row=0,column=0)
         
        self.txtusername = Entry(self.loginframe1,textvariable = self.username,
                                font=("Times new roman",30,"bold"),bd=22)
        self.txtusername.grid(row=0,column=1)
         
        self.labelPassword = Label(self.loginframe1,text="Password",
                                font=("Times new roman",30,"bold"),bd=20,bg="black",fg="white")
        self.labelPassword.grid(row=1,column=0)
         
        self.txtPassword = Entry(self.loginframe1,textvariable = self.Password,
                                font=("Times new roman",30,"bold"),bd=22)
        self.txtPassword.grid(row=1,column=1,padx=85)
        
        #*********************************************************************************************************
        
        
        self.btnLogin = Button(self.Loginframe2, text="LOGIN",width=17,font=("Times new roman",20,"bold","italic"),
                                command = self.Login_System,bg="black",fg="white")
        self.btnLogin.grid(row=0,column=0)
        
        self.btnReset = Button(self.Loginframe2, text="RESET",width=20,font=("Times new roman",20,"bold","italic"),
                                 command=self.Reset,bg="black",fg="white")
        self.btnReset.grid(row=0,column=1)
        
        self.btnExit= Button(self.Loginframe2, text="EXIT",width=20,font=("Times new roman",20,"bold","italic"),
                                     command = self.iExit,bg="black",fg="white")
        self.btnExit.grid(row=0,column=2)

        #*******************************************************************************************************
        
        self.btnRegistration = Button(self.Loginframe3,text="PATIENT REGISTRATION",
                                      state= DISABLED, command=self.Registration_window,
                                      font=("ariel",20,"bold"),bg="black",fg="white")
        self.btnRegistration.grid(row=0,column=0)
        
        self.btnHospital= Button(self.Loginframe3,text="PRESCRIPTION",
                                      font=("ariel",20,"bold"),
                                      state= DISABLED, command=self.Hospital_window,bg="black",fg="white")
        self.btnHospital.grid(row=0,column=1,pady=8,padx=22 )
       
        #***************************************************************************************************
    def Login_System(self):
        user = (self.username.get())
        pas = (self.Password.get())
        if (user == "rafay") and (pas == str(12345)):
            self.btnRegistration.config(state = NORMAL)
            self.btnHospital.config(state = NORMAL)
        else:
             tkinter.messagebox.askyesno("Pharmacy Managment System","You have entered invlaid details")
             self.btnRegistration.config(state = DISABLED)
             self.btnHospital.config(state = DISABLED)
             self.username.set("")
             self.Password.set("")
             self.txtusername.focus()
    def Reset(self):
        self.btnRegistration.config(state = DISABLED)
        self.btnHospital.config(state = DISABLED)
        self.username.set("")
        self.Password.set("")
        self.txtusername.focus()
        
    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Pharmacy Managment System","Confrom If you want to exit")
        if self.iExit > 0:
            self.master.destroy()
            return
    
    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)
        
    def Hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.newWindow)
        
                
class Window2:
    def __init__(self,master):
        self.master= master
        self.master.title("Patients Registration System")
        self.master.iconbitmap("E:/PROGRAMMING FUNDAMENTAL/PROGRAMMING FUNDAMENTAL/Projects/Pharmacy-Management-System/1665121.ico")
        self.master.geometry("1350x750+0+0")
        self.frame=Frame(self.master)
        self.frame.pack()

        DateofOrder=StringVar()
        DateofOrder.set(time.strftime("%d/%m/%Y"))
        
        
        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=IntVar()
        
        Firstname=StringVar()
        Surname=StringVar()
        Address=StringVar()
        Postcode=StringVar()
        Telephone=StringVar()
        Ref=StringVar()
        
        
        Membership=StringVar()
        Membership.set("0")
        #*******************************FUNCTION*************************************************
        def iExit():
            iExit = tkinter.messagebox.askyesno("Pharmacy Managment System","Confrom If you want to exit")
            if iExit > 0:
                self.master.destroy()
                return
        
        def Reset():
            
            Firstname.set("")
            Surname.set("")
            Address.set("")
            Postcode.set("")
            Telephone.set("")
            Ref.set("")
            Membership.set("0")
             
            var1.set("")
            var2.set("")
            var3.set("")
            var4.set(0)
            
            self.cboProve_of_ID.current(0)
            self.cboType_of_Member.current(0)
            self.cboMethod_of_Payment.current(0)
            self.txtMembership.config(state=DISABLED)
        
        def iResetRecord():
            iResetRecord = tkinter.messagebox.askokcancel("Pharmacy Managment System",
                                                       "Confrom If you want to reset the record")
            if iRestRecord > 0:
                Reset()
            elif iRestRecord <= 0:
                Reset()
                self.txtRecipt.delete("1.0",END)
                return
        
        def Ref_NO():
            
            x= random.randint(1000,100000)
            randomRef = str(x)
            Ref.set(randomRef)
        
        def Recipt():
            Ref_NO()
            self.txtReceipt.insert(END,"\t" + Ref.get()+"\t\t"+Firstname.get()+"\t\t"+Surname.get()
                                  +"\t\t" + Address.get() + "\t\t" + DateofOrder.get()+"\t\t"+Telephone.get()
                                  +"\t\t"+Membership.get()+"\n")
        def Membership_fees():
                
                if (var4.get() == 1):
                    self.txtMembership.configure(state=NORMAL)
                    Item1 = (50)
                    Membership.set("RS"+str(Item1))
                    
                elif(var4.get() == 0):
                    self.txtMembership.configure(state=DISABLED)
            
                    Membership.set("0")
        
        #*******************************FRAME*****************************************************
                    
        Mainframe=Frame(self.frame)
        Mainframe.grid()
        
        TitleFrame=Frame(Mainframe, bd=20, width=1350,padx=35,relief=RIDGE)
        TitleFrame.pack(side=TOP)
        
        self.lblTitle=Label(TitleFrame,font=("Monotype Corsiva",59,"bold","underline"),
                            text="Patient Registration",padx=4)
        self.lblTitle.grid()
        
        #*******************************LOWER FRAME***********************
        
        MemberDetailsFrame = LabelFrame(Mainframe,width=1350,height=500,bd=20,pady=5,relief=RIDGE)
        MemberDetailsFrame.pack(side=BOTTOM)
        
        FrameDetails = LabelFrame(MemberDetailsFrame, bd=10,width=880,height=400,relief=RIDGE)
        FrameDetails.pack(side=LEFT)
        
        MemberName_F = LabelFrame(FrameDetails, bd=10,width=350,height=400,
                                  font=("ariel",12,"bold"),text="Custome Name",relief=RIDGE)
        MemberName_F.grid(row=0,column=0)
        
        Recipt_Button_Frame = LabelFrame(MemberDetailsFrame, bd=10,width=1000,height=400,relief=RIDGE)
        Recipt_Button_Frame.pack(side=RIGHT)

#******************************************************************************************************
        self.lblReferenceNO=Label(MemberName_F,font=("ariel",14,"bold"),text="Reference NO" , bd=7)
        self.lblReferenceNO.grid(row=0,column=0,sticky=W)
        self.txtReferenceNO=Entry(MemberName_F,font=("ariel",14,"bold"),text="Reference NO" , bd=7,textvariable=Ref,
                                  state = DISABLED, insertwidth=2)
        self.txtReferenceNO.grid(row=0,column=1)
        
        self.lblFirstname=Label(MemberName_F,font=("ariel",14,"bold"),text="Firstname" , bd=7)
        self.lblFirstname.grid(row=1,column=0,sticky=W)
        self.txtFirstname=Entry(MemberName_F,font=("ariel",14,"bold"),insertwidth=2,
                                textvariable=Firstname)
        self.txtFirstname.grid(row=1,column=1)
        
        self.lblSurname=Label(MemberName_F,font=("ariel",14,"bold"),text="Surname" , bd=7)
        self.lblSurname.grid(row=2,column=0,sticky=W)
        self.txtsurname=Entry(MemberName_F,font=("ariel",14,"bold"),textvariable=Surname,insertwidth=2)
        self.txtsurname.grid(row=2,column=1)
        
        self.lblAddress=Label(MemberName_F,font=("ariel",14,"bold"),text="Address" , bd=7)
        self.lblAddress.grid(row=3,column=0,sticky=W)
        self.txtAddress=Entry(MemberName_F,font=("ariel",14,"bold"),textvariable=Address,insertwidth=2)
        self.txtAddress.grid(row=3,column=1)
        
        self.lblPostcode=Label(MemberName_F,font=("ariel",14,"bold"),text="Postcode" , bd=7)
        self.lblPostcode.grid(row=4,column=0,sticky=W)
        self.txtPostcode=Entry(MemberName_F,font=("ariel",14,"bold"),textvariable=Postcode,
                               insertwidth=2)
        self.txtPostcode.grid(row=4,column=1)
        
        self.lblTelePhone=Label(MemberName_F,font=("ariel",14,"bold"),text="Telephone" , bd=7)
        self.lblTelePhone.grid(row=5,column=0,sticky=W)
        self.txtTelePhone=Entry(MemberName_F,font=("ariel",14,"bold"),textvariable=Telephone,insertwidth=2)
        self.txtTelePhone.grid(row=5,column=1)
        
        self.lblDate=Label(MemberName_F,font=("ariel",14,"bold"),text="Date" , bd=7)
        self.lblDate.grid(row=6,column=0,sticky=W)
        self.txtDate=Entry(MemberName_F,font=("ariel",14,"bold"),bd=7,textvariable=DateofOrder,insertwidth=2)
        self.txtDate.grid(row=6,column=1)
        
        #**************************************MEMBER INFORMATION***********************************
        self.lblProve_of_ID = Label (MemberName_F,font=("ariel",14,"bold"),text="Prove of ID",bd=7)
        self.lblProve_of_ID.grid(row=7,column=0,sticky=W)
        
        self.cboProve_of_ID =ttk.Combobox(MemberName_F,textvariable = var1, state="readonly",
                                             font=("ariel",14,"bold"),width=19)
        self.cboProve_of_ID["value"] = ("","Pilot License", "Driving License","Passport","Student ID")
        self.cboProve_of_ID.current(0)
        self.cboProve_of_ID.grid(row=7,column=1)
            
        self.lblType_of_Member = Label (MemberName_F,font=("ariel",14,"bold"),text="Type of Member",
                                        bd=7)
        self.lblType_of_Member.grid(row=8,column=0,sticky=W)
        
        self.cboType_of_Member = ttk.Combobox (MemberName_F,textvariable = var2 ,state="readonly",font=("ariel",14,"bold"),width=19)
        self.cboType_of_Member["value"] = ("","Full member", "Annual membership","Pay as You Go","Honorary Member")
        self.cboType_of_Member.current(0)
        self.cboType_of_Member.grid(row=8,column=1)
        
        
        self.lblMethod_of_Payment = Label (MemberName_F,font=("ariel",14,"bold"),
                                           text="Method Of Payment",bd=7)
        self.lblMethod_of_Payment.grid(row=9,column=0,sticky=W)
        
        self.cboMethod_of_Payment = ttk.Combobox (MemberName_F,textvariable = var3 ,state="readonly",
                                                  font=("ariel",14,"bold"),width=19)
        self.cboMethod_of_Payment["value"] = ("","Visa Card", "Master card","Cash")
        self.cboMethod_of_Payment.current(0)
        self.cboMethod_of_Payment.grid(row=9,column=1)
        #**********************************CHK BUTTONS*******************************
        self.chkMembership = Checkbutton(MemberName_F,text="Patient Fees", variable=var4, onvalue = 1,
                            offvalue = 0,font=("ariel",16,"bold"),command = Membership_fees).grid(row=10,column=0,sticky=W)
        self.txtMembership = Entry(MemberName_F,bd=7,font=("ariel",16,"bold"),textvariable = Membership,insertwidth=2,state=DISABLED,justify=RIGHT)
        self.txtMembership.grid(row=10,column=1)
        #****************************RECIPT*********************
        self.lblLabel = Label(Recipt_Button_Frame,font=("ariel",10,"bold"),pady=10,
                              text="Patient Ref\tFirstname\tSurname\tAdress\t\tDate Reg\tTelephone\tPatient Paid",bd=7)
        self.lblLabel.grid(row=0,column=0,columnspan=4)
        
        self.txtReceipt = Text(Recipt_Button_Frame,width=112,height=22,font=("ariel",10,"bold"))
        self.txtReceipt.grid(row=1,column=0,columnspan=4)
        
        #***************************BUTTON*******************************
        self.btnRecipt = Button(Recipt_Button_Frame,padx=18,bd=7,font=("ariel",16,"bold"),width=13,
                              text="Receipt",command=Recipt).grid(row=2,column=0)
        
        self.btnReset = Button(Recipt_Button_Frame,padx=18,bd=7,font=("ariel",16,"bold"),width=13,
                              text="Reset",command=Reset).grid(row=2,column=1)
        
        self.btnExit = Button(Recipt_Button_Frame,padx=18,bd=7,font=("ariel",16,"bold"),width=13,
                              text="Exit",command=iExit).grid(row=2,column=2)
        #*******************************************************
        
        
        #*******************************************************
        self.quitButton = Button(self.frame, text="Quit",width=25,command=self.iExit)
        self.quitButton.grid(row=3,column=0)
        
    def close_window(self):
        self.master.destroy()
        
    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Pharmacy Managment System",
                                                 "Confrom If you want to exit?")
        if self.iExit > 0:
            self.master.destroy()
        else:
            selfnewWindow = Toplevel(self.master)
            self.app = Window2(self.newWindow)
            return
        #*********************************************************************************************
class Window3:
    def __init__(self,master):
        self.master= master
        self.master.title("PHARMACY Managment System")
        self.master.iconbitmap("E:/PROGRAMMING FUNDAMENTAL/PROGRAMMING FUNDAMENTAL/Projects/Pharmacy-Management-System/1665121.ico")
        self.master.geometry("1350x750+0+0")
        self.frame=Frame(self.master)
        self.frame.pack()
        #****************************************FRAME*******************************************
        
        #****************************************FRAME*******************************************
        
        cmbNameTablets=StringVar()
        Ref = StringVar()
        Dose = StringVar()
        NumberTablets = StringVar()
        Lot = StringVar()
        IssuedDate = StringVar()
        PossibleSideEffect = StringVar()
        FurtherInformation = StringVar()
        StorageAdvice = StringVar()
        DrivingUsingMachine = StringVar()
        HowtoUseMedication = StringVar()
        PatientID = StringVar()
        NHSNumber = StringVar()
        PatientName = StringVar()
        DateofBirth = StringVar()
        PatientAddress = StringVar()
        ExpDate=StringVar()
        DailyDose=StringVar()
        Prescription = StringVar()
        #*******************************************Function Decleration*************************************
        def iExit():
            iExit=tkinter.messagebox.askyesno("PHARMACY Managment System","Are you sure you want to exit")
            if iExit >0:
                self.master.destroy()
                return
        def iPrescription():
            self.txtPrescription.insert(END,"Name of Tablets: \t\t\t\t" + cmbNameTablets.get() + "\n")
            self.txtPrescription.insert(END,"Reference No: \t\t\t\t" + Ref.get() + "\n")
            self.txtPrescription.insert(END,"Dose: \t\t\t\t" + Dose.get() + "\n")
            self.txtPrescription.insert(END,"Name of Tablets \t\t\t\t" + NumberTablets.get() + "\n")
            self.txtPrescription.insert(END,"Lot: \t\t\t\t" + Lot.get() + "\n")
            self.txtPrescription.insert(END,"Issue Date: \t\t\t\t" +
                                        IssuedDate.get() + "\n")
            self.txtPrescription.insert(END,"Possible SideEffect: \t\t\t\t" +
                                        PossibleSideEffect.get() + "\n")
            self.txtPrescription.insert(END,"FurtherInformation: \t\t\t\t" + FurtherInformation.get() + "\n")
            self.txtPrescription.insert(END,"StorageAdvice: \t\t\t\t" + StorageAdvice.get() + "\n")
            self.txtPrescription.insert(END,"DrivingUsingMachine: \t\t\t\t" + DrivingUsingMachine.get() + "\n")
            self.txtPrescription.insert(END,"How To Use Medication? \t\t\t\t" + HowtoUseMedication.get() + "\n")
            self.txtPrescription.insert(END,"PatientID: \t\t\t\t" + PatientID.get() + "\n")
            self.txtPrescription.insert(END,"NHSNumber: \t\t\t\t" +  NHSNumber.get() + "\n")
            self.txtPrescription.insert(END,"Date of Birth: \t\t\t\t" + DateofBirth.get() + "\n")
            self.txtPrescription.insert(END,"Patient Name: \t\t\t\t" + PatientName.get() + "\n")
            self.txtPrescription.insert(END,"PatientAddress: \t\t\t\t" + PatientAddress.get() + "\n")
            self.txtPrescription.insert(END,"Daily Dose: \t\t\t\t" + DailyDose.get() + "\n")
            self.txtPrescription.insert(END,"Expiry Date: \t\t\t\t" + ExpDate.get() + "\n")
            return
        
        def iPrecriptionData():
            self.txtFrameDetail.insert(END, cmbNameTablets.get()+"\t\t"+ Ref.get()+"\t"+Dose.get()+"\t\t"+
                                       NumberTablets.get()+"\t"+Lot.get()+"\t"+IssuedDate.get() +"\t\t"+ExpDate.get()+"\t"+
                                       DailyDose.get()+"\t\t"+StorageAdvice.get()+"\t"+NHSNumber.get()+"\t\t"+PatientName.get()
                                       +"\t"+DateofBirth.get()+"\t"+PatientAddress.get()+"\n")
                                    
            return
        
        def iDelete():
            
            cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            PossibleSideEffect.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            DrivingUsingMachine.set("")
            HowtoUseMedication.set("")
            PatientID.set("")
            NHSNumber.set("")
            PatientName.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            self.txtPrescription.delete("1.0",END)
            self.txtFrameDetail.delete("1.0",END)
            
            return
        
        def iReset():
            
            cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            PossibleSideEffect.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            DrivingUsingMachine.set("")
            HowtoUseMedication.set("")
            PatientID.set("")
            NHSNumber.set("")
            PatientName.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            self.txtPrescription.delete("1.0",END)
            
            return
        
        
        MainFrame = Frame(self.frame)
        MainFrame.grid()
        
        TitleFrame=Frame(MainFrame,bd=20,width=1350,padx=20,relief=RIDGE)
        TitleFrame.pack(side=TOP)
        
        self.lblTitle = Label(TitleFrame, width=39,font=("Monotype Corsiva",40,"bold"),
                              text="PHARMACY Managment System\t",padx=8)
        self.lblTitle.grid()
        
        FrameDetail = Frame(MainFrame,bd=20,width=1350,height=100,padx=20,relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)
        
        ButtonFrame = Frame(MainFrame,bd=20,width=1350,height=50,padx=20,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        
        DataFrame = Frame(MainFrame,bd=20,width=1350,height=400,padx=20,relief=RIDGE)
        DataFrame.pack(side=BOTTOM)
        
        DataFrameLEFT = LabelFrame(DataFrame,bd=10,width=800,height=300,padx=20,relief=RIDGE,
                                   font=("ariel",12,"bold"),text="Patient Information")
        DataFrameLEFT.pack(side=LEFT)
        
        DataFrameRIGHT = LabelFrame(DataFrame,bd=10,width=450,height=300,padx=20,relief=RIDGE,
                                    font=("ariel",12,"bold"),text="Prescription")
        DataFrameRIGHT.pack(side=RIGHT)
        
        #***************************************************DataFrameLEFT************************************************************
        self.lblNameTablet=Label(DataFrameLEFT, font=("ariel",12,"bold"),text="Name of Tablets:",padx=2,pady=2)
        self.lblNameTablet.grid(row=0,column=0,sticky=W)
        
        self.cboNameTablet=ttk.Combobox(DataFrameLEFT,textvariable=cmbNameTablets,state="readonly",
                                        font=("ariel",12,"bold"),width=23)
        self.cboNameTablet["value"]=("Ibuprofe","CO-codamol","Paracetamol","Amlodipine")
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=0,column=1)
        
        self.FurtherInfo = Label(DataFrameLEFT,font=("ariel",12,"bold"),text="Further Information:",padx=2,pady=2)
        self.FurtherInfo.grid(row=0,column=2,sticky=W)
        self.txtFurtherInfo =Entry(DataFrameLEFT,font=("ariel",12,"bold"),textvariable=FurtherInformation, width=25 )
        self.txtFurtherInfo.grid(row=0,column=3)
        
        self.lblStorage=Label(DataFrameLEFT,font=("ariel",12,"bold"),text="Storage Advice:",padx=2,pady=2)
        self.lblStorage.grid(row=1,column=2,sticky=W)
        self.txtStorage=Entry(DataFrameLEFT,font=("ariel",12,"bold"),textvariable=StorageAdvice, width=25 )
        self.txtStorage.grid(row=1,column=3)
        
        self.lblRef=Label(DataFrameLEFT,font=("ariel",12,"bold"),text="Reference NO:",padx=2,pady=2)
        self.lblRef.grid(row=1,column=0,sticky=W)
        self.txtRef=Entry(DataFrameLEFT,font=("ariel",12,"bold"),textvariable=Ref, width=25 )
        self.txtRef.grid(row=1,column=1)
        
        self.lblDose=Label(DataFrameLEFT,font=("ariel",12,"bold"),text="Dose:",padx=2,pady=2)
        self.lblDose.grid(row=2,column=0,sticky=W)
        self.txtDose=Entry(DataFrameLEFT,font=("ariel",12,"bold"),textvariable=Dose, width=25 )
        self.txtDose.grid(row=2,column=1)
        
        self.lblDuseMachine=Label(DataFrameLEFT,font=("ariel",12,"bold"),text="Driving Machine:",padx=2,pady=2)
        self.lblDuseMachine.grid(row=2,column=2,sticky=W)
        self.txtDuseMachine=Entry(DataFrameLEFT,font=("ariel",12,"bold"),textvariable=DrivingUsingMachine, width=25 )
        self.txtDuseMachine.grid(row=2,column=3)
        
        self.lblNoOfTablets=Label(DataFrameLEFT,font=("ariel",12,"bold"),text="No of Tablets:",padx=2,pady=2)
        self.lblNoOfTablets.grid(row=3,column=0,sticky=W)
        self.txtNoOfTablets=Entry(DataFrameLEFT,font=("ariel",12,"bold"),textvariable=NumberTablets, width=25 )
        self.txtNoOfTablets.grid(row=3,column=1)
        
        self.lblUseMedication=Label(DataFrameLEFT,font=("ariel",12,"bold"),text="Medication:",padx=2,pady=2)
        self.lblUseMedication.grid(row=3,column=2,sticky=W)
        self.txtUseMedication=Entry(DataFrameLEFT,font=("ariel",12,"bold"),textvariable=HowtoUseMedication, width=25 )
        self.txtUseMedication.grid(row=3,column=3)
        
        self.lblLot=Label(DataFrameLEFT,font=("ariel",12,"bold"),text="Lot:",padx=2,pady=2)
        self.lblLot.grid(row=4,column=0,sticky=W)
        self.txtLot=Entry(DataFrameLEFT,font=("ariel",12,"bold"),textvariable=Lot, width=25 )
        self.txtLot.grid(row=4,column=1)
        
        self.lblPatientID=Label(DataFrameLEFT,font=("ariel",12,"bold"),text="Patient ID:",padx=2,pady=2)
        self.lblPatientID.grid(row=4,column=2,sticky=W)
        self.txtPatientID=Entry(DataFrameLEFT,font=("ariel",12,"bold"),textvariable=PatientID,width=25 )
        self.txtPatientID.grid(row=4,column=3)
        
        self.lblIssuedDate=Label(DataFrameLEFT,font=("ariel",12,"bold"),text="Issued Date",padx=2,pady=2)
        self.lblIssuedDate.grid(row=5,column=0,sticky=W)
        self.txtIssuedDate=Entry(DataFrameLEFT,font=("ariel",12,"bold"),textvariable=IssuedDate, width=25 )
        self.txtIssuedDate.grid(row=5,column=1)
        
        self.lblNHSNumber=Label(DataFrameLEFT,font=("ariel",12,"bold"),text="NHS Number:",padx=2,pady=2)
        self.lblNHSNumber.grid(row=5,column=2,sticky=W)
        self.txtNHSNumber=Entry(DataFrameLEFT,font=("ariel",12,"bold"),textvariable=NHSNumber, width=25 )
        self.txtNHSNumber.grid(row=5,column=3)
        
        self.lblExpDate=Label(DataFrameLEFT,font=("ariel",12,"bold"),text="Exp Date:",padx=2,pady=2)
        self.lblExpDate.grid(row=6,column=0,sticky=W)
        self.txtExpDate=Entry(DataFrameLEFT,font=("ariel",12,"bold"),textvariable=ExpDate, width=25 )
        self.txtExpDate.grid(row=6,column=1)
        
        
        self.lblPatientName=Label(DataFrameLEFT,font=("ariel",12,"bold"),text="Patient Name:",padx=2,pady=2)
        self.lblPatientName.grid(row=6,column=2,sticky=W)
        self.txtPatientName=Entry(DataFrameLEFT,font=("ariel",12,"bold"),textvariable=PatientName, width=25 )
        self.txtPatientName.grid(row=6,column=3)
        
        self.lblDailyDose=Label(DataFrameLEFT,font=("ariel",12,"bold"),text="Daily Dose:",padx=2,pady=2)
        self.lblDailyDose.grid(row=7,column=0,sticky=W)
        self.txtDailyDose=Entry(DataFrameLEFT,font=("ariel",12,"bold"),textvariable=DailyDose, width=25 )
        self.txtDailyDose.grid(row=7,column=1)
        
        self.lblDateofBirth=Label(DataFrameLEFT,font=("ariel",12,"bold"),text="Date of Birth:",padx=2,pady=2)
        self.lblDateofBirth.grid(row=7,column=2,sticky=W)
        self.txtDateofBirth=Entry(DataFrameLEFT,font=("ariel",12,"bold"),textvariable=DateofBirth, width=25 )
        self.txtDateofBirth.grid(row=7,column=3)
        
        self.lblSideEffects=Label(DataFrameLEFT,font=("ariel",12,"bold"),text="Side Effects:",
                                  padx=2,pady=2)
        self.lblSideEffects.grid(row=8,column=0,sticky=W)
        self.txtSideEffects=Entry(DataFrameLEFT,font=("ariel",12,"bold"),textvariable=PossibleSideEffect, width=25 )
        self.txtSideEffects.grid(row=8,column=1)
        
        self.lblPatientAddress=Label(DataFrameLEFT,font=("ariel",12,"bold"),text="Patient Address:",
                                     padx=2,pady=2)
        self.lblPatientAddress.grid(row=8,column=2,sticky=W)
        self.txtPatientAddress=Entry(DataFrameLEFT,font=("ariel",12,"bold"),textvariable=PatientAddress,
                                     width=25 )
        self.txtPatientAddress.grid(row=8,column=3)
        
        #**********************************************************************************************************
        
        self.txtPrescription=Text(DataFrameRIGHT, font=("ariel",12,"bold"),width = 43,height=12,padx=2,
                                  pady=6)
        self.txtPrescription.grid(row=0,column=0)
        
        #*********************************************************************************************************
        
        self.btnPrescription=Button(ButtonFrame, text="Prescription",font=("ariel",12,"bold"),width=24,bd=4,
                                    command=iPrescription)
        self.btnPrescription.grid(row=0,column=0)
        
        self.btnPrescriptionData=Button(ButtonFrame, text="Prescription Data",font=("ariel",12,"bold"),width=24,bd=4,
                                    command=iPrecriptionData)
        self.btnPrescriptionData.grid(row=0,column=1)
        self.btnDelete=Button(ButtonFrame, text="Delete",font=("ariel",12,"bold"),width=24,bd=4,
                                    command=iDelete)
        self.btnDelete.grid(row=0,column=2)
        
        self.btnReset=Button(ButtonFrame, text="Reset",font=("ariel",12,"bold"),width=24,bd=4,
                                    command=iReset)
        self.btnReset.grid(row=0,column=3)
        
        self.btnExit=Button(ButtonFrame, text="Exit",font=("ariel",12,"bold"),width=24,bd=4,
                                    command=iExit)
        self.btnExit.grid(row=0,column=4)
        
        #*********************************************************************************************************
        
        self.lblLabel = Label(FrameDetail,font=("ariel",10,"bold"),pady=8,
                              text="Name of Tablets\tReference No.\t Doseage\t NO. of Tablets\t Lot\t Issued Date\t Exp.Date\""
                                    "\tDaily Dose\tStorage Adv.\tNHS Number\t Patient Name\t DOB\t Address",)
        self.lblLabel.grid(row=0,column=0)
         
        self.txtFrameDetail=Text(FrameDetail,font=("ariel",12,"bold"),width =141,height=4,padx=2,pady=4)
        self.txtFrameDetail.grid(row=1,column=0)
         
        
        #**********************************************************************************************************
        
        self.txtPrescription=Text(DataFrameRIGHT, font=("ariel",12,"bold"),width = 43,height=12,padx=2,
                                  pady=6)
        self.txtPrescription.grid(row=0,column=0)
        
        #*********************************************************************************************************
        
        self.btnPrescription=Button(ButtonFrame, text="Prescription",font=("ariel",12,"bold"),width=24,bd=4,
                                    command=iPrescription)
        self.btnPrescription.grid(row=0,column=0)
        
        self.btnPrescriptionData=Button(ButtonFrame, text="Prescription Data",font=("ariel",12,"bold"),width=24,bd=4,
                                    command=iPrecriptionData)
        
        self.btnDelete=Button(ButtonFrame, text="Delete",font=("ariel",12,"bold"),width=24,bd=4,
                                    command=iDelete)
        self.btnDelete.grid(row=0,column=2)
        
        self.btnReset=Button(ButtonFrame, text="Reset",font=("ariel",12,"bold"),width=24,bd=4,
                                    command=iReset)
        self.btnReset.grid(row=0,column=3)
        
        self.btnExit=Button(ButtonFrame, text="Exit",font=("ariel",12,"bold"),width=24,bd=4,
                                    command=iExit)
        self.btnExit.grid(row=0,column=4)
        
        #*********************************************************************************************************
        
        self.lblLabel = Label(FrameDetail,font=("ariel",10,"bold"),pady=8,
                              text="Name of Tablets\tReference No,\t Doseage\t NO of Tablets\t Lot\t Issued Date\t Exp.Date"
                                    "\tDaily Dose\tStorage Adv\tNHS Number\t Patient Name\t DOB\t Address")
        self.lblLabel.grid(row=0,column=0)
         
        self.txtFrameDetail=Text(FrameDetail,font=("ariel",12,"bold"),width =141,height=4,padx=2,pady=4)
        self.txtFrameDetail.grid(row=1,column=0)
         
    
         
         

         



         
    
        
        
                                                                              
        
        
        
        

        
        
    
        
        
        

        
                                 
        
        
        
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        









        

if __name__=="__main__":
     main()
        
        
