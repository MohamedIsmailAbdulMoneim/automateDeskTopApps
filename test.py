import os
import pyautogui
import time

def open_token_generator(app_name):
    # Build the full path to the application on the C partition
    root_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Entrust"  # Replace this with the actual path
    app_path = os.path.join(root_path, app_name)

    # Open the application
    pyautogui.hotkey('winleft', 'r')  # Opens the Run dialogph1g&jEp#e
    
    pyautogui.typewrite(app_path)
    pyautogui.press('enter')

def open_application_from_root(app_name):
    # Build the full path to the application on the C partition
    root_path = "C:\\Program Files (x86)\\Cisco\\Cisco AnyConnect Secure Mobility Client"  # Replace this with the actual path
    app_path = os.path.join(root_path, app_name)

    # Open the application
    pyautogui.hotkey('winleft', 'r')  # Opens the Run dialogph1g&jEp#e
    
    pyautogui.typewrite(app_path)
    pyautogui.press('enter')

def perform_actions():
    # Your actions within the application
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite("ph1g&jEp#e")
    pyautogui.press('enter')
    'IdentityGuard Soft Token'
    

# def close_application():
    # Your actions to close the application

# Main script
app_name = "vpnui.exe"  # Replace with the actual application name
open_application_from_root(app_name)
time.sleep(2)  # Adjust this as needed to allow the application to open
perform_actions()

# close_application()

    