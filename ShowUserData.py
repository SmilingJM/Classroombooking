import sqlite3
from tkinter import *

window = Tk()
window.geometry("550x650+100+100")
F1 = Frame(window,bg="green")
F1.grid(row=0,column=0,columnspan=3)
window.title("ED KKU Room reservation")
label = Label(window, text="ข้อมูลผู้ใช้งาน",font="time 25 bold")
label.grid(row= 0 , column= 0, columnspan=20)

p0 = Label(window, text="No.",font="time 15 bold")
p0.grid(row= 1, column= 0 , padx= 10, pady= 10)

p1 = Label(window, text="StudentID",font="time 15 bold")
p1.grid(row= 1, column= 1 , padx= 10, pady= 10)

p2 = Label(window, text="First Name",font="time 15 bold")
p2.grid(row= 1, column= 2 , padx= 10, pady= 10)

p3 = Label(window, text="Last Name",font="time 15 bold")
p3.grid(row= 1, column= 3 , padx= 10, pady= 10)

p4 = Label(window, text="Status",font="time 15 bold")
p4.grid(row= 1, column= 4 , padx= 10, pady= 10)

conn = sqlite3.connect(r"E:\Booking\Database.db") 
c = conn.cursor()
c.execute("SELECT * FROM user")
r = c.fetchall()

num = 2
for i in r:
    
    Number = Label(window, text= i[0], font="time 15 bold", fg="Salmon" )
    Number.grid(row = num, column= 0, padx= 10 ,pady= 10)

    Room = Label(window, text= i[1], font="time 15 bold", fg="Salmon" )
    Room.grid(row = num, column= 1, padx= 10 ,pady= 10) 

    StudentID = Label(window, text= i[3], font="time 15 bold", fg="Salmon" )
    StudentID.grid(row = num, column= 2, padx= 10 ,pady= 10)

    Start = Label(window, text= i[4], font="time 15 bold", fg="Salmon" )
    Start.grid(row = num, column= 3, padx= 10 ,pady= 10)

    Finish = Label(window, text= i[5], font="time 15 bold", fg="Salmon" )
    Finish.grid(row = num, column= 4, padx= 10 ,pady= 10)


    num = num + 1

window.resizable(False,True)
window.mainloop()
