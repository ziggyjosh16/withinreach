from Tkinter import *

top = Tk()
# Code to add widgets will go here...
sheight = top.winfo_screenheight()
swidth = top.winfo_screenwidth()
top.minsize(width=swidth, height=sheight)
top.maxsize(width=swidth, height=sheight)
top.title( "Test title")
label = Label(top, text="test")
label.pack()
top.mainloop()