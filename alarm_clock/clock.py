import tkinter as tk
from tkinter import ttk
import time
import datetime
import pytz  # Ensure you have pytz installed: pip install pytz

# Initialize the main application window
class DynamicClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic Clock")
        self.root.resizable(False, False)
        self.root.geometry("400x250")
        
        # Define styles
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Courier New", 20))
        
        # Create and place the clock label
        self.clock_label = ttk.Label(self.root, text="", background="black", foreground="white", anchor="center")
        self.clock_label.pack(expand=True, fill='both')
        
        # Create and place the date label
        self.date_label = ttk.Label(self.root, text="", font=("Courier New", 14), background="black", foreground="white", anchor="center")
        self.date_label.pack()
        
        # Start the clock update loop
        self.update_time()

    def get_time_of_day(self, hour):
        if 5 <= hour < 12:
            return "Morning"
        elif 12 <= hour < 18:
            return "Afternoon"
        elif 18 <= hour < 21:
            return "Evening"
        else:
            return "Night"

    def update_time(self):
        # Get current time and date
        now = datetime.datetime.now(pytz.timezone("UTC"))  # Change timezone as needed
        current_time = now.strftime("%I:%M:%S %p")
        current_date = now.strftime("%A, %B %d, %Y")
        hour = now.hour

        # Determine time of day
        time_of_day = self.get_time_of_day(hour)
        
        # Update labels
        self.clock_label.config(text=current_time + f"\nGood {time_of_day}!")
        self.date_label.config(text=current_date)
        
        # Change background color based on time of day
        color = self.get_background_color(time_of_day)
        self.root.configure(background=color)
        self.clock_label.configure(background=color)
        self.date_label.configure(background=color)
        
        # Schedule the update_time function to be called after 1000 milliseconds (1 second)
        self.root.after(1000, self.update_time)

    def get_background_color(self, time_of_day):
        color_mapping = {
            "Morning": "lightblue",
            "Afternoon": "lightyellow",
            "Evening": "orange",
            "Night": "midnight blue"
        }
        return color_mapping.get(time_of_day, "black")

def main():
    # Create the main window
    root = tk.Tk()
    
    # Initialize the DynamicClockApp
    app = DynamicClockApp(root)
    
    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()

