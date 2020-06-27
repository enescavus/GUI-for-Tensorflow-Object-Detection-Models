'''
===============================================================
@ Title:  Tensorflow Object Detection GUI - Tkinter / Welcome Page
@ Author: Enes Çavuş
@ Date:   27 June 2020 

'''

# Import Packages

import sys
import os

try:
    import Tkinter as tk
except ImportError:            # to prevent version issues
    import tkinter as tk
try:
    import ttk
except ImportError:
    import tkinter.ttk as ttk
try:
    from tkinter import messagebox   # to give information to the user 
except:
    # Python 2
    import tkMessageBox as messagebox

# Main Window 
root = tk.Tk()
root.title(" Object Detection GUI / Designed by ENES ÇAVUŞ")
root.geometry("800x650+150+125")
root.config(bg="white")

def start_detection():
    quit()
    os.system('python ObjDetection.py')   # re-direction to the detection page. 
# It is an another python file - named ObjDetection - where you can find in the same location with this file

# We create a frame
framePhoto = tk.Frame(root, bg="#d0dbc1")
framePhoto.place(relheight=0.6, relwidth=0.8, relx=0.1,rely=0.1)
# Quick info about app! 
photoPanel = tk.Label(framePhoto, bg="#d0dbc1", text = "Welcome to the Object Detection App!\n\n\n Designed by ENES ÇAVUŞ\n\n\nTo Continue Press the Button Below" )
# placing the label
photoPanel.place( relheight=1, relwidth=1,)
photoPanel.configure(highlightcolor="black")
photoPanel.configure(activeforeground="black")

# the frame that includes the redirection button
buttonFrame = tk.Frame(root, bg="#d5d9e3")
buttonFrame.place(relheight=0.18, relwidth=0.8, relx=0.1,rely=0.8)
# Button definition
# placing the button in a frame
openDetectionPageButton = tk.Button(buttonFrame, text= "Start Face Detection ", command=start_detection)
openDetectionPageButton.place(relx= 0.05, relwidth=0.9, rely=0.1, relheight=0.8 )

def quit():
    root.destroy()

root.mainloop()


# ENES ÇAVUŞ


