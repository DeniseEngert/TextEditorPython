import sys
from tkinter import *  # import Python's standard GUI
import tkinter.filedialog

# Editor runs with Python3 only

### Variables ###
root = Tk()
root.title("Text Editor")
root.geometry("1000x600")  # size of the frame
root.resizable(True, True)

global open_status_name
open_status_name = False

global selected
selected = False

# add Toolbar
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X, pady=5)

# add mainframe
my_frame = Frame(root)
my_frame.pack(pady=5)

# add scrollbars
vertscroll = Scrollbar(my_frame)
vertscroll.pack(side=RIGHT, fill=Y)
horscroll = Scrollbar(my_frame, orient="horizontal")
horscroll.pack(side=BOTTOM, fill=X)

# add a text box
text = Text(my_frame, width=80, height=20, font=("Helvetica", 16), selectbackground="lightgrey",
            selectforeground="black", undo=True, yscrollcommand=vertscroll.set, xscrollcommand=horscroll.set, wrap="none")
text.pack()

# configure scrollbar
vertscroll.config(command=text.yview)
horscroll.config(command=text.xview)

# add a menu
mymenu = Menu(root)
root.config(menu=mymenu)

# add status bar to buttom
statusbar = Label(root, text="Ready       ", anchor=E)
statusbar.pack(fill=X, side=BOTTOM, ipady=15)

##### Filemenu ##### ToDo

#
# # add a button to save the text
# def saveas():
#     global text
#     t = text.get("1.0", "end-1c")
#     savelocation = tkinter.filedialog.asksaveasfilename()
#     file1 = open(savelocation, "w+")
#     file1.write(t)
#     file1.close()
#
#
# button = Button(root, text="Save", command=saveas)
# button.grid()
#
#
# # add font changer
# def changefont(font):
#     global text
#     text.config(font=font)
#
#
# font = Menubutton(root, text="Font")
# font.grid()
# font.menu = Menu(font, tearoff=0)
# font["menu"] = font.menu
# Helvetica = IntVar()
# Courier = IntVar()
# font.menu.add_checkbutton(label="Courier", variable=Courier, command=lambda: changefont("Courier"))
# font.menu.add_checkbutton(label="Helvetica", variable=Helvetica, command=lambda: changefont("Helvetica"))

# todo colour
# todo Menüleiste
# todo font effects
# todo stuff

root.mainloop()
