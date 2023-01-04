from tkinter import *
import datetime


clock = Tk()
clock.title("     **** Digital Clock ****")
clock.geometry("1000x500")
clock.config(bg="Blue")

hour = Label(clock, text="00", font=("Times New Roman",40,"bold"),
bg='white', fg='black')
hour.place(x=120,y=50,height=110,width=100)

hour_txt = Label(clock, text="HOURS", font=("Times New Roman",20,"bold"),
bg='white', fg='black')
hour_txt.place(x=120,y=190,height=30,width=100)

minute = Label(clock, text="00", font=("Times New Roman",40,"bold"),
bg='white', fg='black')
minute.place(x=340,y=45,height=110,width=100)

minute_txt = Label(clock, text="MIN", font=("Times New Roman",20,"bold"),
bg='white', fg='black')
minute_txt.place(x=340,y=190,height=30,width=100)


clock.mainloop()