import sqlite3
from tkinter import *
from turtle import bgcolor

window = Tk()
window.geometry("1200x650+100+100")
#window.configure(bg="pink")


window.title("ED KKU Room reservation")
label = Label(window, text="ตารางการจองห้อง",font="time 25 bold")
label.grid(row= 0 , column= 0, columnspan=20)

p0 = Label(window, text="Number",font="time 15 bold")
p0.grid(row= 1, column= 0 , padx= 10, pady= 10)

p1 = Label(window, text="Room",font="time 15 bold")
p1.grid(row= 1, column= 1 , padx= 10, pady= 10)

p2 = Label(window, text="StudentID",font="time 15 bold")
p2.grid(row= 1, column= 2 , padx= 10, pady= 10)

p3 = Label(window, text="Start time",font="time 15 bold")
p3.grid(row= 1, column= 3 , padx= 10, pady= 10)

p4 = Label(window, text="Finish time",font="time 15 bold")
p4.grid(row= 1, column= 4 , padx= 10, pady= 10)

p5 = Label(window, text="Status",font="time 15 bold")
p5.grid(row= 1, column= 5 , padx= 10, pady= 10)

p6 = Label(window, text="StudentID2",font="time 15 bold")
p6.grid(row= 1, column= 6 , padx= 10, pady= 10)

p7 = Label(window, text="Start time2",font="time 15 bold")
p7.grid(row= 1, column= 7 , padx= 10, pady= 10)

p8 = Label(window, text="Finish time2",font="time 15 bold")
p8.grid(row= 1, column= 8 , padx= 10, pady= 10)

p9 = Label(window, text="Status2",font="time 15 bold")
p9.grid(row= 1, column= 9 , padx= 10, pady= 10)

conn = sqlite3.connect(r"E:\Booking\Database.db") 
c = conn.cursor()
c.execute("SELECT * FROM room")
r = c.fetchall()

num = 2
for i in r:
    
    Number = Label(window, text= i[0], font="time 15 bold", fg="Salmon" )
    Number.grid(row = num, column= 0, padx= 10 ,pady= 10)

    Room = Label(window, text= i[1], font="time 15 bold", fg="Salmon" )
    Room.grid(row = num, column= 1, padx= 10 ,pady= 10) 

    StudentID = Label(window, text= i[2], font="time 15 bold", fg="Salmon" )
    StudentID.grid(row = num, column= 2, padx= 10 ,pady= 10)

    Start = Label(window, text= i[3], font="time 15 bold", fg="Salmon" )
    Start.grid(row = num, column= 3, padx= 10 ,pady= 10)

    Finish = Label(window, text= i[4], font="time 15 bold", fg="Salmon" )
    Finish.grid(row = num, column= 4, padx= 10 ,pady= 10)

    status = Label(window, text= i[5], font="time 15 bold", fg="Salmon" )
    status.grid(row = num, column= 5, padx= 10 ,pady= 10)
    
    StudentID2 = Label(window, text= i[6], font="time 15 bold", fg="Salmon" )
    StudentID2.grid(row = num, column= 6, padx= 10 ,pady= 10)

    Start2 = Label(window, text= i[7], font="time 15 bold", fg="Salmon" )
    Start2.grid(row = num, column= 7, padx= 10 ,pady= 10)

    Finish2 = Label(window, text= i[8], font="time 15 bold", fg="Salmon" )
    Finish2.grid(row = num, column= 8, padx= 10 ,pady= 10)

    status2 = Label(window, text= i[9], font="time 15 bold", fg="Salmon" )
    status2.grid(row = num, column= 9, padx= 10 ,pady= 10)

    num = num + 1

window.resizable(False,True)
window.mainloop()