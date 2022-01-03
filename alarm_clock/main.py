from tkinter import *
from tkinter import messagebox
from pygame import mixer
import datetime

alarmTime = None
alarmDate = None
now = None
date = None

# ------------------------------ Alarm Sound Initialization ------------------------------
mixer.init()
mixer.music.load('alarm.wav')


# --------------------------------------- Functions ---------------------------------------
# Run the time
def run():
    global now, date, alarmTime, alarmDate
    current_time = datetime.datetime.now()
    now = current_time.strftime("%H:%M:%S")
    date = current_time.strftime("%d/%m/%Y")
    Label.config(timeShow, text=now)

    # Checking time for Alarm
    if now == str(alarmTime) and date == str(alarmDate):
        mixer.music.play()
        Label.config(wakeupLabel, text="Alarm ringing...\n\n")
        messagebox.showinfo("Alarm", "Your Alarm is Ringing")
    clock.after(1000, run)


def setAlarm():
    global alarmTime, alarmDate

    if hourTime.get() and minTime.get() and secTime.get() and nowDate.get() and nowMonth.get() and nowYear.get():
        alarmTime = f"{hourTime.get()}:{minTime.get()}:{secTime.get()}"
        alarmDate = f"{nowDate.get()}/{nowMonth.get()}/{nowYear.get()}"
        Label.config(wakeupLabel, text=f"Alarm set \nat {alarmTime} \non {alarmDate}")
    else:
        messagebox.showerror("Error", "Enter Valid time and date")


# Stop the alarm
def stop():
    global alarmTime, alarmDate
    mixer.music.stop()
    Label.config(wakeupLabel, text="No Alarm set\n\n")
    alarmTime = None
    alarmDate = None

# -------------------------------------------------------UI-------------------------------------------------------------


clock = Tk()
clock.title("Alarm Clock")
clock.config(padx=10, pady=10)
clock.geometry("230x370")

timeShow = Label(text="Time", font=("Keeravani", 50, "normal"))
timeShow.grid(row=0, column=0, columnspan=3)

wakeupLabel = Label(text="No Alarm set\n\n", font=20)
wakeupLabel.grid(row=1, column=0, columnspan=3)

Label(text="").grid(row=2, column=0, columnspan=3)

Label(text="Set your alarm time here", font=14).grid(row=3, column=0, columnspan=3)
Label(text="HH").grid(sticky=E, row=4, column=0)
Label(text="MM").grid(row=4, column=1)
Label(text="SS").grid(sticky=W, row=4, column=2)

hourTime = Entry(clock, width=5)
hourTime.grid(sticky=E, row=5, column=0)
minTime = Entry(clock, width=5)
minTime.grid(row=5, column=1)
secTime = Entry(clock, width=5)
secTime.grid(sticky=W, row=5, column=2)

Label(text="(Enter in 24 hours format)", font=("Arial", 8, "normal")).grid(row=6, column=0, columnspan=3)
Label(text="DD").grid(sticky=E, row=7, column=0)
Label(text="MM").grid(row=7, column=1)
Label(text="YYYY").grid(sticky=W, row=7, column=2)

nowDate = Entry(clock, width=5)
nowDate.grid(sticky=E, row=8, column=0)
nowMonth = Entry(clock, width=5)
nowMonth.grid(row=8, column=1)
nowYear = Entry(clock, width=5)
nowYear.grid(sticky=W, row=8, column=2)

Label(text="").grid(row=9, column=0, columnspan=3)

buttonSet = Button(text="Set Alarm", command=setAlarm)
buttonSet.grid(row=10, column=0)

buttonStop = Button(text="Stop Alarm", command=stop)
buttonStop.grid(row=10, column=2)

Label(text="by: ~XCletus3").grid(row=11, column=2)

run()

clock.resizable(False, False)
clock.mainloop()
