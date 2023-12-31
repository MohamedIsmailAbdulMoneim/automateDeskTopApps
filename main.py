import tkinter as tk
from ui import ScriptUI
from PIL import Image, ImageTk

if __name__ == "__main__":
    root = tk.Tk()
    icon_path = 'C:\\Users\\mkhodeir\\Desktop\\appAutomation\\img\\logo.png'

    # icon = ImageTk.PhotoImage(file=icon_path)
    # root.tk.call('wm', 'iconphoto', root._w, icon)
    # Open the ICO file using Pillow
    img = Image.open(icon_path)
    icon = ImageTk.PhotoImage(img)
    root.iconphoto(True, icon)
    
    # Load the image using Pillow
    image_path = 'C:\\Users\\mkhodeir\\Desktop\\appAutomation\\img\\it_logo.png'  # Replace with the actual path to your image
    img = Image.open(image_path)

    # Resize the image using the thumbnail method
    img.thumbnail((150, 102))

    # Convert the image to a PhotoImage object
    photo = ImageTk.PhotoImage(img)

    # Create a Label widget to display the image
    image_label = tk.Label(root, image=photo)
    image_label.place(relx=0.49, rely=0.5 + 0.2, anchor=tk.CENTER)
    # image_label.pack()

    
    root.geometry('300x300')
    root.resizable(width=False, height=False)
    app = ScriptUI(root)
    root.mainloop()