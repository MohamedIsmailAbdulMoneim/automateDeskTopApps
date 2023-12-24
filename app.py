import tkinter as tk
from tkinter import ttk

from threading import Thread
import os
import pyautogui
import pyperclip
import pygetwindow as gw
import time

def click_button(button_image_path, timeout=30):
    start_time = time.time()

    while time.time() - start_time < timeout:
        button_location = pyautogui.locateOnScreen(button_image_path, confidence=0.9)
        if button_location:
            # Center of the button
            button_center_x = button_location.left + button_location.width / 2
            button_center_y = button_location.top + button_location.height / 2

            # Click the center of the button
            pyautogui.click(button_center_x, button_center_y)
            return True

        time.sleep(1)

    return False

# Your code before clicking the button

# Click the button with the specified image path


# Your code after clicking the button



def open_token_generator(tokenapp_name):
    # Build the full path to the application on the C partition
    root_path = "C:\\Program Files (x86)\\Entrust\\IdentityGuard Soft Token\\"  # Replace this with the actual path
    app_path = os.path.join(root_path, tokenapp_name)
    window_title = "Cisco AnyConnect | 196.46.22.222/CARGAS"
    

    # Open the application
    time.sleep(1)
    pyautogui.hotkey('winleft', 'r')  # Opens the Run dialogph1g&jEp#e
    pyautogui.typewrite(app_path)
    pyautogui.press('enter')
    time.sleep(1)
    gw.getActiveWindow()
    # gw.getWindowsWithTitle("Entrust IdentityGuard...")[0].activate()
    pyautogui.typewrite('1598')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    
    pyautogui.press('space')
    time.sleep(1)
    
    
    time.sleep(3)
    clipboard_content = pyperclip.paste()

# Print the clipboard content (optional)
    time.sleep(3)
    gw.getWindowsWithTitle(window_title)[0].activate()
# Use pyautogui.typewrite to type the content
    time.sleep(3)
    pyautogui.typewrite(clipboard_content)
    time.sleep(1)
    pyautogui.press('enter')


def open_application_from_root(app_name):
    # Build the full path to the application on the C partition
    root_path = "C:\\Program Files (x86)\\Cisco\\Cisco AnyConnect Secure Mobility Client"  # Replace this with the actual path
    app_path = os.path.join(root_path, app_name)
    

    # Open the application
    time.sleep(1)
    pyautogui.hotkey('winleft', 'r')  # Opens the Run dialogph1g&jEp#e
    time.sleep(2)
    pyautogui.typewrite(app_path)
    time.sleep(2)
    # click_button('C:\\Users\\mkhodeir\\Desktop\\appAutomation\\img\\connect.png', timeout=30)
    pyautogui.press('enter')
    time.sleep(2)  #
    perform_actions()
    
def process():
    open_application_from_root(app_name)


def perform_actions():
    # Your actions within the application
    window_title = "Cisco AnyConnect Secure Mobility Client"
    gw.getWindowsWithTitle(window_title)[0].activate()
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(5)

    pyautogui.typewrite("9?nnbZhRaS")
    pyautogui.press('enter')
    time.sleep(4)
    active_window = gw.getActiveWindow()
    # Get the window title
    window_title = active_window.title
    print("Window Title:", window_title, "'")
    open_token_generator(tokenapp_name)
   
    

# def close_application():
    # Your actions to close the application

# Main script
app_name = "vpnui.exe"  # Replace with the actual application name
tokenapp_name = "SoftToken.exe"
# open_application_from_root(app_name)
# time.sleep(2)  # Adjust this as needed to allow the application to open
# perform_actions()

# close_application()
class ScriptUI:
    def __init__(self, master):
        self.master = master
        master.title("Open Vpn")
        
        top_color = "#242222"  # You can replace this with your desired color code
        self.master.configure(bg=top_color)
        
        style = ttk.Style()

                # Create a button with a white background and command
        self.perform_actions_button = tk.Button(master, text="Open", command=process, bg="white", width=17, height=2, fg="black", font=('Helvetica', 10))

        # Place the button to center it both vertically and horizontally
        window_width = master.winfo_reqwidth()
        window_height = master.winfo_reqheight()
        button_width = self.perform_actions_button.winfo_reqwidth()
        button_height = self.perform_actions_button.winfo_reqheight()

        x_position = (150) // 2
        y_position = (75) // 2

        self.perform_actions_button.place(x=x_position, y=y_position)

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

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('300x100')
    root.resizable(width=False, height=False)
    app = ScriptUI(root)
    root.mainloop()
    