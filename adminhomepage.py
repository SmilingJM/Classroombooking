from cProfile import label
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
import tkinter.messagebox
import sys
import os
import time
from PIL import Image,ImageTk
import requests

def _lineNotify(payload,file=None):
    url = 'https://notify-api.line.me/api/notify'
    token = 'w7HiTQrAZxzRPvETylCUEK6Ev8IURNavePZvFNn1fVz'
    headers = {'Authorization':'Bearer '+token}
    return requests.post(url, headers=headers , data = payload, files=file)
#ข้อความ
def lineNotify(message):
    payload = {'message':message}
    return _lineNotify(payload)

conn=sqlite3.connect(r"E:\Booking\Database.db")
c=conn.cursor()
c.execute(''' SELECT StudentIDLogin FROM temp ''')
collect = c.fetchone()
userID = collect[0]
print(userID)
conn.commit()
window2 = Tk()
window2.title("ED KKU Room reservation")
window2.geometry("1079x720+500+150")
window2.iconbitmap('E:\Booking\Education_KKU_Thai_Emblem.ico')
canvas = Canvas(window2, width = 1079, height = 720)
canvas.place(x=0,y=0,relwidth=1,relheight=1)
img = PhotoImage(file=r"E:\Booking\รูป\งานออกแบบที่ไม่มีชื่อ.png")
canvas.create_image(0,0,anchor=NW,image=img)
img2 = PhotoImage(file="E:\Booking\รูป\DDDDD.png")
canvas.create_image(830,150,anchor=NW,image=img2)
img3 = PhotoImage(file="E:\Booking\รูป\Line_group_Guide.png")
canvas.create_image(790,340,anchor=NW,image=img3)

canvas.create_text(551,102,text='ยินดีต้อนรับสู่ระบบจองห้องเรียน',font=("MiPancake",40,BOLD),fill="#5D8D73")
canvas.create_text(550,100,text='ยินดีต้อนรับสู่ระบบจองห้องเรียน',font=("MiPancake",40,BOLD),fill="#D4E6C4")

canvas.create_text(351,182,text='เลือกห้องที่ต้องการจอง   ',font=("MiPancake",30,BOLD),fill="#5D8D73")
canvas.create_text(350,180,text='เลือกห้องที่ต้องการจอง   ',font=("MiPancake",30,BOLD),fill="#D4E6C4")

canvas.create_text(351,252,text='เลือกเวลาเริ่มที่ต้องการจอง',font=("MiPancake",30,BOLD),fill="#5D8D73")
canvas.create_text(350,250,text='เลือกเวลาเริ่มที่ต้องการจอง',font=("MiPancake",30,BOLD),fill="#D4E6C4")

canvas.create_text(351,322,text='เลือกเวลาที่ต้องการออก  ',font=("MiPancake",30,BOLD),fill="#5D8D73")
canvas.create_text(350,320,text='เลือกเวลาที่ต้องการออก  ',font=("MiPancake",30,BOLD),fill="#D4E6C4")

canvas.create_text(351,392,text='ดูห้องว่างก่อนจองนะครับ  ',font=("MiPancake",30,BOLD),fill="#5D8D73")
canvas.create_text(350,390,text='ดูห้องว่างก่อนจองนะครับ  ',font=("MiPancake",30,BOLD),fill="#D4E6C4")

canvas.create_text(351,462,text='ดูข้อมูลผู้ใช้          ',font=("MiPancake",30,BOLD),fill="#5D8D73")
canvas.create_text(350,460,text='ดูข้อมูลผู้ใช้          ',font=("MiPancake",30,BOLD),fill="#D4E6C4")

canvas.create_text(351,532,text='ดูประวัติการใช้ห้อง     ',font=("MiPancake",30,BOLD),fill="#5D8D73")
canvas.create_text(350,530,text='ดูประวัติการใช้ห้อง     ',font=("MiPancake",30,BOLD),fill="#D4E6C4")

list1 = ["1301","1302","1310","1403","1404","1405","1406","1407"]
listroom = StringVar(window2)
listroom = ttk.Combobox(window2, values=list1 , width=20 ,font=('MiPancake',14,BOLD),foreground="#567ACE",justify="center",state="readonly")
listroom.set("เลือกห้องที่ต้องการ")
listroom.place(x=580,y=155)

list2 = ["08:00","09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00"]
listStart = StringVar(window2)
listStart = ttk.Combobox(window2, values=list2 , width=20 ,font=('MiPancake',14,BOLD),foreground="#567ACE",justify="center",state="readonly")
listStart.set("เลือกเวลาเริ่มที่ต้องการ")
listStart.place(x=580,y=230)

list3 = ["09:00","10:00","11:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00"]
listFinish = StringVar(window2)
listFinish = ttk.Combobox(window2, values=list3 , width=20 ,font=('MiPancake',14,BOLD),foreground="#567ACE",justify="center",state="readonly")
listFinish.set("เลือกเวลาออกที่ต้องการ")
listFinish.place(x=580,y=300)

def BookingSaved() :
    if listStart.get() < listFinish.get() :
        if listroom.get() != "เลือกห้องที่ต้องการ" and listStart.get() != "เลือกเวลาเริ่มที่ต้องการ" and listFinish.get() != "เลือกเวลาออกที่ต้องการ" :
            if listStart.get() <= "11:00" and listFinish.get() <= "12:00":
                c=conn.cursor()
                c.execute(' SELECT StatusRoom FROM room WHERE RoomID=?',(listroom.get(),))
                roomstatus = c.fetchone()
                print(roomstatus[0])
                conn.commit()
                if "Available" == roomstatus[0] :
                    status1 = "unavailable"
                    c=conn.cursor()
                    c.execute('''UPDATE room SET StudentID=?,Start=?,Finish=? ,StatusRoom=? WHERE RoomID = ? ''',(userID,listStart.get(),listFinish.get(),status1,listroom.get()))
                    c.execute('INSERT INTO history(RoomID,StudentID,Start,Finish)VALUES(?,?,?,?)',(listroom.get(),userID,listStart.get(),listFinish.get()))
                    conn.commit()
                    tkinter.messagebox.showinfo("ED KKU Room reservation","จองสำเร็จแล้วนะครับ \nอย่าลืมปิดไฟปิดแอร์ก่อนออกจากห้องด้วยนะครับ")
                    lineNotify(f"{userID} ได้ทำกาจองห้อง {listroom.get()} ตั้งแต่เวลา {listStart.get()}-{listFinish.get()} ครับ")
                else :
                    tkinter.messagebox.showinfo("ED KKU Room reservation","จองไม่สำเร็จนะครับ \nโปรดเช็คข้อมูลห้องว่างอีกครั้ง")
            elif listStart.get() >= "13:00" and listFinish.get() > "13:00":
                c=conn.cursor()
                c.execute(' SELECT StatusRoom2 FROM room WHERE RoomID=?',(listroom.get(),))
                roomstatus = c.fetchone()
                print(roomstatus[0])
                conn.commit()
                if "Available" == roomstatus[0] :
                    status1 = "unavailable"
                    c=conn.cursor()
                    c.execute('''UPDATE room SET StudentID2=?,Start2=?,Finish2=? ,StatusRoom2=? WHERE RoomID = ? ''',(userID,listStart.get(),listFinish.get(),status1,listroom.get()))
                    c.execute('INSERT INTO history(RoomID,StudentID,Start,Finish)VALUES(?,?,?,?)',(listroom.get(),userID,listStart.get(),listFinish.get()))
                    conn.commit()
                    tkinter.messagebox.showinfo("ED KKU Room reservation","จองสำเร็จแล้วนะครับ \nอย่าลืมปิดไฟปิดแอร์ก่อนออกจากห้องด้วยนะครับ")
                    lineNotify(f"{userID} ได้ทำกาจองห้อง {listroom.get()} ตั้งแต่เวลา {listStart.get()}-{listFinish.get()} ครับ")
                else :
                    tkinter.messagebox.showinfo("ED KKU Room reservation","จองไม่สำเร็จนะครับ \nโปรดเช็คข้อมูลห้องว่างอีกครั้ง")
            else :
                tkinter.messagebox.showinfo("ED KKU Room reservation","สามารถจองช่วงเช้าได้ถึง 12:00")
        else :
            print("Error")
            tkinter.messagebox.showinfo("ED KKU Room reservation","จองไม่สำเร็จนะครับ \nโปรดกรอกข้อมูลให้ครบท้วน")
    else :
        tkinter.messagebox.showinfo("ED KKU Room reservation","จองไม่สำเร็จนะครับ \nโปรดกรอกเวลาให้ถูกต้อง")

def ShowTable() :
    bookedpage = "E:\Booking\ShowBookedTable.py"
    os.system(bookedpage)

def ShowHistory() :
    historypage = "E:\Booking\ShowHistory.py"
    os.system(historypage)

def ShowUserData() :
    ShowUserData = "E:\Booking\ShowUserData.py"
    os.system(ShowUserData)

def logout() :
    window2.destroy()
    Return = "E:/Booking/login.py"
    os.system(Return)

def CheckTimeOut() :
    c=conn.cursor()
    c.execute(''' SELECT Finish FROM room ''')
    Endtime = c.fetchall()
    c.execute(''' SELECT Finish2 FROM room ''')
    Endtime2 = c.fetchall()
    print(Endtime2)
    conn.commit()
    timeis = time.localtime()
    a = time.strftime('%H:00', timeis)
    for i in range(1,9) :
        if a >= "12:00" and Endtime[i-1][0] != "-" : 
            c=conn.cursor()
            c.execute('''UPDATE room SET StudentID=?,Start=?,Finish=? ,StatusRoom=? WHERE id = ? ''',("-","-","-","Available",i))
            c.execute(' SELECT RoomID FROM room WHERE id=?',(i,))
            roomid = c.fetchone()
            print(roomid)
            conn.commit()
            tkinter.messagebox.showinfo("ED KKU Room reservation",f"ห้อง {Endtime[i-1][0]} หมดเวลาแล้ว \nอย่าลืมปิดไฟปิดแอร์ก่อนออกจากห้องด้วยนะครับ")
            lineNotify(f"ห้อง {roomid[0]} หมดเวลาแล้ว อย่าลืมปิดไฟปิดแอร์ก่อนออกจากห้องด้วยนะครับ")
        if a >= "20:00" and Endtime2[i-1][0] != "-"  : 
            c=conn.cursor()
            c.execute('''UPDATE room SET StudentID2=?,Start2=?,Finish2=? ,StatusRoom2=? WHERE id = ? ''',("-","-","-","Available",i))
            c.execute(' SELECT RoomID FROM room WHERE id=?',(i,))
            roomid = c.fetchone()
            print(roomid)
            conn.commit()
            tkinter.messagebox.showinfo("ED KKU Room reservation",f"ห้อง {Endtime[i-1][0]} หมดเวลาแล้ว \nอย่าลืมปิดไฟปิดแอร์ก่อนออกจากห้องด้วยนะครับ")
            lineNotify(f"ห้อง {roomid[0]} หมดเวลาแล้ว อย่าลืมปิดไฟปิดแอร์ก่อนออกจากห้องด้วยนะครับ")
            
def opendb() :
    conn.close()
    opendbapp = "E:\Booking\Database.db"
    os.system(opendbapp)

CheckTimeOut()
logo = PhotoImage(file="E:\Booking\รูป\Show_table_button.png")
logo2 = PhotoImage(file="E:\Booking\รูป\Show_user_data_button.png")
logo3 = PhotoImage(file="E:\Booking\รูป\Show_history_button.png")
logo4 = PhotoImage(file="E:\Booking\รูป\Refresh_button.png")
logo5 = PhotoImage(file="E:\Booking\รูป\Save_booking_Button1.png")
logo6 = PhotoImage(file="E:\Booking\รูป\Open_db_button.png")
logo7 = PhotoImage(file="E:\Booking\รูป\log_out_button.png")
mybutton = Button(window2,image=logo,bg="#D9598C",command=ShowTable).place(x=580,y=365)
mybutton = Button(window2,image=logo2,bg="#F2D2E7",command=ShowUserData).place(x=580,y=435)
mybutton = Button(window2,image=logo3,bg="#A6E0E1",command=ShowHistory).place(x=580,y=500)
mybutton = Button(window2,image=logo4,bg="#567ACE",command=CheckTimeOut).place(x=200,y=590)
mybutton = Button(window2,image=logo5,bg="#B7D3E9",command=BookingSaved).place(x=440,y=590)
mybutton = Button(window2,image=logo6,bg="#aed768",command=opendb).place(x=680,y=590)
mybutton = Button(window2,image=logo7,bg="#FF1616",command=logout).place(x=950,y=70)

window2.resizable(False, False)
window2.mainloop()