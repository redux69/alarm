from tkinter import *
from tkinter import ttk
import time
import os
from tkinter import messagebox
root = Tk()
root.title("Alarm")
def SubmitButton():
  AlarmTime= entry1.get()
  Message1()
  CurrentTime = time.strftime("%H:%M")
  print("Alarma este setată la ora {}".format(AlarmTime))
  while AlarmTime != CurrentTime:
    CurrentTime = time.strftime("%H:%M")
    time.sleep(1)
  if AlarmTime == CurrentTime:
     print("Alarm")
     os.system("start alarm-music.mp3")
     label2.config(text = "Alarming...")
     messagebox.showinfo(title= 'Alarm', message= "{}".format(entry2.get()))
def Message1():
    AlarmTimeLable= entry1.get()
    messagebox.showinfo(message = 'The alarm is set to {}'.format(AlarmTimeLable))     
frame1 = ttk.Frame(root)
frame1.pack()
frame1.config(height = 100, width = 100)
label1= ttk.Label(frame1,text = "Set the hour::")
label1.pack()
entry1 = ttk.Entry(frame1, width = 30)
entry1.pack()
labelAlarmMessage= ttk.Label(frame1, text="Message:")
labelAlarmMessage.pack()
entry2= ttk.Entry(frame1, width=30)
entry2.pack()
button1= ttk.Button(frame1, text= "Set", command=SubmitButton)
button1.pack()
label2= ttk.Label(frame1)
label2.pack()
root.mainloop()
