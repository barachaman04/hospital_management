import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox


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
                             text = "Date   Ref Id   Firstname   Lastname   Mobile No   Address   Pincode   Gender   Membership")
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


if __name__ == "__main__":
    root = Tk()
    app = Registration(root)
    root.mainloop() 