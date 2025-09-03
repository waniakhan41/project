import datetime
import time
import threading
import winsound
from tkinter import *
from tkinter import messagebox

# Function to run the alarm in background
def run_alarm(alarm_time, sound_file):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            messagebox.showinfo("Alarm", "Wake up! Alarm ringing...")
            winsound.PlaySound(sound_file, winsound.SND_FILENAME)
            break
        time.sleep(1)

# Function to set the alarm
def set_alarm():
    alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    sound_file = "alarm.wav"  # replace with your own WAV file
    messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
    
    # Run alarm in background thread
    t = threading.Thread(target=run_alarm, args=(alarm_time, sound_file))
    t.start()

# GUI setup
root = Tk()
root.title("Beautiful Alarm Clock")
root.geometry("400x300")
root.config(bg="#2c3e50")

Label(root, text="Set Alarm Time", font=("Helvetica", 18, "bold"), bg="#2c3e50", fg="white").pack(pady=20)

frame = Frame(root, bg="#2c3e50")
frame.pack()

# Dropdown for hours, minutes, seconds
hour = StringVar(root)
hours = [f"{i:02}" for i in range(24)]
hour.set(hours[0])
OptionMenu(frame, hour, *hours).grid(row=0, column=0, padx=5)

minute = StringVar(root)
minutes = [f"{i:02}" for i in range(60)]
minute.set(minutes[0])
OptionMenu(frame, minute, *minutes).grid(row=0, column=1, padx=5)

second = StringVar(root)
seconds = [f"{i:02}" for i in range(60)]
second.set(seconds[0])
OptionMenu(frame, second, *seconds).grid(row=0, column=2, padx=5)

# Set alarm button
Button(root, text="Set Alarm", font=("Helvetica", 14, "bold"), bg="#27ae60", fg="white", command=set_alarm).pack(pady=30)

root.mainloop()
