import pyautogui
import time

def open_calculator():
    pyautogui.hotkey('winleft', 'r')  # Opens the Run dialog
    pyautogui.typewrite('calc.exe')
    pyautogui.press('enter')

def perform_calculation():
    # Wait for the Calculator to open (adjust the sleep time as needed)
    time.sleep(2)

    # Perform a simple calculation (e.g., 5 + 3)
    pyautogui.typewrite('5')
    pyautogui.press('plus')
    pyautogui.typewrite('3')
    pyautogui.press('enter')

def close_calculator():
    # Wait for the result to be ready (adjust the sleep time as needed)
    # Close the Calculator
    pyautogui.hotkey('alt', 'f4')



# Main script
open_calculator()
perform_calculation()
close_calculator()
