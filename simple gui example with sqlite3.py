from tkinter import *
import sqlite3
window=Tk()
fn=StringVar()
ln=StringVar()
def store():
    conn_obj=sqlite3.connect("myemp.db")
    cur_obj=conn_obj.cursor()
    cur_obj.execute("""create table emp2(fname string,
lname string)""")
    cur_obj.execute("insert into emp2 values(?,?)",
                    (fn.get(),ln.get()))
    cur_obj.execute("commit")
    cur_obj.close()
    conn_obj.close()
L1=Label(window,text="enter First Name: ").place(x=10,y=20)
E1=Entry(window,bd=5,textvariable=fn).place(x=150,y=20)
L2=Label(window,text="enter Last Name: ").place(x=10,y=50)
E2=Entry(window,bd=5,textvariable=ln).place(x=150,y=50)
B1=Button(window,text="submit",command=store).place(x=50,y=75)



    
