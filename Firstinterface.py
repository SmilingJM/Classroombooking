import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
import tkinter.messagebox
from PIL import Image,ImageTk
import sys
import os


window = Tk()
window.title("ED KKU Room reservation")
window.geometry("1079x720+500+150")
window.iconbitmap('E:\Booking\Education_KKU_Thai_Emblem.ico')
def JumpToRegister() :
    window.destroy()
    register = "E:/Booking/register.py"
    os.system(register)
    
def JumpTologin() :
    window.destroy()
    Return = "E:/Booking/login.py"
    os.system(Return)
logo = PhotoImage(file="E:\Booking\รูป\Register_Button.png")
logo2 = PhotoImage(file="E:\Booking\รูป\Login_Button.png")
canvas = Canvas(window, width = 1079, height = 720)
canvas.place(x=0,y=0,relwidth=1,relheight=1)
img = PhotoImage(file="E:\Booking\รูป\งานออกแบบที่ไม่มีชื่อ.png")
img2 = PhotoImage(file="E:\Booking\รูป\Guide.png")
canvas.create_image(0,0,anchor=NW,image=img)
canvas.create_text(551,102,text='Welcome to Classroom Booking',font=("MiPancake",40,BOLD),fill="white")
canvas.create_text(550,100,text='Welcome to Classroom Booking',font=("MiPancake",40,BOLD),fill="#FFAE80")

canvas.create_text(551,182,text='จัดทำโดย',font=("MiPancake",30,BOLD),fill="white")
canvas.create_text(550,180,text='จัดทำโดย',font=("MiPancake",30,BOLD),fill="#FFAE80")

canvas.create_text(551,242,text='นายนฤเบศ เงินโพธิ์กลาง 643050408-8',font=("MiPancake",30,BOLD),fill="white")
canvas.create_text(550,240,text='นายนฤเบศ เงินโพธิ์กลาง 643050408-8',font=("MiPancake",30,BOLD),fill="#FFAE80")

canvas.create_text(551,302,text='นายศุภกิตติ์ เมืองมา 643050420-8',font=("MiPancake",30,BOLD),fill="white")
canvas.create_text(550,300,text='นายศุภกิตติ์ เมืองมา 643050420-8',font=("MiPancake",30,BOLD),fill="#FFAE80")

canvas.create_text(551,362,text='อาจารย์ที่ปรึกษา',font=("MiPancake",30,BOLD),fill="white")
canvas.create_text(550,360,text='อาจารย์ที่ปรึกษา',font=("MiPancake",30,BOLD),fill="#FFAE80")

canvas.create_text(551,422,text='ผู้ช่วยศาสตราจารย์ ดร.นฏกร ประมายันต์',font=("MiPancake",30,BOLD),fill="white")
canvas.create_text(550,420,text='ผู้ช่วยศาสตราจารย์ ดร.นฏกร ประมายันต์',font=("MiPancake",30,BOLD),fill="#FFAE80")

canvas.create_text(301,542,text='ลงทะเบียนสมาชิกใหม่',font=("MiPancake",30,BOLD),fill="white")
canvas.create_text(300,540,text='ลงทะเบียนสมาชิกใหม่',font=("MiPancake",30,BOLD),fill="#FF916C")

canvas.create_text(221,602,text='เข้าสู่ระบบ',font=("MiPancake",30,BOLD),fill="white")
canvas.create_text(220,600,text='เข้าสู่ระบบ',font=("MiPancake",30,BOLD),fill="#FF916C")

canvas.create_image(740,400,anchor=NW,image=img2)
mybutton = Button(window,image=logo,bg="#F1C3AB",command=JumpToRegister,padx=70,pady=7).place(x=550,y=520)
mybutton = Button(window,image=logo2,bg="#F1C3AB",command=JumpTologin,padx=70,pady=7).place(x=550,y=580)

window.resizable(False, False)
window.mainloop()
