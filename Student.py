from tkinter import * 
from tkinter import ttk
import psycopg2
from tkinter import messagebox
class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x1000+0+0")
        

        title = Label(self.root,text="S t u d e n t    M a n a g e m e n t    S y s t e m",bd=1,relief=GROOVE,font=("stencil",35),bg="yellow",fg="black")
        title.pack(side=TOP,fill=X)

        #variables for database
        self.varRollNo = StringVar()
        self.varName = StringVar()
        self.varEmail = StringVar()
        self.varGender = StringVar()
        self.varContactNo = StringVar()
        self.varDob = StringVar()
        self.varCity = StringVar()
        self.varSearchMain = StringVar()
        self.varSearchTxt = StringVar()
        self.testName = StringVar()
        self.testEmail = StringVar()
        self.testGender = StringVar()
        self.testContactNo = StringVar()
        self.testDob = StringVar()
        self.testCity = StringVar()
        self.testRollNo = StringVar()

        #for manage student data
        manage_frame = Frame(self.root,bd=1,relief=RIDGE,bg="sky blue")
        manage_frame.place(x=20,y=100,width=450,height=700)
        m_title = Label(manage_frame,text="Manage  Students",font=("stencil",24),bg="sky blue",fg="black")
        m_title.grid(row=0,columnspan=2,pady=20)
        lbl_roll = Label(manage_frame,text="Roll No.",font=("Copperplate Gothic Bold",20),bg="sky blue",fg="black")
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        txt_roll = Entry(manage_frame,textvariable=self.varRollNo,font=("times new roman",15,"bold"),relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name = Label(manage_frame,text="Name.",font=("Copperplate Gothic Bold",20),bg="sky blue",fg="black")
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        txt_name = Entry(manage_frame,textvariable=self.varName,font=("times new roman",15,"bold"),relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_email = Label(manage_frame,text="Email.",font=("Copperplate Gothic Bold",20),bg="sky blue",fg="black")
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        txt_email = Entry(manage_frame,textvariable=self.varEmail,font=("times new roman",15,"bold"),relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_gender = Label(manage_frame,text="Gender.",font=("Copperplate Gothic Bold",20),bg="sky blue",fg="black")
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        txt_gender = ttk.Combobox(manage_frame,textvariable=self.varGender,font=("times new roman",13,"bold"),state="readonly")
        txt_gender['values'] = ("Male","Female","Transgender")
        txt_gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        lbl_contact = Label(manage_frame,text="Contact.",font=("Copperplate Gothic Bold",20),bg="sky blue",fg="black")
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        txt_contact = Entry(manage_frame,textvariable=self.varContactNo,font=("times new roman",15,"bold"),relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_DOB= Label(manage_frame,text="D.O.B.",font=("Copperplate Gothic Bold",20),bg="sky blue",fg="black")
        lbl_DOB.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        txt_DOB = Entry(manage_frame,textvariable=self.varDob,font=("times new roman",15,"bold"),relief=GROOVE)
        txt_DOB.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_city = Label(manage_frame,text="City.",font=("Copperplate Gothic Bold",20),bg="sky blue",fg="black")
        lbl_city.grid(row=7,column=0,pady=10,padx=20,sticky="w")
        txt_city = Entry(manage_frame,textvariable=self.varCity,font=("times new roman",15,"bold"),relief=GROOVE)
        txt_city.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        #frame for buttons in manage students frame 
        btn_frame = Frame(manage_frame,relief=RIDGE,bg="sky blue",padx=5,pady=8)
        btn_frame.place(x=10,y=610,width=430)
        add_button = Button(btn_frame,text="Add",bd=0.5,width=9,command=self.AddStudent,bg="blue",fg="white",font=("times new roman",12,"bold")).grid(row=0,column=0,padx=5,pady=5)
        update_button = Button(btn_frame,text="Update",bd=0.5,width=9,command=self.updateData,bg="blue",fg="white",font=("times new roman",12,"bold")).grid(row=0,column=1,padx=5,pady=5)
        delete_button = Button(btn_frame,text="Delete",bd=0.5,width=9,command=self.deleteRecord,bg="blue",fg="white",font=("times new roman",12,"bold")).grid(row=0,column=2,padx=5,pady=5)
        clear_button = Button(btn_frame,text="Clear",bd=0.5,width=9,command=self.clearData,bg="blue",fg="white",font=("times new roman",12,"bold")).grid(row=0,column=3,padx=5,pady=5)

        #main frame for searching and content showing
        manage_frame1 = Frame(self.root,bd=1,relief=RIDGE,bg="sky blue")
        manage_frame1.place(x=500,y=100,width=1000,height=700)
        lbl_search = Label(manage_frame1,text="Search By.",font=("times new roman",20,"bold"),bg="sky blue",fg="black")
        lbl_search.grid(row=0,column=1,pady=10,padx=20,sticky="w")
        txt_search = ttk.Combobox(manage_frame1,textvariable=self.varSearchMain,font=("times new roman",13,"bold"),state="readonly")
        txt_search['values'] = ("rollno","name","contactno")
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w") 

        txt_srch = Entry(manage_frame1,textvariable=self.varSearchTxt,font=("times new roman",15,"bold"),relief=GROOVE)
        txt_srch.grid(row=0,column=3,pady=10,padx=20,sticky="w")
       
        lbl_srch = Button(manage_frame1,command=self.searchData,bd=0.5,width=9,text="Search",bg="blue",fg="white",font=("times new roman",12,"bold"))
        lbl_srch.grid(row=0,column=4,pady=10,padx=20,sticky="w")

        lbl_showall = Button(manage_frame1,command=self.FetchData,bd=0.5,width=9,text="Show All",bg="blue",fg="white",font=("times new roman",12,"bold"))
        lbl_showall.grid(row=0,column=5,pady=10,padx=20,sticky="w")
        #lblDev = Label(manage_frame1,text="Email.",font=("Copperplate Gothic Bold",20),bg="sky blue",fg="black")
        #lblDev.grid(row=1,column=3,pady=50,padx=100,sticky="w")
        #For Content showing
        manage_frame2 = Frame(manage_frame1,bd=1,relief=RIDGE,bg="white")
        manage_frame2.place(x=20,y=100,width=950,height=532)
        scrolling_x = Scrollbar(manage_frame2,orient=HORIZONTAL)
        scrolling_y = Scrollbar(manage_frame2,orient=VERTICAL)
        self.studentsView = ttk.Treeview(manage_frame2,columns=("ROLLNO","NAME","EMAIL","GENDER","CONTACT","DOB","CITY"),xscrollcommand=scrolling_x.set,yscrollcommand=scrolling_y.set)
        scrolling_x.pack(side=BOTTOM,fill=X)
        scrolling_y.pack(side=RIGHT,fill=Y)
        scrolling_x.config(command=self.studentsView.xview)
        scrolling_y.config(command=self.studentsView.yview)
        self.studentsView.heading("ROLLNO",text="RollNo.")
        self.studentsView.heading("NAME",text="Name.")
        self.studentsView.heading("EMAIL",text="Email.")
        self.studentsView.heading("GENDER",text="Gender.")
        self.studentsView.heading("CONTACT",text="Contact.")
        self.studentsView.heading("DOB",text="D.O.B.")
        self.studentsView.heading("CITY",text="City.")
        self.studentsView['show']='headings'
        self.studentsView.column("ROLLNO",width=100)
        self.studentsView.column("NAME",width=130)
        self.studentsView.column("EMAIL",width=130)
        self.studentsView.column("GENDER",width=100)
        self.studentsView.column("CONTACT",width=100)
        self.studentsView.column("DOB",width=100)
        self.studentsView.column("CITY",width=100)
        self.studentsView.pack(fill=BOTH,expand=1)
        self.FetchData()
        self.studentsView.bind("<ButtonRelease-1>",self.getData)
        self.testerUpdate()
        manage_frame3 = Frame(manage_frame1,bd=0,relief=RIDGE,bg="sky blue")
        manage_frame3.place(x=20,y=635,width=950,height=50) 
        Devs = Label(manage_frame3,text="UI/DB - Taru.Chetan.K",font=("Comic Sans MS",12),bg="sky blue",fg="black")
        Devs.place(x=700,y=-2)
        Devs = Label(manage_frame3,text="Email - taruchetan8@gmail.com",font=("Comic Sans MS",12),bg="sky blue",fg="black")
        Devs.place(x=700,y=24)
        #Functions to operate buttons
    def AddStudent(self):
        if self.varRollNo.get()!="" and self.varName.get()!="" and self.varEmail.get()!="" and self.varGender.get()!="" and self.varContactNo.get()!="" and self.varDob.get()!="" and self.varCity.get()!="":

            con = psycopg2.connect(host="localhost",user="postgres",password="7191",database="StudentMgmt")
            cr = con.cursor()
            cr.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.varRollNo.get(),
                                                                        self.varName.get(),
                                                                        self.varEmail.get(),
                                                                        self.varGender.get(),
                                                                        self.varContactNo.get(),
                                                                        self.varDob.get(),
                                                                        self.varCity.get()
                                                                        ))
            con.commit()
            self.FetchData()
            self.clearData()
            con.close()
            messagebox.showinfo("Success...","Record inserted...!!!")
        else:
            messagebox.showerror("Error!!!","All Fields are Required!!!")

    
    def FetchData(self):
        con = psycopg2.connect(host="localhost",user="postgres",password="7191",database="StudentMgmt")
        cr = con.cursor()
        cr.execute("select * from students ORDER BY rollno ASC")
        rows = cr.fetchall()
        if len(rows)!=0:
            self.studentsView.delete(*self.studentsView.get_children())
            for rw in rows: 
                self.studentsView.insert('',END,values=rw)
        con.commit()
        con.close()

    def deleteRecord(self):
        if self.varRollNo.get()!="" or self.varName.get()!="" or self.varEmail.get()!="" or self.varGender.get()!="" or self.varContactNo.get()!="" or self.varDob.get()!="" or self.varCity.get()!="":

            con = psycopg2.connect(host="localhost",user="postgres",password="7191",database="StudentMgmt")
            cr = con.cursor()
            #cr.execute("delete from students where rollno='" + str(self.varRollNo.get())+"'")
            cr.execute("delete from students where rollno=%s",self.varRollNo.get())
            con.commit()
            con.close()
            self.FetchData()
            self.clearData()
            messagebox.showinfo("Success...","Record deleted...!!!")
        else:
            messagebox.showerror("Error!!!","Empty fields can't be deleted!!!")
    
    def getData(self,extra):
        crRow = self.studentsView.focus()
        rowData = self.studentsView.item(crRow)
        data = rowData['values']
        self.varRollNo.set(data[0])
        self.varName.set(data[1])
        self.varEmail.set(data[2])
        self.varGender.set(data[3])
        self.varContactNo.set(data[4])
        self.varDob.set(data[5])
        self.varCity.set(data[6])

    def updateData(self):
        if self.varRollNo.get()!="" or self.varName.get()!="" or self.varEmail.get()!="" or self.varGender.get()!="" or self.varContactNo.get()!="" or self.varDob.get()!="" or self.varCity.get()!="":
            if self.varRollNo.get()!=self.testRollNo or self.varName.get()!=self.testName or self.varEmail.get()!=self.testEmail or self.varGender.get()!=self.testGender or self.varContactNo.get()!=self.testContactNo or self.varDob.get()!=self.testDob or self.varCity.get()!=self.testCity:

                con = psycopg2.connect(host="localhost",user="postgres",password="7191",database="StudentMgmt")
                cr = con.cursor()
                cr.execute("update students set name=%s,email=%s,gender=%s,contactno=%s,dob=%s,city=%s where rollno=%s",(
                                                                                                                        self.varName.get(),
                                                                                                                        self.varEmail.get(),
                                                                                                                        self.varGender.get(),
                                                                                                                        self.varContactNo.get(),
                                                                                                                        self.varDob.get(),
                                                                                                                        self.varCity.get(),
                                                                                                                        self.varRollNo.get()
                                                                            ))
                con.commit()
                self.FetchData()
                self.clearData()
                con.close()
                messagebox.showinfo("Success...","Record Updated...!!!")
            else:
                messagebox.showerror("Error!!!","you can't change anything!!!")                
        else:
            messagebox.showerror("Error!!!","Empty fields can,t update!!!")
    
    def clearData(self):
        if self.varRollNo.get()!="" or self.varName.get()!="" or self.varEmail.get()!="" or self.varGender.get()!="" or self.varContactNo.get()!="" or self.varDob.get()!="" or self.varCity.get()!="":

            self.varRollNo.set('')
            self.varName.set('')
            self.varEmail.set('')
            self.varGender.set('')
            self.varContactNo.set('')
            self.varDob.set('')
            self.varCity.set('')
        else:
            messagebox.showwarning("Checking...","Nothing to clear...")

    def searchData(self):
        if self.varSearchTxt.get()!="":

            con = psycopg2.connect(host="localhost",user="postgres",password="7191",database="StudentMgmt")
            cr = con.cursor()
            cr.execute("select * from students where "+str(self.varSearchMain.get())+" LIKE '"+str(self.varSearchTxt.get())+"%'")
            rows = cr.fetchall()
            if len(rows)!=0:
                self.studentsView.delete(*self.studentsView.get_children())
                for rw in rows:
                    self.studentsView.insert('',END,values=rw)
            con.commit()
            con.close()
        else:
            messagebox.showwarning("Checking...","Plz enter search contain...")
    
    def testerUpdate(self):
        self.testName = self.varName.get()
        self.testEmail = self.varEmail.get()
        self.testGender = self.varGender.get()
        self.testContactNo = self.varContactNo.get()
        self.testDob = self.varDob.get()
        self.testCity = self.varCity.get()
        self.testRollNo = self.varRollNo.get()

    '''def deleteAll(self):
        con = psycopg2.connect(host="localhost",user="postgres",password="7191",database="StudentMgmt")
        cr = con.cursor()
        cr.execute("delete from students")'''

root = Tk()
ob = Student(root)
root.mainloop()