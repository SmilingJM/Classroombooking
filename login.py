from lib2to3.pgen2.token import STRING
import sqlite3
from tkinter import *
from tkinter.font import BOLD
import tkinter.messagebox
import sys
import os
from PIL import Image,ImageTk

window = Tk()
window.title("ED KKU Room reservation")
window.iconbitmap('E:\Booking\Education_KKU_Thai_Emblem.ico')
conn=sqlite3.connect(r"E:\Booking\Database.db")
canvas = Canvas(window, width = 1079, height = 720)
canvas.place(x=0,y=0,relwidth=1,relheight=1)
img = PhotoImage(file=r"E:\Booking\รูป\งานออกแบบที่ไม่มีชื่อ.png")
canvas.create_image(0,0,anchor=NW,image=img)
canvas.create_text(551,102,text='ยินดีต้อนรับสู่หน้าเข้าสู่ระบบ',font=("MiPancake",40,BOLD),fill="#BBB0DB")
canvas.create_text(550,100,text='ยินดีต้อนรับสู่หน้าเข้าสู่ระบบ',font=("MiPancake",40,BOLD),fill="#938BB6")

canvas.create_text(351,222,text='กรอก USER NAME(รหัสนักศึกษา)',font=("MiPancake",30,BOLD),fill="#BBB0DB")
canvas.create_text(350,220,text='กรอก USER NAME(รหัสนักศึกษา)',font=("MiPancake",30,BOLD),fill="#938BB6")
canvas.create_text(349,302,text='กรอก PASSWORD(รหัสผ่าน)    ',font=("MiPancake",30,BOLD),fill="#BBB0DB")
canvas.create_text(348,300,text='กรอก PASSWORD(รหัสผ่าน)    ',font=("MiPancake",30,BOLD),fill="#938BB6")

name_entry = StringVar()
name_entry = Entry(window,textvariable=name_entry,font="MiPancake 13 bold",foreground="#938BB6")
name_entry.place(x=650,y=200)

name_entry2 = StringVar()
name_entry2 = Entry(window,textvariable=name_entry,font="MiPancake 13 bold",foreground="#938BB6",show="•")
name_entry2.place(x=650,y=280)

def checkLogin() :
    c=conn.cursor()
    c.execute(' SELECT * FROM user WHERE UserOrStudentID=? and Password=? ',(name_entry.get(),name_entry2.get()))
    collect = c.fetchall()
    conn.commit()
    print(collect)
    print(len(collect))
    print(type(collect))
    if len(collect) == 0:
        print("fail")
        tkinter.messagebox.showinfo("รายระเอียดโปรแกรม","login fail")

    elif len(collect) == 1: 
        print("successfully")
        tkinter.messagebox.showinfo("รายระเอียดโปรแกรม","login successfully")
        c=conn.cursor()
        c.execute('''UPDATE temp SET StudentIDLogin=? WHERE id =?''',(collect[0][1],1))
        conn.commit()
        if collect[0][5] == "User" :
            window.destroy()
            Userpage = "E:/Booking/userhomepage.py"
            os.system(Userpage)
        elif collect[0][5] == "Admin":
            window.destroy()
            Adminpage = "E:/Booking/adminhomepage.py"
            os.system(Adminpage)
def RetundToFirstpage() :
    window.destroy()
    Return = "E:\Booking\Firstinterface.py"
    os.system(Return)

logo = PhotoImage(file="E:\Booking\รูป\Login_button2.png")
logo2 = PhotoImage(file="E:\Booking\รูป\Return_homepage_button2.png")
img2 = PhotoImage(file="E:\Booking\รูป\Guide_Login_1.png")
img3 = PhotoImage(file="E:\Booking\รูป\Guide_Return_to_regis1.png")
btn = Button(window,image=logo,bg="#D4E6C4",command=checkLogin,padx=300,pady=60).place(x=400,y=380)
btn = Button(window,image=logo2,bg="#D4E6C4",command=RetundToFirstpage,padx=300,pady=60).place(x=400,y=470)
canvas.create_image(740,400,anchor=NW,image=img3)
canvas.create_image(10,300,anchor=NW,image=img2)
window.geometry("1079x720+500+150")
window.resizable(False,False)
window.mainloop()
