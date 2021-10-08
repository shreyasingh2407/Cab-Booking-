import pandas as pd
import mysql.connector as con
import random
from sqlalchemy import create_engine
import pymysql
mydb=con.connect(host='localhost',user='root',passwd='123456',database='SHREYA')
mycursor=mydb.cursor()
if mydb.is_connected():
    st='select* from MEMBERSHIP;'
    df=pd.read_sql(st,mydb)
    print(df)
    mydb.close()
else:
   print("Connection Problem")
      
g=1050
p=1550
s=900
r=550
print('========================  MEMBERSHIP  =================================')


d=input("Enter 1. For New Membership, 2. For Upgradation, 3. For Surrender,4. To Skip:")
#BOOKING FUNCTION
if d=='1':
    m0=str(input("Enter your name:"))
    m1=input("Enter your age:")
    m2=input("Enter your gender:")
    m3=input("Please enter your contact_no:")
    m4=input("Enter your E-mail address:")
    m5=input("Enter your membership :")
    m=random.randint(1000,2000)
    m6=input("Enter your membership :")
    print("YOUR UNIQUE MEMBER ID IS:",m)
   
    if m6=='G' or m6=='g':
        q=("YOUR TOTAL DUE IS Rs.1050(including taxes)")
        print(q)
    elif m6=='P' or m6=='p':
        q=("YOUR TOTAL DUE IS Rs.1550(including taxes)")
        print(q)
    elif m6=='S' or m6=='s':
        q=("YOUR TOTAL DUE IS Rs.900(including taxes)")
        print(q)
    elif m6=='R' or m6=='r':
        q=("YOUR TOTAL DUE IS Rs.550(including taxes)")
        print(q)
    else:
        print("MEMBERSHIP TYPE INVALID! PLEASE ENTER IT AGAIN!")
        m6=input("Enter the type of Membership wanted(type G for gold,P for platinum,S for silver,R for regular):")
        
    m7=input("Enter mode of transaction(P FOR PAYTM ,CR FOR CREDIT):")
    if m7=='p' or m7=='P':
        p=input("Enter your PAYTM no.:")
        p1=input('Enter OTP:')
        print("PAYMENT SUCESSFULL!")
    elif m7=='CR' or m7=='cr':
        print("Please enter your card details:\n")
        c1=input("Enter the card number:")
        l=len(c1)
        if l==16:
            c2=input("Enter the expiry date:")
        else:
            print("Please check your card no and enter again")
            c1=int(input("Enter the card number:"))
        c2=int(input("Enter your cvv no:"))
        c3=int(input("Enter the amount payable:"))
        if c3==q:
            c4=input("Enter the OTP:")
        else:
            print("RECHECK THE AMOUNT PAYABLE AND ENTER AGAIN")
            c3=int(input("Enter the amount payable:"))
        m=random.randint(1000,2500)
                          
        
        print("YOUR UNIQUE MEMBER ID IS:",m)
    print("TRANSACTION SUCESSFULL!")
    import pandas as pd
    import mysql.connector as sqltor
    from sqlalchemy import create_engine
    import pymysql
    mycon=sqltor.connect(host='localhost',user='root',passwd='123456',database='disha')
    df1=pd.read_sql('select * from member1;',mycon)
    r=len(df1)
    df1.loc[r,:]=[m0,m1,m2,m3,m4,m5,m]
    engine=create_engine('mysql+pymysql://root:123456@localhost/disha')
    mycon=engine.connect()
    df1.to_sql('member1',mycon,index=False,if_exists='replace')
    print("CONGRATULATIONS! YOU ARE SUCESSFULLY REGISTERED AS A MEMBER.")


#UPGRADATION FUNCTION    
    
elif d=='2': 
    print("-----THE MEMBER DETAILS ARE-----:")
    mydb=con.connect(host='localhost',user='root',passwd='123456',database='disha')
    mycursor=mydb.cursor()
    v='select* from member1;'
    df1=pd.read_sql(v,mydb)
    print(df1)
    mydb.close()
    print('ALERT!!YOU CAN UPDATE ONLY YOUR MEMBERSHIP!')
    z=input("Enter your name:")
    u=input('Enter the type of membership you have:')
    print(df1)
    print("YOUR PREVIOUS MEMBERSHIP PAYMENT IS REFUNDED!! :).IF YOU DO NOT RECEIVE YOUR PAYMENT WITHIN 24 HRS ,PLEASE CONTACT US AT GOVERNMENTBOOKINGS_HELPDESK@GMAIL.COM WITHIN 72 WORKING HOURS.THANK YOU!")
    print('Enter your info to be updated:')
    u=input("Enter the type of membership you want to upgrade to(type G for gold,P for platinum,S for silver,R for regular):")
    if u=='G' or u=='g':
        print("YOUR TOTAL DUE IS Rs,",g,"(including taxes)")
    
    elif u=='P' or u=='p':
        print("YOUR TOTAL DUE IS Rs.",p,"(including taxes)")
        
    elif u=='S' or u=='s':
        print("YOUR TOTAL DUE IS Rs.",s,"(including taxes)")
        
    elif u4=='R' or u4=='r':
        print("YOUR TOTAL DUE IS Rs.",r,"(including taxes)")
        
    else:
        print("MEMBERSHIP TYPE INVALID! PLEASE ENTER IT AGAIN!")
        u=input("Enter the type of Membership you want to upgrade to(type G for gold,P for platinum,S for silver,R for regular):")
            
            
    u5=input("Enter mode of transaction(P FOR PAYTM ,CR FOR CREDIT):")
    if u5=='p' or u5=='P':
        p=input("Enter your PAYTM no.:")
        p1=input('Enter OTP:')
        print("PAYMENT SUCESSFULL!")
    elif u5=='CR' or u5=='cr':
        print("Please enter your card details:\n")
        c1=input("Enter the card number:")
        
        l=len(c1)
        if l==16:
            c2=input("Enter the expiry date:")
        else:
            print("Please check your card no and enter again")
            c1=int(input("Enter the card number:"))
            
        c2=int(input("Enter your cvv no:"))
        c3=int(input("Enter the amount payable:"))
        if c3==u4:
            c4=input("Enter the OTP:")
        else:
            print("RECHECK THE AMOUNT PAYABLE AND ENTER AGAIN")
            c3=int(input("Enter the amount payable:"))
    import pandas as pd
    import mysql.connector as sqltor
    from sqlalchemy import create_engine
    import pymysql
    mycon=sqltor.connect(host='localhost',user='root',passwd='123456',database='disha')
    df1=pd.read_sql('select * from member1;',mycon)
    mycon.close()
    st=input("enter name of the member:")
    gr=input("enter membership type to which you want to upgrade:")
    for (row,rowseries) in df1.iterrows():
        if df1.loc[row]['name']==st:
            pd.options.mode.chained_assignment = None  #[suppressing the SettingWithCopyWarning]
            #df1['membership']=df1['membership'].replace([u],gr)
            df1.membership[row]=gr
            print("updated")
    engine=create_engine('mysql+pymysql://root:123456@localhost/disha')
    mycon=engine.connect()
    df1.to_sql('member1',mycon,index=False,if_exists='replace')
    print('Data updated sucessfully')  
            
        

        
    print("TRANSACTION SUCESSFULL!")
        
    print("CONGRATULATIONS! YOUR MEMBER DETAILS ARE SUCESSFULLY UPGRADED.")
#CANCELLATION FUNCTION
elif d=='3':
    print("-----TO DELETE YOUR MEMBERSHIP-----")
    print('-----MEMBER DETAILS ARE-------')
    mydb=con.connect(host='localhost',user='root',passwd='123456',database='disha')
    mycursor=mydb.cursor()
    v='select* from member1;'

    df1=pd.read_sql(v,mydb)
    print(df1)
    mydb.close()
    import pandas as pd
    import mysql.connector as sqltor
    from sqlalchemy import create_engine
    import pymysql
    mycon=sqltor.connect(host='localhost',user='root',passwd='123456',database='disha')
    df1=pd.read_sql('select * from member1;',mycon)
    mycon.close()
    st=input("enter your name = ")
    #t=input("enter your membership = ")
    for (row,rowseries) in df1.iterrows():
        if df1.loc[row]['name']==st:
            #if df1.loc[row]['membership']==t:
            df1.drop([row],inplace=True)
    engine=create_engine('mysql+pymysql://root:123456@localhost/disha')
    mycon=engine.connect()
    df1.to_sql('member1',mycon,index=False,if_exists='replace') 
        #DROP
    print("YOUR MEMBERSHIP IS CANCELLED!\n")
    print("YOUR PAYMEMNT WILL BE REFUNDED WITHIN 24 WORKING HOURS!")
    print("IF YOU HAVE ANY OTHER ISSUES OR QUERY PLEASE CONTACT US AT GOVERNMENTBOOKINGS_HELPDESK@GMAIL.COM")
    print("THANK YOU! FOR CHOOISNG OUR SERVICES.")
else:
    exit

#########################CAR BOOKINGS################################################
print('============================== CAR BOOKING ================================')
u=input('Do you want to book a ride?y/n :')
if  u=='Y' or u=='y':
 from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox as ms
import sqlite3
  

Item4 = 0


# make database and users (if not exists already) table at programme start up
with sqlite3.connect('Users.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEXT NOT NULL)')
db.commit()
db.close()

#main Class
class user:
    def __init__(self,master):
    	# Window 
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        #Create Widgets
        self.widgets()

    #Login Function
    def login(self):
    	#Establish Connection
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] = "Welcome "
            self.head.configure(fg="khaki",bg='darkkhaki')
            self.head.pack(fill=X)
            application = travel(root)
            
        else:
            ms.showerror('Oops!','Username Not Found.')
            
    def new_user(self):
    	#Establish Connection
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user,[(self.username.get())])        
        if c.fetchall():
            ms.showerror('Error!','Username Already Taken!')
        else:
            ms.showinfo('Success!','Account Created!')
            self.log()
        #Create New Account 
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        db.commit()

        #Frame Packing Methords
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
        
    #Draw Widgets
    def widgets(self):
        self.head = Label(self.master,text = 'LOGIN',font = ('',35),pady = 10)
        self.head.pack()
        self.logf = Frame(self.master,padx =10,pady = 10,bg='white')
        Label(self.logf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.login).grid()
        Button(self.logf,text = ' Create Account ',bd = 3 ,activebackground='red',activeforeground='white',font = ('',15),padx=5,pady=5,command=self.cr).grid(row=2,column=1)
        self.logf.pack()
        
        self.crf = Frame(self.master,padx =10,pady = 10)
        Label(self.crf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.crf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.crf,text = 'Create Account',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.new_user).grid()
        Button(self.crf,text = 'Go to Login',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.log).grid(row=2,column=1)

class travel:

    def __init__(self,root):
        self.root = root
        self.root.title("Taxi Booking System ")
        self.root.geometry(geometry) 
        self.root.configure(background='black')

        DateofOrder=StringVar()
        DateofOrder.set(time.strftime(" %d / %m / %Y "))
        Receipt_Ref=StringVar()
        PaidTax=StringVar()
        SubTotal=StringVar()
        TotalCost=StringVar()

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        journeyType=IntVar()
        carType=IntVar()
        
        varl1=StringVar()
        varl2=StringVar()
        varl3=StringVar()
        reset_counter=0


        Firstname=StringVar()
        Surname=StringVar()
        Address=StringVar()
        Postcode=StringVar()
        Mobile=StringVar()
        Telephone=StringVar()
        Email=StringVar()

        TaxiTax=StringVar()
        Km=StringVar()
        Travel_Ins=StringVar()
        Luggage=StringVar()
        Receipt=StringVar()


        Standard=StringVar()
        PrimeSedan=StringVar()
        PremiumSedan=StringVar()
        
        Platinum=StringVar()
        Silver=StringVar()
        Gold=StringVar()
        Regular=StringVar()



        TaxiTax.set("0")
        Km.set("0")
        Travel_Ins.set("0")
        Luggage.set("0")


        Standard.set("0")
        PrimeSedan.set("0")
        PremiumSedan.set("0")

        Platinum.set("0")
        Silver.set("0")
        Gold.set("0")
        Regular.set("0")
       
        

    
    #==========================================Define Functiom==================================================

        def iExit():
            iExit= ms.askyesno("Prompt!","Do you want to exit?")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            TaxiTax.set("0")
            Km.set("0")
            Travel_Ins.set("0")
            Luggage.set("0")

            Standard.set("0")
            PrimeSedan.set("0")
            PremiumSedan.set("0")

            Firstname.set("")
            Surname.set("")
            Address.set("")
            Postcode.set("")
            Mobile.set("")
            Telephone.set("")
            Email.set("")

            PaidTax.set("")
            SubTotal.set("")
            TotalCost.set("")
            self.txtReceipt1.delete("1.0",END)
            self.txtReceipt2.delete("1.0",END)
            
            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            journeyType.set(0)
            carType.set(0)
            varl1.set("0")
            varl2.set("0")
            varl3.set("0")

            self.cboPickup.current(0)
            self.cboDrop.current(0)
            self.cboPooling.current(0)

            self.txtTaxiTax.configure(state=DISABLED)
            self.txtKm.configure(state=DISABLED)
            self.txtTravel_Ins.configure(state=DISABLED)
            self.txtLuggage.configure(state=DISABLED)
        
            self.txtStandard.configure(state=DISABLED)
            self.txtPrimeSedan.configure(state=DISABLED)
            self.txtPremiumSedan.configure(state=DISABLED)

            self.txtPlatinum.configure(state=DISABLED)
            self.txtSilver.configure(state=DISABLED)
            self.txtGold.configure(state=DISABLED)
            self.txtRegular.configure(state=DISABLED)

            self.reset_counter=1

        def Receiptt():
            if reset_counter is 0 and Firstname.get()!="" and Surname.get()!="" and Address.get()!="" and Postcode.get()!="" and Mobile.get()!="" and Telephone.get()!="" and Email.get()!="":
                self.txtReceipt1.delete("1.0",END)
                self.txtReceipt2.delete("1.0",END)
                x=random.randint(10853,500831)
                randomRef = str(x)
                Receipt_Ref.set(randomRef)

                self.txtReceipt1.insert(END,"Receipt Ref:\n")
                self.txtReceipt2.insert(END, Receipt_Ref.get() + "\n")
                self.txtReceipt1.insert(END,'Date:\n')
                self.txtReceipt2.insert(END, DateofOrder.get() + "\n")
                self.txtReceipt1.insert(END,'Taxi No:\n')
                self.txtReceipt2.insert(END, 'TR ' + Receipt_Ref.get() + " BW\n")
                self.txtReceipt1.insert(END,'Firstname:\n')
                self.txtReceipt2.insert(END, Firstname.get() + "\n")
                self.txtReceipt1.insert(END,'Surname:\n')
                self.txtReceipt2.insert(END, Surname.get() + "\n")
                self.txtReceipt1.insert(END,'Address:\n')
                self.txtReceipt2.insert(END, Address.get() + "\n")
                self.txtReceipt1.insert(END,'Postal Code:\n')
                self.txtReceipt2.insert(END, Postcode.get() + "\n")
                self.txtReceipt1.insert(END,'Telephone:\n')
                self.txtReceipt2.insert(END, Telephone.get() + "\n")
                self.txtReceipt1.insert(END,'Mobile:\n')
                self.txtReceipt2.insert(END, Mobile.get() + "\n")
                self.txtReceipt1.insert(END,'Email:\n')
                self.txtReceipt2.insert(END, Email.get() + "\n")
                self.txtReceipt1.insert(END,'From:\n')
                self.txtReceipt2.insert(END, varl1.get() + "\n")
                self.txtReceipt1.insert(END,'To:\n')
                self.txtReceipt2.insert(END, varl2.get() + "\n")
                self.txtReceipt1.insert(END,'Pooling:\n')
                self.txtReceipt2.insert(END, varl3.get() + "\n")
                self.txtReceipt1.insert(END,'Standard:\n')
                self.txtReceipt2.insert(END, Standard.get() + "\n")
                self.txtReceipt1.insert(END,'Prime Sedan:\n')
                self.txtReceipt2.insert(END, PrimeSedan.get() + "\n")
                self.txtReceipt1.insert(END,'Premium Sedan:\n')
                self.txtReceipt2.insert(END, PremiumSedan.get() + "\n")
                self.txtReceipt1.insert(END,'Paid:\n')
                self.txtReceipt2.insert(END, PaidTax.get() + "\n")
                self.txtReceipt1.insert(END,'SubTotal:\n')
                self.txtReceipt2.insert(END, str(SubTotal.get()) + "\n")
                self.txtReceipt1.insert(END,'Total Cost:\n')
                self.txtReceipt2.insert(END, str(TotalCost.get()))
                
            else:
                self.txtReceipt1.delete("1.0",END)
                self.txtReceipt2.delete("1.0",END)
                self.txtReceipt1.insert(END,"\nNo Input")
                

        def Taxi_Tax():
            global Item1
            if var1.get() == 1:
                self.txtTaxiTax.configure(state = NORMAL)
                Item1=float(50)
                TaxiTax.set("Rs " + str(Item1))
            elif var1.get() == 0:
                self.txtTaxiTax.configure(state=DISABLED)
                TaxiTax.set("0")
                Item1=0

        
        def Kilo():
            if var2.get() == 0:
                self.txtKm.configure(state=DISABLED)
                Km.set("0")
            elif var2.get() == 1 and varl1.get() != "" and varl2.get() != "":
                self.txtKm.configure(state=NORMAL)
                if varl1.get() == "SALT LAKE":
                    switch ={"VIP Road": 10,"Moira Street": 8,"Aurobindo Sranai":6,"Salt Lake": 0}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "VIP Road":
                    switch ={"VIP Road": 0,"Moira Street": 2,"Aurobindo Sarani":5,"Salt Lake": 10}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "Moira Street":
                    switch ={"VIP Road": 2,"Moira Street": 0,"Aurobindo Sarani":3,"Salt Lake": 8}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "Aurobindo Sarani":
                    switch ={"VIP Road": 5,"Moira Street": 3,"Aurobindo Sarani":0,"Salt Lake": 6}
                    Km.set(switch[varl2.get()])        

        
        def Travelling():
            global Item3
            if var3.get() == 1:
                self.txtTravel_Ins.configure(state = NORMAL)
                Item3=float(10)
                Travel_Ins.set("Rs " + str(Item3))
            elif var3.get() == 0:
                self.txtTravel_Ins.configure(state = DISABLED)
                Travel_Ins.set("0")
                Item3=0

        
        def Lug():
            global Item4
            if (var4.get()==1):
                self.txtLuggage.configure(state = NORMAL)
                Item4=float(30)
                Luggage.set("Rs "+ str(Item4))
            elif var4.get()== 0:
                self.txtLuggage.configure(state = DISABLED)
                Luggage.set("0")
                Item4=0

        
        def selectCar():
            global Item5
            if carType.get() == 1:
                self.txtPrimeSedan.configure(state = DISABLED)
                PrimeSedan.set("0") 
                self.txtPremiumSedan.configure(state = DISABLED)
                PremiumSedan.set("0")
                self.txtStandard.configure(state = NORMAL)
                Item5 = float(8)
                Standard.set("Rs "+ str(Item5))
            elif carType.get() == 2:
                self.txtStandard.configure(state =DISABLED)
                Standard.set("0")
                self.txtPremiumSedan.configure(state = DISABLED)
                PremiumSedan.set("0")
                self.txtPrimeSedan.configure(state = NORMAL)
                Item5 = float(10)
                PrimeSedan.set("Rs "+ str(Item5))
            else:
                self.txtStandard.configure(state =DISABLED)
                Standard.set("0")
                self.txtPrimeSedan.configure(state = DISABLED)
                PrimeSedan.set("0")
                self.txtPremiumSedan.configure(state = NORMAL)
                Item5 = float(15)
                PremiumSedan.set("Rs "+ str(Item5))
                
          
        def Total_Paid():
            if ((var1.get() == 1 and var2.get() == 1 and var3.get() == 1 or var4.get() == 1) and carType.get() != 0  and journeyType.get() != 0 and (varl1.get() != "" and varl2.get() !="")):
                if journeyType.get()==1:
                    Item2=Km.get()
                    Cost_of_fare = (Item1+(float(Item2)*Item5)+Item3+Item4)

                    Tax = "Rs " + str('%.2f'%((Cost_of_fare) *0.09))
                    ST = "Rs " + str('%.2f'%((Cost_of_fare)))
                    TT = "Rs " + str('%.2f'%(Cost_of_fare+((Cost_of_fare)*0.9)))
                elif journeyType.get()==2:
                    Item2=Km.get()
                    Cost_of_fare = (Item1+(float(Item2)*Item5)*1.5+Item3+Item4)

                    Tax = "Rs " + str('%.2f'%((Cost_of_fare) *0.09))
                    ST = "Rs " + str('%.2f'%((Cost_of_fare)))
                    TT = "Rs " + str('%.2f'%(Cost_of_fare+((Cost_of_fare)*0.9)))
                else:
                    Item2=Km.get()
                    Cost_of_fare = (Item1+(float(Item2)*Item5)*2+Item3+Item4)

                    Tax = "Rs " + str('%.2f'%((Cost_of_fare) *0.09))
                    ST = "Rs " + str('%.2f'%((Cost_of_fare)))
                    TT = "Rs " + str('%.2f'%(Cost_of_fare+((Cost_of_fare)*0.9)))

                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)
            else:
                w = ms.showwarning("Error !","Invalid Input\nPlease try again !!!")

            

   #================================================mainframe========================================================================

        MainFrame=Frame(self.root)
        MainFrame.pack(fill=BOTH,expand=True)
        
        Tops = Frame(MainFrame,bg='khaki', bd=20, width=1500,relief=RIDGE)
        Tops.pack(side=TOP,fill=BOTH,expand=True)

        self.lblTitle=Label(Tops,font=('arial',70,'bold'),text="       Taxi Booking System      ",bg='khaki')
        self.lblTitle.grid()

    #================================================customerframedetail=============================================================
        CustomerDetailsFrame=LabelFrame(MainFrame,bg='khaki', width=1350,height=500,bd=20, pady=5, relief=RIDGE)
        CustomerDetailsFrame.pack(side=BOTTOM,fill=BOTH,expand=True)

        FrameDetails=Frame(CustomerDetailsFrame,bg='khaki' ,width=880,height=400,bd=10, relief=RIDGE)
        FrameDetails.pack(side=LEFT,fill=BOTH,expand=True)

        CustomerName=LabelFrame(FrameDetails,bg='khaki' ,width=150,height=250,bd=10, font=('arial',12,'bold'),text="Customer Name", relief=RIDGE)
        CustomerName.grid(row=0,column=0)

        TravelFrame = LabelFrame(FrameDetails,bd=10,bg='khaki' ,width=300,height=250, font=('arial',12,'bold'),text="Booking Detail", relief=RIDGE)
        TravelFrame.grid(row=0,column=1)

        Book_Frame=LabelFrame(FrameDetails,width=400,bg='khaki',height=200,relief=FLAT)
        Book_Frame.grid(row=1,column=0)

        CostFrame = LabelFrame(FrameDetails,width=150,bg='khaki',height=150,bd=5,relief=FLAT)
        CostFrame.grid(row=1,column=1)


    #===============================================recipt======================================================================
        Receipt_BottonFrame=LabelFrame(CustomerDetailsFrame,bd=10,bg='khaki', width=450,height=400, relief=RIDGE)
        Receipt_BottonFrame.pack(side=RIGHT,fill=BOTH,expand=True)

        ReceiptFrame=LabelFrame(Receipt_BottonFrame, width=350,bg='white',height=300, font=('arial',12,'bold'),text="Receipt", relief=RIDGE)
        ReceiptFrame.grid(row=0,column=0)

        ButtonFrame=LabelFrame(Receipt_BottonFrame, width=350,bg='khaki',height=100, relief=RIDGE)
        ButtonFrame.grid(row=1,column=0)
    #=========================================================CustomerName====================================================

        self.lblFirstname=Label(CustomerName,font=('arial',14,'bold'),text="Firstname",bd=7,bg='khaki')
        self.lblFirstname.grid(row=0,column=0,sticky=W)
        self.txtFirstname=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Firstname,bd=7,insertwidth=2,justify=RIGHT)
        self.txtFirstname.grid(row=0,column=1)


        self.lblSurname=Label(CustomerName,font=('arial',14,'bold'),bg='khaki',text="Surname",bd=7)
        self.lblSurname.grid(row=1,column=0,sticky=W)
        self.txtSurname=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Surname,bd=7,insertwidth=2,justify=RIGHT)
        self.txtSurname.grid(row=1,column=1,sticky=W)


        self.lblAddress=Label(CustomerName,font=('arial',14,'bold'),bg='khaki',text="Address",bd=7)
        self.lblAddress.grid(row=2,column=0,sticky=W)
        self.txtAddress=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Address,bd=7,insertwidth=2,justify=RIGHT)
        self.txtAddress.grid(row=2,column=1)


        self.lblPostcode=Label(CustomerName,font=('arial',14,'bold'),bg='khaki',text="Postcode",bd=7)
        self.lblPostcode.grid(row=3,column=0,sticky=W)
        self.txtPostcode=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Postcode,bd=7,insertwidth=2,justify=RIGHT)
        self.txtPostcode.grid(row=3,column=1)


        self.lblTelephone=Label(CustomerName,font=('arial',14,'bold'),bg='khaki',text="Telephone",bd=7)
        self.lblTelephone.grid(row=4,column=0,sticky=W)
        self.txtTelephone=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Telephone,bd=7,insertwidth=2,justify=RIGHT)
        self.txtTelephone.grid(row=4,column=1)

        self.lblMobile=Label(CustomerName,font=('arial',14,'bold'),bg='khaki',text="Mobile",bd=7)
        self.lblMobile.grid(row=5,column=0,sticky=W)
        self.txtMobile=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Mobile,bd=7,insertwidth=2,justify=RIGHT)
        self.txtMobile.grid(row=5,column=1)

        self.lblEmail=Label(CustomerName,font=('arial',14,'bold'),bg='khaki',text="Email",bd=7)
        self.lblEmail.grid(row=6,column=0,sticky=W)
        self.txtEmail=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Email,bd=7,insertwidth=2,justify=RIGHT)
        self.txtEmail.grid(row=6,column=1)

 
    #===============================================Taxi Information==============================================================
        self.lblPickup=Label(TravelFrame,font=('arial',14,'bold'),bg='khaki',text="Pickup",bd=7)
        self.lblPickup.grid(row=0,column=0,sticky=W)

        self.cboPickup =ttk.Combobox(TravelFrame, textvariable = varl1 , state='readonly', font=('arial',20,'bold'), width=14)
        self.cboPickup['value']=(' ','Salt Lake','Aurobindo Sarani','Moira Street','VIP Road')
        self.cboPickup.current(0)
        self.cboPickup.grid(row=0,column=1)


        self.lblDrop=Label(TravelFrame,font=('arial',14,'bold'),bg='khaki',text="Drop",bd=7)
        self.lblDrop.grid(row=1,column=0,sticky=W)

        self.cboDrop =ttk.Combobox(TravelFrame, textvariable = varl2 , state='readonly', font=('arial',20,'bold'), width=14)
        self.cboDrop['value']=(' ','VIP Road','Moira Street','Salt Lake','Aurobindo Sarani')
        self.cboDrop.current(0)
        self.cboDrop.grid(row=1,column=1)

        self.lblPooling=Label(TravelFrame,font=('arial',14,'bold'),bg='khaki',text="Pooling",bd=7)
        self.lblPooling.grid(row=2,column=0,sticky=W)

        self.cboPooling =ttk.Combobox(TravelFrame, textvariable = varl3 , state='readonly', font=('arial',20,'bold'), width=14)
        self.cboPooling['value']=('','1','2','3','4')
        self.cboPooling.current(1)
        self.cboPooling.grid(row=2,column=1)

    #===============================================Taxi Information==============================================================

        self.chkTaxiTax=Checkbutton(TravelFrame,text="Taxi Tax(Base Charge) *",variable = var1, onvalue=1, offvalue=0,font=('arial',16,'bold'),bg='khaki',command=Taxi_Tax).grid(row=3, column=0, sticky=W)
        self.txtTaxiTax=Label(TravelFrame,font=('arial',14,'bold'),textvariable=TaxiTax,bd=6,width=18,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN)
        self.txtTaxiTax.grid(row=3,column=1)


        self.chkKm=Checkbutton(TravelFrame,text="Distance(KMs) *",variable = var2, onvalue=1, offvalue=0,font=('arial',16,'bold'),bg='khaki',command=Kilo).grid(row=4, column=0, sticky=W)
        self.txtKm=Label(TravelFrame,font=('arial',14,'bold'),textvariable=Km,bd=6,width=18,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN,highlightthickness=0)
        self.txtKm.grid(row=4,column=1)

        self.chkTravel_Ins=Checkbutton(TravelFrame,text="Travelling Insurance *",variable = var3,bg='khaki', onvalue=1, offvalue=0,font=('arial',16,'bold'),command=Travelling).grid(row=5, column=0, sticky=W)
        self.txtTravel_Ins=Label(TravelFrame,font=('arial',14,'bold'),textvariable=Travel_Ins,bd=6,width=18,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN)
        self.txtTravel_Ins.grid(row=5,column=1)

      
        self.chkLuggage=Checkbutton(TravelFrame,text="Extra Luggage",bg='khaki',variable = var4, onvalue=1, offvalue=0,font=('arial',16,'bold'),command=Lug).grid(row=6, column=0, sticky=W)
        self.txtLuggage=Label(TravelFrame,font=('arial',14,'bold'),textvariable=Luggage,bd=6,width=18,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN)
        self.txtLuggage.grid(row=6,column=1)
    
    #=================================payment information ===========================================================================
         
        self.lblPaidTax=Label(CostFrame,font=('arial',14,'bold'),bg='khaki',text="Paid Tax\t\t",bd=7)
        self.lblPaidTax.grid(row=0,column=2,sticky=W)
        self.txtPaidTax = Entry(CostFrame,font=('arial',14,'bold'),textvariable=PaidTax,bd=7, width=26, justify=RIGHT,relief=SUNKEN)
        self.txtPaidTax.grid(row=0,column=3)
            

        
        self.lblSubTotal=Label(CostFrame,font=('arial',14,'bold'),bg='khaki',text="Sub Total",bd=7)
        self.lblSubTotal.grid(row=1,column=2,sticky=W)
        self.txtSubTotal =Entry(CostFrame,font=('arial',14,'bold'),textvariable=SubTotal,bd=7, width=26, justify=RIGHT,relief=SUNKEN)
        self.txtSubTotal.grid(row=1,column=3)



        self.lblTotalCost=Label(CostFrame,font=('arial',14,'bold'),bg='khaki',text="Total Cost",bd=7)
        self.lblTotalCost.grid(row=2,column=2,sticky=W)
        self.txtTotalCost = Entry(CostFrame,font=('arial',14,'bold'),textvariable=TotalCost,bd=7, width=26, justify=RIGHT,relief=SUNKEN)
        self.txtTotalCost.grid(row=2,column=3)

    #==========================================================taxiselect=======================================================================

        self.chkStandard=Radiobutton(Book_Frame,text="Standard",bg='khaki',value=1,variable = carType,font=('arial',14,'bold'),command=selectCar).grid(row=0, column=0, sticky=W)
        self.txtStandard = Label(Book_Frame,font=('arial',14,'bold'),width =7,textvariable=Standard,bd=5, state= DISABLED, justify=RIGHT,bg='white',relief=SUNKEN)
        self.txtStandard.grid(row=0,column=1)
        

        self.chkPrimeSedand=Radiobutton(Book_Frame,text="PrimeSedan",bg='khaki',value=2,variable = carType,font=('arial',14,'bold'),command=selectCar).grid(row=1, column=0, sticky=W)
        self.txtPrimeSedan= Label(Book_Frame,font=('arial',14,'bold'),width =7,textvariable=PrimeSedan,bd=5, state= DISABLED, justify=RIGHT,bg='white',relief=SUNKEN)
        self.txtPrimeSedan.grid(row=1,column=1)
             
       
        self.chkPremiumSedan = Radiobutton(Book_Frame,text="PremiumSedan",bg='khaki',value=3,variable = carType,font=('arial',14,'bold'),command=selectCar).grid(row=2, column=0)
        self.txtPremiumSedan = Label(Book_Frame,font=('arial',14,'bold'),width =7,textvariable=PremiumSedan,bd=5, state= DISABLED, justify=RIGHT,bg='white',relief=SUNKEN)
        self.txtPremiumSedan.grid(row=2,column=1)
      
        
 #==========================================================membershipselect=======================================================================
        self.chkSingle =Radiobutton(Book_Frame,text="Platinum",bg='khaki',value=1,variable = journeyType,font=('arial',14,'bold')).grid(row=0, column=3, sticky=W)
        self.chkReturn =Radiobutton(Book_Frame,text="Silver",bg='khaki',value=2,variable = journeyType,font=('arial',14,'bold')).grid(row=1, column=3, sticky=W)
        self.chkSpecialsNeeds =Radiobutton(Book_Frame,text="Gold",bg='khaki',value=3,variable = journeyType,font=('arial',14,'bold')).grid(row=2, column=3, sticky=W)
        self.chkSpecialsNeeds =Radiobutton(Book_Frame,text="Regular",bg='khaki',value=4,variable = journeyType,font=('arial',14,'bold')).grid(row=3, column=3, sticky=W)
    #=======================================Recipt====================================================================================

        self.txtReceipt1 = Text(ReceiptFrame,width = 22, height = 21,font=('arial',10,'bold'),borderwidth=0)
        self.txtReceipt1.grid(row=0,column=0,columnspan=2)
        self.txtReceipt2 = Text(ReceiptFrame,width = 22, height = 21,font=('arial',10,'bold'),borderwidth=0)
        self.txtReceipt2.grid(row=0,column=2,columnspan=2)


    #======================================Button========================================================================================
        
        self.btnTotal = Button(ButtonFrame,padx=18,bd=7,font=('arial',11,'bold'),bg='darkkhaki',width = 2,text='Total',command=Total_Paid).grid(row=0,column=0)
        self.btnReceipt = Button(ButtonFrame,padx=18,bd=7,font=('arial',11,'bold'),bg='darkkhaki',width = 2,text='Receipt',command=Receiptt).grid(row=0,column=1)
        self.btnReset = Button(ButtonFrame,padx=18,bd=7,font=('arial',11,'bold'),bg='darkkhaki',width = 2,text='Reset',command=Reset).grid(row=0,column=2)
        self.btnExit = Button(ButtonFrame,padx=18,bd=7,font=('arial',11,'bold'),bg='darkkhaki',width = 2,text='Exit', command=iExit).grid(row=0,column=3)
        
    #====================================================================================================================================

        
if __name__=='__main__':
    root = Tk()

    #=========================================== Getting Screen Width ==================================================================
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    geometry="%dx%d+%d+%d"%(w,h,0,0)
    
    root.geometry("500x300+320+200")
    root.title('Login Form')
    application = user(root)
    root.mainloop()
    


elif (u=='n' or u=='N'): 
    exit

##########################  ADMIN  ###########################################################    
print('========================ADMIN========================')        
m=input('Are you admin?y/n :')
if m=='y' or m=='Y':
    #*********************ADDING FUNCTONS***********************************************************
    def addmember():
        def submitadd():
            name=nameval.get()
            age=ageval.get()
            gender=genderval.get()
            contact=contactval.get()
            email=emailval.get()
            membership=membershipval.get()
            id1=idval.get()

            try:
                strr='insert into member1 values(%s,%s,%s,%s,%s,%s,%s);'
                mycursor.execute(strr,(name,age,gender,contact,email,membership,id1))
                con.commit()
                res = messagebox.askyesnocancel('NOTIFICATION','MEMBER ADDED SUCESSFULLY!....Do you want to clean the form?',parent=addroot)
                if(res==True):
                    nameval.set('')
                    ageval.set('')
                    genderval.set('')
                    contactval.set('')
                    emailval.set('')
                    membershipval.set('')
                    idval.set('')
            except:
                messagebox.showerror('NOTIFICATION','ID ALREADY EXISTS TRY ANOTHER ID',parent=addroot)
        strr='select * from member1'
        mycursor.execute(strr)
        datas=mycursor.fetchall()
        membertable.delete(*membertable.get_children())
        for i in datas:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
            membertable.insert('',END,values=vv)

            
        addroot = Toplevel(master=DataEntryFrame)
        addroot.grab_set()
        addroot.geometry('470x470+220+200')
        addroot.title('NEW MEMBERSHIP!!')
        addroot.config(bg='pink')
        addroot.resizable(False,False)
    #--------------------ADD LABEL------------------------------------
        namelabel=Label(addroot,text="Enter Name:",bg='gray',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
        namelabel.place(x=10,y=10)
        agelabel=Label(addroot,text="Enter Age:",bg='gray',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
        agelabel.place(x=10,y=70)
        genderlabel=Label(addroot,text="Enter Gender:",bg='gray',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
        genderlabel.place(x=10,y=130)
        contactlabel=Label(addroot,text="Enter Contact_No:",bg='gray',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
        contactlabel.place(x=10,y=190)
        emaillabel=Label(addroot,text="Enter Email_id:",bg='gray',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
        emaillabel.place(x=10,y=250)
        membershiplabel=Label(addroot,text="Enter Membership:",bg='gray',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
        membershiplabel.place(x=10,y=310)
        member_idlabel=Label(addroot,text="Enter a Unique_Id:",bg='gray',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
        member_idlabel.place(x=10,y=370)
    #--------------------------ENTRY BOX---------------------------------------------
        nameval=StringVar()
        ageval=StringVar()
        genderval=StringVar()
        contactval=StringVar()
        emailval=StringVar()
        membershipval=StringVar()
        idval=StringVar()
    
        nameentry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
        nameentry.place(x=250,y=10)
        ageentry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=ageval)
        ageentry.place(x=250,y=70)
        genderentry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
        genderentry.place(x=250,y=130)
        contactentry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=contactval)
        contactentry.place(x=250,y=190)
        emailentry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
        emailentry.place(x=250,y=250)
        membershipentry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=membershipval)
        membershipentry.place(x=250,y=310)
        identry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
        identry.place(x=250,y=370)
    #-------------------------ADD BUTTON---------------------------------------------------------
        submitbutton= Button(addroot,text='SUBMIT',font=('roman',15,'bold'),bd=5,width=20,activebackground='red',activeforeground='white',command=submitadd)
        submitbutton.place(x=150,y=430)
        addroot.mainloop()
#*******************************************UPGRADE************************************************************************************************************************    
    def upgrademember():
        def update():
            name=nameval.get()
            age=ageval.get()
            gender=genderval.get()
            contact=contactval.get()
            email=emailval.get()
            membership=membershipval.get()
            id1=idval.get()
            if(id1!=''):
                strr='update member1 set name=%s,age=%s,gender=%s,contactno=%s,emailid=%s,membership=%s where memberid=%s'
            
                mycursor.execute(strr,(name,age,gender,contact,email,membership,id1))
                con.commit()
                res=messagebox.showinfo('NOTIFICATION','ID UPDATED SUCESSFULLY',parent=upgraderoot)
                strr='select * from member1'
   
                mycursor.execute(strr)
                datas=mycursor.fetchall()
                membertable.delete(*membertable.get_children())
                for i in datas:
                    vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
                    membertable.insert('',END,values=vv)
            
            
        upgraderoot = Toplevel(master=DataEntryFrame)
        upgraderoot.grab_set()
        upgraderoot.geometry('540x540+220+200')
        upgraderoot.title('MEMBERSHIP UPGRADATION!')
        upgraderoot.config(bg='pink')
        upgraderoot.resizable(False,False)
    #-----------------------UPGRADE LABEL------------------------------------------------------------------------------------------------
        namelabel=Label(upgraderoot,text="Update Name:",bg='gray',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
        namelabel.place(x=10,y=10)
        agelabel=Label(upgraderoot,text="Update Age:",bg='gray',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
        agelabel.place(x=10,y=70)
        genderlabel=Label(upgraderoot,text="Update Gender:",bg='gray',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
        genderlabel.place(x=10,y=130)
        contactlabel=Label(upgraderoot,text="Update Contact_No:",bg='gray',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
        contactlabel.place(x=10,y=190)
        emaillabel=Label(upgraderoot,text="Update Email_id:",bg='gray',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
        emaillabel.place(x=10,y=250)
        membershiplabel=Label(upgraderoot,text="Update Membership:",bg='gray',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
        membershiplabel.place(x=10,y=310)
        member_idlabel=Label(upgraderoot,text="Your Member_id:",bg='gray',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
        member_idlabel.place(x=10,y=370)
    #--------------------------ENTRY BOX---------------------------------------------
        nameval=StringVar()
        ageval=StringVar()
        genderval=StringVar()
        contactval=StringVar()
        emailval=StringVar()
        membershipval=StringVar()
        idval=StringVar()
    
        nameentry= Entry(upgraderoot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
        nameentry.place(x=250,y=10)
        ageentry= Entry(upgraderoot,font=('roman',15,'bold'),bd=5,textvariable=ageval)
        ageentry.place(x=250,y=70)
        genderentry= Entry(upgraderoot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
        genderentry.place(x=250,y=130)
        contactentry= Entry(upgraderoot,font=('roman',15,'bold'),bd=5,textvariable=contactval)
        contactentry.place(x=250,y=190)
        emailentry= Entry(upgraderoot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
        emailentry.place(x=250,y=250)
        membershipentry= Entry(upgraderoot,font=('roman',15,'bold'),bd=5,textvariable=membershipval)
        membershipentry.place(x=250,y=310)
        identry= Entry(upgraderoot,font=('roman',15,'bold'),bd=5,textvariable=idval)
        identry.place(x=250,y=370)
    #-------------------------UPGRADE BUTTON---------------------------------------------------------
        submitbutton= Button(upgraderoot,text='SUBMIT',font=('roman',15,'bold'),bd=5,width=20,activebackground='red',activeforeground='white',command=update)
        submitbutton.place(x=150,y=430)
        cc=membertable.focus()
        content=membertable.item(cc)
        pp=content['values']
        if (len(pp) !=0):
            nameval.set(pp[0])
            ageval.set(pp[1])
            genderval.set(pp[2])
            contactval.set(pp[3])
            emailval.set(pp[4])
            membershipval.set(pp[5])
            idval.set(pp[6])
        
        upgraderoot.mainloop()
#********************************************CANCELLATION*******************************************************************************************************************   
    def cancelmember():
        cc=membertable.focus()
        content=membertable.item(cc)
        pp=content['values'][6]
        strr='delete from member1 where memberid=%s'
        mycursor.execute(strr,(pp))
        con.commit()
        messagebox.showinfo('NOTIFICATION','Membership Deleted sucessfully!')
        strr='select * from member1'
        mycursor.execute(strr)
        datas=mycursor.fetchall()
        membertable.delete(*membertable.get_children())
        for i in datas:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
            membertable.insert('',END,values=vv)
            
 #***************************************************************************************************************************************************************    
    def showallmember():
        strr='select * from member1'
        mycursor.execute(strr)
        datas=mycursor.fetchall()
        membertable.delete(*membertable.get_children())
        for i in datas:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
            membertable.insert('',END,values=vv)
    
    
#***************************************************************************************************************************************************************
    def exitmember():
        res=messagebox.askyesnocancel('NOTIFICATION','Do You Want To Exit?')
        if (res==True):
            root.destroy()
    





#*********INTROSLIDES****************************************************************************
    def IntroLabelTick():
        global count,text
        if (count>=len(ss)):
            count=-1
            text=''
            SliderLabel.config(text=text)
        else:
            text=text+ss[count]
            SliderLabel.config(text=text)
        count+=1
        SliderLabel.after(200,IntroLabelTick)
#**************CLOCK******************************************************
    def tick():
        time_string=time.strftime('%H:%M:%S')
        date_string=time.strftime('%d/%m/%Y')
        Clock.configure(text='Date : '+date_string+"\n"+" Time : "+time_string)
        Clock.after(200,tick)
#***************COLOURS**********************************************************
    import random
    colors =['black','white','darkslategray','brown']
    def IntroLabelColorTick():
        fg=random.choice(colors)
        SliderLabel.config(fg=fg)
#*************CONNECTION OF DATABASE**********************************************************************    
    def connectdb():
        def submitdb():
            global con,mycursor
            host=hostval.get()
            user=userval.get()
            passwd=passwdval.get()
            try:
                con=pymysql.connect(host=host,user=user,passwd=passwd)
                mycursor=con.cursor()
            except:
                messagebox.showerror('NOTIFICATION','Data Is Incorrect Please Try Again')
                return
            try:
                strr='create database disha'
                mycursor.execute(strr)
                strr='use disha'
                mycursor.execute(strr)
                strr='create table member1(name char(100),age int(30),gender char(100),contactno int(50) ,emailid varchar(150),membership char(100),memberid int(50))'
                mycursor.execute(strr)
                strr='alter table member1 modify column memberid int not null'
                mycursor.execute(strr)
                strr='alter table member1 modify column memberid int primary key'
                mycursor.execute(strr)
                messagebox.showinfo('NOTIFICATION','Database Created And Now You Are Connected!',parent=dbroot)
            except:
                strr='use disha'
                mycursor.execute(strr)
                messagebox.showinfo('NOTIFICATION','You Are Now Connected To A Database!',parent=dbroot)
            dbroot.destroy()    
        dbroot= Toplevel()
        dbroot.grab_set()
        dbroot.geometry('470x250+800+230')
        dbroot.resizable(False,False)
        dbroot.config(bg='pink')

#********************CONNECTION LABELS**************************************************    
        hostLabel= Label(dbroot,text="Enter Admin:",bg='gray',fg='white',font=('chiller',22,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
        hostLabel.place(x=10,y=10)
        userLabel= Label(dbroot,text="Enter User:",bg='gray',fg='white',font=('chiller',22,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
        userLabel.place(x=10,y=70)
        passwdLabel= Label(dbroot,text="Enter Password:",bg='gray',fg='white',font=('chiller',22,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
        passwdLabel.place(x=10,y=130)
#************************CONNECTDB ENTRY*****************************************************************
        hostval=StringVar()
        userval=StringVar()
        passwdval=StringVar()

        hostentry=Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
        hostentry.place(x=250,y=10)
   
        userentry=Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=userval)
        userentry.place(x=250,y=70)
    
        passwdentry=Entry(dbroot,font=('roman',15,'bold'),show='*',bd=5,textvariable=passwdval)
        passwdentry.place(x=250,y=130)
#************************CONNECTIONDB BUTTON************************************************************
        submitbutton= Button(dbroot,text='SUBMIT',font=('roman',15,'bold'),bd=5,width=20,activebackground='red',activeforeground='white',command=submitdb)
        submitbutton.place(x=150,y=190)
        dbroot.mainloop()

        
############################ IMPORT FUNCTION ################################################################################
    from tkinter import *
    import time
    import random
    from tkinter import Toplevel,messagebox
    from tkinter.ttk import Treeview
    from tkinter import ttk
    import pymysql

###################################################################################################
    root=Tk()
    root.title('CAR BOOKING SYSTEM')
    root.config(bg='pink')
    root.geometry('1174x700+200+50')
    #root.iconbitmap('mana.icon')#(for setting the icon)
    root.resizable(False,False)
#***************************FRAMES********************************************************
    DataEntryFrame=Frame(root,bg='pink',relief=GROOVE,borderwidth=5)
    DataEntryFrame.place(x=10,y=80,width=500,height=600)
#****************************DATAENTRY FRAME********************************************************
    frontLabel= Label(DataEntryFrame,text='-----------------WELCOME----------------',width=30,font=('arial',22,'italic bold'),bg='pink',fg='black',anchor='w')
    frontLabel.pack(side=TOP,expand=True)
    addbtn =Button(DataEntryFrame,text='1. ADD MEMBER',width=30,font=('chiller',20,'bold'),bd=6,bg='gray',fg='white',activebackground='pink',activeforeground='black',anchor='w',command=addmember)
    addbtn.pack(side=TOP,expand=True)
    updatebtn =Button(DataEntryFrame,text='2. UPGRADE MEMBER',width=30,font=('chiller',20,'bold'),bd=6,bg='gray',fg='white',activebackground='pink',activeforeground='black',anchor='w',command=upgrademember)
    updatebtn.pack(side=TOP,expand=True)
    delbtn =Button(DataEntryFrame,text='3. DELETE MEMBER',width=30,font=('chiller',20,'bold'),bd=6,bg='gray',fg='white',activebackground='pink',activeforeground='black',anchor='w',command=cancelmember)
    delbtn.pack(side=TOP,expand=True)
    showallbtn =Button(DataEntryFrame,text='4. SHOW ALL MEMBERS',width=30,font=('chiller',20,'bold'),bd=6,bg='gray',fg='white',activebackground='pink',activeforeground='black',anchor='w',command=showallmember)
    showallbtn.pack(side=TOP,expand=True)
    exitbtn =Button(DataEntryFrame,text='5. EXIT',width=30,font=('chiller',20,'bold'),bd=6,bg='gray',fg='white',activebackground='pink',activeforeground='black',anchor='w',command=exitmember)
    exitbtn.pack(side=TOP,expand=True)
  





#******************************SHOW DATA FRAME***********************************************
    ShowDataFrame=Frame(root,bg='gray',relief=GROOVE,borderwidth=5)
    ShowDataFrame.place(x=550,y=80,width=620,height=600)
#------------------------------------------------------
    style=ttk.Style()
    style.configure('Treeveiw.Heading',font=('chiller',100,'bold'),foreground='white',bg='gray')
    style.configure('Treeveiw',font=('chiller',100,'bold'),foreground='white',bg='gray')
    scroll_x= Scrollbar(ShowDataFrame,orient=HORIZONTAL)
    scroll_y= Scrollbar(ShowDataFrame,orient=VERTICAL)
    membertable= Treeview(ShowDataFrame,columns=('NAME','AGE','GENDER','CONTACT_NO','EMAIL_ID','MEMBERSHIP','ID'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=membertable.xview)
    scroll_y.config(command=membertable.yview)
    membertable.heading('NAME',text='NAME')
    membertable.heading('AGE',text='AGE')
    membertable.heading('GENDER',text='GENDER')
    membertable.heading('CONTACT_NO',text='CONTACT_NO')
    membertable.heading('EMAIL_ID',text='EMAIL_ID')
    membertable.heading('MEMBERSHIP',text='MEMBERSHIP')
    membertable.heading('ID',text='MEMBER_ID')
    membertable['show']='headings'
    membertable.column('ID',width=100)
    membertable.column('MEMBERSHIP',width=200)
    membertable.column('EMAIL_ID',width=250)
    membertable.column('CONTACT_NO',width=200)
    membertable.column('GENDER',width=100)
    membertable.column('AGE',width=100)
    membertable.column('NAME',width=100)

    membertable.pack(fill=BOTH,expand=1)



#*************************SLIDER***********************************************************
    ss='CAR BOOKING SYSTEM'
    count=0
    text=''
    SliderLabel=Label(root,text=ss,relief=RIDGE,borderwidth=4,font=('chiller',30,'italic bold'),width=35,bg='gray',fg='white')
    SliderLabel.place(x=260,y=0)
    IntroLabelTick()
    IntroLabelColorTick()
#************************CLOCK*************************************************************
    Clock =Label(root,relief=RIDGE,borderwidth=4,font=('times',14,'bold'),width=20,bg='gray',fg='white')
    Clock.place(x=0,y=0)
    tick()
#****************************CONNECT DATABASE**********************************************  
    connectbutton =Button(root,text='CONNECT TO DATABASE',width=23,relief=RIDGE,borderwidth=4,font=('chiller',18,'italic bold'),bg='gray',fg='white',activebackground='pink',activeforeground='black',command=connectdb)
    connectbutton.place(x=930,y=0)
    root.mainloop()

    
#else:
    exit
        
###########################  REPORT ###########################################################
print('===================== REPORTS ==========================')
r=input('Do You Want To See Our Performance Through the years?y/n :')
if r=='y' or r=='Y':
    import matplotlib.pyplot as plt
    plt.figure(figsize=(110,110))
    x=['2012','2013','2014','2015','2016','2017','2018','2018','2019','2020']
    y=[12,10,15,12,11,10,14,20,15,11]
    q={'PROFIT(in lakhs)':y}
    w=pd.DataFrame((q),index=x)
    print(w)
    plt.plot(x,y,'mo',markersize=5,markeredgecolor='k',linestyle='solid')
    plt.xlabel('YEAR')
    plt.ylabel('PROFIT')
    plt.grid(True)
    plt.show()
else:
    exit
#=========================================================    
q=input('Do you want to see our monthly performance?y/n :')
if q=='y' or q=='Y':
    import matplotlib.pyplot as plt
    plt.figure(figsize=(110,110))
    x=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    y=[50,42,20,60,20,15,10,31,20,80,50,80]
    q={'PROFIT(in thousands)':y}
    w=pd.DataFrame((q),index=x)
    print(w)
    plt.bar(x,y,color='cyan')
    plt.xlabel('MONTH')
    plt.ylabel('PROFIT')
    plt.show()
else:
    exit
#=========================================================     
s= input('Do you want to see our members membership preferences?y/n :')
if s=='y' or s=='Y':
    import matplotlib.pyplot as plt
    plt.figure(figsize=(110,110))
    x=['GOLD','SILVER','PLATINUM','REGULAR']
    y=[50,56,80,60]
    colors=['coral','orchid','lightseagreen','yellowgreen']
    explode=[0,0,0.1,0]
    q={'Popularity(in %)':y}
    w=pd.DataFrame((q),index=x)
    print(w)
    plt.pie(y,explode=explode,labels=x,colors=colors,autopct='%1.1f%%',shadow=True,startangle=140)
    plt.axis('equal')
    plt.legend(loc='upper left')
    plt.title('MEMBERSHIP PREFERENCES')
    plt.show()
else:
    exit
#=========================================================
s= input('Do you want to see our customers car preferences?y/n :')
if s=='y' or s=='Y':
    import matplotlib.pyplot as plt
    plt.figure(figsize=(110,110))
    x=['STANDARD','PRIME SEDAN','PREMIUM SEDAN']
    y=[40,56,60]
    colors=['pink','lightskyblue','salmon']
    explode=[0,0,0.1]
    q={'Popularity(in %)':y}
    w=pd.DataFrame((q),index=x)
    print(w)
    plt.pie(y,explode=explode,labels=x,colors=colors,autopct='%1.1f%%',shadow=True,startangle=140)
    plt.legend(loc='upper left')
    plt.axis('equal')
    plt.title('CAR PREFERENCES')
    plt.show()
else:
    exit
##########################################################
print('----------THANK YOU FOR VISITING US! :) ------------')
print('======== See You Soon !=========')

