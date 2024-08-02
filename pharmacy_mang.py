import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class Windows1:
    def __init__(self, master):
        self.master = master
        self.master.title("Pharmacy Management System")
        self.master.geometry("1350x750+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.LabelTitle = Label(self.frame, text="Pharmacy Management System", 
                                font=("Arial", 40, "bold"),
                                bd=10, relief="sunken")
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=20)

        self.Loginframe1 = Frame(self.frame, width=1000, height=300, bd=10, relief="groove")
        self.Loginframe1.grid(row=1, column=0)

        self.Loginframe2 = Frame(self.frame, width=1000, height=100, bd=10, relief="groove")
        self.Loginframe2.grid(row=2, column=0, pady=15)

        self.Loginframe3 = Frame(self.frame, width=1000, height=200, bd=10, relief="groove")
        self.Loginframe3.grid(row=3, column=0, pady=5)

        self.button_reg = Button(self.Loginframe3, text="Patient Registration Window", state=DISABLED, font=("Arial", 15, "bold"), command=self.Registration_window)
        self.button_reg.grid(row=0, column=0, padx=10, pady=5)

        self.button_Hosp = Button(self.Loginframe3, text="Hospital Window", state=DISABLED, font=("Arial", 15, "bold"), command=self.Hospital_window)
        self.button_Hosp.grid(row=0, column=1, padx=10, pady=5)

        
        # name and password frame
        self.LabelUsername = Label(self.Loginframe1, text="User Name", font=("Arial", 20, "bold"), bd=3)
        self.LabelUsername.grid(row=0, column=0)
        self.textUsername = Entry(self.Loginframe1, font=("Arial", 20, "bold"), bd=3, textvariable=self.Username)
        self.textUsername.grid(row=0, column=1, padx=40, pady=15)

        self.LabelPassword = Label(self.Loginframe1, text="Password", font=("Arial", 20, "bold"), bd=3)
        self.LabelPassword.grid(row=1, column=0)

        self.textPassword = Entry(self.Loginframe1, font=("Arial", 20, "bold"), show="*", bd=3, textvariable=self.Password)
        self.textPassword.grid(row=1, column=1, padx=40, pady=15)

        self.button_login = Button(self.Loginframe2, text="Login", width=20, font=("arial", 18, "bold"),
                                   command=self.login_system)
        self.button_login.grid(row=0, column=0, padx=10, pady=10)

        self.button_Reset = Button(self.Loginframe2, text="Reset", width=20, font=("arial", 18, "bold"),
                                   command=self.reset_btn)
        self.button_Reset.grid(row=0, column=1, padx=10, pady=10)

        self.button_Exit = Button(self.Loginframe2, text="Exit", width=20, font=("arial", 18, "bold"),
                                  command=self.Exit_btn)
        self.button_Exit.grid(row=0, column=2, padx=10, pady=10)

    def login_system(self):
        user = self.Username.get()
        pswd = self.Password.get()
        if user == "admin" and pswd == "admin":
            self.button_reg.config(state=NORMAL)
            self.button_Hosp.config(state=NORMAL)
            self.button_Dr_appt.config(state=NORMAL)
            self.button_med_stock.config(state=NORMAL)
        else:
            tkinter.messagebox.showerror("Pharmacy Management System", "You have entered an invalid username or password")
            self.button_reg.config(state=DISABLED)
            self.button_Hosp.config(state=DISABLED)
            self.button_Dr_appt.config(state=DISABLED)
            self.button_med_stock.config(state=DISABLED)
            self.reset_fields()

    def reset_fields(self):
        self.Username.set("")
        self.Password.set("")
        self.textUsername.focus()

    def reset_btn(self):
        self.button_reg.config(state=DISABLED)
        self.button_Hosp.config(state=DISABLED)
        self.button_Dr_appt.config(state=DISABLED)
        self.button_med_stock.config(state=DISABLED)

        self.Username.set("")
        self.Password.set("")
        self.textUsername.focus()

    def Exit_btn(self):
        self.Exit_btn = tkinter.messagebox.askyesno("Pharmacy Management System", "Are you sure you want to exit?")
        if self.Exit_btn > 0:
            self.master.destroy()
            return


    def exit_system(self):
        exit_confirmation = tkinter.messagebox.askyesno("Pharmacy Management System", "Do you want to exit the system?")
        if exit_confirmation:
            self.master.destroy()

    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Registration(self.newWindow)

    def Hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Hospital(self.newWindow)

    



class Registration:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Registration System")
        self.root.geometry("1350x700+0+0")
        self.root.configure(background="black")

        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))

        Ref = StringVar()
        Mobile_no = StringVar()
        Pincode = StringVar()
        Address = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()

        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4 = StringVar()
        var5 = IntVar()

        Membership = StringVar()
        Membership.set("0")

        ######## functions #######
        def exitbtt():
            exitbtt = tkinter.messagebox.askyesno("Member Registration System", "Are you sure yoyu want to exit ? ")
            if exitbtt > 0:
                root.destroy()
            else:
                self.newWindow = Toplevel(self.master)
                self.app = Registration(self.newWindow)
                return

        def resetbtt():
            Firstname.set("")
            Ref.set("")
            Mobile_no.set("")
            Pincode.set("")
            Address.set("")
            Lastname.set("")
            var1.set("")
            var2.set("")
            var3.set("")
            var4.set("")
            var5.set("")
            Membership.set("0")
            member_gendercmb.current(0)
            member_id_proofcmb.current(0)
            member_memtypecmb.current(0)
            member_paymentcmb.current(0)
            member_membershiptxt(state = DISABLED)

        def reeesetbtt():
            reeesetbtt = tkinter.messagebox.askokcancel("member Registration form","You want to add as new Record")
            if reeesetbtt > 0:
                resetbtt()
                return
            else:
                resetbtn()
                detail_labeltxt.delete("1.0", END)
                return

        def Reference_number():
            ranumber = random.randint(100000,9999999) 
            randomnumber = str(ranumber)
            Ref.set(randomnumber)

        def membership_fees():
            if (var5.get() == 1):
                member_membershiptxt.configure(state=NORMAL)
                item = float(15000)
                Membership.set(str(item)+ "Rs")
            elif var5.get() == 0:
                member_membershiptxt.configure(state=DISABLED)
                Membership.set("0") 

        def Receipt():
                        Reference_number()
                        detail_labeltxt.insert(END, "\t" + Date_of_Registration.get() + "\t" + Ref.get() + "\t" +
                        Firstname.get() + "\t" + Lastname.get() + "\t" + Mobile_no.get() + "\t" +
                        Address.get() + "\t" + Pincode.get() + "\t" + member_gendercmb.get() + "\t" + Membership.get() + "\n")
         


        ############ TITLE #############
        title = Label(self.root, text="Member Registration Form", font=("Monotype Corsiva", 30, "bold"), bd=5,
              relief=GROOVE, bg="#E6005C", fg="#000000")
        title.pack(side=TOP, fill=X)

        ########### member frame #########
        Manage_Frame = Frame(self.root, bd=4,relief= RIDGE, bg= "#001a66")
        Manage_Frame.place(x=20, y=100, width=450, height=630)


       

        ####### text, label, comboboxes in manage frame ######
        Cus_title = Label(Manage_Frame, text="Customer Details", font=("Arial", 20, "bold"), bg="#001a66", fg="white")
        Cus_title.grid(row=0, columnspan=2, pady=5)

        member_detailb1 = Label(Manage_Frame, text="Date", font=("Arial", 15, "bold"), bg="#001a66", fg="white")
        member_detailb1.grid(row=1, column=0, pady=5, padx=10, sticky="w")

        member_datatxt = Entry(Manage_Frame, font=("Arial", 15, "bold"), textvariable=Date_of_Registration)
        member_datatxt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        member_refb1 = Label(Manage_Frame, text="Reference ID", font=("Arial", 15, "bold"), bg="#001a66", fg="white")
        member_refb1.grid(row=2, column=0, pady=5, padx=10, sticky="w")

        member_reftxt = Entry(Manage_Frame, font=("Arial", 15, "bold"), state=DISABLED, textvariable=Ref)
        member_reftxt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        member_fnamelb1 = Label(Manage_Frame, text="First Name", font=("Arial", 15, "bold"), bg="#001a66", fg="white")
        member_fnamelb1.grid(row=3, column=0, pady=5, padx=10, sticky="w")

        member_fnametxt = Entry(Manage_Frame, font=("Arial", 15, "bold"), textvariable=Firstname)
        member_fnametxt.grid(row=3, column=1, pady=5, padx=10, sticky="w")

        member_lnamelb1 = Label(Manage_Frame, text="Last Name", font=("Arial", 15, "bold"), bg="#001a66", fg="white")
        member_lnamelb1.grid(row=4, column=0, pady=5, padx=10, sticky="w")

        member_lnametxt = Entry(Manage_Frame, font=("Arial", 15, "bold"), textvariable=Lastname)
        member_lnametxt.grid(row=4, column=1, pady=5, padx=10, sticky="w")

        member_mobilelb1 = Label(Manage_Frame, text="Mobile No", font=("Arial", 15, "bold"), bg="#001a66", fg="white")
        member_mobilelb1.grid(row=5, column=0, pady=5, padx=10, sticky="w")

        member_mobiletxt = Entry(Manage_Frame, font=("Arial", 15, "bold"), textvariable=Mobile_no)
        member_mobiletxt.grid(row=5, column=1, pady=5, padx=10, sticky="w")

        member_addresslb1 = Label(Manage_Frame, text="Address", font=("Arial", 15, "bold"), bg="#001a66", fg="white")
        member_addresslb1.grid(row=6, column=0, pady=5, padx=10, sticky="w")

        member_addresstxt = Entry(Manage_Frame, font=("Arial", 15, "bold"), textvariable=Address)
        member_addresstxt.grid(row=6, column=1, pady=5, padx=10, sticky="w")

        member_pincodelb1 = Label(Manage_Frame, text="Pin Code", font=("Arial", 15, "bold"), bg="#001a66", fg="white")
        member_pincodelb1.grid(row=7, column=0, pady=5, padx=10, sticky="w")

        member_pincodetxt = Entry(Manage_Frame, font=("Arial", 15, "bold"), textvariable=Pincode)
        member_pincodetxt.grid(row=7, column=1, pady=5, padx=10, sticky="w")

        member_genderlb1 = Label(Manage_Frame, text="Gender", font=("Arial", 15, "bold"), bg="#001a66", fg="white")
        member_genderlb1.grid(row=8, column=0, pady=5, padx=10, sticky="w")  # Changed row from 3 to 8

        member_gendercmb = ttk.Combobox(Manage_Frame, textvariable=var4, state="readonly", font=("Arial", 15, "bold"),
                                        width=15)
        member_gendercmb['values'] = ("", "Male", "Female", "Other")
        member_gendercmb.current(0)
        member_gendercmb.grid(row=8, column=1, pady=5, padx=10, sticky="w")


        member_id_prooflb1 = Label(Manage_Frame, text="ID Proof", font=("Arial", 15, "bold"), bg="#001a66", fg="white")
        member_id_prooflb1.grid(row=9, column=0, pady=5, padx=10, sticky="w")  # Changed row from 3 to 8

        member_id_proofcmb = ttk.Combobox(Manage_Frame, textvariable=var3, state="readonly", font=("Arial", 15, "bold"),
                                        width=15)
        member_id_proofcmb['values'] = ("", "Aadhar Card", "Pasport", "Driving License","Pan Card","Student ID")
        member_id_proofcmb.current(0)
        member_id_proofcmb.grid(row=9, column=1, pady=5, padx=10, sticky="w")

        member_memtypelb1 = Label(Manage_Frame, text="Member Type", font=("Arial", 15, "bold"), bg="#001a66", fg="white")
        member_memtypelb1.grid(row=10, column=0, pady=5, padx=10, sticky="w")  # Changed row from 3 to 8

        member_memtypecmb = ttk.Combobox(Manage_Frame, textvariable=var2, state="readonly", font=("Arial", 15, "bold"),
                                        width=15)
        member_memtypecmb['values'] = ("", "Ayushman card", "Insurance", "Pay Immedialtely","Pay when leaving")
        member_memtypecmb.current(0)
        member_memtypecmb.grid(row=10, column=1, pady=5, padx=10, sticky="w")

        member_paymentlb1 = Label(Manage_Frame, text="Payment", font=("Arial", 15, "bold"), bg="#001a66", fg="white")
        member_paymentlb1.grid(row=11, column=0, pady=5, padx=10, sticky="w")  # Changed row from 3 to 8

        member_paymentcmb = ttk.Combobox(Manage_Frame, textvariable=var1, state="readonly", font=("Arial", 15, "bold"),
                                        width=15)
        member_paymentcmb['values'] = ("", "Cash", "Debit Card - RuPay", "Debit Card - Visa","Debit Card - Mastercard","Credit Card","Phonepe","GooglePay","Paytm")
        member_paymentcmb.current(0)
        member_paymentcmb.grid(row=11, column=1, pady=5, padx=10, sticky="w")

        member_membership = Checkbutton(Manage_Frame, text="Membership Fees", variable=var5, onvalue=1, offvalue=0, font=("Arial", 15, "bold"), bg="#001a66", fg="white",command= membership_fees)
        member_membership.grid(row=12, column=0,sticky="w")
        member_membershiptxt = Entry(Manage_Frame, font= ("arial",15,"bold"), state=DISABLED,justify= RIGHT,textvariable= Membership)
        member_membershiptxt.grid(row=12, column=1, pady=5,padx=2,sticky="w")
                            
        ######### Dtail frame ##########
        detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#001a66")
        detail_Frame.place(x=500, y=100, width=820, height=650)

        detail_label = Label(detail_Frame, font= ("arial",11,"bold"),pady=10,padx=2,width=120,
                             text = "Date        Ref Id        Firstname      Lastname      Mobile No      Address      Pincode      Gender       Membership")
        detail_label.grid(row=0, column=0, columnspan=4,sticky="w")
        detail_labeltxt = Text(detail_Frame, width= 123, height= 34, font= ("arial",10))
        detail_labeltxt.grid(row=1, column=0, columnspan=4)
        
        ########## we will add button in detail frame ####
        receiptbtn = Button(detail_Frame, padx=15, bd=5, font=("Arial", 12, "bold"),
                bg="#aff966", width=20, text="Receipt",command= Receipt)
        receiptbtn.grid(row=2, column=0)

        resetbtn = Button(detail_Frame, padx=15, bd=5, font=("Arial", 12, "bold"),
                bg="#aff966", width=20, text="Reset", command= reeesetbtt)
        resetbtn.grid(row=2, column=1)

        exitbtn = Button(detail_Frame, padx=15, bd=5, font=("Arial", 12, "bold"),
                bg="#aff966", width=20, text="Exit", command= exitbtt)
        exitbtn.grid(row=2, column=2)

class Hospital():
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1700x900+0+0")
        self.root.config(background= "black")


        ###################variable declaration###########
        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))

        def Reference_numfunc():
            ranumber = random.randint(10000,9999999)
            randomnumber = str(ranumber)
            Ref.set(randomnumber)

        def prescriptionfunc():
            Reference_numfunc()
            TextPrescription.insert(END,"Patient ID: \t\t"+PatientId.get()+"\n")
            TextPrescription.insert(END,"Patient Name: \t\t"+PatientName.get()+"\n")
            TextPrescription.insert(END,"Tablet: \t\t"+cmbTabletNames.get()+"\n")
            TextPrescription.insert(END,"Number of tablet: \t\t"+Number_of_Tablets.get()+"\n")
            TextPrescription.insert(END,"Daily Dose: \t\t"+DailyDose.get()+"\n")
            TextPrescription.insert(END,"Issued Date: \t\t"+IssuedDate.get()+"\n")
            TextPrescription.insert(END,"Expiry Date: \t\t"+ExpiryDate.get()+"\n")
            TextPrescription.insert(END,"Storage: \t\t"+StorageAdvice.get()+"\n")
            TextPrescription.insert(END,"More Information: \t\t"+MoreInformation.get()+"\n")



        def prescriptiondatafunc():
            Reference_numfunc()
            TextPrescriptionData.insert(END,Date_of_Registration.get()+"\t"+Ref.get()+"\t\t"+PatientId.get()+"\t"
            +PatientName.get()+"\t"+DateofBirth.get()+"\t\t"+ NHSnumber.get()+"\t\t"+cmbTabletNames.get()+"\t"+
            Number_of_Tablets.get()+"\t\t"+IssuedDate.get()+"\t\t"+ExpiryDate.get()+"\t\t"+DailyDose.get()+"\t\t"+
            StorageAdvice.get()+"\t"+PatientId.get()+"\n")
            return

        Ref = StringVar()
        cmbTabletNames = StringVar()
        HospitalCode = StringVar()
        Number_of_Tablets = StringVar()
        Lot = StringVar()
        IssuedDate = StringVar()
        ExpiryDate = StringVar()
        DailyDose = StringVar()
        SideEffects = StringVar()
        MoreInformation =StringVar()
        PatientId = StringVar()
        PatientNHnumber = StringVar()
        PatientName = StringVar()
        DateofBirth = StringVar()
        PatientAddress = StringVar()
        Prescription = StringVar()
        NHSnumber = StringVar()

        def exitbtn():
            exitbtn = tkinter.messagebox.askyesno("Hospitl Management System"," Are uou sure you want to exit ?")
            if exitbtn > 0:
                root.destroy()
                return
            
        def deletefunc():
            Ref.set("")
            cmbTabletNames.set("")
            HospitalCode.set("")
            Number_of_Tablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            PatientId.set("")
            PatientNHnumber.set("")
            PatientName.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            Prescription.set("")
            NHSnumber.set("")
            TextPrescription.delete("1.0",END)
            TextPrescriptionData.delete("1.0",END)

            return
        
        def resetfunc():
            Ref.set("")
            cmbTabletNames.set("")
            HospitalCode.set("")
            Number_of_Tablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            PatientId.set("")
            PatientNHnumber.set("")
            PatientName.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            Prescription.set("")
            NHSnumber.set("")
            TextPrescription.delete("1.0",END)

            return




############################TITLE########################
        title = Label(self.root, text="Hospital Management System", font=("monotype corsiva",42,"bold"),bd= 5,
                      relief=GROOVE, bg="#2eb8b8", fg="black")
        title.pack(side= TOP, fill= X)

#########################  FRAMES  ######################
        Manage_Frame = Frame(self.root,width= 1510, height= 400, bd= 5, relief= RIDGE, bg= "#0099cc")
        Manage_Frame.place(x=10,y=80)


        Button_Frame = Frame(self.root, width=1510, height=55, bd=4, relief=RIDGE, bg="#328695")
        Button_Frame.place(x=10,y=460)

        Data_Frame = LabelFrame(self.root, width= 1510, height=270, bd= 4, relief= RIDGE, bg= "#266e73")
        Data_Frame.place(x=10,y=510)

        ############### INNER FRAMES ################

        Data_FrameLeft = LabelFrame(Manage_Frame,width= 1050, text= "General Information",
        font= ("arial",20,"italic bold"), height= 390 ,bd= 7, relief= RIDGE, bg= "#0099cc")
        Data_FrameLeft.pack(side= LEFT)

        Data_FrameRight = LabelFrame(Manage_Frame,width= 1050, text= "Prescription",
        font= ("arial",20,"italic bold"), height= 390 ,bd= 7, relief= RIDGE, bg= "#0099cc")
        Data_FrameRight.pack(side= RIGHT)

        Data_Framedata = LabelFrame(Data_Frame, width=1050, height=390, text="Prescription Data", 
                            font=("aerial", 12, "italic bold"), bd=4, relief=RIDGE, bg="#3eb7bb")
        Data_Framedata.pack(side=LEFT)  

        ################### LABELS #####################

        Dateb1 = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text= "Date", padx=2, bg="#0099cc")
        Dateb1.grid(row=0,column=0,padx=10,pady=5, sticky= W)
        Datetxt = Entry(Data_FrameLeft, font= ("arial",12,"bold"),width= 27, textvariable= Date_of_Registration)
        Datetxt.grid(row=0,column=1,padx=10,pady=5, sticky= E)

        ######REF#############

        Refb1 = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text= "Reference Number", padx=2, bg="#0099cc")
        Refb1.grid(row=1,column=0,padx=10,pady=5, sticky= W)
        Reftxt = Entry(Data_FrameLeft, font= ("arial",12,"bold"),width= 27,state= DISABLED, textvariable= Ref)
        Reftxt.grid(row=1,column=1,padx=10,pady=5, sticky= E)

        ##### Patient ID

        PatientIdb1 = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text= "Patient Id", padx=2, bg="#0099cc")
        PatientIdb1.grid(row=2,column=0,padx=10,pady=5, sticky= W)
        PatientIdtxt = Entry(Data_FrameLeft, font= ("arial",12,"bold"),width= 27, textvariable= PatientId)
        PatientIdtxt.grid(row=2,column=1,padx=10,pady=5, sticky= E)

        ######PATIENT NAME

        PatientNameb1 = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text= "Patient Name", padx=2, bg="#0099cc")
        PatientNameb1.grid(row=3,column=0,padx=10,pady=5, sticky= W)
        PatientNametxt = Entry(Data_FrameLeft, font= ("arial",12,"bold"),width= 27, textvariable= PatientName)
        PatientNametxt.grid(row=3,column=1,padx=10,pady=5, sticky= E)

        ######DATE OF BIRTH

        DateofBirthb1 = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text= "Date of Birth", padx=2, bg="#0099cc")
        DateofBirthb1.grid(row=4,column=0,padx=10,pady=5, sticky= W)
        DateofBirthtxt = Entry(Data_FrameLeft, font= ("arial",12,"bold"),width= 27, textvariable= DateofBirth)
        DateofBirthtxt.grid(row=4,column=1,padx=10,pady=5, sticky= E)

        #####ADDRESS

        Addressb1 = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text= "Address", padx=2, bg="#0099cc")
        Addressb1.grid(row=5,column=0,padx=10,pady=5, sticky= W)
        Addresstxt = Entry(Data_FrameLeft, font= ("arial",12,"bold"),width= 27, textvariable= PatientAddress)
        Addresstxt.grid(row=5,column=1,padx=10,pady=5, sticky= E)

        #######NHS NUMBER

        NHSnumberb1 = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text= "NHS unique number", padx=2, bg="#0099cc")
        NHSnumberb1.grid(row=6,column=0,padx=10,pady=5, sticky= W)
        NHSnumbertxt = Entry(Data_FrameLeft, font= ("arial",12,"bold"),width= 27, textvariable= NHSnumber)
        NHSnumbertxt.grid(row=6,column=1,padx=10,pady=5, sticky= E)
        
        ########Tablet name

        Tabletb1 = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text= "Tablet", padx=2, bg="#0099cc")
        Tabletb1.grid(row=7,column=0,padx=10,pady=5, sticky= W)

        Tabletcmb = ttk.Combobox(Data_FrameLeft, textvariable= cmbTabletNames, width= 25, state= "readonly",
        font= ("aerial",12,"bold"))

        Tabletcmb['values'] = ("", "Paracetamol", "Dan-p", "Dio-1 one","Calpol", "Amlodipine Besylate", "Nexium",
                               "Singulair", "Plavix", "Amoxicillian", "Azithromycin", "Limcin-900")
        
        Tabletcmb.current(0)

        Tabletcmb.grid(row=7,column=1,padx=10,pady=5)

        #######NO OF TABLETS TO TAKE

        No_of_Tabletsb1 = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text= "Number of Tablets", padx=2, bg="#0099cc")
        No_of_Tabletsb1.grid(row=8,column=0,padx=10,pady=5, sticky= W)
        No_of_Tabletstxt = Entry(Data_FrameLeft, font= ("arial",12,"bold"),width= 27, textvariable= Number_of_Tablets )
        No_of_Tabletstxt.grid(row=8,column=1,padx=10,pady=5, sticky= E)

        ##### OTHER DETAILS IN THE SAME FRAME

        ###### HOSPITAL CODE

        HospitalCodeb1 = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text= "Hospital Code", padx=2, bg="#0099cc")
        HospitalCodeb1.grid(row=0,column=2,padx=10,pady=5, sticky= W)
        HospitalCodetxt = Entry(Data_FrameLeft, font= ("arial",12,"bold"),width= 25, textvariable= HospitalCode)
        HospitalCodetxt.grid(row=0,column=3,padx=10,pady=5, sticky= E)

        ######STORAGE ADVICE WHERE TO KEEP MEDICINE

        StorageAdviceb1 = Label(Data_FrameLeft, font=("Arial", 12, "bold"), width=20, text="Storage Advice", padx=2, bg="#0099cc")
        StorageAdviceb1.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        StorageAdvice = StringVar()  # Add this line to define the variable
        StorageAdvicecmb = ttk.Combobox(Data_FrameLeft, textvariable=StorageAdvice, width=25, state="readonly",
                                        font=("Arial", 12, "bold"))
        StorageAdvicecmb.grid(row=1, column=3, padx=10, pady=5)  # Add this line to position the Combobox

        StorageAdvicecmb['values'] = ("", "Under room temp", "below 5*C","below 0*C","Refrigration" )
        
        StorageAdvicecmb.current(0)
        StorageAdvicecmb.grid(row=1,column=3,padx=10,pady=5, sticky= E)

        #####LOT NUMBER OF MEDICINE

        Lot_nob1 = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text= "Lot number", padx=2, bg="#0099cc")
        Lot_nob1.grid(row=2,column=2,padx=10,pady=5, sticky= W)
        Lot_notxt = Entry(Data_FrameLeft, font= ("arial",12,"bold"),width= 25, textvariable= Lot)
        Lot_notxt.grid(row=2,column=3,padx=10,pady=5, sticky= E)

        ######## ISSUED DATE

        IssuedDateb1 = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text= "Date of Issue", padx=2, bg="#0099cc")
        IssuedDateb1.grid(row=3,column=2,padx=10,pady=5, sticky= W)
        IssuedDatetxt = Entry(Data_FrameLeft, font= ("arial",12,"bold"),width= 25, textvariable= IssuedDate)
        IssuedDatetxt.grid(row=3,column=3,padx=10,pady=5, sticky= E)

        #########EXPIRY DATE

        ExpiryDateb1 = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text= "Date of Expiry", padx=2, bg="#0099cc")
        ExpiryDateb1.grid(row=4,column=2,padx=10,pady=5, sticky= W)
        ExpiryDatetxt = Entry(Data_FrameLeft, font= ("arial",12,"bold"),width= 25, textvariable= ExpiryDate)
        ExpiryDatetxt.grid(row=4,column=3,padx=10,pady=5, sticky= E)

        ########DAILY DOSE

        DailyDoseb1 = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text= "Dsily Dosage", padx=2, bg="#0099cc")
        DailyDoseb1.grid(row=5,column=2,padx=10,pady=5, sticky= W)
        DailyDosetxt = Entry(Data_FrameLeft, font= ("arial",12,"bold"),width= 25, textvariable= DailyDose )
        DailyDosetxt.grid(row=5,column=3,padx=10,pady=5, sticky= E)

        ########SIDE EFFECTS

        SideEffectsb1 = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text= "Side Effects", padx=2, bg="#0099cc")
        SideEffectsb1.grid(row=6,column=2,padx=10,pady=5, sticky= W)
        SideEffectstxt = Entry(Data_FrameLeft, font= ("arial",12,"bold"),width= 25, textvariable= SideEffects )
        SideEffectstxt.grid(row=6,column=3,padx=10,pady=5, sticky= E)

        ######## more if realted to doctor not in the list

        MoreInformationb1 = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text= "More Information", padx=2, bg="#0099cc")
        MoreInformationb1.grid(row=7,column=2,padx=10,pady=5, sticky= W)
        MoreInformationtxt = Entry(Data_FrameLeft, font= ("arial",12,"bold"),width= 25, textvariable= MoreInformation )
        MoreInformationtxt.grid(row=7,column=3,padx=10,pady=5, sticky= E)

        ########MEDICATION (YES/NO)

        Medicationb1 = Label(Data_FrameLeft, font=("Arial", 12, "bold"), width=20, text="Medication", padx=2, bg="#0099cc")
        Medicationb1.grid(row=8, column=2, padx=10, pady=5, sticky=W)

        Medication = StringVar()  # Add this line to define the variable
        Medicationtxt = Entry(Data_FrameLeft, font=("Arial", 12, "bold"), width=25, textvariable=Medication)
        Medicationtxt.grid(row=8, column=3, padx=10, pady=5, sticky=E)
        
        ######## TEXT FIELD PRESCRIPTION

        TextPrescription = Text(Data_FrameRight, font=("arail",12,"bold"),width=55, height=12)
        TextPrescription.grid(row=0,column=0)

        #######EXIT FOR PRESCRIPTION DATA

        TextPrescriptionData = Text(Data_Framedata, font=("arail",12,"bold"),width=203, height=17, padx=3,pady=5)
        TextPrescriptionData.grid(row=1,column=0)

        #####BUTTON TO THE MIDDLE FRAME

        Prescriptionbtn = Button(Button_Frame, text="Prescription", bg="#ffaab0", activebackground= "#fcceb2",
                                 font= ("arial",15,"bold"), width=22,command=prescriptionfunc)
        Prescriptionbtn.grid(row=0, column=0, padx=15)

        Receiptbtn = Button(Button_Frame, text="Prescription Data", bg="#ffaab0", activebackground= "#fcceb2",
                                 font= ("arial",15,"bold"), width=22,command= prescriptiondatafunc)
        Receiptbtn.grid(row=0, column=1, padx=15)

        Resetbtn = Button(Button_Frame, text="Reset", bg="#ffaab0", activebackground= "#fcceb2",
                                 font= ("arial",15,"bold"), width=22,command=resetfunc)
        Resetbtn.grid(row=0, column=2, padx=15)

        Deletebtn = Button(Button_Frame, text="Delete", bg="#ffaab0", activebackground= "#fcceb2",
                                 font= ("arial",15,"bold"), width=22,command= deletefunc )
        Deletebtn.grid(row=0, column=3, padx=15)

        Exitbtn = Button(Button_Frame, text="Exit", bg="#ffaab0", activebackground= "#fcceb2",
                                 font= ("arial",15,"bold"), width=22, command= exitbtn)
        Exitbtn.grid(row=0, column=4, padx=15)

        prescriptiondatarow = Label(Data_Framedata, bg= "white", font=("arial",12,"bold"),
             text= "Date\tReference Id\tPatient Name\tDate of Birth\tNHS Number\tTablet\tNo of Tablet\tIssued Date\tExpiry Dose\tStorage Advise\tPatient Id")
        prescriptiondatarow.grid(row=0, column=0, sticky= W)






def main():
    root = Tk()
    app = Windows1(root)
    root.mainloop()

if __name__ == "__main__":
    main()