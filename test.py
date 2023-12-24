import os
import pyautogui
import pyperclip
import pygetwindow as gw
import time



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
    time.sleep(1)
    pyautogui.typewrite(app_path)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)  #
    perform_actions()


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
open_application_from_root(app_name)
# time.sleep(2)  # Adjust this as needed to allow the application to open
# perform_actions()

# close_application()

    