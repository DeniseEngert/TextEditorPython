import sys
from tkinter import * # import Python's standard GUI
import tkinter.filedialog

# Editor runs with Python3

root=Tk("Text Editor")

# add a text box
text=Text(root)
text.grid()

# add a button to save the text
def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = tkinter.filedialog.asksaveasfilename()
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()

button = Button(root, text="Save", command=saveas)
button.grid()

# add font changer
# def changefont(font):
#     global text
#     text.config(font=font)

def FontHelvetica():
    global text
    text.config(font="Helvetica")

def FontCourier():
    global text
    text.config(font="Courier")

font=Menubutton(root, text="Font")
font.grid()
font.menu=Menu(font, tearoff=0)
font["menu"]=font.menu
Helvetica=IntVar()
Courier=IntVar()
font.menu.add_checkbutton(label="Courier", variable=Courier, command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=Helvetica, command=FontHelvetica)

root.mainloop()




