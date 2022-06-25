from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title('Hospital Management System')
        self.root.geometry('1360x735+0+0')


        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NoOfTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.Furtherinfo=StringVar()
        self.BP=StringVar()
        self.StorageAdvice=StringVar()
        self.medication=StringVar()
        self.P_id=StringVar()
        self.nhsNumber=StringVar()
        self.P_nm=StringVar()
        self.DOB=StringVar()
        self.P_Address=StringVar()
        

        #------------------------------- DataFrames --------------------------------------------

        label=Label(self.root,bd=15,fg='red',bg='white',text='HOSPITAL MANAGEMENT SYSTEM',relief=RIDGE,font=('times new roman',30,'bold'))
        label.pack(side=TOP,fill=X)

        dataframe=Frame(self.root,bd=15,relief=RIDGE)
        dataframe.place(x=0,y=85,width=1360,height=390)

        dataframeleft=LabelFrame(dataframe,bd=10,relief=RIDGE,padx=10,font=('times new roman',14,'bold'),text='Patient Information')
        dataframeleft.place(x=7,y=2,width=890,height=350)
        
        dataframeright=LabelFrame(dataframe,bd=10,relief=RIDGE,padx=10,font=('times new roman',14,'bold'),text='Prescription')
        dataframeright.place(x=903,y=2,width=410,height=350)


        # ------------------------------Button Frames ---------------------------------------

        buttonframe=Frame(self.root,bd=15,relief=RIDGE)
        buttonframe.place(x=0,y=485,width=1360,height=70)


        # ------------------------------Details Frames ---------------------------------------

        detailsframe=Frame(self.root,bd=15,relief=RIDGE)
        detailsframe.place(x=0,y=565,width=1360,height=190)


        # ------------------------------dataframeleft-----------------------------------------

        Label(dataframeleft,text='Name of Tablets:', font=('aerial',12,'bold'),padx=2,pady=4).grid(row=0,column=0)
        comNameTablet=ttk.Combobox(dataframeleft,textvariable=self.Nameoftablets,font=('times new roman',12,'italic'),width=30)
        comNameTablet['values']=('Metoprolol','Aspirin EC','Acetaminophen','Adderall','Amlodipine','Ativan')
        comNameTablet.grid(row=0,column=1)

        Label(dataframeleft,text='Reference No.:',font=('aerial',12,'bold'),padx=2,pady=6).grid(row=1,column=0,sticky=W)
        Entry(dataframeleft,textvariable=self.ref,font=('aerial',13,'italic'),width=30).grid(row=1,column=1)

        Label(dataframeleft,text='Dose:',font=('aerial',12,'bold'),padx=2,pady=6).grid(row=2,column=0,sticky=W)
        Entry(dataframeleft,textvariable=self.Dose,font=('aerial',13,'italic'),width=30).grid(row=2,column=1)

        Label(dataframeleft,text='No.of Tablets:',font=('aerial',12,'bold'),padx=2,pady=6).grid(row=3,column=0,sticky=W)
        Entry(dataframeleft,textvariable=self.NoOfTablets,font=('aerial',13,'italic'),width=30).grid(row=3,column=1)

        Label(dataframeleft,text='Lot:',font=('aerial',12,'bold'),padx=2,pady=6).grid(row=4,column=0,sticky=W)
        Entry(dataframeleft,textvariable=self.Lot,font=('aerial',13,'italic'),width=30).grid(row=4,column=1)

        Label(dataframeleft,text='IssueDate:',font=('aerial',12,'bold'),padx=2,pady=6).grid(row=5,column=0,sticky=W)
        Entry(dataframeleft,textvariable=self.Issuedate,font=('aerial',13,'italic'),width=30).grid(row=5,column=1)

        Label(dataframeleft,text='Exp Date:',font=('aerial',12,'bold'),padx=2,pady=6).grid(row=6,column=0,sticky=W)
        Entry(dataframeleft,textvariable=self.ExpDate,font=('aerial',13,'italic'),width=30).grid(row=6,column=1)
        
        Label(dataframeleft,text='Daily Dose:',font=('aerial',12,'bold'),padx=2,pady=6).grid(row=7,column=0,sticky=W)
        Entry(dataframeleft,textvariable=self.DailyDose,font=('aerial',13,'italic'),width=30).grid(row=7,column=1)

        Label(dataframeleft,text='Side Effect:',font=('aerial',12,'bold'),padx=2,pady=6).grid(row=8,column=0,sticky=W)
        Entry(dataframeleft,textvariable=self.sideEffect,font=('aerial',13,'italic'),width=30).grid(row=8,column=1)

        Label(dataframeleft,text='Further Info:',font=('aerial',12,'bold'),padx=2,pady=6).grid(row=0,column=2,sticky=W)
        Entry(dataframeleft,textvariable=self.Furtherinfo,font=('aerial',13,'italic'),width=30).grid(row=0,column=3)

        Label(dataframeleft,text='Blood Pressure:',font=('aerial',12,'bold'),padx=2,pady=6).grid(row=1,column=2,sticky=W)
        Entry(dataframeleft,textvariable=self.BP,font=('aerial',13,'italic'),width=30).grid(row=1,column=3)

        Label(dataframeleft,text='Storage Advice:',font=('aerial',12,'bold'),padx=2,pady=6).grid(row=2,column=2,sticky=W)
        Entry(dataframeleft,textvariable=self.StorageAdvice,font=('aerial',13,'italic'),width=30).grid(row=2,column=3)

        Label(dataframeleft,text='Medication:',font=('aerial',12,'bold'),padx=2,pady=6).grid(row=3,column=2,sticky=W)
        Entry(dataframeleft,textvariable=self.medication,font=('aerial',13,'italic'),width=30).grid(row=3,column=3)

        Label(dataframeleft,text='Patient ID:',font=('aerial',12,'bold'),padx=2,pady=6).grid(row=4,column=2,sticky=W)
        Entry(dataframeleft,textvariable=self.P_id,font=('aerial',13,'italic'),width=30).grid(row=4,column=3)

        Label(dataframeleft,text='NHS Number:',font=('aerial',12,'bold'),padx=2,pady=6).grid(row=5,column=2,sticky=W)
        Entry(dataframeleft,textvariable=self.nhsNumber,font=('aerial',13,'italic'),width=30).grid(row=5,column=3)

        Label(dataframeleft,text='Patient Name:',font=('aerial',12,'bold'),padx=2,pady=6).grid(row=6,column=2,sticky=W)
        Entry(dataframeleft,textvariable=self.P_nm,font=('aerial',13,'italic'),width=30).grid(row=6,column=3)

        Label(dataframeleft,text='Date of Birth:',font=('aerial',12,'bold'),padx=2,pady=6).grid(row=7,column=2,sticky=W)
        Entry(dataframeleft,textvariable=self.DOB,font=('aerial',13,'italic'),width=30).grid(row=7,column=3)

        Label(dataframeleft,text='Patient Address:',font=('aerial',12,'bold'),padx=2,pady=6).grid(row=8,column=2,sticky=W)
        Entry(dataframeleft,textvariable=self.P_Address,font=('aerial',13,'italic'),width=30).grid(row=8,column=3)




        # ----------------------------DataFrameRight-----------------------------------

        scroll_y=Scrollbar(dataframeright)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.txtPrescription=Text(dataframeright,font=('mv boli',13,'bold'),yscrollcommand=scroll_y.set)
        self.txtPrescription.pack()

        scroll_y.config(command=self.txtPrescription.yview)


        #-----------------------------Buttons--------------------------------------
        
        btnPrescription=Button(buttonframe,text='Prescription',fg='white',bg='green',font=('aerail',12,'bold'),width=21,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)
        btnPrescription.bind('<ButtonPress-1>',self.iPrescripton)

        btnPrescriptionData=Button(buttonframe,text='Add Data',fg='white',bg='green',font=('aerail',12,'bold'),width=21,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=1)
        btnPrescriptionData.bind('<ButtonRelease-1>',self.AddData)

        btnUpdate=Button(buttonframe,text='Update',fg='white',bg='green',font=('aerail',12,'bold'),width=21,padx=2,pady=6)
        btnUpdate.grid(row=0,column=3)
        btnUpdate.bind('<ButtonRelease-1>',self.update)

        btnDelete=Button(buttonframe,text='Delete',fg='white',bg='green',font=('aerail',12,'bold'),width=21,padx=2,pady=6)
        btnDelete.grid(row=0,column=4)
        btnDelete.bind('<ButtonRelease-1>',self.delete)

        btnClear=Button(buttonframe,text='Clear',fg='white',bg='green',font=('aerail',12,'bold'),width=21,padx=2,pady=6)
        btnClear.grid(row=0,column=5)
        btnClear.bind('<ButtonRelease-1>',self.Clear)

        btnExit=Button(buttonframe,text='Exit',fg='white',bg='green',font=('aerail',12,'bold'),width=21,padx=2,pady=6)
        btnExit.grid(row=0,column=6)
        btnExit.bind('<ButtonRelease-1>',self.Exit)




        # ---------------------------Tables -----------------------------------------------
        # -----------------------------Scrollbar -----------------------------------------

        scroll_y=Scrollbar(detailsframe,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        columns=['nm_of_tab','ref_no','dose','no_of_tab','lot','issuedate','expdate','daily_dose',
                'storage','nhs_no','p_nm','dob','address']
        self.hospital_table=ttk.Treeview(detailsframe,show='headings',yscrollcommand=scroll_y.set)

        scroll_y.config(command=self.hospital_table.yview)

        l4=['Name of tablets','Reference No.','Dose','No.of Tablets','Lot','IssueDate','Exp Date',
           'Daily Dose','Storage','NHS Number','Patient Name','DOB','Address']
        self.hospital_table['columns']=columns
        
        for i in range(len(l4)):
            self.hospital_table.heading(columns[i],text=l4[i])

        for i in columns:
            self.hospital_table.column(i,width=100)

        self.hospital_table.pack(expand=True,fill=BOTH)
        self.hospital_table.bind('<ButtonRelease-1>',self.get_data)

        self.fetch_data()


    #----------------------------------------Functonality Declaration------------------------------
    def AddData(self,event):
        if self.Nameoftablets.get()=='' or self.ref.get()=='':
            mb.showerror('Error','All fields are required')
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='ZySQLInstaller',database='trial')
            my_cursor=conn.cursor()
            query='insert into hospital value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            value=(self.Nameoftablets.get(),self.ref.get(),self.Dose.get(),self.NoOfTablets.get(),
                   self.Lot.get(),self.Issuedate.get(),self.ExpDate.get(),self.DailyDose.get(),
                   self.StorageAdvice.get(),self.nhsNumber.get(),self.P_nm.get(),self.DOB.get(),
                   self.P_Address.get())
            try:
                my_cursor.execute(query,value)
                conn.commit()
                self.fetch_data()
                mb.showinfo('Success','Your record has been inserted')
            except:
                mb.showerror('Error','No 2 records can have same Ref. ID...')
            finally:
                conn.close()

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='ZySQLInstaller',database='trial')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from hospital')
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert('',END,values=i)
        conn.close()


    def get_data(self,event):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content['values']

        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NoOfTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.P_nm.set(row[10])
        self.DOB.set(row[11])
        self.P_Address.set(row[12])


    def update(self,event):
        conn=mysql.connector.connect(host='localhost',user='root',password='ZySQLInstaller',database='trial')
        my_cursor=conn.cursor()
        query='''update hospital set Nameoftablets=%s,dose=%s,Numberoftablets=%s,lot=%s,issuedate=%s,expdate=%s,
            dailydose=%s,storage=%s,nhsnumber=%s,patientname=%s,DOB=%s,patientaddress=%s where Reference_No=%s'''
        my_cursor.execute(query,(self.Nameoftablets.get(),
                                self.Dose.get(),
                                self.NoOfTablets.get(),
                                self.Lot.get(),
                                self.Issuedate.get(),
                                self.ExpDate.get(),
                                self.DailyDose.get(),
                                self.StorageAdvice.get(),
                                self.nhsNumber.get(),
                                self.P_nm.get(),
                                self.DOB.get(),
                                self.P_Address.get(),
                                self.ref.get()))
        conn.commit()
        conn.close()

        self.fetch_data()
        mb.showinfo('Updated!','Your data has been updated...')



    def iPrescripton(self,event):
        self.txtPrescription.delete('1.0',END)

        self.txtPrescription.insert(END,'\nName of Tablets:\t\t'+self.Nameoftablets.get()+'\n')
        self.txtPrescription.insert(END,'Reference No.:\t\t'+self.ref.get()+'\n')
        self.txtPrescription.insert(END,'Dose:\t\t'+self.Dose.get()+'\n')
        self.txtPrescription.insert(END,'Number of Tablets:\t\t'+self.NoOfTablets.get()+'\n')
        self.txtPrescription.insert(END,'Lot:\t\t'+self.Lot.get()+'\n')
        self.txtPrescription.insert(END,'Issue Date:\t\t'+self.Issuedate.get()+'\n')
        self.txtPrescription.insert(END,'Exp Date:\t\t'+self.ExpDate.get()+'\n')
        self.txtPrescription.insert(END,'Daily Dose:\t\t'+self.DailyDose.get()+'\n')
        self.txtPrescription.insert(END,'Side Effect:\t\t'+self.sideEffect.get()+'\n')
        self.txtPrescription.insert(END,'Further info:\t\t'+self.Furtherinfo.get()+'\n')
        self.txtPrescription.insert(END,'Storage Advice:\t\t'+self.StorageAdvice.get()+'\n')
        self.txtPrescription.insert(END,'BP:\t\t'+self.BP.get()+'\n')
        self.txtPrescription.insert(END,'PatientID:\t\t'+self.P_id.get()+'\n')
        self.txtPrescription.insert(END,'NHS No.:\t\t'+self.nhsNumber.get()+'\n')
        self.txtPrescription.insert(END,'PatientName:\t\t'+self.P_nm.get()+'\n')
        self.txtPrescription.insert(END,'DOB:\t\t'+self.DOB.get()+'\n')
        self.txtPrescription.insert(END,'PatientAddress:\t\t'+self.P_Address.get()+'\n')
    
    def delete(self,event):
        conn=mysql.connector.connect(host='localhost',user='root',password='ZySQLInstaller',database='trial')
        my_cursor=conn.cursor()
        query='delete from hospital where Reference_No=%s'
        my_cursor.execute(query,(self.ref.get(),))
        conn.commit()
        conn.close()

        self.fetch_data()
        mb.showinfo('Delete','Patient data has been deleted...')

    def Clear(self,event):
        self.Nameoftablets.set('')
        self.ref.set('')
        self.Dose.set('')
        self.NoOfTablets.set('')
        self.Lot.set('')
        self.Issuedate.set('')
        self.ExpDate.set('')
        self.DailyDose.set('')
        self.sideEffect.set('')
        self.Furtherinfo.set('')
        self.StorageAdvice.set('')
        self.BP.set('')
        self.medication.set('')
        self.P_id.set('')
        self.nhsNumber.set('')
        self.P_nm.set('')
        self.DOB.set('')
        self.P_Address.set('')
        self.txtPrescription.delete('1.0',END)

    def Exit(self,event):
        result=mb.askyesno('Hospital Management System','Do you really want to exit?')
        if result:
            self.root.destroy()


root=Tk()
obj=Hospital(root)





root.mainloop()