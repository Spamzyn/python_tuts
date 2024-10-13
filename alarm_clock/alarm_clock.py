from tkinter import *
import datetime
import time
from threading import Thread, Event
from pygame import mixer
import sys

# Initialize mixer once
mixer.init()

# Create the main window
root = Tk()
root.title("Alarm Clock")
root.geometry("500x300")
root.resizable(False, False)

# Event to stop the alarm thread
stop_event = Event()

def threading_alarm():
    global alarm_thread
    if not alarm_thread.is_alive():
        stop_event.clear()
        alarm_thread = Thread(target=alarm)
        alarm_thread.start()
        status_label.config(text="Alarm is set.")
    else:
        status_label.config(text="Alarm is already running.")

def alarm():
    while not stop_event.is_set():
        # Get the alarm time from user input
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        current_time_label.config(text=f"Current Time: {current_time}")
        
        # Debug print (optional)
        print(f"Current Time: {current_time} | Alarm Time: {set_alarm_time}")
        
        if current_time == set_alarm_time:
            status_label.config(text="Wake Up!")
            try:
                mixer.music.load("sound.wav")
                mixer.music.play(-1)  # Play indefinitely
            except Exception as e:
                status_label.config(text=f"Error playing sound: {e}")
            break
        time.sleep(1)

def stop_alarm():
    stop_event.set()
    mixer.music.stop()
    status_label.config(text="Alarm stopped.")

# Labels
Label(root, text="Alarm Clock", font=("Helvetica", 20, "bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica", 15, "bold")).pack()

# Frame for time selection
frame = Frame(root)
frame.pack(pady=10)

# Hour Dropdown
hour = StringVar(root)
hours = [f"{i:02d}" for i in range(0, 24)]
hour.set(hours[0])
hrs = OptionMenu(frame, hour, *hours)
hrs.config(width=3)
hrs.pack(side=LEFT, padx=5)

# Minute Dropdown
minute = StringVar(root)
minutes = [f"{i:02d}" for i in range(0, 60)]
minute.set(minutes[0])
mins = OptionMenu(frame, minute, *minutes)
mins.config(width=3)
mins.pack(side=LEFT, padx=5)

# Second Dropdown
second = StringVar(root)
seconds = [f"{i:02d}" for i in range(0, 60)]
second.set(seconds[0])
secs = OptionMenu(frame, second, *seconds)
secs.config(width=3)
secs.pack(side=LEFT, padx=5)

# Set Alarm Button
Button(root, text="Set Alarm", font=("Helvetica", 12), command=threading_alarm).pack(pady=20)

# Stop Alarm Button
Button(root, text="Stop Alarm", bg="red", fg="white", font=("Helvetica", 12), command=stop_alarm).pack(pady=10)

# Status Labels
status_label = Label(root, text="No alarm set.", font=("Helvetica", 12))
status_label.pack(pady=5)

current_time_label = Label(root, text="", font=("Helvetica", 12))
current_time_label.pack()

# Initialize alarm thread
alarm_thread = Thread(target=alarm)
alarm_thread.daemon = True  # Daemonize thread to exit when main program exits

root.mainloop()

