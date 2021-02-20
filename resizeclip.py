#import tkinter as tk #import library of gui
#window = tk.Tk() #creating window object
#intro = tk.Label(text="Welcome!") #creating label
#intro.pack() #incorporando os elementos

#widgets: Label, Button, Entry, Text, Frame
#entry widgets: get(), delete(), insert()	ex:name = entry.get()
#get() in texts need parameters: The line number of a character and The position of a character on that line. ex: text_box.get("1.0", "1.5")
#insert()/delete() receives an intenteger character which will be inserted/deleted. ex: entry.insert(0, "Python") / entry.delete(0, tk.END)
#parameters: text,foreground / fg,background / bg, width, height
#colors HTML, hexdec RGB
#width and height are measured in text unit (not pixels)
#window.mainloop() This method listens for events, such as button clicks or keypresses, and blocks any code that comes after it from running until the window it’s called on is closed.
#window.destroy() to destroy the window
#border_effects: relief = {tk.FLAT, tk.SUNKEN, tk.RAISED, tk.GROOVE, tk.RIDGE}
#frame.pack(side=tk.LEFT): da pack à esquerda
#geometry managers: .pack(), .place(), .grid()
#When no anchor point is specified when .pack() is called for each Frame, they’re all centered inside of their parcels. That’s why each Frame is centered in the window.
#arguments of pack(): fill=tk.X / fill=tk.Y / fill=tk.BOTH (fills the parcel)
#arguments of pack(): side=tk.LEFT / side=tk.BOTTOM / side=tk.RIGHT / side=tk.TOP
#grid(): frame.grid(row=i, column=j, padx=5, pady=5)
#setting minsize: window.columnconfigure(0, minsize=50)
#setting minsize: window.rowconfigure([0, 1], minsize=50)
#sticky parameter:sticky="n"/"s"/"e"/"w" (north,south, east, west)... ne/new/se/sw ... ns/ew(vertical/horizontal) ... nsew (fill)

#.bind(a,b): a:"<event_name>"(Tkinter’s events), b:An event handler(function)
#Events: "<Button-1>" = left mouse click on button / "<Button-2>" = middle click / "<Button-3>" = right click

#get text from label:   label = Tk.Label(text="Hello") / text = label["text"] / label["text"] = "Good bye"
#function increase: def increase(): / value = int(lbl_value["text"]) / lbl_value["text"] = f"{value + 1}"

import os
import datetime
import tkinter as tk
from PIL import Image #image manip
from PIL import ImageGrab #image manip
from pynput import keyboard #hotkeys
from pynput.keyboard import HotKey, Key, KeyCode, Listener
from tkinter import *

dir_path = "C:\\Users\\josivania\\Desktop\\Python\\Project Reclip"

#Setting window and tk variables
window = tk.Tk()
window.title('Reclip v0.5') #Title
saveOrOpen = tk.IntVar()    #variable for radio button
ddoption = tk.StringVar()   #variable for drop down menu
ddoption.set("BMP")         #default value

#Frame 1 w/ label and entry (create and load)
frm1 = tk.Frame(height=2, width=100, bg="black")
lbl1 = tk.Label(text="Width", master=frm1, width=12) #colocando a label dentro do master: frame
ent1 = tk.Entry(fg="white", bg="grey", width=10, master=frm1)
frm1.grid(row=1, column=1, padx=5, pady=5)
lbl1.grid(row=0,column=0)
ent1.grid(row=0,column=1)

#Frame 2 w/ label and entry (create and load)
frm2 = tk.Frame(height=2, width=100, bg="black")
lbl2 = tk.Label(text="Height", master=frm2, width=12)
ent2 = tk.Entry(fg="white", bg="grey", width=10, master=frm2)
frm2.grid(row=2, column=1, padx=5, pady=5)
lbl2.grid(row=0,column=0)
ent2.grid(row=0,column=1)

#Frame 3 w/ label and entry (create and load)
frm3 = tk.Frame(height=2, width=100, bg="black")
lbl3 = tk.Label(text="Directory", master=frm3, width=12)
ent3 = tk.Entry(fg="white", bg="grey", width=10, master=frm3)
frm3.grid(row=3, column=1, padx=5, pady=5)
lbl3.grid(row=0,column=0)
ent3.grid(row=0,column=1)

#Frame 4 w/ label and entry (create and load)
frm4 = tk.Frame(height=2, width=100, bg="black")
lbl4 = tk.Label(text="Hotkey", master=frm4, width=12)
ent4 = tk.Entry(fg="white", bg="grey", width=10, master=frm4)
frm4.grid(row=4, column=1, padx=5, pady=5)
lbl4.grid(row=0,column=0)
ent4.grid(row=0,column=1)

#Frame 5 w/ label (create and load)
frm5 = tk.Frame(height=2, width=100)
lbl5 = tk.Label(text="Save or open:", master=frm5, width=12)
frm5.grid(row=1, column=2, padx=5, pady=5, sticky="W")
lbl5.grid(row=0,column=0)

#Radios to "save" or "open"
btn_save = tk.Radiobutton(
    text="Save",
    variable=saveOrOpen, #important: saveOrOpen = tk.IntVar() after window = tk.Tk()
    value=1,
    master=frm5)
btn_save.grid(row=1, column=0, padx=2, pady=2)

btn_open = tk.Radiobutton(
    text="Open",
    variable=saveOrOpen,
    value=2,
    master=frm5)
btn_open.grid(row=1, column=1, padx=2, pady=2)


#Frame 6 w/ label (create and load)
frm6 = tk.Frame(height=2, width=100)
lbl6 = tk.Label(text="Image format:", master=frm6, width=12)
frm6.grid(row=2, column=2, padx=0, pady=0, sticky="W")
lbl6.grid(row=0,column=0)

#Dropdown menu for frame 6

ddmenu = OptionMenu(frm6, ddoption, "BMP","PNG","JPEG")
ddmenu.grid(row=1, column=1 , padx=2, pady=2)


#button_go function
def clip_it():
    
    imgclip = ImageGrab.grabclipboard()

    model_width = int(ent1.get())
    model_height = int(ent2.get())

    output_coords = (imgclip.size[0]/2 - (model_width/2),imgclip.size[1]/2 - model_height/2,imgclip.size[0]/2 + model_width/2, imgclip.size[1]/2 + model_height/2)

    output = imgclip.crop(output_coords)
    
    choice = int(saveOrOpen.get())
    image_format = str(ddoption.get())

    if image_format == "JPEG":
        output = output.convert('RGB')

    if choice == 1:
        timenow = str(datetime.datetime.now()).replace(":","-")[0:19]
        image_name = ("%s" %timenow) + "." + ("%s" %image_format)
        file_path = os.path.join( dir_path, image_name) #join paths***
        output.save(file_path, "%s" %image_format)

        print(output.size, image_name, " saved in ", file_path)
        print(image_format)
        print(choice)

    if choice == 2:
        output.show()
        print(output.size, " showed")
        print(image_format)
        print(choice)

#Button to confirm parameters (create and load)
btn_go = tk.Button(
    text="Go!",
    width=5,
    height=2,
    bg="grey",
    fg="white",
    command=clip_it
)
btn_go.grid(row=5, column=1, padx=5, pady=5)

#function to convert user hotkey input


model_hotkey = "<ctrl>+o"

def function_1():
    print('Function 1 activated')

def function_2():
    print('Function 2 activated')

def save_hotkey():
    model_hotkey = str(ent4.get()).replace("^","<ctrl>+").replace("~","<shift>+").replace("!","<alt>+").replace("#","<win>+")
    print(model_hotkey+' setted as hotkey')

    
    with keyboard.GlobalHotKeys({
        '%s' %model_hotkey: clip_it,
        '<alt>+<ctrl>+t': function_1,
        '<alt>+<ctrl>+y': function_2}) as h:
        h.join()


#Button to confirm hotkey
btn_sethotkey = tk.Button(
    text="Set",
    width=5,
    height=2,
    bg="grey",
    fg="white",
    command=save_hotkey
)

btn_sethotkey.grid(row=5, column=2, padx=5, pady=5)

#Text area for showing output (creat and load)
txt1 = tk.Text(width=10, height=5)
txt1.grid(row=5, column=3, padx=5, pady=5)


""" #event
def button_pressed(event):
    #Print the character associated to the key pressed
    print("button was pressed")

# Bind keypress event to handle_keypress()
window.bind("<Button-1>", button_pressed) """

#Creating variables to store user iputs
#model_width = int(ent1.get())
#model_heigth = int(ent2.get())
#model_directory = ent3.get()
#model_hotkey = ent4.get()




window.mainloop()





