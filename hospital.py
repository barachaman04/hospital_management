import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox


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

        DailyDoseb1 = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text= "Daily Dosage", padx=2, bg="#0099cc")
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


if __name__ =="__main__":
    root = Tk()
    app = Hospital(root)
    root.mainloop()