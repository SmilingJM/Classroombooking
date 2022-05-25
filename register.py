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
window.geometry("1079x720+500+150")
label=Label(window,text="EDKKU Room Reservation")
label.pack(side=TOP,fill=X)
canvas = Canvas(window, width = 1079, height = 720)
canvas.place(x=0,y=0,relwidth=1,relheight=1)
img = PhotoImage(file=r"E:\Booking\รูป\งานออกแบบที่ไม่มีชื่อ.png")
canvas.create_image(0,0,anchor=NW,image=img)

canvas.create_text(551,102,text='ยินดีต้อนรับสู่หน้าลงทะเบียน',font=("MiPancake",40,BOLD),fill="#5D8D73")
canvas.create_text(550,100,text='ยินดีต้อนรับสู่หน้าลงทะเบียน',font=("MiPancake",40,BOLD),fill="#D4E6C4")
canvas.create_text(370,182,text='กรอก USER NAME(รหัสนักศึกษามี-)',font=("MiPancake",30,BOLD),fill="#5D8D73")
canvas.create_text(369,180,text='กรอก USER NAME(รหัสนักศึกษามี-)',font=("MiPancake",30,BOLD),fill="#D4E6C4")
canvas.create_text(349,242,text='กรอก PASSWORD(รหัสผ่าน)    ',font=("MiPancake",30,BOLD),fill="#5D8D73")
canvas.create_text(348,240,text='กรอก PASSWORD(รหัสผ่าน)    ',font=("MiPancake",30,BOLD),fill="#D4E6C4")
canvas.create_text(351,302,text='กรอก ชื่อจริง(ภาษาอังกฤษ)       ',font=("MiPancake",30,BOLD),fill="#5D8D73")
canvas.create_text(350,300,text='กรอก ชื่อจริง(ภาษาอังกฤษ)       ',font=("MiPancake",30,BOLD),fill="#D4E6C4")
canvas.create_text(349,362,text='กรอก นามสกุล(ภาษาอังกฤษ)     ',font=("MiPancake",30,BOLD),fill="#5D8D73")
canvas.create_text(348,360,text='กรอก นามสกุล(ภาษาอังกฤษ)     ',font=("MiPancake",30,BOLD),fill="#D4E6C4")

name_entry = StringVar()
name_entry = Entry(window,textvariable=name_entry,font="MiPancake 13 bold",foreground="#5D8D73")
name_entry.place(x=650,y=160)

name_entry2 = StringVar()
name_entry2 = Entry(window,textvariable=name_entry2,font="MiPancake 13 bold",foreground="#5D8D73")
name_entry2.place(x=650,y=220)

name_entry3 = StringVar()
name_entry3 = Entry(window,textvariable=name_entry2,font="MiPancake 13 bold",foreground="#5D8D73")
name_entry3.place(x=650,y=280)

name_entry4 = StringVar()
name_entry4 = Entry(window,textvariable=name_entry4,font="MiPancake 13 bold",foreground="#5D8D73")
name_entry4.place(x=650,y=340)


def savedata():
    check = name_entry3.get().isalpha()
    check2 = name_entry4.get().isalpha()
    if str(name_entry.get()) != "" and str(name_entry2.get()) != "" and str(name_entry3.get()) != "" and str(name_entry4.get()) != "" and len(name_entry.get()) == 11   :
        if  check == True and check2 == True and len(name_entry2.get()) >= 6 and name_entry.get()[9] == "-":
            conn=sqlite3.connect(r"E:\Booking\Database.db")
            c=conn.cursor()
            Status = 'User'
            c.execute('INSERT INTO user(UserOrStudentID,Password,Fname,Lname,Status)VALUES(?,?,?,?,?)',(name_entry.get(),name_entry2.get(),name_entry3.get(),name_entry4.get(),Status))
            conn.commit()
            tkinter.messagebox.showinfo("ED KKU Room reservation"," ลงทะเบียนเสร็จเรียบร้อยแล้วนะครับ")
        elif check == True and check2 == True and len(name_entry2.get()) >= 6 and name_entry.get()[9] != "-":
            tkinter.messagebox.showinfo("ED KKU Room reservation","กรุณากรอกรหัสนักศึกษาให้ถูกต้อง")
        elif check == True and check2 == True and len(name_entry2.get()) < 6 and name_entry.get()[9] == "-":
            tkinter.messagebox.showinfo("ED KKU Room reservation","กรุณากรอกรหัสผ่านมากกว่า6ตัว")
        elif check == False  and len(name_entry2.get()) >= 6 and name_entry.get()[9] == "-":
            tkinter.messagebox.showinfo("ED KKU Room reservation","กรุณากรอกชื่อสกุลให้ถูกต้อง")
        elif check2 == False and len(name_entry2.get()) >= 6 and name_entry.get()[9] == "-":
            tkinter.messagebox.showinfo("ED KKU Room reservation","กรุณากรอกชื่อสกุลให้ถูกต้อง")
    elif str(name_entry.get()) == "" or str(name_entry2.get()) == "" or str(name_entry3.get()) == "" or str(name_entry4.get()) == "":
        tkinter.messagebox.showinfo("ED KKU Room reservation"," ลงทะเบียนไม่สำเร็จ\nโปรดใส่ข้อมููลให้ครบนะครับ")
    elif str(name_entry.get()) != "" and str(name_entry2.get()) != "" and str(name_entry3.get()) != "" and str(name_entry4.get()) != "" and len(name_entry.get()) != 11 :
        tkinter.messagebox.showinfo("ED KKU Room reservation"," ลงทะเบียนไม่สำเร็จ\nโปรดใส่กรอกรหัสนักศึกษาให้ถูกต้อง")
    
def ReturnToLogin():
    window.destroy()
    Return = "E:/Booking/login.py"
    os.system(Return)
logo = PhotoImage(file="E:\Booking\รูป\Savedata_button.png")
logo2 = PhotoImage(file="E:\Booking\รูป\Returnlogin_Button.png")
btn = Button(window,image=logo,bg="#D4E6C4",command=savedata,padx=300,pady=60).place(x=400,y=450)
btn = Button(window,image=logo2,bg="#D4E6C4",command=ReturnToLogin,padx=300,pady=60).place(x=400,y=540)

img2 = PhotoImage(file="E:\Booking\รูป\Guide_Return_to_login.png")
canvas.create_image(740,400,anchor=NW,image=img2)
window.resizable(False,False)
window.mainloop()
