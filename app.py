import tkinter as tk
from tkinter import ttk
from threading import Thread
import os
import pyautogui
import pyperclip
import pygetwindow as gw
import time
# from PIL import Image



def click_button(button_image_path, timeout=30):
    start_time = time.time()

    while time.time() - start_time < timeout:
        button_location = pyautogui.locateOnScreen(button_image_path, confidence=0.8)
        if button_location:
            # Center of the button
            button_center_x = button_location.left + button_location.width / 2
            button_center_y = button_location.top + button_location.height / 2

            # Click the center of the button
            pyautogui.click(button_center_x, button_center_y)
            return True

        time.sleep(1)

    return False

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
    # gw.getWindowsWithTitle("Entrust IdentityGuard...")[0].activate()
    pyautogui.typewrite('1598')
    time.sleep(2)
    click_button('C:\\Users\\mkhodeir\\Desktop\\appAutomation\\img\\copy.png', timeout=30)
    
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
    pyautogui.press('enter')
    time.sleep(1)
    perform_actions()
    
def process():
    open_application_from_root(app_name)


def perform_actions():
    # Your actions within the application
    window_title = "Cisco AnyConnect Secure Mobility Client"
    gw.getWindowsWithTitle(window_title)[0].activate()
    # locate_by_text('Connect', confidence=0.9)
    time.sleep(3)
    click_button('C:\\Users\\mkhodeir\\Desktop\\appAutomation\\img\\connect.png', timeout=30)
    time.sleep(10)
    click_button('C:\\Users\\mkhodeir\\Desktop\\appAutomation\\img\\connect_anyway.png', timeout=30)
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
