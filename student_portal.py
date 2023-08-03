#!/usr/bin/env python
# coding: utf-8

# In[9]:


from tkinter import * 
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
conn=mysql.connector.connect(host="localhost",port="3306",user="root")
cur=conn.cursor()
try:
    cur.execute("create database prj;")
except:
    pass
try:
    cur.execute("use prj;")
except:
    pass
try:
    cur.execute("create table sdata(Username varchar(40) unique key,Password varchar(40),name varchar(30),course varchar(20),roll int primary key,year int,batch varchar(10),sem int);")
except:
    pass
try:
    cur.execute("create table stdata(username varchar(40) unique key,marks int,att int,pfees int,rollno int primary key);")
    cur.execute("create trigger t before insert on sdata for each row insert into stdata(Username,rollno) values(new.Username,new.roll);")
except:
    pass
try:
    cur.execute("create table adata(Username varchar(40) unique key,Password varchar(40),name varchar(30),dept varchar(10),empno int unique key);")
    cur.execute("insert into adata values('SK1119','SK@1119','Kunal SK Sukhija','CSE',1119);")
    cur.execute("insert into adata values('MK9222','MK@9222','Kashish MK Mehta','CSE',9222);")
except:
    pass
class prj:
    def home(self):
        self.fh=Tk()
        self.w=self.fh.winfo_screenwidth()
        self.h=self.fh.winfo_screenheight()
        self.fh.geometry(f"{self.w}x{self.h}")
        self.fh.configure(bg="black")
        self.fh.title("HOME")
        try:
            self.img=Image.open(r"1.jpg")
            self.ri=self.img.resize((self.w,self.h))
            self.i=ImageTk.PhotoImage(self.ri)
            self.gg=Label(self.fh,image=self.i)
            self.gg.image=self.i
            self.gg.place(x=0,y=0)
        except:
            pass
        self.b1=Button(self.fh,text="STUDENT LOGIN",fg="blue",bg="white",font=("Jokerman",15),command=studin)
        self.b2=Button(self.fh,text="ADMIN LOGIN",bg="#106891",fg="white",font=("Jokerman",15),command=adin)
        self.b3=Button(self.fh,text="SIGN UP",fg="blue",bg="white",font=("Jokerman",15),command=signi)
        self.b312=Button(self.fh,text="EXIT",bg="#0C5678",fg="white",font=("Jokerman",15),command=lambda:o.fh.destroy())
        self.b1.place(relx=0.435,rely=0.35)
        self.b2.place(relx=0.445,rely=0.45)
        self.b3.place(relx=0.462,rely=0.55)
        self.b312.place(relx=0.475,rely=0.65)
        self.fh.mainloop()
    def stdlin(self):
        self.fsl=Tk()
        self.w=self.fsl.winfo_screenwidth()
        self.h=self.fsl.winfo_screenheight()
        self.fsl.geometry(f"{self.w}x{self.h}")
        self.fsl.title("STUDENT LOGIN")
        self.fsl.configure(bg="black")
        try:
            self.img=Image.open(r"2.jpg")
            self.ri=self.img.resize((self.w,self.h))
            self.i=ImageTk.PhotoImage(self.ri)
            self.gg=Label(self.fsl,image=self.i)
            self.gg.image=self.i
            self.gg.place(x=0,y=0)
        except:
            pass
        self.l1=Label(self.fsl,text="Username : ",bg="#0C5678",fg="white",font=("MV Boli",15))
        self.l2=Label(self.fsl,text="Password : ",bg="#0C5678",fg="white",font=("MV Boli",15))
        self.l1.place(relx=0.4,rely=0.4)
        self.l2.place(relx=0.4,rely=0.4625)
        self.e1=Entry(self.fsl,bg="#DCF5F8",fg="black",font=("MV Boli",11))
        self.e2=Entry(self.fsl,bg="#DCF5F8",fg="black",font=("MV Boli",11))
        self.e1.place(relx=0.5,rely=0.4)
        self.e2.place(relx=0.5,rely=0.4625)
        self.b4=Button(self.fsl,text="LOGIN",fg="blue",bg="white",font=("Jokerman",15),command=studlin)
        self.b4.place(relx=0.4,rely=0.525)
        self.b41=Button(self.fsl,text="BACK",fg="white",bg="#0C5678",font=("Jokerman",15),command= a)
        self.b31=Button(self.fsl,text="EXIT",bg="white",fg="blue",font=("Jokerman",15),command=lambda:o.fsl.destroy())
        self.b41.place(relx=0.475,rely=0.525)
        self.b31.place(relx=0.55,rely=0.525)
        self.fsl.mainloop()
    def adlin(self):
        self.fal=Tk()
        self.w=self.fal.winfo_screenwidth()
        self.h=self.fal.winfo_screenheight()
        self.fal.geometry(f"{self.w}x{self.h}")
        self.fal.title("ADMIN LOGIN")
        self.fal.configure(bg="black")
        try:
            self.img=Image.open(r"2.jpg")
            self.ri=self.img.resize((self.w,self.h))
            self.i=ImageTk.PhotoImage(self.ri)
            self.gg=Label(self.fal,image=self.i)
            self.gg.image=self.i
            self.gg.place(x=0,y=0)
        except:
            pass
        self.l3=Label(self.fal,text="Username : ",bg="#0C5678",fg="white",font=("MV Boli",15))
        self.l4=Label(self.fal,text="Password : ",bg="#0C5678",fg="white",font=("MV Boli",15))
        self.l3.place(relx=0.4,rely=0.4)
        self.l4.place(relx=0.4,rely=0.4625)
        self.e3=Entry(self.fal,bg="#DCF5F8",fg="black",font=("MV Boli",11))
        self.e4=Entry(self.fal,bg="#DCF5F8",fg="black",font=("MV Boli",11))
        self.e3.place(relx=0.5,rely=0.4)
        self.e4.place(relx=0.5,rely=0.4625)
        self.b5=Button(self.fal,text="LOGIN",bg="white",fg="blue",font=("Jokerman",15),command=admlin)
        self.b51=Button(self.fal,text="BACK",bg="#0C5678",fg="white",font=("Jokerman",15),command= b)       
        self.b321=Button(self.fal,text="EXIT",bg="white",fg="blue",font=("Jokerman",15),command=lambda:o.fal.destroy())
        self.b5.place(relx=0.4,rely=0.525)
        self.b51.place(relx=0.475,rely=0.525)
        self.b321.place(relx=0.55,rely=0.525)
        self.fal.mainloop()
    def sign(self):
        self.fs=Tk()
        self.w=self.fs.winfo_screenwidth()
        self.h=self.fs.winfo_screenheight()
        self.fs.geometry(f"{self.w}x{self.h}")
        self.fs.configure(bg="black")
        self.fs.title("SIGNUP")
        try:
            self.img=Image.open(r"4.jpg")
            self.ri=self.img.resize((self.w,self.h))
            self.i=ImageTk.PhotoImage(self.ri)
            self.gg=Label(self.fs,image=self.i)
            self.gg.image=self.i
            self.gg.place(x=0,y=0)
        except:
            pass
        self.l5=Label(self.fs,text="Username : ",bg="#04614C",fg="white",font=("MV Boli",15))
        self.l6=Label(self.fs,text="Password : ",bg="#04614C",fg="white",font=("MV Boli",15))
        self.l61=Label(self.fs,text="Name : ",bg="#04614C",fg="white",font=("MV Boli",15))
        self.l63=Label(self.fs,text="Rollno : ",bg="#04614C",fg="white",font=("MV Boli",15))
        self.l62=Label(self.fs,text="Course : ",bg="#04614C",fg="white",font=("MV Boli",15))
        self.l64=Label(self.fs,text="Year : ",bg="#04614C",fg="white",font=("MV Boli",15))
        self.l65=Label(self.fs,text="Batch : ",bg="#04614C",fg="white",font=("MV Boli",15))
        self.l66=Label(self.fs,text="Semester : ",bg="#04614C",fg="white",font=("MV Boli",15))
        self.l5.place(relx=0.4,rely=0.25)
        self.l6.place(relx=0.4,rely=0.3)
        self.l61.place(relx=0.4,rely=0.35)
        self.l62.place(relx=0.4,rely=0.4)
        self.l63.place(relx=0.4,rely=0.45)
        self.l64.place(relx=0.4,rely=0.5)
        self.l65.place(relx=0.4,rely=0.55)
        self.l66.place(relx=0.4,rely=0.6)
        self.e5=Entry(self.fs,bg="#B6F3DC",fg="black",font=("MV Boli",11))
        self.e6=Entry(self.fs,bg="#B6F3DC",fg="black",font=("MV Boli",11))
        self.e61=Entry(self.fs,bg="#B6F3DC",fg="black",font=("MV Boli",11))
        self.e63=Entry(self.fs,bg="#B6F3DC",fg="black",font=("MV Boli",11))
        self.e64=Entry(self.fs,bg="#B6F3DC",fg="black",font=("MV Boli",11))
        self.e65=Entry(self.fs,bg="#B6F3DC",fg="black",font=("MV Boli",11))
        self.e66=Entry(self.fs,bg="#B6F3DC",fg="black",font=("MV Boli",11))
        self.e5.place(relx=0.5,rely=0.25)
        self.e6.place(relx=0.5,rely=0.3)
        self.e61.place(relx=0.5,rely=0.35)
        self.op=['B.Tech. (CSE)','B.Tech. (ME)','B.Tech. (ECE)','B.Tech. (ELE)','B.Tech. (Civil)','B.Tech. (IT)','BCA','BBA','MBA','M.Tech.']
        self.v=StringVar()
        self.v.set("Select The Course")
        self.m=OptionMenu(self.fs,self.v,*self.op)
        self.m.configure(bg="#B6F3DC",fg="black",font=("MV Boli",11))
        self.m.place(relx=0.5,rely=0.4)
        self.e63.place(relx=0.5,rely=0.45)
        self.e64.place(relx=0.5,rely=0.5)
        self.e65.place(relx=0.5,rely=0.55)
        self.e66.place(relx=0.5,rely=0.6)
        self.b6=Button(self.fs,text="SUBMIT",bg="#B6F3DC",fg="black",font=("Jokerman",15),command=sub)
        self.b61=Button(self.fs,text="BACK",fg="#B6F3DC",bg="#052A19",font=("Jokerman",15),command= c)
        self.b33=Button(self.fs,text="EXIT",bg="#B6F3DC",fg="black",font=("Jokerman",15),command=lambda:o.fs.destroy())
        self.b6.place(relx=0.4,rely=0.65)
        self.b61.place(relx=0.475,rely=0.65)
        self.b33.place(relx=0.535,rely=0.65)
        self.fs.mainloop()
    def lgins(self):
        self.fls=Tk()
        self.w=self.fls.winfo_screenwidth()
        self.h=self.fls.winfo_screenheight()
        self.fls.geometry(f"{self.w}x{self.h}")
        self.fls.configure(bg="black")
        self.fls.title("STUDENT PORTAL")
        try:
            self.img=Image.open(r"3.jpg")
            self.ri=self.img.resize((self.w,self.h))
            self.i=ImageTk.PhotoImage(self.ri)
            self.gg=Label(self.fls,image=self.i)
            self.gg.image=self.i
            self.gg.place(x=0,y=0)
        except:
            pass
        self.l7=Button(self.fls,text="RESULT",bg="gray",font=("MV Boli",15),command=res)
        self.l7.place(relx=0.365,rely=0.425)
        self.l7=Button(self.fls,text="ATTENDANCE",bg="gray",font=("MV Boli",15),command=att)
        self.l7.place(relx=0.435,rely=0.425)
        self.l7=Button(self.fls,text="PENDING FEE",bg="gray",font=("MV Boli",15),command=fee)
        self.l7.place(relx=0.545,rely=0.425)
        self.b7=Button(self.fls,text="BACK",bg="gray",font=("Jokerman",15),command=backs)
        self.b34=Button(self.fls,text="EXIT",bg="gray",font=("Jokerman",15),command=lambda:o.fls.destroy())
        self.b71=Button(self.fls,text="HOME",bg="gray",font=("Jokerman",15),command=D)
        self.l=Label(self.fls)
        self.b7.place(relx=0.4,rely=0.5)
        self.b71.place(relx=0.475,rely=0.5)
        self.b34.place(relx=0.55,rely=0.5)
    def lgina(self):
        self.fla=Tk()
        self.w=self.fla.winfo_screenwidth()
        self.h=self.fla.winfo_screenheight()
        self.fla.geometry(f"{self.w}x{self.h}")
        self.fla.configure(bg="black")
        self.fla.title("ADMIN PORTAL")
        try:
            self.img=Image.open(r"3.jpg")
            self.ri=self.img.resize((self.w,self.h))
            self.i=ImageTk.PhotoImage(self.ri)
            self.gg=Label(self.fla,image=self.i)
            self.gg.image=self.i
            self.gg.place(x=0,y=0)
        except:
            pass
        self.l81=Button(self.fla,text="SHOW DETAILS",bg="gray",font=("MV Boli",17),command=shd)
        self.l81.place(relx=0.445,rely=0.175)
        self.l8=Button(self.fla,text="UPDATE RECORDS",bg="gray",font=("MV Boli",17),command=upd)
        self.l8.place(relx=0.28,rely=0.275)
        self.l9=Button(self.fla,text="END SESSION",bg="gray",font=("MV Boli",17),command=end)
        self.l9.place(relx=0.4475,rely=0.275)
        self.l0=Button(self.fla,text="PENDING FEE",bg="gray",font=("MV Boli",17),command=fe)
        self.l0.place(relx=0.579,rely=0.275)
        self.b8=Button(self.fla,text="BACK",bg="gray",font=("Jokerman",15),command=backa)
        self.b81=Button(self.fla,text="HOME",bg="gray",font=("Jokerman",15),command=E)        
        self.b35=Button(self.fla,text="EXIT",bg="gray",font=("Jokerman",15),command=lambda:o.fla.destroy())
        self.b8.place(relx=0.4,rely=0.9)
        self.b81.place(relx=0.475,rely=0.90)
        self.b35.place(relx=0.55,rely=0.9)
def studin():
    o.fh.destroy()
    o.stdlin()
def adin():
    o.fh.destroy()
    o.adlin()
def signi():
    o.fh.destroy()
    o.sign()
def studlin():
    eu=o.e1.get()
    ep=o.e2.get()
    cur.execute(f"select * from sdata where Username='{eu}' and Password='{ep}';")
    global val
    val=cur.fetchall()
    try:
        if len(val)>0:
            o.fsl.destroy()
            o.lgins()
    except:
        messagebox.showwarning("Incorrect Details","The details that are entered do not match any record")
def admlin():
    eau=o.e3.get()
    eap=o.e4.get()
    cur.execute(f"select * from adata where Username='{eau}' and Password='{eap}';")
    va=cur.fetchall()
    if len(va)>0:
        o.fal.destroy()
        o.lgina()
    else:
        o.e3.delete(0,END)
        o.e4.delete(0,END)
        messagebox.showwarning("Incorrect Details","The details that are entered do not match any record")
def backs():
    o.fls.destroy()
    o.stdlin()
def backa():
    o.fla.destroy()
    o.adlin()
def sub():
    U=o.e5.get()
    P=o.e6.get()
    N=o.e61.get()
    C=o.v.get()
    R=o.e63.get()
    Y=o.e64.get()
    B=o.e65.get()
    S=o.e66.get()
    cur.execute(f"insert into sdata values('{U}','{P}','{N}','{C}','{R}','{Y}','{B}','{S}');")
    messagebox.showinfo("Submit","Details Registered")
    o.fs.destroy()
    o.stdlin()
def a():
    o.fsl.destroy()
    o.home()
def b():
    o.fal.destroy()
    o.home()
def c():
    o.fs.destroy()
    o.home()
def D():
    o.fls.destroy()
    o.home()
def E():
    o.fla.destroy()
    o.home()
def res():
    cur.execute(f"select marks from stdata where Username='{val[0][0]}'")
    g=cur.fetchall()
    if g[0][0] is None:
        messagebox.showwarning("Error","Record Not Found Please Contact Administrator")
    else:
        o.l.destroy()
        o.l=Label(o.fls,text=f"The Marks of {val[0][0]} are: {g[0][0]}",bg="gray",font=("MV Boli",25))
        o.l.place(relx=0.365,rely=0.6)
def att():
    cur.execute(f"select att from stdata where Username='{val[0][0]}'")
    g=cur.fetchall()
    print(type(g[0][0]))
    if g[0][0] is None:
        messagebox.showwarning("Error","Record Not Found Please Contact Administrator")
    else:
        o.l.destroy()
        o.l=Label(o.fls,text=f"The Attendance of {val[0][0]} is: {g[0][0]}%",bg="gray",font=("MV Boli",25))
        o.l.place(relx=0.34,rely=0.6)
def fee():
    cur.execute(f"select pfees from stdata where Username='{val[0][0]}'")
    g=cur.fetchall()
    if g[0][0] is None:
        messagebox.showwarning("Error","Record Not Found Please Contact Administrator")
    else:
        o.l.destroy()
        o.l=Label(o.fls,text=f"The Pending Dues of {val[0][0]} are: Rs.{g[0][0]}",bg="gray",font=("MV Boli",25))
        o.l.place(relx=0.32,rely=0.6)
def de():
    R=o.e.get()
    M=o.eq1.get()
    A=o.eq2.get()
    F=o.eq3.get()
    cur.execute(f"select * from stdata where rollno={R};")
    ww=cur.fetchall()
    if len(ww)>0:
        cur.execute(f"update stdata set marks={M},att={A},pfees={F} where rollno={R};")
        messagebox.showinfo("Updated","Records Updated SuccessFully")
    else:
        messagebox.showwarning("Error","Record Not Found")
def df():
    R=o.ee.get()
    cur.execute(f"select * from stdata join sdata on stdata.rollno=sdata.roll where rollno={R};")
    ww=cur.fetchall()
    if len(ww)>0:
        l=Label(o.fla,text=f"Username:{ww[0][0]}\nMarks:{ww[0][1]}\nAttendance:{ww[0][2]}\nPending Fees:{ww[0][3]}\nRollno:{ww[0][4]}\nName:{ww[0][7]}\nCourse:{ww[0][8]}\nYear:{ww[0][10]}\nBatch:{ww[0][11]}\nSemester:{ww[0][12]}",bg="gray",font=("MV Boli",18))
        l.place(relx=0.4,rely=0.488)
    else:
        messagebox.showwarning("Error","Record not found")
def upd():
    o.fla.destroy()
    o.lgina()
    l=Label(o.fla,text="Student's Rollno:",bg="gray",font=("MV Boli",15))
    o.e=Entry(o.fla,bg="gray",font=("MV Boli",15))
    l.place(relx=0.33,rely=0.375)
    o.e.place(relx=0.48,rely=0.375)
    o.q1=Label(o.fla,text="Marks:",bg="gray",font=("MV Boli",15))
    o.q2=Label(o.fla,text="Attendance:",bg="gray",font=("MV Boli",15))
    o.q3=Label(o.fla,text="Pending Fees:",bg="gray",font=("MV Boli",15))
    o.q1.place(relx=0.33,rely=0.425)
    o.q2.place(relx=0.33,rely=0.475)
    o.q3.place(relx=0.33,rely=0.525)
    o.eq1=Entry(o.fla,bg="gray",font=("MV Boli",15))
    o.eq2=Entry(o.fla,bg="gray",font=("MV Boli",15))
    o.eq3=Entry(o.fla,bg="gray",font=("MV Boli",15))
    o.eq1.place(relx=0.48,rely=0.425)
    o.eq2.place(relx=0.48,rely=0.475)
    o.eq3.place(relx=0.48,rely=0.525)
    s=Button(text="UPDATE",bg="gray",font=("MV Boli",15),command=de)
    s.place(relx=0.49,rely=0.575)
def shd():
    o.fla.destroy()
    o.lgina()
    l=Label(o.fla,text="Student's Rollno:",bg="gray",font=("MV Boli",15))
    o.ee=Entry(o.fla,bg="gray",font=("MV Boli",15))
    l.place(relx=0.33,rely=0.375)
    o.ee.place(relx=0.48,rely=0.375)
    s=Button(text="SHOW",bg="gray",font=("MV Boli",15),command=df)
    s.place(relx=0.49,rely=0.4355)
def d():
    u=o.e.get()
    cur.execute(f"select marks from stdata where rollno={u};")
    g=cur.fetchall()
    if len(g)>0:
        if g[0][0]>40:
            cur.execute(f"update sdata set sem=sem+1 where roll={u}")
            messagebox.showinfo("Passed",f"Student passes with {g[0][0]}% marks \nPromoted SuccessFully")
        else:
            messagebox.showinfo("OOPS!",f"Student fails with {g[0][0]}% marks \nBetter Luck Next Time")
    else:
        messagebox.showwarning("Error","Record Not Found")
def end():
    o.fla.destroy()
    o.lgina()
    l=Label(o.fla,text="Student's Rollno:",bg="gray",font=("MV Boli",15))
    o.e=Entry(o.fla,bg="gray",font=("MV Boli",15))
    l.place(relx=0.33,rely=0.375)
    o.e.place(relx=0.48,rely=0.375)
    s=Button(text="END",bg="gray",font=("MV Boli",15),command=d)
    s.place(relx=0.49,rely=0.425)
def e():
    f=o.e1.get()
    r=o.e.get()
    cur.execute(f"update stdata set pfees=pfees-{f} where rollno={r};")
    messagebox.showinfo("RECEIPT","Fees Updated SuccessFully")
def pf():
    u=o.e.get()
    cur.execute(f"select pfees from stdata where rollno={u};")
    g=cur.fetchall()
    if len(g)>0:
        l1=Label(o.fla,text=f"Pending Fees=\n{g[0][0]}",bg="gray",font=("MV Boli",15))
        l1.place(relx=0.49,rely=0.57)
        l2=Label(o.fla,text="Fees Paid:",bg="gray",font=("MV Boli",15))
        l2.place(relx=0.4,rely=0.655)
        o.e1=Entry(o.fla,bg="gray",font=("MV Boli",15))
        o.e1.place(relx=0.49,rely=0.655)
        b=Button(o.fla,text="UPDATE",bg="gray",font=("MV Boli",15),command=e)
        b.place(relx=0.485,rely=0.71)
    else:
        messagebox.showwarning("Error","Record Not Found")
def fe():
    o.fla.destroy()
    o.lgina()
    l=Label(o.fla,text="Student's Rollno:",bg="gray",font=("MV Boli",15))
    o.e=Entry(o.fla,bg="gray",font=("MV Boli",15))
    l.place(relx=0.33,rely=0.375)
    o.e.place(relx=0.48,rely=0.375)
    s=Button(text="SUBMIT",bg="gray",font=("MV Boli",15),command=pf)
    s.place(relx=0.49,rely=0.425)
o=prj()

o.home()
cur.close()
conn.commit()
conn.close()

