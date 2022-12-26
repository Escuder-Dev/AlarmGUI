from tkinter.ttk import *
from tkinter import *
from threading import Thread

from pygame import mixer
from PIL import ImageTk, Image

from datetime import datetime
from time import sleep

#Style and colours
bgColour = '#00FF00'
col = '#296D00'
col2= '#91FF4F'

#Window
window = Tk()
window.title("Alarm")
window.geometry('400x200')
window.configure(bg = bgColour)

#Window Frames
frameLine = Frame(window, width= 400, height=20, bg=col)
frameLine.grid(row=0, column=0)

frameBody = Frame(window, width= 400, height=200, bg=col2)
frameBody.grid(row=1, column=0)

#Configure Frames
img = Image.open('Alarm1.png')
img.resize((10,10))
img = ImageTk.PhotoImage(img)

appImage = Label(frameBody, height=100, width=100,image=img, bg=col2)
appImage.place(x=15, y=15)

title = Label(frameBody, text = "Alarm", height=1, font=('Arial 24 bold'), bg = col2)
title.place(x=125, y=10)

hour = Label(frameBody, text = "Hour", height=1, font=('Arial 10 bold'), bg = col2)
hour.place(x=125, y=60)

cHour = Combobox(frameBody, width=2, font=('arial 15'))
cHour['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
cHour.current(0)
cHour.place(x=127, y=78)

minute = Label(frameBody, text = "Minutes", height=1, font=('Arial 10 bold'), bg = col2)
minute.place(x=170, y=60)

cMinutes = Combobox(frameBody, width=2, font=('arial 15'))
cMinutes['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28","29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
cMinutes.current(0)
cMinutes.place(x=174, y=78)

second = Label(frameBody, text = "Seconds", height=1, font=('Arial 10 bold'), bg = col2)
second.place(x=222, y=60)

cSeconds = Combobox(frameBody, width=2, font=('arial 15'))
cSeconds['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28","29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
cSeconds.current(0)
cSeconds.place(x=225, y=78)

MornAft = Label(frameBody, text = "Period", height=1, font=('Arial 10 bold'), bg = col2)
MornAft.place(x=280, y=60)

cMornAft = Combobox(frameBody, width=3, font=('arial 15'))
cMornAft['values'] = ("AM", "PM")
cMornAft.current(0)
cMornAft.place(x=284, y=78)

#Alarm creation
def activateAlarm():
    t = Thread(target=alarm)
    t.start()

def deactivateAlarm():
    print('Deactivated Alarm: ', selected.get())
    mixer.music.stop()

selected = IntVar()

rAct = Radiobutton(frameBody, font=('Arial 12 bold'), value = 1, text = "Activate", bg=col2, command=activateAlarm, variable=selected) 
rAct.place(x = 125, y=115)

#Load sound
def alarmSound():
    mixer.music.load('alarmSound.wav')
    mixer.music.play()
    selected.set(0)

    rDeactivate = Radiobutton(frameBody, font=('Arial 12 bold'), value = 1, text = "Deactivate", bg=col2, command=deactivateAlarm, variable=selected) 
    rDeactivate.place(x = 190, y=115)

def alarm():
    while True:
        control = selected.get()
        print(control)

        alarmHour = cHour.get()
        alarmMinute = cMinutes.get()
        alarmSecond = cSeconds.get()
        alarmPeriod = cMornAft.get()
        alarmPeriod = str(alarmPeriod).upper()

        now = datetime.now()

        hour = now.strftime("%I")
        minute = now.strftime("%M")
        second = now.strftime("%S")
        period = now.strftime("%p")

        if control == 1:
            if alarmPeriod == period:
                if alarmHour == hour:
                    if alarmMinute == minute:
                        if alarmSecond == second:
                            print("Time to check the Stock Market and Email!")
                            alarmSound()
        sleep(1)
mixer.init()
window.mainloop()




