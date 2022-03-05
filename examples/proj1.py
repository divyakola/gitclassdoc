from tkinter import *
from tkinter import messagebox
import sqlite3
import csv
window=Tk()
window['bg']="powderblue"
window.geometry("700x500")
fn=StringVar()
ln=StringVar()
add=StringVar()
con=IntVar()
email=StringVar()
gender=StringVar()
conn_obj=sqlite3.connect('IhubPy.db')
cur_obj=conn_obj.cursor()
cur_obj.execute("""create table student1(fname string,lname string,
address string,contact integer,email string,gender string)""")
def confirm():
    messagebox.showinfo("congrates",
                        "record successfully inserted")
    
def insert():
    cur_obj.execute("insert into student1 values(?,?,?,?,?,?)",
                (fn.get(),ln.get(),add.get(),con.get(),
                     email.get(),gender.get()))
    cur_obj.execute("commit")
    confirm()
    fn.set('')
    ln.set('')
    add.set('')
    con.set(0)
    email.set('')
    gender.set(1)
def get():
    cur_obj.execute("select * from student1")
    with open('ihubstudent.csv','w') as f1:
        writer_obj=csv.writer(f1)
        for rec in cur_obj:
            writer_obj.writerow(list(rec))
        

L=Label(window,text="Welcome To My Application",fg="red",
        bg="blue",font=('elephant',30,'italic')).pack()
L1=Label(window,text="Enter First Name",fg="brown",font=20)
L1.place(x=50,y=75)
E1=Entry(window,fg="blue",font=20,bd=5,textvariable=fn)
E1.place(x=250,y=75)
L2=Label(window,text="Enter Last Name",fg="brown",font=20)
L2.place(x=50,y=110)
E2=Entry(window,fg="blue",font=20,bd=5,textvariable=ln)
E2.place(x=250,y=110)
L3=Label(window,text="Enter Address",fg="brown",font=20)
L3.place(x=50,y=145)
E3=Entry(window,fg="blue",font=20,bd=5,textvariable=add)
E3.place(x=250,y=145)
L4=Label(window,text="Enter Mobile Number",fg="brown",font=20)
L4.place(x=50,y=180)
E4=Entry(window,fg="blue",font=20,bd=5,textvariable=con)
E4.place(x=250,y=180)
L5=Label(window,text="Enter Email",fg="brown",font=20)
L5.place(x=50,y=215)
E5=Entry(window,fg="blue",font=20,bd=5,textvariable=email)
E5.place(x=250,y=215)
L6=Label(window,text="Select Gender",fg="brown",font=20)
L6.place(x=50,y=250)
R1=Radiobutton(window,text="male",value=1,variable=gender,name='m')
R1.place(x=250,y=250)
R2=Radiobutton(window,text="feMale",value=0,variable=gender,name='f')
R2.place(x=400,y=250)
B1=Button(window,text="Insert",command=insert)
B1.place(x=200,y=300)
B2=Button(window,text="Get",command=get)
B2.place(x=300,y=300)
