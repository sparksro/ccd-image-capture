import numpy as np
import cv2
from Tkinter import *
import Tkinter as tk
import tkMessageBox
import Image, ImageTk
import time


#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("Cam-Snapy")
window.config(background="grey")

#Graphics window
imageFrame = tk.Frame(window, width=300, height=250)
imageFrame.grid(row=0, column=0, padx=10, pady=2)

#Capture video frames
lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)
try:
    cap = cv2.VideoCapture(0)
except:
    print("Please turn your cammera on with the camera key.")
    tkMessageBox.showinfo("Error", "Please turn your camera on with the camera key!")
    exit()

def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)

def close():
    cap.release()
    cv2.destroyAllWindows()
    exit()

def snapPicture():
    retval, img = cap.read()
    timeVal =  str(time.strftime("%m%d%y%H%M%S"))
    file = "CS" + timeVal + ".png"
    cv2.imwrite(file, img)
    time.sleep(1)
    close()

# bottom frame to possition buttons
bottomFrame = tk.Frame(window, width=600, height=100, bg="grey")
bottomFrame.grid( row = 600, column=0, padx=10, pady=2)
button1 = Button(bottomFrame, text="Take Picture", command=snapPicture)
button2 = Button(bottomFrame, text="Exit", command=close)
button1.grid(row = 600, column=1, padx =4)
button2.grid(row = 600, column=4, padx =4)

show_frame()  #Display 2
window.mainloop()  #Starts GUI