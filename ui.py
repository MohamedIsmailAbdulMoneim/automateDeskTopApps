import tkinter as tk
from tkinter import ttk
from threading import Thread
from app import process, perform_actions

class ScriptUI:
    def __init__(self, master):
        self.master = master
        master.title("Open Vpn")
        
        top_color = "#D1E4EC"  # You can replace this with your desired color code
        self.master.configure(bg=top_color)
        
        style = ttk.Style()

                # Create a button with a white background and command
        self.perform_actions_button = tk.Button(master, text="Open", command=process, bg="white", width=17, height=2, fg="black", font=('Helvetica', 10), borderwidth=1, highlightthickness=1)

        self.close_button = tk.Button(master, text="Close", command=process, bg="white", width=17, height=2, fg="black", font=('Helvetica', 10), borderwidth=1, highlightthickness=1)
        # Place the button to center it both vertically and horizontally
        window_width = master.winfo_reqwidth()
        window_height = master.winfo_reqheight()
        button_width = self.perform_actions_button.winfo_reqwidth()
        button_height = self.perform_actions_button.winfo_reqheight()
        button_width = self.close_button.winfo_reqwidth()
        button_height = self.close_button.winfo_reqheight()

        x_position = (150) // 2
        y_position = (75) // 2

        self.perform_actions_button.place(x=x_position, y=y_position)
        self.close_button.place(x=x_position, y=y_position + 60)

    def perform_actions(self):
        # Disable the button during script execution
        self.perform_actions_button.config(state=tk.DISABLED)

        # Run the script in a separate thread to prevent blocking the UI
        script_thread = Thread(target=perform_actions)
        script_thread.start()

        # Enable the button after the script finishes
        self.master.after(100, lambda: self.check_thread(script_thread))

    def check_thread(self, script_thread):
        if script_thread.is_alive():
            self.master.after(100, lambda: self.check_thread(script_thread))
        else:
            # Enable the button
            self.perform_actions_button.config(state=tk.NORMAL)